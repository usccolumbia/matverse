"""Download an immutable upstream release, verify bytes, and retain receipts.

This command uses only the standard library and does not publish a release.
Run build_catalog after it succeeds to validate and activate the release.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.request


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def mirror(inventory, root, workers=4):
    meta = json.loads(Path(inventory).read_text())
    revision = meta["revision"]
    release = Path(root) / "releases" / revision
    release.mkdir(parents=True, exist_ok=True)
    entries = [f for f in meta["files"] if f["type"] == "file"]
    started = time.time()

    def fetch(entry):
        rel = Path(entry["path"])
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError("Unsafe upstream path")
        dst = release / "upstream" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        expected = entry.get("lfs", {}).get("oid")
        if dst.exists() and dst.stat().st_size == entry["size"]:
            actual = digest(dst)
            if expected is None or actual == expected:
                return {"path": str(rel), "bytes": dst.stat().st_size, "sha256": actual}
        url = f'https://huggingface.co/datasets/{meta["repo"]}/resolve/{revision}/{entry["path"]}'
        partial = dst.with_name(dst.name + ".partial")
        for attempt in range(5):
            try:
                with urllib.request.urlopen(url, timeout=120) as source, open(partial, "wb") as out:
                    for block in iter(lambda: source.read(4 * 1024 * 1024), b""):
                        out.write(block)
                actual = digest(partial)
                if partial.stat().st_size != entry["size"] or (expected and actual != expected):
                    raise ValueError(f"Integrity mismatch: {rel}")
                if not expected:
                    body = partial.read_bytes()
                    git_hash = hashlib.sha1(b"blob " + str(len(body)).encode() + b"\0" + body).hexdigest()
                    if git_hash != entry["oid"]:
                        raise ValueError(f"Git blob mismatch: {rel}")
                os.replace(partial, dst)
                print(json.dumps({"downloaded": str(rel), "bytes": dst.stat().st_size}), flush=True)
                return {"path": str(rel), "bytes": dst.stat().st_size, "sha256": actual}
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(min(2 ** attempt, 10))

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        receipts = list(executor.map(fetch, entries))
    result = {"revision": revision, "repo": meta["repo"], "files": receipts,
              "bytes": sum(x["bytes"] for x in receipts), "seconds": time.time() - started}
    (release / "source_inventory.json").write_text(json.dumps(meta, indent=2))
    (release / "mirror_receipt.json").write_text(json.dumps(result, indent=2))
    print(json.dumps({"status": "mirror_verified", "revision": revision,
                      "files": len(receipts), "bytes": result["bytes"]}), flush=True)
    return release


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    mirror(args.inventory, args.root, args.workers)
