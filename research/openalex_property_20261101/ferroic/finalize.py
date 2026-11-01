import json,pathlib,re,hashlib,importlib.util,requests,concurrent.futures
b=pathlib.Path(__file__).parent
# Preserve primary publication identifiers for supplementary leads sent by parent.
extra=['10.1038/s41598-024-58351-w','10.1038/s41597-026-07083-9','10.5061/dryad.vmcvdnd6s']
p=b/'raw/openalex-primary-verification.json';metadata=json.load(open(p))
def get(d):
 r=requests.get('https://api.openalex.org/works/https://doi.org/'+d,timeout=30)
 return d,r.json() if r.status_code==200 else {'error':r.status_code}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:metadata.update(dict(ex.map(get,extra)))
p.write_text(json.dumps(metadata,indent=2))
r=requests.get('https://api.figshare.com/v2/articles/30581240',timeout=30);(b/'raw/figshare-30581240.json').write_text(r.text)
new=json.load(open(b/'additions.json'));canon=json.load(open('data/datasets.json'))
for x in new:
 if x['id']=='cde-refractive-dielectric-2022':x['count_derivation']={'method':'separate refractive-index and dielectric records, not unique chemicals','values':[49076,60804]}
 if x['id']=='refractiveindex-info':x['count_derivation']={'method':'December 2023 linear + nonlinear optical data records, not disjoint material counts','values':[3135,193]}
(b/'additions.json').write_text(json.dumps(new,indent=2,ensure_ascii=False)+'\n')
newdoi={}
for x in new:
 for u in x['links'].values():
  m=re.search(r'doi.org/(.+)',u)
  if m:newdoi[m.group(1).lower()]=x['id']
newdoi['10.1038/s41597-023-02898-2']='refractiveindex-info'
existing={}
for x in canon:
 for v in list(x.get('links',{}).values())+[s['url'] for s in x['sources']]:
  for d in re.findall(r'10\.\d{4,9}/[^\s?<>]+',v):existing[d.lower().rstrip('/')]=x['id']
leads={};queries=[]
for f in sorted((b/'raw').glob('*.json')):
 try:o=json.load(open(f))
 except:continue
 if not isinstance(o,dict) or o.get('mode')!='search':continue
 queries.append({'file':'raw/'+f.name,'query':o['query'],'returned':len(o['results']),'network_status':o['network_status'],'per_source':50,'sources':['openalex']})
 for x in o['results']:
  doi=x.get('doi');key=(doi or x['title']).lower()
  if key in leads:leads[key]['queries'].append(f.name);continue
  disposition='added' if doi and doi.lower() in newdoi else 'existing' if doi and doi.lower() in existing else 'lead'
  reason='Included in additions with primary release evidence.' if disposition=='added' else 'Existing catalog parent/release or derivative already represented.' if disposition=='existing' else 'Search hit retained for triage; no additional released dataset verified in this task (may be unrelated, a method-only work, or a duplicate/version).'
  md=metadata.get(doi,{})
  leads[key]={'title':x['title'],'doi':doi,'openalex_id':md.get('id'),'year':x.get('year'),'disposition':disposition,'dataset_id':newdoi.get((doi or '').lower()) or existing.get((doi or '').lower()),'reason':reason,'queries':[f.name]}
for doi,md in metadata.items():
 if doi not in leads:leads[doi]={'title':md.get('title'),'doi':doi,'openalex_id':md.get('id'),'year':md.get('publication_year'),'disposition':'added','dataset_id':newdoi.get(doi),'reason':'Primary dataset/paper independently verified; supplemental lead or direct DOI verification.','queries':[]}
(b/'leads.json').write_text(json.dumps({'verified_date':'2026-11-01','queries':queries,'leads':list(leads.values())},indent=2,ensure_ascii=False)+'\n')
import sys; sys.path.insert(0,str(pathlib.Path('scripts').resolve()))
spec=importlib.util.spec_from_file_location('catalog','scripts/build_catalog.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.validate(canon+new,[])
manifest={str(f.relative_to(b)):{'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in (b/'raw').iterdir() if f.is_file()}
(b/'raw_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('validated',len(new),'new records against',len(canon),'existing; queries',len(queries),'unique leads',len(leads))
