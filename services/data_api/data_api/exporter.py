"""Bounded export execution. Invoked in a disposable worker subprocess."""
import argparse
import gzip
import io
import json
from pathlib import Path
import re
import tarfile
import time

from . import config, state
from .build_catalog import sql_string
from .mirror import digest
from .query import Selection, catalog, connection, selection_sql


README = """MaterialsAtlas Data API export

Source collection: AI4QC/MateriaViva-Open, mirrored at the revision in manifest.json.
Please cite MateriaViva and the original providers identified by each record.
The original licence and source fields are retained. Property exports include
only rows the publisher labels licence_class=open. This is a metadata-based
selection, not an independent assessment of provider licensing.

Multiple property values per structure are preserved: methods and sources can
differ. Values are not averaged or silently deduplicated. Units are recorded in
the manifest; a missing unit means unspecified, not necessarily dimensionless.
Prediction tasks are ML estimates, not new experimental or DFT calculations;
their publisher-supplied model metadata accompanies the export when requested.

CIFs are the representative coordinates supplied in this release. Membership
in a source database does not establish that it supplied the stored coordinates.
Use origin_source / structure_origin_source and origin_open to distinguish this.
Upstream n_sites and formula sometimes describe a primitive cell while the CIF
contains a conventional cell. They are retained as reported.

SHA-256 values in manifest.json cover every data file. CIFs are unique within
the export, named by material_id, and divided into archive parts. The table and
structure-metadata table join on material_id. A query limit applies to output
table rows, not a promised number of unique structures.
"""


def execute(identity, lease, work):
    job = state.get(identity)
    if not job or job["lease"] != lease or job["status"] != "running":
        raise ValueError("Job lease is no longer valid")
    selection = Selection.model_validate_json(job["query"])
    work = Path(work)
    work.mkdir(parents=True, exist_ok=True)
    directory = config.release_dir(selection.release)
    data = catalog(selection.release)
    sql, args = selection_sql(selection)
    started = time.time()
    with connection(selection.release, work / "spill") as db:
        state.update(identity, lease, progress="Selecting records")
        # Materialize once, in compressed columnar form, for repeated joins and exports.
        table_path = work / "records.parquet"
        db.execute(f"COPY ({sql}) TO {sql_string(table_path)} (FORMAT PARQUET, COMPRESSION ZSTD)", args)
        count, unique = db.execute("SELECT count(*),count(DISTINCT material_id) FROM read_parquet(?)", [str(table_path)]).fetchone()
        excluded = 0
        if selection.property:
            upstream_selection = selection.model_copy(update={"limit": None})
            raw_sql, raw_args = selection_sql(upstream_selection, include_nonopen=True)
            excluded = db.execute(f"SELECT count(*) FROM ({raw_sql}) WHERE licence_class != 'open' OR licence_class IS NULL", raw_args).fetchone()[0]
        state.update(identity, lease, progress=f"Selected {count:,} rows / {unique:,} structures")
        if selection.format == "csv.gz":
            db.execute(f"COPY (SELECT * FROM read_parquet({sql_string(table_path)})) TO {sql_string(work / 'records.csv.gz')} (FORMAT CSV, HEADER TRUE, COMPRESSION GZIP)")
        cif_count = 0
        if selection.include_cifs:
            metadata = work / "structure_metadata.parquet"
            db.execute(f"COPY (SELECT s.* EXCLUDE(shard,row_group,row_in_group,row_id) FROM structures s SEMI JOIN read_parquet({sql_string(table_path)}) p USING(material_id)) TO {sql_string(metadata)} (FORMAT PARQUET, COMPRESSION ZSTD)")
            cif_query = "SELECT s.material_id, s.cif FROM read_parquet(?) s SEMI JOIN read_parquet(?) p USING(material_id)"
            reader = db.execute(cif_query, [str(directory / "upstream/data/*.parquet"), str(table_path)]).fetch_record_batch(4096)
            part = 0
            tar = None
            compressed = None
            out = None
            try:
                for batch in reader:
                    for row in batch.to_pylist():
                        if cif_count % config.PART_CIFS == 0:
                            if tar:
                                tar.close(); compressed.close(); out.close()
                            part += 1
                            out = open(work / f"cifs-{part:04d}.tar.gz", "wb")
                            compressed = gzip.GzipFile(fileobj=out, mode="wb", mtime=0)
                            tar = tarfile.open(fileobj=compressed, mode="w|")
                            info = tarfile.TarInfo("README.txt")
                            payload = README.encode()
                            info.size = len(payload)
                            tar.addfile(info, io.BytesIO(payload))
                        identifier = row["material_id"]
                        if not re.fullmatch(r"[A-Za-z0-9_.:+-]{1,150}", identifier):
                            raise ValueError("Unsafe source material identifier")
                        if not row["cif"]:
                            raise ValueError(f"Missing CIF for {identifier}")
                        payload = row["cif"].encode()
                        info = tarfile.TarInfo(f"cifs/{identifier}.cif")
                        info.size = len(payload)
                        info.mode = 0o644
                        tar.addfile(info, io.BytesIO(payload))
                        cif_count += 1
                    state.update(identity, lease, progress=f"Packaging CIFs: {cif_count:,} / {unique:,}")
            finally:
                if tar:
                    tar.close(); compressed.close(); out.close()
            if cif_count != unique:
                raise ValueError(f"CIF join/count mismatch: {cif_count} != {unique}")
        if selection.format == "csv.gz":
            table_path.unlink()
    (work / "README.txt").write_text(README)
    item = None
    if selection.property:
        item = next(p for p in data["properties"] if p["name"] == selection.property)
    if selection.prediction:
        item = next(p for p in data["predictions"] if p["name"] == selection.prediction)
        (work / "model_metadata.json").write_text(json.dumps(item["model"], indent=2))
    files = [{"name": p.name, "bytes": p.stat().st_size, "sha256": digest(p)}
             for p in sorted(work.iterdir()) if p.is_file()]
    result = {"schema_version": 1, "id": identity, "collection": config.COLLECTION,
              "release": selection.release, "query": selection.model_dump(),
              "rows": count, "unique_structures": unique, "cifs": cif_count,
              "excluded_nonopen_rows_before_limit": excluded,
              "record_type": "ml_prediction" if selection.prediction else "source_property" if selection.property else "structure",
              "unit": item.get("unit") if item else None,
              "property_metadata": item, "files": files, "seconds": time.time()-started,
              "source": data["upstream"], "licence_policy": data["licence_policy"],
              "created_at": time.time()}
    (work / "manifest.json").write_text(json.dumps(result, indent=2))
    print(json.dumps({"rows": count, "unique_structures": unique, "cifs": cif_count}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("id")
    parser.add_argument("lease")
    parser.add_argument("work")
    args = parser.parse_args()
    execute(args.id, args.lease, args.work)
