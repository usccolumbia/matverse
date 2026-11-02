"""Matbench-style convenience functions for named property datasets."""
from .client import MaterialsAtlas


def get_available_datasets(*,release=None,base_url="https://materialsatlas.org"):
    """Return names of property tables with public rows in the selected release."""
    with MaterialsAtlas(release=release,base_url=base_url) as atlas:
        return [p["name"] for p in atlas.properties() if p["rows"]]


def download_dataset(name,*,directory=None,release=None,base_url="https://materialsatlas.org"):
    """Download a verified Parquet property table and return its local path."""
    with MaterialsAtlas(release=release,base_url=base_url) as atlas:
        return atlas.download_property(name,directory)


def load_dataset(name,*,release=None,base_url="https://materialsatlas.org",**read_parquet_kwargs):
    """Return a pandas DataFrame; requires materialsatlas[data].

    Entire large tables can exceed available memory. Use download_dataset and
    PyArrow/DuckDB batch reads instead when processing millions of rows.
    """
    try:
        import pandas as pd
    except ImportError as exc:
        raise ImportError("Install materialsatlas[data] to load pandas DataFrames") from exc
    path=download_dataset(name,release=release,base_url=base_url)
    return pd.read_parquet(path,**read_parquet_kwargs)
