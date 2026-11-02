import hashlib
import json
import httpx
import pytest

from materialsatlas import MaterialsAtlas,MaterialsAtlasError


def test_verified_cache_and_metadata(tmp_path):
    content=b'parquet-fixture';digest=hashlib.sha256(content).hexdigest();gets=[]
    def handler(request):
        gets.append(request.url.path)
        if request.url.path.endswith('/band_gap'):
            return httpx.Response(200,json={'release':'a'*40,'sha256':digest,'bytes':len(content),'download_url':'https://example.org/file'})
        return httpx.Response(200,stream=httpx.ByteStream(content))
    with MaterialsAtlas('https://example.org',cache_dir=tmp_path,transport=httpx.MockTransport(handler)) as atlas:
        file=atlas.download_property('band_gap');assert file.read_bytes()==content
        assert atlas.download_property('band_gap')==file
        assert gets.count('/file')==1
        assert json.loads(file.with_suffix('.metadata.json').read_text())['sha256']==digest


def test_resume_and_integrity(tmp_path):
    content=b'0123456789';digest=hashlib.sha256(content).hexdigest();target=tmp_path/'data.parquet'
    target.with_name(target.name+'.partial').write_bytes(content[:4])
    def handler(request):
        assert request.headers['Range']=='bytes=4-'
        return httpx.Response(206,headers={'Content-Range':'bytes 4-9/10'},stream=httpx.ByteStream(content[4:]))
    with MaterialsAtlas('https://example.org',transport=httpx.MockTransport(handler)) as atlas:
        assert atlas._download('https://example.org/file',target,digest,10).read_bytes()==content
        with pytest.raises(MaterialsAtlasError):atlas._download('https://evil.example/file',tmp_path/'other',digest)
        with pytest.raises(MaterialsAtlasError):atlas._download('https://example.org/file',target,'0'*64)


def test_server_ignores_range_restarts_cleanly(tmp_path):
    content=b'complete';path=tmp_path/'data';(tmp_path/'data.partial').write_bytes(b'old')
    with MaterialsAtlas('https://example.org',transport=httpx.MockTransport(lambda r:httpx.Response(200,stream=httpx.ByteStream(content)))) as atlas:
        assert atlas._download('https://example.org/file',path,hashlib.sha256(content).hexdigest()).read_bytes()==content


def test_mismatch_never_publishes_download(tmp_path):
    with MaterialsAtlas('https://example.org',transport=httpx.MockTransport(lambda r:httpx.Response(200,stream=httpx.ByteStream(b'bad')))) as atlas:
        with pytest.raises(MaterialsAtlasError):atlas._download('https://example.org/file',tmp_path/'data','0'*64)
        assert not (tmp_path/'data').exists()


def test_optimade_pagination_and_http_error():
    def handler(request):
        if request.url.path.endswith('/properties'):
            return httpx.Response(400,json={'detail':'bad release'})
        page=request.url.params.get('page_offset')
        return httpx.Response(200,json={'data':[{'id':'b' if page else 'a'}],'links':{'next':None if page else 'https://example.org/optimade/v1/structures?page_offset=1'}})
    with MaterialsAtlas('https://example.org',transport=httpx.MockTransport(handler)) as atlas:
        assert [x['id'] for x in atlas.optimade()]==['a','b']
        with pytest.raises(MaterialsAtlasError,match='bad release'):atlas.properties()
