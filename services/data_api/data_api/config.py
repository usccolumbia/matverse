import os
from pathlib import Path

ROOT = Path(os.environ.get("DATA_API_ROOT", "/data/materialsatlas-data"))
BASE_URL = os.environ.get("DATA_API_BASE_URL", "https://materialsatlas.org").rstrip("/")
PREFIX = "/api/data/v1"
COLLECTION = "materiaviva-open"
EXPORT_TTL = int(os.environ.get("DATA_API_EXPORT_TTL", 7 * 86400))
CACHE_LIMIT = int(os.environ.get("DATA_API_CACHE_BYTES", 30_000_000_000))
WORK_LIMIT = int(os.environ.get("DATA_API_WORK_BYTES", 20_000_000_000))
TOTAL_LIMIT = int(os.environ.get("DATA_API_TOTAL_BYTES", 100_000_000_000))
MAX_JOB_BYTES = int(os.environ.get("DATA_API_MAX_JOB_BYTES", 8_000_000_000))
MIN_FREE = int(os.environ.get("DATA_API_MIN_FREE_BYTES", 10_000_000_000))
MAX_JOB_SECONDS = int(os.environ.get("DATA_API_JOB_TIMEOUT", 3600))
PART_CIFS = int(os.environ.get("DATA_API_PART_CIFS", 100_000))
USE_ACCEL = os.environ.get("DATA_API_ACCEL", "0") == "1"


def current_revision():
    return (ROOT / "current").read_text().strip()


def release_dir(revision=None):
    import re
    revision = revision or current_revision()
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Release must be a full 40-character revision")
    path = ROOT / "releases" / revision
    if not (path / "READY.json").is_file():
        raise ValueError("Release is not available")
    return path
