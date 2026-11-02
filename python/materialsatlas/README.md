# MaterialsAtlas Python client

Download materials property datasets, source-filtered CIF archives, and
normalized OPTIMADE structures from [MaterialsAtlas](https://materialsatlas.org/data-downloads/).

```sh
pip install materialsatlas-datasets
# Optional pandas/Parquet support:
pip install 'materialsatlas-datasets[data]'
# Optional pymatgen Structure objects:
pip install 'materialsatlas-datasets[structures]'
```

## Named property datasets

```python
from materialsatlas import get_available_datasets, download_dataset, load_dataset

names = get_available_datasets()
path = download_dataset("band_gap")       # Cached Parquet + metadata receipt
df = load_dataset("curie_temperature")   # pandas DataFrame; install [data]
```

Full tables can contain millions of rows. Prefer Parquet batch reads or DuckDB
for large datasets instead of loading them entirely into pandas.

## Filtered records and matching CIFs

```python
from materialsatlas import MaterialsAtlas

with MaterialsAtlas() as atlas:
    job = atlas.export(
        property="band_gap",
        property_source="materials-project",
        elements=["Li", "O"],
        include_cifs=True,
        format="parquet",
    )
    print(job.id)
    files = job.download("./downloads")

    # All structures held by OQMD; this may be a large export.
    files = atlas.download_cifs(structure_source="oqmd", directory="./downloads")
```

Downloads support resume and SHA-256 verification. Repeated exports reuse the
server cache. Archives are not extracted automatically. Resume a queued export
with `atlas.job(export_id).download(...)`. Temporary exports normally expire
after seven days; the service returns the exact expiry.

Use `MaterialsAtlas(release="<revision>")` to pin a release. Every export retains
its resolved revision, query, row counts, distinct structure count, checksums,
methods, source identifiers, and licensing metadata. Multiple values per
structure are preserved, not averaged.

## OPTIMADE and pymatgen

```python
with MaterialsAtlas() as atlas:
    for record in atlas.optimade('elements HAS ALL "Li", "O" AND nelements=2'):
        print(record["id"], record["attributes"]["chemical_formula_reduced"])

    # Optional pymatgen integration: use an ID returned by the service.
    record = next(atlas.iter_structures(elements=["Si"], page_size=1))
    structure = atlas.get_structure(record["material_id"])
```

The OPTIMADE endpoint serves the active normalized release; raw CIFs remain
available for source records that cannot be normalized. This client provides
data access and optional pymatgen integration; it is not a replacement for
pymatgen's computational materials tools.

## Predictions and provenance

```python
with MaterialsAtlas() as atlas:
    tasks = atlas.predictions()
    path = atlas.download_prediction("lattice_thermal_conductivity__gga")
```

ML prediction tables are explicit, separate downloads. They are not experiments
or new DFT calculations. Source-property exports include only records labelled
open by the upstream publisher. Their original record-level terms still apply.

`property_source` selects who reported a property; `structure_source` selects
database membership; `origin_source` selects the stored CIF's recorded origin.
These are different filters. The first collection is AI4QC/MateriaViva-Open;
it aggregates records from original providers. Cite both the collection and
the relevant providers, and retain the downloaded attribution/licence fields.

## Configuration

- `MaterialsAtlas(base_url=..., release=..., cache_dir=..., timeout=120)`
- `MATERIALSATLAS_CACHE`: override the default `~/.cache/materialsatlas` directory.
- Network operations retry bounded transient failures. Expensive export failures
  and quota limits are reported explicitly.

Client software: MIT. Dataset licences are independent of the software licence.
