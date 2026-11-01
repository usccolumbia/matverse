"""Refresh public Crossref journal metadata from the repository root; never run in CI."""
import json,urllib.request,urllib.parse,time,hashlib,re
from pathlib import Path
out=Path('research/sdata_20261101');cache=Path('research/cache/sdata_journal')
out.mkdir(parents=True,exist_ok=True);cache.mkdir(parents=True,exist_ok=True)
base='https://api.crossref.org/journals/2052-4463/works';cursor='*';seen=set();works=[];receipts=[];total=None
for page in range(1,100):
 params={'rows':1000,'cursor':cursor,'select':'DOI,title,published,type,link','filter':'until-pub-date:2026-11-01'};url=base+'?'+urllib.parse.urlencode(params)
 for attempt in range(3):
  try:
   r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MatVerse materials dataset survey (public bibliographic metadata)'}),timeout=40);b=r.read();break
  except Exception:
   if attempt==2:raise
   time.sleep(2)
 p=json.loads(b)['message'];total=p['total-results'];items=p['items'];cache.joinpath(f'page_{page:03}.json').write_bytes(b)
 receipts.append({'page':page,'status':r.status,'total_reported':total,'returned':len(items),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'cursor_sha256':hashlib.sha256(cursor.encode()).hexdigest()})
 fresh=0
 for w in items:
  doi=w['DOI'].lower()
  if doi in seen:continue
  seen.add(doi);fresh+=1
  parts=w.get('published',{}).get('date-parts',[[]])[0];date='-'.join(str(x).zfill(2) if i else str(x) for i,x in enumerate(parts))
  works.append({'doi':doi,'title':w.get('title',[''])[0] if w.get('title') else '', 'publication_date':date,'type':w.get('type'),'url':'https://doi.org/'+doi})
 print('Page',page,'returned',len(items),'unique',len(works),'total',total,flush=True)
 out.joinpath('journal_harvest_receipts.json').write_text(json.dumps({'source':base,'journal':'Scientific Data','issn':'2052-4463','cutoff':'2026-11-01','complete':False,'unique_works':len(works),'total_reported':total,'pages':receipts},indent=2)+'\n')
 if not items or not fresh or len(works)>=total:break
 cursor=p['next-cursor']
pat=re.compile('material|crystal|alloy|metal|semiconductor|perovskite|oxide|ceramic|ferro|magnet|superconduct|thermoelectric|thermal|conduct|electrolyt|batter|cataly|adsorp|\\bmof|\\bcof|zeolit|phonon|dielect|piezo|diffraction|spectroscop|microscop|microstructur|synthesis|atomistic|density.functional|molecular.dynamics|atom.probe|chemical|polymer|mechanic|stress|strain|fracture|fatigue|corrosion|weld|manufactur|graphene|two.dimensional|\\b2d\\b|nanomaterial|carbon|quantum|elastic|hardness|tensile|wurtz|heusler|topolog|hydrogen.storage|inorganic|ab.initio|electronic|band.gap|surface|interface|nanoparticle|raman|x.ray|infrared|\\bxrd\\b|plasma|sinter|diffus|migration|propert|compound|enthalp|simulation|energy|spectr|nanostruct|lithium|sodium|electron|silicon|steel|alumin|titanium|copper|stabilit|transition|grain|amorph|coating|thermodynamic|high.entropy',re.I)
candidates=[dict(w,screening_status='Title-keyword candidate; not a verified materials dataset') for w in works if pat.search(w['title'])]
out.joinpath('journal_works.json').write_text(json.dumps(works,ensure_ascii=False,indent=2)+'\n');out.joinpath('journal_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
out.joinpath('journal_harvest_receipts.json').write_text(json.dumps({'source':base,'journal':'Scientific Data','issn':'2052-4463','cutoff':'2026-11-01','complete':len(works)>=total,'unique_works':len(works),'title_candidates':len(candidates),'total_reported':total,'title_keyword_regex':pat.pattern,'pages':receipts,'note':'Full journal title/DOI metadata retrieval through the cutoff; title-keyword triage is broad and can include biomedical or environmental false positives. Primary-source audit controls catalog promotion.'},indent=2)+'\n')
print('COMPLETE',len(works),'CANDIDATES',len(candidates),flush=True)
