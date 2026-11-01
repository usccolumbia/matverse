import pathlib,json,glob,hashlib,datetime
p=pathlib.Path(__file__).parent
A=json.load(open(p/'additions.json'));M=json.load(open(p/'candidate_metadata.json'))
addmap={}
for a in A:
 for k,u in a['links'].items():
  if 'doi.org/' in u:addmap[u.split('doi.org/')[-1].lower()]=a['id']
addmap.update({'10.48550/arxiv.2502.14234':'obelix','10.48550/arxiv.2508.06459':'migration-barriers-literature-2025','10.6084/m9.figshare.7180817':'oxygen-migration-perovskites-2016','10.6084/m9.figshare.1546772':'uw-cmg-dilute-solute-diffusion','10.11583/dtu.27202446':'polyanion-sodium-cathode-2025'})
why={
 '10.1002/adts.202501125':('lead','Composite polymer/inorganic SSE database reported for >400 materials; public reusable bulk release and licence not verified. Polymer composite scope is adjacent to crystalline solids.'),
 '10.1088/1674-1056/ae88e2':('lead','Primary publisher confirms 6,928 materials and 20,320 CHGNet-assisted NEB paths. Downloadable bulk release and licence unresolved; values are ML-potential NEB, not all DFT-NEB.'),
 '10.1038/s41597-024-03575-8':('lead','Verified CALiSol-23 public liquid-electrolyte conductivity dataset, 13,825 measurements; adjacent resource, excluded from crystal-specific additions.'),
 '10.1038/s41597-023-01936-3':('lead','Verified KIT liquid-electrolyte experiment dataset; adjacent liquid scope, excluded from crystal-specific additions.'),
 '10.5281/zenodo.7244938':('lead','Concept DOI for the verified 5,035-experiment liquid-electrolyte dataset; versioned release 10.5281/zenodo.7244939. Adjacent scope.'),
 '10.18126/k9tn-3965':('lead','Foundry 372-row derivative of Liverpool Ionics; do not add as independent dataset or replace original 820-record corpus.'),
 '10.1038/s41524-026-01972-8':('lead','Model/benchmark companion using 619 pathways; same underlying migration dataset family as added Zenodo621 archive, not an additional dataset.'),
 '10.1039/d2ee03499a':('lead','Primary article reports original Laskowski1,346 conductivity dataset; already contributes to later OBELiX/Caltech lineage. Exact standalone machine-readable release and version not verified here.'),
 '10.1038/s41524-018-0081-z':('lead','Methodological small-data paper; possible original materials-property data but distinct reusable property release not verified.'),
 '10.1109/access.2021.3089032':('lead','Battery dataset review includes device cycle-life/RUL datasets; discovery source rather than new crystal-property release.'),
 '10.1016/j.actamat.2020.09.079':('lead','Mg alloy diffusion-mobility assessment for23elements. Published database identified; downloadable parameter package and licence not verified.'),
 '10.1016/j.dib.2018.08.144':('lead','Explicit26Ni-Xdiffusion/creep data descriptor; primary supplementary content and overlap with other Ni diffusion collections need verification.'),
 '10.1016/j.dib.2015.10.024':('lead','Mg dilute-alloy diffusion data descriptor; relation to the expanded UW/CMG host-solute collection not fully resolved. Avoid premature independent addition.'),
 '10.1016/j.dib.2020.105458':('lead','ZrO2-coated Ni-rich cathode study-specific data. Reusable archive, tabular properties and material granularity not verified.'),
 '10.48550/arxiv.2203.08697':('lead','Virtual-battery database framework; independent public release versus overlapping Materials Project derivatives not verified.'),
 '10.1016/j.ssi.2012.02.014':('lead','Bond-valence screening of alkali-containing ICSD structures; bulk redistribution rights and current release endpoint not verified.'),
 '10.1021/acs.jpcb.2c01635':('lead','Liquid ionic transport database application; adjacent molecular/liquid scope and not an independent crystalline release established.'),
 '10.1016/j.actamat.2017.06.056':('lead','Ni-Al melt diffusion/thermotransport study; liquid scope adjacent, distinct public archive not verified.'),
 '10.6028/nist.ir.6927':('lead','NIST database report; historical thermodynamics/diffusion resource requiring release and current-access investigation.'),
}
L=[]
for r in M:
 doi=(r.get('doi')or'').lower();meta=r.get('verified_openalex_metadata',{})
 if doi in addmap:
  aid=addmap[doi];tr='added';ev='Included as '+aid+'; primary-source evidence, version and count caveats are in additions.json.'
 elif doi=='10.1016/j.nanoms.2023.08.002':aid='digbat';tr='existing';ev='Historical DDSE publication in the existing DigBat family; parent survey handles release history and current counts.'
 else:
  aid=None;tr,ev=why.get(doi,('lead','Dataset-related discovery result; primary release and relevance not verified.'))
 if any(s in (r.get('title')or'').lower() for s in ['nerve','disco','skin flux','diffusion kurtosis']):ev='Excluded: biomedical diffusion/imaging dataset outside materials/crystal scope.'
 z=dict(title=r.get('title')or meta.get('title')or {'10.22002/23mvv-6gk43':'Experimental Li-Ion Conductivity and Crystal Structure Database and Predictions','10.18126/k9tn-3965':'Foundry Liverpool conductivity export'}.get(doi,doi),doi=doi,openalex_id=r.get('openalex_id'),year=r.get('year')or meta.get('publication_year'),treatment=tr,dataset_id=aid,evidence=ev,links={'doi':'https://doi.org/'+doi},primary_verification=('completed; see additions.json' if tr=='added' else 'see evidence field'),discovery_sources=r.get('sources',[]))
 if doi in ['10.1002/adts.202501125','10.1088/1674-1056/ae88e2','10.1039/d2ee03499a']:z['links']['primary']={'10.1002/adts.202501125':'https://onlinelibrary.wiley.com/doi/10.1002/adts.202501125','10.1088/1674-1056/ae88e2':'https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ae88e2','10.1039/d2ee03499a':'https://pubs.rsc.org/en/content/articlelanding/2023/ee/d2ee03499a'}[doi]
 if doi=='10.5281/zenodo.7244938':z['links']['primary']='https://zenodo.org/records/7244939';z['primary_verification']='Public release metadata verified, CC BY4.0; file Conductivtiy_experiment.csv checksum preserved in evidence.'
 L.append(z)
# CALiSol discovery query did not use dataset in title; retain this explicitly verified adjacent resource.
if not any(x['doi']=='10.1038/s41597-024-03575-8' for x in L):
 for f in p.glob('0*.json'):
  for r in json.load(open(f))['results']:
   if r.get('doi')=='10.1038/s41597-024-03575-8':
    L.append(dict(title=r['title'],doi=r['doi'],openalex_id=None,year=r['year'],treatment='lead',dataset_id=None,evidence=why[r['doi']][1],links={'paper':'https://pmc.ncbi.nlm.nih.gov/articles/PMC11237020/'},primary_verification='Primary full text confirms13,825measurement points from27papers and CC BY4.0 data licence.',discovery_sources=['openalex']));break
  else:continue
  break
(p/'leads.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
# Exact metadata-only query receipts and cross-query deduplication.
Q=[];U={}
for f in sorted(p.glob('0*.json')):
 x=json.load(open(f));Q.append(dict(file=f.name,query=x['query'],stats=x['stats'],network_status=x['network_status'],coverage=x['coverage'],warnings=x['warnings'],advisories=x['advisories']))
 for r in x['results']:U[r.get('doi')or(r.get('title')or'').casefold()]=r
(p/'query_receipts.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n');(p/'deduplicated_discovery.json').write_text(json.dumps(list(U.values()),ensure_ascii=False,indent=2)+'\n')
print('queries',len(Q),'raw',sum(q['stats']['raw_hits']for q in Q),'returned',sum(q['stats']['shown']for q in Q),'unique',len(U),'leads',len(L),'IDs',sum(bool(x['openalex_id'])for x in L))
# Manifest is written last, excluding itself, preserving SHA256 for source receipts and payloads.
F=[]
for f in sorted(p.rglob('*')):
 if f.is_file()and f.name!='manifest.json':F.append(dict(path=str(f.relative_to(p)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(p/'manifest.json').write_text(json.dumps(dict(verified_date='2026-11-01',files=F),indent=2)+'\n')
