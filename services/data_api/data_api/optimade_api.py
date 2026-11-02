from datetime import datetime, timezone
import json
from pathlib import Path
import re
from urllib.parse import urlencode

import duckdb
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, Response
from optimade.models import StructureResourceAttributes
import pyarrow.parquet as pq

from . import config
from .optimade_filter import FIELDS, FilterCompiler


router = APIRouter()
API_VERSION = "1.2.0"
BASE = "/optimade/v1"
ALL_ATTRS = set(StructureResourceAttributes.model_fields)


def meta(request, returned=0, more=False, available=None, warnings=None):
    result = {"query": {"representation": request.url.path + ("?" + str(request.url.query) if request.url.query else "")},
              "schema": "https://schemas.optimade.org/openapi/v1.2.0/optimade.json",
              "api_version": API_VERSION, "more_data_available": more,
              "time_stamp": datetime.now(timezone.utc).isoformat(), "data_returned": returned,
              "implementation": {"name": "MaterialsAtlas", "version": "0.1.0",
                                 "homepage": "https://materialsatlas.org/data-downloads/",
                                 "source_url": "https://github.com/usccolumbia/matverse"}}
    if available is not None:
        result["data_available"] = available
    if warnings:
        result["warnings"] = [{"type": "warning", "title": "UnknownProviderProperty", "detail": "Unknown provider fields are treated as null: " + ', '.join(warnings)}]
    return result


def error(request, message, status=400):
    return JSONResponse({"meta": meta(request), "errors": [{"status": str(status), "title": "OPTIMADE request error", "detail": message}]},status_code=status)


def available():
    directory = config.release_dir()
    ready = directory / "OPTIMADE_READY.json"
    if not ready.exists():
        raise ValueError("OPTIMADE index is still being prepared")
    return directory, json.loads(ready.read_text())


def check_params(request, allowed):
    allowed = set(allowed) | {"api_hint", "response_format", "email_address"}
    for key in request.query_params:
        if key not in allowed:
            if key.startswith("_"):
                continue
            raise ValueError(f"Unknown query parameter: {key}")
    if request.query_params.get("response_format", "json") != "json":
        raise ValueError("Only response_format=json is supported")


@router.get("/optimade/versions")
def versions():
    return Response("version\n1\n", media_type="text/csv; header=present")


@router.get(BASE + "/info")
def info(request: Request):
    try:
        check_params(request, [])
        directory, ready = available()
    except (ValueError,OSError) as exc:
        return error(request,str(exc),503 if "prepared" in str(exc) else 400)
    return {"meta": meta(request,1), "data": {"id": "/", "type": "info", "attributes": {
        "api_version": API_VERSION,
        "available_api_versions": [{"url": config.BASE_URL + BASE, "version": API_VERSION}],
        "formats": ["json"], "available_endpoints": ["info", "structures", "links"],
        "entry_types_by_format": {"json": ["structures"]}, "is_index": False,
        "license": "https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/" + directory.name + "/licences.json"}}}


@router.get(BASE + "/info/structures")
def structure_info(request: Request):
    try:
        check_params(request, [])
    except ValueError as exc:
        return error(request,str(exc))
    schema = StructureResourceAttributes.model_json_schema()
    properties = {"id": {"description": "Stable MateriaViva material identifier", "type": "string", "sortable": True},
                  "type": {"description": "Resource type: structures", "type": "string", "sortable": False}}
    def kind(field):
        value = field.get("type")
        if value is None:
            value = next((x.get("type") for x in field.get("anyOf",[]) if x.get("type") not in (None,"null")), "string")
        return {"array": "list", "object": "dictionary", "number": "float"}.get(value,value)
    for name, field in schema["properties"].items():
        properties[name] = {"description": field.get("description", name), "type": kind(field),
                            "sortable": name in FIELDS and name not in ("elements", "elements_ratios", "structure_features", "dimension_types", "assemblies"),
                            "queryable": name in FIELDS}
        if name == "last_modified":
            properties[name]["type"] = "timestamp"
    return {"meta": meta(request,1), "data": {"id": "structures", "type": "info", "properties": properties,
            "description": "MateriaViva Open structures normalized from stored CIFs. Raw CIF downloads, source provenance and export archives are available at /api/data/v1. Unsupported CIFs are excluded from this normalized interface and retained in raw downloads.",
            "formats": ["json"], "output_fields_by_format": {"json": list(properties)}}}


def load_attrs(directory, records):
    grouped = {}
    out = {}
    for record in records:
        grouped.setdefault((record["shard"],record["row_group"]),[]).append(record)
    for (shard,group), selected in grouped.items():
        table = pq.ParquetFile(directory / "optimade" / shard).read_row_group(group,columns=["id","attributes_json"])
        for row in selected:
            i = row["row_in_group"]
            if table["id"][i].as_py() != row["id"]:
                raise ValueError("Normalized structure index integrity failure")
            out[row["id"]] = json.loads(table["attributes_json"][i].as_py())
    return out


def resources(request, identifier=None):
    try:
        check_params(request, {"filter", "response_fields", "sort", "page_limit", "page_offset", "page_number", "include"})
        directory, ready = available()
        q = request.query_params
        limit = int(q.get("page_limit", 20))
        offset = int(q.get("page_offset", 0))
        if "page_number" in q:
            offset = (int(q["page_number"])-1)*limit
        if limit<0 or limit>200:
            return error(request,"page_limit must be between 0 and 200",403)
        if offset<0:
            raise ValueError("Invalid pagination offset")
        if q.get("include", "references") not in ("", "references"):
            raise ValueError("Unknown relationship in include")
        sql, args, unknown = FilterCompiler().compile(q.get("filter", ""))
        if identifier is not None:
            sql = "id = ?"
            args = [identifier]
        requested = q.get("response_fields")
        fields = {x.strip() for x in requested.split(",") if x.strip()} if requested is not None else ALL_ATTRS
        for f in fields - ALL_ATTRS - {"id","type"}:
            if not f.startswith("_"):
                raise ValueError(f"Unknown response field: {f}")
            unknown.append(f)
        order = []
        for item in q.get("sort", "id").split(","):
            name = item.lstrip("-")
            if name not in FIELDS or name in ("elements", "elements_ratios", "structure_features", "dimension_types", "assemblies"):
                raise ValueError(f"Unsupported sorting property: {name}")
            order.append(FIELDS[name] + (" DESC" if item.startswith("-") else " ASC"))
        if "id" not in q.get("sort", "id").split(","):
            order.append("id ASC")
        with duckdb.connect(str(directory / "optimade.duckdb"),read_only=True) as db:
            db.execute("SET threads=1")
            db.execute("SET memory_limit='1GB'")
            matched = db.execute(f"SELECT count(*) FROM structures WHERE {sql}",args).fetchone()[0]
            rows = db.execute(f"SELECT id,shard,row_group,row_in_group FROM structures WHERE {sql} ORDER BY {','.join(order)} LIMIT ? OFFSET ?",[*args,1 if identifier else limit,0 if identifier else offset]).fetch_arrow_table().to_pylist()
        attributes = load_attrs(directory,rows)
        data = [{"id": row["id"], "type": "structures", "attributes": {f:attributes[row["id"]].get(f) for f in fields if f not in ("id","type")},
                 "links": {"self": config.BASE_URL + BASE + "/structures/" + row["id"]}} for row in rows]
        more = not identifier and limit > 0 and offset+len(data)<matched
        next_url = None
        if more:
            next_params = dict(q)
            next_params.pop("page_number",None)
            next_params.update(page_offset=offset+len(data),page_limit=limit)
            next_url = config.BASE_URL + BASE + "/structures?" + urlencode(next_params)
        return {"meta": meta(request,matched,more,ready["accepted"],unknown),
                "links": {"self": config.BASE_URL + str(request.url.path) + ("?" + str(q) if q else ""), "next": next_url},
                "data": (data[0] if data else None) if identifier else data}
    except (ValueError,OSError) as exc:
        return error(request,str(exc),503 if "prepared" in str(exc) else 400)
    except duckdb.Error:
        return error(request,"Filter is incompatible with the selected property type")


@router.get(BASE + "/structures")
def structures(request: Request):
    return resources(request)


@router.get(BASE + "/structures/{identifier}")
def structure(request: Request,identifier: str):
    return resources(request,identifier)


@router.get(BASE + "/links")
def links(request: Request):
    return {"meta": meta(request,0,False,0), "links": {"next": None}, "data": []}


@router.get("/optimade/{version}/{tail:path}")
def version_alias(request: Request,version: str,tail: str):
    if version == "v1":
        return error(request,"Endpoint not found",404)
    if version not in ("v1.2", "v1.2.0"):
        return error(request,"Unsupported OPTIMADE API version",553)
    from fastapi.responses import RedirectResponse
    return RedirectResponse(config.BASE_URL + BASE + "/" + tail + ("?" + str(request.url.query) if request.url.query else ""),status_code=307)
