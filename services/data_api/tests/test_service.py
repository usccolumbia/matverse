import json
import os
from pathlib import Path
import shutil
import tarfile
import time

from fastapi.testclient import TestClient
import pyarrow.parquet as pq
import pytest

from data_api import config,state
from data_api.query import Selection,catalog,connection,resolve,selection_sql
from data_api.exporter import execute
from data_api.api import app
from fixture_data import create,REV,CIF


@pytest.fixture(scope="module")
def root(tmp_path_factory):
    root=tmp_path_factory.mktemp('service')
    create(root)
    return root


@pytest.fixture
def service(root,monkeypatch):
    monkeypatch.setattr(config,'ROOT',root)
    monkeypatch.setattr(config,'USE_ACCEL',False)
    monkeypatch.setattr(config,'BASE_URL','http://testserver')
    monkeypatch.setattr(config,'PART_CIFS',1)
    catalog.cache_clear()
    for name in ['state','tmp','exports','logs']:(root/name).mkdir(exist_ok=True)
    shutil.rmtree(root/'state');(root/'state').mkdir()
    with TestClient(app) as client:
        yield client


def test_counts_licences_and_sources(service):
    p=service.get('/api/data/v1/properties').json()['properties'][0]
    assert (p['upstream_rows'],p['rows'],p['excluded_rows'],p['structures'])==(4,3,1,2)
    r=service.get('/api/data/v1/properties/band_gap/download')
    assert r.status_code==200
    import io
    rows=pq.read_table(io.BytesIO(r.content)).to_pylist()
    assert {x['licence_class'] for x in rows}=={'open'}
    assert len([r for r in rows if r['material_id']=='mat-0'])==2
    assert service.get('/api/data/v1/structures?structure_source=oqmd').json()['structures'][0]['material_id']=='mat-0'
    assert len(service.get('/api/data/v1/structures?origin_source=legacy-local').json()['structures'])==1


def test_join_source_semantics_and_filter(service):
    s=resolve(Selection(property='band_gap',property_source='materials-project',include_cifs=True))
    sql,args=selection_sql(s)
    with connection(s.release) as db:rows=db.execute(sql,args).fetch_arrow_table().to_pylist()
    assert len(rows)==1 and rows[0]['material_id']=='mat-0' and rows[0]['structure_origin_source']=='oqmd'
    assert service.post('/api/data/v1/exports',json={'property':'unknown'}).status_code==400
    assert service.post('/api/data/v1/exports',json={'property_source':'oqmd'}).status_code==422
    assert service.post('/api/data/v1/exports',json={'property':'band_gap','value_min':10,'value_max':1}).status_code==422


def test_export_deduplicated_cifs_and_manifest(service,root):
    query={'property':'band_gap','include_cifs':True,'format':'csv.gz'}
    response=service.post('/api/data/v1/exports',json=query)
    assert response.status_code==202
    identity=response.json()['id']
    assert service.post('/api/data/v1/exports',json=query).json()['id']==identity
    job=state.claim()
    work=root/'tmp'/f"{identity}-{job['lease']}"
    execute(identity,job['lease'],work)
    result=json.loads((work/'manifest.json').read_text())
    assert (result['rows'],result['unique_structures'],result['cifs'],result['excluded_nonopen_rows_before_limit'])==(3,2,2,1)
    archives=list(work.glob('cifs-*.tar.gz'));assert len(archives)==2
    ids=[]
    for path in archives:
        with tarfile.open(path) as tar:
            ids += [name for name in tar.getnames() if name.endswith('.cif')]
            for member in tar.getmembers():
                if member.name.endswith('.cif'):assert tar.extractfile(member).read().decode()==CIF
    assert len(ids)==len(set(ids))==2
    os.replace(work,root/'exports'/identity)
    state.update(identity,job['lease'],status='complete',result=json.dumps(result),expires=time.time()+100)
    cached=service.post('/api/data/v1/exports',json=query)
    assert cached.status_code==200 and cached.json()['cache_reused']
    url=f'/api/data/v1/exports/{identity}/files/records.csv.gz'
    downloaded=service.get(url,headers={'Range':'bytes=0-10'})
    assert downloaded.status_code==206 and len(downloaded.content)==11
    assert service.get(f'/api/data/v1/exports/{identity}/files/jobs.sqlite3').status_code==404


def test_predictions_explicit_and_restart_recovery(service):
    assert service.get('/api/data/v1/predictions').json()['predictions'][0]['record_type']=='ml_prediction'
    identity=service.post('/api/data/v1/exports',json={'prediction':'test__gga'}).json()['id']
    old=state.claim()
    with state.connect() as db:db.execute('UPDATE jobs SET updated=? WHERE id=?',(time.time()-300,identity))
    new=state.claim()
    assert new['id']==identity and new['lease']!=old['lease'] and new['attempts']==2
    assert not state.update(identity,old['lease'],status='complete')


def test_no_sql_injection_or_path_escape(service):
    r=service.get('/api/data/v1/structures',params={'formula':"Si' OR 1=1 --"})
    assert r.status_code==200 and r.json()['structures']==[]
    assert service.get('/api/data/v1/properties/../../state/jobs.sqlite3').status_code==404
    assert service.get('/api/data/v1/structures/not-found/cif').status_code==404


def test_optimade_normalizes_real_cif_and_filters(service):
    r=service.get('/optimade/v1/structures',params={'filter':'elements HAS ONLY "Si" AND nsites=2','page_limit':1})
    assert r.status_code==200,r.text
    d=r.json();assert d['meta']['data_returned']==3 and d['meta']['more_data_available']
    a=d['data'][0]['attributes'];assert a['nsites']==2 and len(a['cartesian_site_positions'])==2
    assert a['chemical_formula_reduced']=='Si'
    assert service.get(d['links']['next']).json()['data'][0]['id']!=d['data'][0]['id']
    assert service.get('/optimade/v1/structures',params={'filter':'elements HAS < "O"'}).json()['meta']['data_returned']==0
    assert service.get('/optimade/v1/structures',params={'filter':'elements_ratios HAS > 0.5'}).json()['meta']['data_returned']==3
    assert service.get('/optimade/v1/structures',params={'filter':'elements_ratios HAS < 0.5'}).json()['meta']['data_returned']==0
    assert service.get('/optimade/v1/structures',params={'filter':'nsites=2; DROP TABLE structures'}).status_code==400
    assert service.get('/optimade/v1/structures',params={'response_fields':'elements'}).json()['data'][0]['attributes']=={'elements':['Si']}
    assert service.get('/optimade/v1/structures/missing').json()['data'] is None


def test_quota_limits_uncached_work(service):
    for i in range(4):
        assert service.post('/api/data/v1/exports',json={'property':'band_gap','value_min':i}).status_code==202
    assert service.post('/api/data/v1/exports',json={'property':'band_gap','value_min':5}).status_code==429
    # An existing job remains reusable even when the client has hit its queue quota.
    assert service.post('/api/data/v1/exports',json={'property':'band_gap','value_min':0}).status_code==202
