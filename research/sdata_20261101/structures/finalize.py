import pathlib,json,hashlib,re
P=pathlib.Path(__file__).parent
A=json.load(open(P/'additions.json'));works=json.load(open(P.parent/'journal_works.json'));existing=json.load(open('data/datasets.json'))
added={d['links']['paper'].split('doi.org/')[-1].lower():d['id']for d in A}
old={}
for d in existing:
 for u in list(d.get('links',{}).values())+[s['url']for s in d.get('sources',[])]:
  m=re.search(r'10\.1038/(s41597-[a-z0-9-]+|sdata\.\d{4}\.\d+)',u,re.I)
  if m:old.setdefault(m[0].lower(),[]).append(d['id'])
extra={
'10.1038/s41597-022-01292-8':'Spin-splitting 2D release: paper identifies 358 materials, archived DataCite description reports 315. Deferred pending release-level reconciliation; 436 screened candidates also differ from spin-splitting-positive count.',
'10.1038/s41597-022-01641-7':'Correction to spin-splitting descriptor; retain with original and resolve version counts before adding.',
'10.1038/s41597-022-01754-z':'C2DB-derived DOS fingerprints; primarily a descriptor/method companion rather than an independent crystal/material collection.',
'10.1038/s41597-020-0385-y':'OE62 comprises crystal-forming isolated molecules; original crystal context does not make gas-phase molecule coordinates periodic crystals. Adjacent/deferred.',
'10.1038/s41597-022-01142-7':'Organic-material repurposing using molecular data; periodic crystal payload not verified. Adjacent/deferred.',
'10.1038/s41597-023-02200-4':'Atomically precise nanoclusters; molecular/finite-system corpus adjacent to periodic crystal scope. Deferred.',
'10.1038/s41597-019-0081-y':'Catalysis-Hub platform aggregates multiple corpora; the Mamun2019 dataset is separately added and should not be double-counted with platform totals.',
'10.1038/s41597-020-00637-5':'Materials Cloud is an archival platform, not one additive dataset. Included releases are catalogued individually.',
'10.1038/s41597-021-00974-z':'OPTIMADE is a data-access interoperability API, not an independent additive crystal dataset.',
'10.1038/s41597-023-02107-0':'Materials Provenance Store is a data/provenance platform; independent stable release and unique count not verified.',
'10.1038/s41597-023-02501-8':'Materials metadata standards paper; no independent additive crystal corpus established.',
'10.1038/s41597-025-05126-1':'Simulation workflow metadata practices; methods/infrastructure rather than additive crystal corpus.',
'10.1038/sdata.2016.125':'Historical JARVIS-FF descriptor; existing jarvis-ff family, not a separate new corpus.',
'10.1038/sdata.2017.153':'5,329 ABO3 property cohort overlaps existing mdf-wolverton-oxides/MAST-ML records. Keep original descriptor linkage rather than duplicate.',
'10.1038/s41597-025-06109-y':'Massive Atomic Diversity family already present as mad15/mad16; version-specific paper evidence should update lineage, not create another summed dataset.',
'10.1038/s41597-025-04885-1':'Single-atom-alloy C-H dissociation paper; primary reusable release not read in this perspective. Deferred for catalysis-specific follow-up.',
'10.1038/s41597-025-06412-8':'Material fracturing/failure simulations are mesoscale/continuum adjacent; periodic atomic payload not established here.',
'10.1038/s41597-023-02721-y':'3DSC is being handled by the properties perspective; not independently duplicated here.',
'10.1038/s41597-020-0418-6':'High-dielectric ternary oxide candidate handled by properties perspective.',
}
# Historical descriptors without a DOI already in the canonical record are linked explicitly.
explicit_existing={'10.1038/sdata.2016.125':['jarvis-ff'],'10.1038/sdata.2017.153':['mdf-wolverton-oxides'],'10.1038/s41597-025-06109-y':['mad15','mad16']}
L=[]
for w in works:
 doi=w['doi'].lower()
 if doi not in added and doi not in old and doi not in extra:continue
 ids=explicit_existing.get(doi,old.get(doi,[]));status='added'if doi in added else'existing'if ids else'deferred'
 L.append(dict(doi=doi,title=w['title'],url='https://doi.org/'+doi,publication_date=w.get('publication_date'),disposition=status,dataset_id=added.get(doi),existing_dataset_ids=ids,evidence=('Primary descriptor and release verified; see additions.json and receipts.'if status=='added' else extra.get(doi,'Canonical catalog already includes this dataset release/family.')),deposit_urls=([a['links']['data']for a in A if a['id']==added[doi]]if doi in added else[])))
(P/'leads.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
q={'verified_date':'2026-11-01','metadata_basis':'../journal_works.json and ../journal_candidates.json; centrally harvested Crossref Scientific Data journal census, 9,304 works through cutoff','method':'Title screening supplemented by primary Nature/Scientific Data web discovery, primary full-text reads, deposit metadata and selected payload checks. No OpenAlex bulk calls.', 'web_query_families':['Scientific Data crystal structures / periodic datasets','Scientific Data interatomic potentials / DFT / molecular dynamics','Scientific Data MOF / COF / zeolite / frameworks','Scientific Data monolayer / two-dimensional / bilayer / MXene','Scientific Data first-principles alloys / perovskite / surface energies','Scientific Data older sdata.* releases','Targeted TBHubbard / PAH101 / ElectroFace licence and count checks'],'added':len(A),'lead_rows':len(L),'dispositions':{s:sum(x['disposition']==s for x in L)for s in ['added','existing','deferred']}}
(P/'coverage_receipt.json').write_text(json.dumps(q,indent=2)+'\n')
M=[]
for f in sorted(P.glob('*')):
 if f.is_file()and f.name!='manifest.json':M.append(dict(path=f.name,bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(P/'manifest.json').write_text(json.dumps({'verified_date':'2026-11-01','files':M},indent=2)+'\n')
print(q['added'],'additions;',len(L),'lead rows;',q['dispositions'])
