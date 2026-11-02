"""MaterialsAtlas data downloads and OPTIMADE access."""
from .client import MaterialsAtlas, ExportJob, MaterialsAtlasError
from .datasets import download_dataset, load_dataset, get_available_datasets

__version__ = "0.1.0"
__all__ = ["MaterialsAtlas", "ExportJob", "MaterialsAtlasError", "download_dataset", "load_dataset", "get_available_datasets"]
