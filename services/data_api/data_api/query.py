from functools import lru_cache
import json
import re
from typing import Literal

import duckdb
import pyarrow.parquet as pq
from pydantic import BaseModel, ConfigDict, Field, model_validator

from . import config


class Selection(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    collection: Literal["materiaviva-open"] = "materiaviva-open"
    release: str | None = None
    property: str | None = Field(default=None, max_length=150)
    prediction: str | None = Field(default=None, max_length=200)
    property_source: str | None = Field(default=None, max_length=100)
    structure_source: str | None = Field(default=None, max_length=100)
    origin_source: str | None = Field(default=None, max_length=100)
    origin_open: bool | None = None
    method: str | None = Field(default=None, max_length=300)
    formula: str | None = Field(default=None, max_length=150)
    elements: list[str] = Field(default_factory=list, max_length=20)
    n_sites_min: int | None = Field(default=None, ge=1)
    n_sites_max: int | None = Field(default=None, ge=1)
    value_min: float | None = Field(default=None, allow_inf_nan=False)
    value_max: float | None = Field(default=None, allow_inf_nan=False)
    material_ids: list[str] = Field(default_factory=list, max_length=10000)
    include_cifs: bool = False
    format: Literal["parquet", "csv.gz"] = "parquet"
    limit: int | None = Field(default=None, ge=1, le=10_903_588)

    @model_validator(mode="after")
    def validate_selection(self):
        if self.property and self.prediction:
            raise ValueError("Choose a source property or an ML prediction, not both")
        if (self.property_source or self.method) and not self.property:
            raise ValueError("property_source and method apply only to source property tables")
        if (self.value_min is not None or self.value_max is not None) and not (self.property or self.prediction):
            raise ValueError("Value filters require a property or prediction")
        if self.value_min is not None and self.value_max is not None and self.value_min > self.value_max:
            raise ValueError("value_min exceeds value_max")
        if self.n_sites_min and self.n_sites_max and self.n_sites_min > self.n_sites_max:
            raise ValueError("n_sites_min exceeds n_sites_max")
        if any(not re.fullmatch(r"[A-Z][a-z]?", x) for x in self.elements):
            raise ValueError("elements must contain chemical element symbols")
        if any(not re.fullmatch(r"[A-Za-z0-9_.:+-]{1,150}", x) for x in self.material_ids):
            raise ValueError("Invalid material ID")
        self.elements = sorted(set(self.elements))
        self.material_ids = sorted(set(self.material_ids))
        return self


@lru_cache(maxsize=4)
def catalog(revision):
    return json.loads((config.release_dir(revision) / "catalog.json").read_text())


def resolve(selection):
    if not selection.release or selection.release == "latest":
        selection = selection.model_copy(update={"release": config.current_revision()})
    elif re.fullmatch(r"[0-9a-f]{8,39}", selection.release):
        versions = [x.name for x in (config.ROOT / "releases").iterdir()
                    if x.name.startswith(selection.release) and (x / "READY.json").exists()]
        if len(versions) != 1:
            raise ValueError("Release prefix is unavailable or ambiguous")
        selection = selection.model_copy(update={"release": versions[0]})
    data = catalog(selection.release)
    if selection.property:
        item = next((p for p in data["properties"] if p["name"] == selection.property), None)
        if item is None:
            raise ValueError("Unknown property; see /properties")
        if selection.property_source and selection.property_source not in item.get("upstream_sources", item["sources"]):
            raise ValueError("Source is not present in this property dataset")
        if selection.method and selection.method not in item["methods"]:
            raise ValueError("Method is not present in this public property dataset")
        if item["kind"] == "text" and (selection.value_min is not None or selection.value_max is not None):
            raise ValueError("Numeric filters are unavailable for text properties")
    if selection.prediction and selection.prediction not in {p["name"] for p in data["predictions"]}:
        raise ValueError("Unknown or unfinished prediction task; see /predictions")
    if selection.structure_source and selection.structure_source not in {p["name"] for p in data["sources"]}:
        raise ValueError("Unknown structure source; see /sources")
    return selection


def connection(revision, temp_dir=None):
    db = duckdb.connect(str(config.release_dir(revision) / "index.duckdb"), read_only=True)
    db.execute("SET threads=1")
    db.execute("SET memory_limit='2GB'")
    if temp_dir:
        db.execute("SET temp_directory=?", [str(temp_dir)])
        db.execute("SET max_temp_directory_size='4GB'")
    return db


def structure_where(s, alias="s"):
    clauses = []
    args = []
    for key, column in [("structure_source", "open_sources"), ("origin_source", "origin_source"),
                        ("formula", "formula"), ("origin_open", "origin_open")]:
        value = getattr(s, key)
        if value is not None:
            clauses.append(f"list_contains({alias}.{column}, ?)" if key == "structure_source" else f"{alias}.{column} = ?")
            args.append(value)
    for element in s.elements:
        clauses.append(f"list_contains({alias}.elements, ?)")
        args.append(element)
    for key, op in [("n_sites_min", ">="), ("n_sites_max", "<=")]:
        if getattr(s, key) is not None:
            clauses.append(f"{alias}.n_sites {op} ?")
            args.append(getattr(s, key))
    if s.material_ids:
        clauses.append(f"{alias}.material_id IN (SELECT unnest(?))")
        args.append(s.material_ids)
    return clauses, args


def selection_sql(s, include_nonopen=False):
    directory = config.release_dir(s.release)
    clauses, args = structure_where(s)
    if s.property or s.prediction:
        folder = "properties" if s.property else "predictions"
        name = s.property or s.prediction
        file = directory / "upstream" / folder / f"{name}.parquet"
        args = [str(file)] + args
        relation = "read_parquet(?) p JOIN structures s USING(material_id)"
        if s.property and not include_nonopen:
            clauses.append("p.licence_class = 'open'")
        if s.property_source:
            clauses.append("p.source = ?")
            args.append(s.property_source)
        if s.method:
            clauses.append("p.method = ?")
            args.append(s.method)
        value_col = "value"
        if s.prediction:
            cols = next(x["columns"] for x in catalog(s.release)["predictions"] if x["name"] == name)
            candidates = [c for c in cols if c != "material_id"]
            value_col = "value" if "value" in cols else candidates[0]
        quoted = '"' + value_col.replace('"', '""') + '"'
        for key, op in [("value_min", ">="), ("value_max", "<=")]:
            if getattr(s, key) is not None:
                clauses.append(f"TRY_CAST(p.{quoted} AS DOUBLE) {op} ?")
                args.append(getattr(s, key))
        fields = "p.*, s.formula, s.chemical_system, s.licence AS structure_licence, s.licence_from AS structure_licence_from, s.origin_source AS structure_origin_source, s.origin_open, s.open_sources, s.open_source_ids"
    else:
        relation = "structures s"
        fields = "s.* EXCLUDE(shard, row_group, row_in_group, row_id)"
    where = " AND ".join(clauses) if clauses else "TRUE"
    sql = f"SELECT {fields} FROM {relation} WHERE {where}"
    if s.limit:
        # Limit is deliberately applied to deterministic output records, not distinct structures.
        sql += " ORDER BY s.row_id"
        if s.property:
            sql += ", p.source, p.method, p.source_native_id, p.value"
        sql += f" LIMIT {s.limit}"
    return sql, args


def get_cifs(revision, records):
    """Read only the row groups required by an indexed preview."""
    grouped = {}
    for record in records:
        grouped.setdefault((record["shard"], record["row_group"]), []).append(record)
    result = {}
    for (shard, group), selected in grouped.items():
        pf = pq.ParquetFile(config.release_dir(revision) / "upstream/data" / shard)
        table = pf.read_row_group(group, columns=["material_id", "cif"])
        for row in selected:
            i = row["row_in_group"]
            if table["material_id"][i].as_py() != row["material_id"]:
                raise ValueError("Structure index integrity mismatch")
            result[row["material_id"]] = table["cif"][i].as_py()
    return result
