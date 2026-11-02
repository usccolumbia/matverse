"""Two bounded processes, persistent jobs, leases, restart recovery and cache TTL."""
import json
import multiprocessing
import os
import re
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

from . import config, state


def size(path):
    return sum(p.stat().st_size for p in Path(path).rglob("*") if p.is_file()) if Path(path).exists() else 0


def clean():
    now = time.time()
    with state.connect() as db:
        db.execute("BEGIN IMMEDIATE")
        expired = db.execute("SELECT id FROM jobs WHERE status='complete' AND expires<?", (now,)).fetchall()
        for row in expired:
            shutil.rmtree(config.ROOT / "exports" / row["id"], ignore_errors=True)
            db.execute("UPDATE jobs SET status='expired', result=NULL WHERE id=?", (row["id"],))
        # Keep ready download URLs valid until their advertised expiry; reject new jobs
        # if the bounded cache cannot hold them instead of silently evicting downloads.
        active = {r[0] + '-' + r[1] for r in db.execute("SELECT id,lease FROM jobs WHERE status='running' AND lease IS NOT NULL")}
        for path in (config.ROOT / "tmp").iterdir():
            if path.is_dir() and re.fullmatch(r"[a-f0-9]{32}-[a-f0-9]{32}",path.name) and path.name not in active and now-path.stat().st_mtime > 600:
                shutil.rmtree(path, ignore_errors=True)


def loop():
    stopping = False
    child = None

    def stop(signum, frame):
        nonlocal stopping
        stopping = True
        if child and child.poll() is None:
            child.terminate()

    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    last_clean = 0
    while not stopping:
        if time.time()-last_clean > 60:
            clean()
            last_clean = time.time()
        job = state.claim()
        if not job:
            time.sleep(2)
            continue
        identity, lease = job["id"], job["lease"]
        work = config.ROOT / "tmp" / f"{identity}-{lease}"
        work.mkdir(parents=True, exist_ok=True)
        error = None
        try:
            if shutil.disk_usage(config.ROOT).free < config.MIN_FREE:
                raise ValueError("Insufficient free storage; retry later")
            if size(config.ROOT) > config.TOTAL_LIMIT - config.MAX_JOB_BYTES:
                raise ValueError("Service storage budget reached; retry later")
            if size(config.ROOT / "exports") > config.CACHE_LIMIT - config.MAX_JOB_BYTES:
                raise ValueError("Download cache is full; retry after existing exports expire")
            log_path = config.ROOT / "logs" / f"export-{identity}.log"
            with open(log_path, "w") as log:
                child = subprocess.Popen([sys.executable, "-m", "data_api.exporter", identity, lease, str(work)], stdout=log, stderr=subprocess.STDOUT)
                started = time.time()
                while child.poll() is None:
                    state.update(identity, lease)
                    if time.time()-started > config.MAX_JOB_SECONDS:
                        error = "Export exceeded the time limit; narrow the query"
                    elif size(work) > config.MAX_JOB_BYTES or size(config.ROOT / "tmp") > config.WORK_LIMIT:
                        error = "Export exceeded the working-space limit; narrow the query"
                    elif shutil.disk_usage(config.ROOT).free < config.MIN_FREE:
                        error = "Insufficient free storage; retry later"
                    if error or stopping:
                        child.terminate()
                        try:
                            child.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            child.kill(); child.wait()
                        break
                    time.sleep(3)
                if child.returncode != 0:
                    raise ValueError(error or "Export failed; reference this export ID when contacting MaterialsAtlas")
            if stopping:
                # Keep a running lease; another worker will reclaim it after expiry.
                continue
            manifest = json.loads((work / "manifest.json").read_text())
            result_size = size(work)
            with state.connect() as db:
                db.execute("BEGIN IMMEDIATE")
                current = db.execute("SELECT status,lease FROM jobs WHERE id=?", (identity,)).fetchone()
                if current["lease"] != lease or current["status"] != "running":
                    raise ValueError("Export lease changed")
                if size(config.ROOT / "exports") + result_size > config.CACHE_LIMIT:
                    raise ValueError("Download cache is full; retry later")
                final = config.ROOT / "exports" / identity
                if final.exists():
                    shutil.rmtree(final)
                os.replace(work, final)
                now = time.time()
                db.execute("UPDATE jobs SET status='complete',updated=?,expires=?,result=?,progress='Ready to download' WHERE id=? AND lease=?", (now,now+config.EXPORT_TTL,json.dumps(manifest),identity,lease))
            print(json.dumps({"event": "export_complete", "id": identity, "rows": manifest["rows"], "bytes": result_size}), flush=True)
        except Exception as exc:
            print(json.dumps({"event": "export_failed", "id": identity, "error": str(exc)}), flush=True)
            if not stopping:
                state.update(identity, lease, status="failed", error=str(exc))
        finally:
            child = None
            if work.exists():
                shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    for name in ["state", "exports", "tmp", "logs"]:
        (config.ROOT / name).mkdir(parents=True, exist_ok=True)
    state.initialize()
    slots = min(2, max(1, int(os.environ.get("DATA_API_WORKERS", "2"))))
    children = [multiprocessing.Process(target=loop) for _ in range(slots)]
    for child in children:
        child.start()
    def shutdown(signum, frame):
        for child in children:
            if child.is_alive():
                child.terminate()
        for child in children:
            child.join(timeout=20)
        sys.exit(0)
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    for child in children:
        child.join()
    sys.exit(1)  # Compose restarts the worker if a child unexpectedly exits.
