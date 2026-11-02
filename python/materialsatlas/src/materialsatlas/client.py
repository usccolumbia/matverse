from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import quote, urljoin, urlparse

import httpx


class MaterialsAtlasError(RuntimeError):
    """An API, export, or integrity error with actionable service context."""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


class MaterialsAtlas:
    """Client for public datasets hosted by MaterialsAtlas.

    Prefer a context manager to close network connections. Set ``release`` to
    a recorded revision for reproducibility. Predictions must be requested
    explicitly and are never substituted for source property records.
    """

    def __init__(self, base_url="https://materialsatlas.org", *, release=None,
                 cache_dir=None, timeout=120.0, transport=None):
        self.base_url = base_url.rstrip("/")
        self.api_url = self.base_url + "/api/data/v1"
        self.release = release
        self.cache_dir = Path(cache_dir or os.environ.get("MATERIALSATLAS_CACHE", Path.home()/".cache/materialsatlas"))
        self.http = httpx.Client(timeout=timeout, follow_redirects=True, transport=transport,
                                 headers={"User-Agent": "materialsatlas-python/0.1.0"})

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        self.http.close()

    def _url(self, url):
        target = urljoin(self.base_url + "/", url)
        if urlparse(target).netloc != urlparse(self.base_url).netloc:
            raise MaterialsAtlasError("Server returned a download URL on an unexpected host")
        return target

    def _request(self, method, path, **kwargs):
        url = self._url(path) if path.startswith(("http", "/")) else self.api_url + "/" + path
        for attempt in range(4):
            try:
                response = self.http.request(method,url,**kwargs)
            except httpx.TransportError as exc:
                if attempt == 3:
                    raise MaterialsAtlasError(f"Could not reach MaterialsAtlas: {exc}") from exc
                time.sleep(2**attempt)
                continue
            if response.status_code in (429,502,503,504) and attempt<3:
                delay=response.headers.get("Retry-After",str(2**attempt))
                time.sleep(min(60,float(delay) if delay.isdigit() else 2**attempt))
                continue
            try:
                data=response.json()
            except ValueError:
                data={"detail":f"HTTP {response.status_code}"}
            if response.is_error:
                raise MaterialsAtlasError(str(data.get("detail",data.get("errors",data))))
            return data
        raise MaterialsAtlasError("Request retries exhausted")

    def collections(self):
        return self._request("GET","collections")["collections"]

    def properties(self):
        return self._request("GET","properties",params=self._revision())["properties"]

    def sources(self):
        return self._request("GET","sources",params=self._revision())["sources"]

    def predictions(self):
        return self._request("GET","predictions",params=self._revision())["predictions"]

    def _revision(self):
        return {"revision":self.release} if self.release else {}

    def property_info(self,name):
        return self._request("GET",f"properties/{quote(name,safe='')}",params=self._revision())

    def _download(self,url,path,expected_hash=None,expected_bytes=None):
        path=Path(path)
        path.parent.mkdir(parents=True,exist_ok=True)
        if path.exists():
            if expected_hash and sha256(path)==expected_hash:
                return path
            raise MaterialsAtlasError(f"Refusing to overwrite an existing file with different or unknown content: {path}")
        partial=path.with_name(path.name+".partial")
        etag_file=partial.with_name(partial.name+".etag")
        for attempt in range(4):
            offset=partial.stat().st_size if partial.exists() else 0
            headers={"Accept-Encoding":"identity"}
            if offset:
                headers["Range"]=f"bytes={offset}-"
                if etag_file.exists():
                    headers["If-Range"]=etag_file.read_text().strip()
            try:
                with self.http.stream("GET",self._url(url),headers=headers) as response:
                    if response.status_code==416 and partial.exists() and expected_hash and sha256(partial)==expected_hash:
                        os.replace(partial,path)
                        etag_file.unlink(missing_ok=True)
                        return path
                    if response.status_code==416:
                        partial.unlink(missing_ok=True)
                        etag_file.unlink(missing_ok=True)
                        continue
                    response.raise_for_status()
                    append=response.status_code==206 and offset>0
                    if append:
                        content_range=response.headers.get("Content-Range","")
                        if not content_range.startswith(f"bytes {offset}-"):
                            raise MaterialsAtlasError("Invalid resume response; partial download preserved")
                    if response.headers.get("ETag"):
                        etag_file.write_text(response.headers["ETag"])
                    elif not append:
                        etag_file.unlink(missing_ok=True)
                    with partial.open("ab" if append else "wb") as out:
                        for block in response.iter_raw():
                            out.write(block)
                if expected_bytes is not None and partial.stat().st_size!=expected_bytes:
                    raise MaterialsAtlasError("Downloaded file size does not match the manifest")
                if expected_hash and sha256(partial)!=expected_hash:
                    partial.unlink(missing_ok=True)
                    etag_file.unlink(missing_ok=True)
                    raise MaterialsAtlasError("SHA-256 verification failed; invalid partial file removed")
                os.replace(partial,path)
                etag_file.unlink(missing_ok=True)
                return path
            except httpx.TransportError as exc:
                if attempt==3:
                    raise MaterialsAtlasError(f"Download interrupted; retry to resume {partial}") from exc
                time.sleep(2**attempt)
            except httpx.HTTPStatusError as exc:
                raise MaterialsAtlasError(f"Download failed with HTTP {exc.response.status_code}") from exc
        raise MaterialsAtlasError("Download retries exhausted")

    def download_property(self,name,directory=None):
        """Download an entire public property table, verifying its SHA-256."""
        info=self.property_info(name)
        if not info.get("download_url"):
            raise MaterialsAtlasError("This property has no public rows in the selected release")
        target=Path(directory) if directory else self.cache_dir/info["release"]/'properties'
        file=self._download(info["download_url"],target/f"{name}.parquet",info["sha256"],info["bytes"])
        file.with_suffix(".metadata.json").write_text(json.dumps(info,indent=2))
        return file

    def download_prediction(self,task,directory=None):
        """Explicitly download ML estimates and their publisher's model metadata."""
        info=self._request("GET",f"predictions/{quote(task,safe='')}",params=self._revision())
        target=Path(directory) if directory else self.cache_dir/info["release"]/'predictions'
        file=self._download(info["download_url"],target/f"{task}.parquet",info["sha256"],info["bytes"])
        file.with_suffix(".metadata.json").write_text(json.dumps(info,indent=2))
        return file

    def export(self,**query):
        """Submit a reproducible export. Returns an ExportJob without waiting."""
        query.setdefault("release",self.release)
        data=self._request("POST","exports",json=query)
        return ExportJob(self,data["id"],data)

    def job(self,identity):
        if not re.fullmatch(r"[a-f0-9]{32}",identity):
            raise ValueError("Invalid export ID")
        return ExportJob(self,identity)

    def download_cifs(self,*,structure_source=None,directory=".",**filters):
        """Download CIF archive parts and metadata; archives are not auto-extracted."""
        return self.export(structure_source=structure_source,include_cifs=True,**filters).download(directory)

    def iter_structures(self,*,page_size=100,**filters):
        """Iterate source metadata with keyset pagination, without loading all rows."""
        params={**self._revision(),**filters,"limit":page_size}
        if isinstance(params.get("elements"),list):
            params["elements"]=','.join(params["elements"])
        while True:
            data=self._request("GET","structures",params=params)
            yield from data["structures"]
            if data["next_after"] is None:
                return
            params["after"]=data["next_after"]

    def get_cif(self,material_id):
        response=self.http.get(self.api_url+f"/structures/{quote(material_id,safe='')}/cif",params=self._revision())
        if response.is_error:
            raise MaterialsAtlasError(f"CIF retrieval failed: HTTP {response.status_code}")
        return response.text

    def get_structure(self,material_id):
        """Return a pymatgen Structure; requires materialsatlas[structures]."""
        try:
            from pymatgen.core import Structure
        except ImportError as exc:
            raise ImportError("Install materialsatlas[structures] for pymatgen objects") from exc
        return Structure.from_str(self.get_cif(material_id),fmt="cif")

    def optimade(self,filter="",*,response_fields=None,page_limit=20):
        """Iterate normalized OPTIMADE structures. This endpoint uses the active release."""
        if self.release:
            active=self.collections()[0]["release"]
            if not active.startswith(self.release):
                raise MaterialsAtlasError("OPTIMADE currently serves the active release; use exports for historical releases")
        params={"filter":filter,"page_limit":page_limit}
        if response_fields:
            params["response_fields"]=','.join(response_fields) if isinstance(response_fields,list) else response_fields
        url=self.base_url+"/optimade/v1/structures"
        while url:
            data=self._request("GET",url,params=params)
            yield from data["data"]
            url=data.get("links",{}).get("next")
            if isinstance(url,dict):
                url=url.get("href")
            params=None


class ExportJob:
    def __init__(self,client,identity,status=None):
        self.client=client
        self.id=identity
        self._status=status

    def status(self):
        self._status=self.client._request("GET",f"exports/{self.id}")
        return self._status

    def wait(self,timeout=3600,poll_interval=3):
        started=time.monotonic()
        while True:
            status=self.status()
            if status["status"]=="complete":
                return status
            if status["status"] in ("failed","expired"):
                raise MaterialsAtlasError(status.get("error") or f"Export {self.id} is {status['status']}")
            if time.monotonic()-started>=timeout:
                raise TimeoutError(f"Export {self.id} is still {status['status']}; resume with atlas.job('{self.id}')")
            time.sleep(poll_interval)

    def download(self,directory=".",*,timeout=3600):
        """Wait, download all artifacts with resume/checksum checks, and return paths."""
        status=self.wait(timeout=timeout)
        target=Path(directory)/self.id
        target.mkdir(parents=True,exist_ok=True)
        paths=[]
        for info in status["files"]:
            name=info["name"]
            if Path(name).name!=name or name in (".",".."):
                raise MaterialsAtlasError("Unsafe filename in export manifest")
            paths.append(self.client._download(info["url"],target/name,info["sha256"],info["bytes"]))
        manifest=self.client._request("GET",status["manifest_url"])
        (target/'manifest.json').write_text(json.dumps(manifest,indent=2))
        paths.append(target/'manifest.json')
        return paths
