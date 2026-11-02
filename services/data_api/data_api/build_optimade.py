"""Create a separate, audited OPTIMADE index from successfully normalized CIFs."""
import argparse
from collections import Counter
import concurrent.futures
import json
from pathlib import Path
import time

import duckdb
import pyarrow as pa
import pyarrow.parquet as pq

from .build_catalog import sql_string
from .mirror import digest
from .optimade_data import attributes


SCHEMA = pa.schema([
    ("id", pa.string()), ("immutable_id", pa.string()), ("last_modified", pa.string()),
    ("elements", pa.list_(pa.string())), ("nelements", pa.int32()),
    ("elements_ratios", pa.list_(pa.float64())),
    ("chemical_formula_descriptive", pa.string()), ("chemical_formula_reduced", pa.string()),
    ("chemical_formula_anonymous", pa.string()), ("nsites", pa.int32()),
    ("nperiodic_dimensions", pa.int32()), ("structure_features", pa.list_(pa.string())),
    ("attributes_json", pa.string()), ("shard", pa.string()),
    ("row_group", pa.int32()), ("row_in_group", pa.int32())
])


def shard_job(args):
    file, directory, revision = args
    file = Path(file)
    directory = Path(directory)
    out = directory / file.name
    receipt_path = out.with_suffix(".receipt.json")
    if receipt_path.exists() and out.exists():
        return json.loads(receipt_path.read_text())
    rejected = Counter()
    total = 0
    rows = 0
    started = time.time()
    batch_out = []
    group = 0
    with pq.ParquetWriter(out, SCHEMA, compression="zstd") as writer, open(out.with_suffix(".rejected.jsonl"), "w") as errors:
        for batch in pq.ParquetFile(file).iter_batches(batch_size=2048, columns=["material_id", "cif"]):
            for row in batch.to_pylist():
                total += 1
                try:
                    attr = attributes(row["cif"],row["material_id"],revision)
                except Exception as exc:
                    # Keep rejected IDs available through the raw CIF/export API.
                    reason = str(exc).splitlines()[0][:150]
                    rejected[reason] += 1
                    errors.write(json.dumps({"id": row["material_id"], "reason": reason}) + "\n")
                    continue
                entry = {k: attr.get(k) for k in SCHEMA.names}
                entry.update(id=row["material_id"], attributes_json=json.dumps(attr,separators=(",", ":")),
                             shard=file.name, row_group=group, row_in_group=len(batch_out))
                batch_out.append(entry)
                rows += 1
                if len(batch_out) >= 2048:
                    writer.write_table(pa.Table.from_pylist(batch_out, schema=SCHEMA))
                    batch_out = []
                    group += 1
        if batch_out:
            writer.write_table(pa.Table.from_pylist(batch_out,schema=SCHEMA))
    receipt = {"file": file.name, "total": total, "accepted": rows, "rejected": total-rows,
               "reasons": dict(rejected), "sha256": digest(out), "seconds": time.time()-started}
    receipt_path.write_text(json.dumps(receipt,indent=2))
    print(json.dumps(receipt),flush=True)
    return receipt


def build(root, revision, workers=2):
    release = Path(root) / "releases" / revision
    directory = release / "optimade"
    directory.mkdir(exist_ok=True)
    files = sorted((release / "upstream/data").glob("*.parquet"))
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        receipts = list(executor.map(shard_job, [(str(f),str(directory),revision) for f in files]))
    path = release / "optimade.duckdb"
    db = duckdb.connect(str(path))
    db.execute("SET threads=2")
    db.execute("SET memory_limit='4GB'")
    db.execute("SET temp_directory=?", [str(Path(root) / "tmp/optimade-index")])
    db.execute(f"CREATE OR REPLACE TABLE structures AS SELECT * EXCLUDE(attributes_json), row_number() OVER ()-1 AS row_id FROM read_parquet({sql_string(directory / '*.parquet')})")
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS opti_id ON structures(id)")
    db.execute("CREATE INDEX IF NOT EXISTS opti_rows ON structures(row_id)")
    db.execute("CHECKPOINT")
    db.close()
    manifest = {"revision": revision, "accepted": sum(r["accepted"] for r in receipts),
                "rejected": sum(r["rejected"] for r in receipts), "shards": receipts,
                "api_version": "1.2.0", "checked_at": time.time(),
                "normalization": "CIF cells and coordinates expanded with Gemmi; partial occupancies retained, near-unit occupancy rounded within 0.001. Unsupported or invalid CIFs excluded only from OPTIMADE; raw downloads remain available."}
    (release / "OPTIMADE_READY.json").write_text(json.dumps(manifest,indent=2))
    print(json.dumps({"status": "optimade_ready", "accepted": manifest["accepted"], "rejected": manifest["rejected"]}),flush=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--root",required=True)
    p.add_argument("--revision",required=True)
    p.add_argument("--workers",type=int,default=2)
    a = p.parse_args()
    build(a.root,a.revision,a.workers)
