import requests,pathlib,hashlib,json,concurrent.futures
from bs4 import BeautifulSoup
root=pathlib.Path('research/cache/sdata_structures');root.mkdir(parents=True,exist_ok=True)
urls=['s41597-023-02116-z','s41597-024-03447-1','s41597-024-03720-3','s41597-024-04008-2','s41597-020-0452-4','s41597-022-01181-0','s41597-022-01292-8','s41597-025-05302-3','s41597-025-05867-z']
def go(doi):
 u='https://www.nature.com/articles/'+doi+'?error=cookies_not_supported';r=requests.get(u,timeout=40);b=r.content;f=root/(doi+'.html');f.write_bytes(b);s=BeautifulSoup(r.text,'html.parser');t=s.get_text(' ',strip=True);(root/(doi+'.txt')).write_text(t)
 paras=[]
 for h in s.find_all(['h2','h3']):
  if any(x in h.get_text().lower()for x in ['data records','data availability','code availability']):
   a=[]
   for z in h.next_siblings:
    if getattr(z,'name',None)in['h2']:break
    if hasattr(z,'get_text'):a.append(z.get_text(' ',strip=True))
   paras.append(h.get_text()+': '+' '.join(a))
 print(doi,s.title.get_text()if s.title else'',r.status_code,'\n','\n'.join(paras)[:11000],flush=True)
 return dict(url=u,status=r.status_code,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),cache_path=str(f))
a=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(go,urls));pathlib.Path('research/sdata_20261101/structures/primary_receipts.json').write_text(json.dumps(a,indent=2))
