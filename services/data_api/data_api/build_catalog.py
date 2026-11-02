"""Validate mirrored data, publish open property tables, and build a compact index."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import time

import duckdb
import pyarrow as pa
import pyarrow.parquet as pq

from .mirror import digest


def sql_string(value):
    return "'" + str(value).replace("'", "''") + "'"


def build(root, revision):
    root = Path(root)
    directory = root / "releases" / revision
    receipt = json.loads((directory / "mirror_receipt.json").read_text())
    assert receipt["revision"] == revision
    upstream = directory / "upstream"
    # Do not modify the index of an activated release.
    if (directory / "READY.json").exists():
        print("Release already validated", flush=True)
        return
    started = time.time()
    for entry in receipt["files"]:
        file = upstream / entry["path"]
        if file.stat().st_size != entry["bytes"] or digest(file) != entry["sha256"]:
            raise ValueError(f"Mirror integrity failure: {entry['path']}")
    print("All source hashes verified", flush=True)
    published = directory / "published"
    (published / "properties").mkdir(parents=True, exist_ok=True)
    metadata_path = directory / "metadata.parquet"
    writer = None
    counts = Counter()
    rows = 0
    for file in sorted((upstream / "data").glob("*.parquet")):
        pf = pq.ParquetFile(file)
        columns = [name for name in pf.schema_arrow.names if name != "cif"]
        for group in range(pf.num_row_groups):
            table = pf.read_row_group(group, columns=columns)
            count = len(table)
            table = table.append_column("shard", pa.array([file.name] * count))
            table = table.append_column("row_group", pa.array([group] * count, type=pa.int32()))
            table = table.append_column("row_in_group", pa.array(range(count), type=pa.int32()))
            table = table.append_column("row_id", pa.array(range(rows, rows + count), type=pa.int64()))
            if writer is None:
                writer = pq.ParquetWriter(metadata_path, table.schema, compression="zstd")
            writer.write_table(table)
            for values in table["open_sources"].to_pylist():
                counts.update(set(values or []))
            rows += count
        print(json.dumps({"indexed": file.name, "structures": rows}), flush=True)
    writer.close()
    db = duckdb.connect(str(directory / "index.duckdb"))
    db.execute("SET threads=2")
    db.execute("SET memory_limit='4GB'")
    db.execute("SET temp_directory=?", [str(root / "tmp" / "ingest")])
    db.execute(f"CREATE OR REPLACE TABLE structures AS SELECT * FROM read_parquet({sql_string(metadata_path)})")
    duplicates = db.execute("SELECT count(*)-count(DISTINCT material_id) FROM structures").fetchone()[0]
    if duplicates:
        raise ValueError(f"Duplicate material IDs: {duplicates}")
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS material_id_idx ON structures(material_id)")
    db.execute("CREATE INDEX IF NOT EXISTS row_id_idx ON structures(row_id)")
    manifest = json.loads((upstream / "properties/MANIFEST.json").read_text())
    properties = []
    total = 0
    open_total = 0
    for name, declared in sorted(manifest["per_property"].items()):
        file = upstream / "properties" / f"{name}.parquet"
        path = sql_string(file)
        count, distinct, missing = db.execute(f"SELECT count(*), count(DISTINCT p.material_id), count(*) FILTER(WHERE s.material_id IS NULL) FROM read_parquet({path}) p LEFT JOIN structures s USING(material_id)").fetchone()
        if count != declared["rows"] or distinct != declared["structures"] or missing:
            raise ValueError(f"Property counts or joins failed: {name}: {count}, {distinct}, {missing}")
        classes = dict(db.execute(f"SELECT licence_class,count(*) FROM read_parquet({path}) GROUP BY licence_class").fetchall())
        methods = [r[0] for r in db.execute(f"SELECT DISTINCT method FROM read_parquet({path}) WHERE licence_class='open' ORDER BY method").fetchall()]
        sources = dict(db.execute(f"SELECT source,count(*) FROM read_parquet({path}) WHERE licence_class='open' GROUP BY source ORDER BY source").fetchall())
        public = published / "properties" / f"{name}.parquet"
        db.execute(f"COPY (SELECT * FROM read_parquet({path}) WHERE licence_class='open') TO {sql_string(public)} (FORMAT PARQUET, COMPRESSION ZSTD)")
        item = {"name": name, **declared, "upstream_rows": count,
                "rows": classes.get("open", 0), "structures": db.execute(f"SELECT count(DISTINCT material_id) FROM read_parquet({sql_string(public)})").fetchone()[0],
                "excluded_rows": count - classes.get("open", 0), "licence_classes": classes,
                "methods": methods, "upstream_sources": declared["sources"], "sources": sources, "bytes": public.stat().st_size,
                "sha256": digest(public), "kind": declared["kind"], "record_type": "source_property"}
        properties.append(item)
        total += count
        open_total += item["rows"]
        print(json.dumps({"property": name, "rows": count, "public": item["rows"]}), flush=True)
    if total != manifest["rows"]:
        raise ValueError("Global property counts failed")
    predictions = []
    pm = json.loads((upstream / "predictions/MANIFEST.json").read_text())
    for name, declared in sorted(pm["tasks"].items()):
        if declared["state"] != "done":
            continue
        file = upstream / "predictions" / f"{name}.parquet"
        pf = pq.ParquetFile(file)
        if pf.metadata.num_rows != declared["rows"]:
            raise ValueError(f"Prediction rows failed: {name}")
        missing = db.execute(f"SELECT count(*) FROM read_parquet({sql_string(file)}) p ANTI JOIN structures s USING(material_id)").fetchone()[0]
        if missing:
            raise ValueError(f"Prediction joins failed: {name}")
        predictions.append({"name": name, **declared, "record_type": "ml_prediction",
                            "bytes": file.stat().st_size, "sha256": digest(file),
                            "columns": pf.schema_arrow.names,
                            "model": json.loads(file.with_suffix(".json").read_text())})
    if sum(x["rows"] for x in predictions) != pm["rows_total"]:
        raise ValueError("Prediction global count failed")
    db.execute("CHECKPOINT")
    db.close()
    metadata_path.unlink()  # Reproducible intermediate; canonical index is the checked DB.
    licences = json.loads((upstream / "licences.json").read_text())
    sources = [{"name": key, "structures": value, "details": licences.get(key, {})}
               for key, value in sorted(counts.items(), key=lambda x: (-x[1], x[0]))]
    catalog = {"collection": "materiaviva-open", "revision": revision,
               "upstream": f"https://huggingface.co/datasets/{receipt['repo']}",
               "structures": rows, "properties": properties, "predictions": predictions,
               "sources": sources, "upstream_property_rows": total, "public_property_rows": open_total,
               "prediction_rows": sum(x["rows"] for x in predictions),
               "source_bytes": receipt["bytes"], "built_at": time.time(),
               "licence_policy": "Property exports include only rows labelled open by the publisher; labels are preserved, not independently reassessed."}
    (directory / "catalog.json").write_text(json.dumps(catalog, indent=2))
    ready = {"revision": revision, "structures": rows, "properties": len(properties),
             "property_rows": total, "public_property_rows": open_total,
             "prediction_rows": catalog["prediction_rows"], "files_verified": len(receipt["files"]),
             "index_sha256": digest(directory / "index.duckdb"),
             "seconds": time.time() - started, "checked_at": time.time()}
    (directory / "READY.json").write_text(json.dumps(ready, indent=2))
    current = root / "current.next"
    current.write_text(revision + "\n")
    os.replace(current, root / "current")
    print(json.dumps({"status": "ready", **ready}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--revision", required=True)
    args = parser.parse_args()
    build(args.root, args.revision)
