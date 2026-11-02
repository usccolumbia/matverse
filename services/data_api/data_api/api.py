from contextlib import asynccontextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import time
from urllib.parse import quote

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles

from . import config, state
from .query import Selection, catalog, connection, get_cifs, resolve, structure_where


@asynccontextmanager
async def lifespan(app):
    state.initialize()
    yield


app = FastAPI(title="MaterialsAtlas Data API", version="0.1.0", lifespan=lifespan,
              description="Versioned source-property datasets, labelled ML predictions, and queued CIF exports. Public property downloads retain only publisher-labelled open rows.",
              docs_url=config.PREFIX + "/docs", redoc_url=None,
              openapi_url=config.PREFIX + "/openapi.json")


@app.exception_handler(ValueError)
def invalid(request, exc):
    return JSONResponse({"detail": str(exc)}, status_code=400)


@app.middleware("http")
async def common_headers(request, call_next):
    started = time.time()
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["X-Response-Time"] = f"{time.time()-started:.3f}s"
    if request.url.path.startswith("/optimade"):
        response.headers["Access-Control-Allow-Origin"] = "*"
    return response


def release(value=None):
    try:
        return resolve(Selection(release=value)).release
    except FileNotFoundError:
        raise HTTPException(503, "Dataset is being prepared; retry later")


def file_response(path, sha256=None, media_type="application/octet-stream"):
    path = Path(path)
    if not path.is_file():
        raise HTTPException(404, "Artifact is unavailable")
    relative = path.resolve().relative_to(config.ROOT.resolve())
    headers = {"Content-Disposition": f'attachment; filename="{path.name}"',
               "Cache-Control": "public, max-age=3600", "Accept-Ranges": "bytes"}
    if sha256:
        headers["ETag"] = f'"{sha256}"'
        headers["X-Checksum-SHA256"] = sha256
    if config.USE_ACCEL:
        headers["X-Accel-Redirect"] = "/_materials_data/" + quote(str(relative), safe="/")
        return Response(headers=headers, media_type=media_type)
    return FileResponse(path, headers=headers, media_type=media_type)


@app.get(config.PREFIX + "/health")
def health():
    try:
        rev = config.current_revision()
        ready = json.loads((config.release_dir(rev) / "READY.json").read_text())
        return {"status": "ready", "revision": rev, "structures": ready["structures"]}
    except (OSError, ValueError):
        return JSONResponse({"status": "preparing"}, status_code=503)


@app.get(config.PREFIX + "/collections")
def collections():
    rev = release()
    data = catalog(rev)
    versions = sorted(p.name for p in (config.ROOT / "releases").iterdir() if (p / "READY.json").exists())
    return {"collections": [{"id": config.COLLECTION, "title": "MateriaViva Open",
                              "release": rev, "available_releases": versions,
                              "structures": data["structures"], "properties": len(data["properties"]),
                              "public_property_rows": data["public_property_rows"],
                              "upstream_property_rows": data["upstream_property_rows"],
                              "prediction_tasks": len(data["predictions"]), "prediction_rows": data["prediction_rows"],
                              "source": data["upstream"], "licence_policy": data["licence_policy"]}]}


@app.get(config.PREFIX + "/properties")
def properties(revision: str | None = None):
    rev = release(revision)
    return {"release": rev, "properties": catalog(rev)["properties"]}


@app.get(config.PREFIX + "/properties/{name}")
def property_info(name: str, revision: str | None = None):
    rev = release(revision)
    item = next((p for p in catalog(rev)["properties"] if p["name"] == name), None)
    if not item:
        raise HTTPException(404, "Property not found")
    return {"release": rev, **item,
            "download_url": f"{config.BASE_URL}{config.PREFIX}/properties/{quote(name)}/download?revision={rev}" if item["rows"] else None}


@app.get(config.PREFIX + "/properties/{name}/download")
def property_download(name: str, revision: str | None = None):
    item = property_info(name, revision)
    if not item["rows"]:
        raise HTTPException(404, "This property has no publisher-labelled open rows in this release")
    state.increment("property_download_requests")
    return file_response(config.release_dir(item["release"]) / "published/properties" / f"{name}.parquet", item["sha256"])


@app.get(config.PREFIX + "/predictions")
def predictions(revision: str | None = None):
    rev = release(revision)
    return {"release": rev, "warning": "ML estimates, not experimental measurements or new DFT calculations",
            "predictions": catalog(rev)["predictions"]}


@app.get(config.PREFIX + "/predictions/{name}")
def prediction_info(name: str, revision: str | None = None):
    rev = release(revision)
    item = next((p for p in catalog(rev)["predictions"] if p["name"] == name), None)
    if not item:
        raise HTTPException(404, "Completed prediction task not found")
    return {"release": rev, **item,
            "download_url": f"{config.BASE_URL}{config.PREFIX}/predictions/{quote(name)}/download?revision={rev}"}


@app.get(config.PREFIX + "/predictions/{name}/download")
def prediction_download(name: str, revision: str | None = None):
    item = prediction_info(name, revision)
    state.increment("prediction_download_requests")
    return file_response(config.release_dir(item["release"]) / "upstream/predictions" / f"{name}.parquet", item["sha256"])


@app.get(config.PREFIX + "/sources")
def sources(revision: str | None = None):
    rev = release(revision)
    return {"release": rev, "sources": catalog(rev)["sources"],
            "note": "Structure source means database membership, not necessarily the origin of the stored CIF. Counts overlap across sources."}


@app.get(config.PREFIX + "/structures")
def structures(revision: str | None = None, structure_source: str | None = None,
               origin_source: str | None = None, origin_open: bool | None = None,
               formula: str | None = None, elements: str | None = None,
               n_sites_min: int | None = Query(None, ge=1), n_sites_max: int | None = Query(None, ge=1),
               after: int = Query(-1, ge=-1), limit: int = Query(20, ge=1, le=200)):
    s = resolve(Selection(release=revision, structure_source=structure_source, origin_source=origin_source,
                          origin_open=origin_open, formula=formula, elements=elements.split(",") if elements else [],
                          n_sites_min=n_sites_min,n_sites_max=n_sites_max))
    clauses, args = structure_where(s)
    clauses.append("s.row_id > ?")
    args += [after,limit+1]
    with connection(s.release) as db:
        rows = db.execute("SELECT * EXCLUDE(shard,row_group,row_in_group) FROM structures s WHERE " + " AND ".join(clauses) + " ORDER BY row_id LIMIT ?", args).fetch_arrow_table().to_pylist()
    more = len(rows)>limit
    rows = rows[:limit]
    return {"release": s.release, "structures": rows,
            "next_after": rows[-1]["row_id"] if more else None}


@app.get(config.PREFIX + "/structures/{material_id}/cif")
def cif_download(material_id: str, revision: str | None = None):
    rev = release(revision)
    if not re.fullmatch(r"[A-Za-z0-9_.:+-]{1,150}", material_id):
        raise HTTPException(400, "Invalid material ID")
    with connection(rev) as db:
        rows = db.execute("SELECT material_id,shard,row_group,row_in_group FROM structures WHERE material_id=?", [material_id]).fetch_arrow_table().to_pylist()
    if not rows:
        raise HTTPException(404, "Structure not found")
    return Response(get_cifs(rev, rows)[material_id], media_type="chemical/x-cif",
                    headers={"Content-Disposition": f'attachment; filename="{material_id}.cif"'})


def public_job(job):
    result = json.loads(job["result"]) if job.get("result") else None
    status = job["status"]
    if status == "complete" and job["expires"] <= time.time():
        status = "expired"
        result = None
    payload = {"id": job["id"], "status": status, "progress": job["progress"],
               "error": job["error"], "query": json.loads(job["query"]),
               "created_at": datetime.fromtimestamp(job["created"], timezone.utc).isoformat(),
               "expires_at": datetime.fromtimestamp(job["expires"], timezone.utc).isoformat() if job["expires"] else None,
               "status_url": f"{config.BASE_URL}{config.PREFIX}/exports/{job['id']}"}
    if result:
        payload["result"] = result
        payload["files"] = [{**f, "url": f"{config.BASE_URL}{config.PREFIX}/exports/{job['id']}/files/{quote(f['name'])}"} for f in result["files"]]
        payload["manifest_url"] = f"{config.BASE_URL}{config.PREFIX}/exports/{job['id']}/files/manifest.json"
    return payload


@app.post(config.PREFIX + "/exports")
def create_export(selection: Selection, request: Request):
    selection = resolve(selection)
    try:
        job, reused = state.submit(selection, request.client.host if request.client else "unknown")
    except ValueError as exc:
        raise HTTPException(429, str(exc), headers={"Retry-After": "60"})
    return JSONResponse({**public_job(job), "cache_reused": reused}, status_code=200 if job["status"] == "complete" else 202)


@app.get(config.PREFIX + "/exports/{identity}")
def export_status(identity: str):
    if not re.fullmatch(r"[a-f0-9]{32}", identity):
        raise HTTPException(404, "Export not found")
    job = state.get(identity)
    if not job:
        raise HTTPException(404, "Export not found")
    return public_job(job)


@app.get(config.PREFIX + "/exports/{identity}/files/{name}")
def export_download(identity: str, name: str):
    payload = export_status(identity)
    if payload["status"] == "expired":
        raise HTTPException(410, "Export expired; submit the same query to rebuild it")
    if payload["status"] != "complete":
        raise HTTPException(409, "Export is not ready")
    allowed = {f["name"]: f for f in payload["result"]["files"]}
    allowed["manifest.json"] = {}
    if name not in allowed:
        raise HTTPException(404, "File not found")
    state.increment("export_download_requests")
    return file_response(config.ROOT / "exports" / identity / name, allowed[name].get("sha256"))


@app.get(config.PREFIX + "/metrics")
def metrics():
    with state.connect() as db:
        counts = {row[0]: row[1] for row in db.execute("SELECT status,count(*) FROM jobs GROUP BY status")}
        counters = {row[0]: row[1] for row in db.execute("SELECT key,value FROM metrics")}
        stale = db.execute("SELECT count(*) FROM jobs WHERE status='running' AND updated<?", (time.time()-180,)).fetchone()[0]
    return {"jobs": counts, "requests": counters, "stale_workers": stale}


# OPTIMADE is an independent protocol surface; archive exports remain in /api/data/v1.
try:
    from .optimade_api import router as optimade_router
    app.include_router(optimade_router)
except ImportError:
    pass  # Ingestion-only images can be built before the protocol module is present.

app.mount("/data-downloads", StaticFiles(directory=Path(__file__).parent.parent / "static", html=True), name="data-downloads")
