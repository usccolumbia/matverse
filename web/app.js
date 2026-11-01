/* MatVerse UI. MIT; catalog metadata retains CC BY 4.0 and upstream terms. */
'use strict';
const REPO = 'https://github.com/usccolumbia/matverse';
const DEFAULT_STATE = {q:'', category:'', access:'', structure:'', license:'', unit:'', sort:'category', view:'datasets'};
function normalize(value){return String(value ?? '').normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[‐‑–—_-]/g,' ').replace(/\s+/g,' ').trim();}
function queryTokens(query){return (String(query).match(/"[^"]+"|\S+/g)||[]).map(t=>normalize(t.replace(/^"|"$/g,''))).filter(Boolean);}
function searchable(record,categories={}){return normalize(JSON.stringify(record)+' '+(categories[record.category]||''));}
function matchesQuery(record,query,categories={}){const text=searchable(record,categories);return queryTokens(query).every(token=>text.includes(token));}
function unitKind(d){
  const u=normalize(d.count_unit);
  if(/frame|configuration|ionic step|snapshot/.test(u))return 'configurations';
  if(/property|observations|measurement|source paper|synthesis|procedure|reaction|curve|pattern|reference entr|sample|composition|instance/.test(u))return 'observations';
  if(/structure|crystal|material|compound|framework|monolayer|bilayer|polymorph/.test(u))return 'structures';
  return d.structure_level==='periodic_atomic'?'structures':'observations';
}
function licenseUnknown(d){return /not verified|unverified|not stated/i.test(d.license);}
function sortDatasets(rows,sort,categories){
  const rank=Object.keys(categories);
  const name=(a,b)=>a.name.localeCompare(b.name,'en',{sensitivity:'base'})||a.id.localeCompare(b.id);
  return [...rows].sort((a,b)=>{
    if(sort==='name')return name(a,b);
    if(sort==='newest')return (b.year??-1)-(a.year??-1)||name(a,b);
    if(sort==='category'){const c=rank.indexOf(a.category)-rank.indexOf(b.category);if(c)return c;}
    if(a.count===null&&b.count!==null)return 1;
    if(b.count===null&&a.count!==null)return -1;
    return (sort==='smallest'?(a.count??0)-(b.count??0):(b.count??0)-(a.count??0))||name(a,b);
  });
}
function filterDatasets(data,state,categories){
  return sortDatasets(data.filter(d=>
    (!state.category||d.category===state.category)&&(!state.access||d.access===state.access)&&
    (!state.structure||d.structure_level===state.structure)&&
    (!state.license||(state.license==='unknown'?licenseUnknown(d):!licenseUnknown(d)))&&
    (!state.unit||(state.unit==='unknown'?d.count===null:unitKind(d)===state.unit))&&matchesQuery(d,state.q,categories)
  ),state.sort,categories);
}
function filterResources(data,state){return data.filter(d=>matchesQuery(d,state.q)).sort((a,b)=>a.name.localeCompare(b.name,'en',{sensitivity:'base'}));}
function csvFor(rows,kind='datasets'){
  const fields=kind==='resources'?['name','kind','url','description','sources']:['id','name','category','version','year','count','count_display','count_unit','count_scope','count_precision','structure_level','provenance','properties','access','license','links','sources','caveats','tags'];
  const quote=value=>{
    let s=value==null?'':typeof value==='object'?JSON.stringify(value):String(value);
    if(typeof value==='string'&&/^[=+@-]/.test(s))s="'"+s;
    return '"'+s.replace(/"/g,'""')+'"';
  };
  return '\uFEFF'+[fields.map(quote).join(','),...rows.map(row=>fields.map(f=>quote(row[f])).join(','))].join('\r\n')+'\r\n';
}
function escapeHTML(value){return String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function safeURL(value){try{const u=new URL(value);return ['https:','http:'].includes(u.protocol)?u.href:'#';}catch{return '#';}}
function formatCount(d){return d.count===null?'Unranked':({exact:'',approximate:'~',lower_bound:'≥'}[d.count_precision]||'')+d.count.toLocaleString('en-US');}
function startApp(){
  const catalog=JSON.parse(document.getElementById('catalog-data').textContent);
  const {datasets,resources,categories}=catalog;
  const params=new URLSearchParams(location.search);
  let state={...DEFAULT_STATE};
  for(const k of Object.keys(DEFAULT_STATE))if(params.has(k))state[k]=params.get(k);
  if(!Object.keys(categories).includes(state.category))state.category='';
  if(!['datasets','resources'].includes(state.view))state.view='datasets';
  if(!['category','largest','smallest','name','newest'].includes(state.sort))state.sort='category';
  if(!['','structures','configurations','observations','unknown'].includes(state.unit))state.unit='';
  const expanded=new Set();
  let visible=[];
  const $=id=>document.getElementById(id);
  const esc=escapeHTML;
  const external=(url,label,cls='')=>`<a href="${esc(safeURL(url))}" target="_blank" rel="noopener"${cls?` class="${cls}"`:''}>${label}</a>`;
  const categoryShort={aggregated_crystals:'Aggregated crystal collections',bulk_computed:'Computed bulk crystals',experimental_crystallography:'Crystallography & reference data',mlip_configurations:'MLIP configurations',two_dimensional:'2D & layered materials',porous_frameworks:'MOFs, COFs & zeolites',molecular_crystals:'Molecular crystals & ice',surfaces_catalysis:'Surfaces & catalysis',property_benchmarks:'Property benchmarks',generation_benchmarks:'Generation & discovery',experimental_properties:'Experimental properties & literature',diffraction_spectroscopy:'Diffraction & spectroscopy'};
  const accessLabel={open:'Public access',registration:'Registration',restricted:'Restricted',commercial:'Commercial',mixed:'Mixed access'};
  const structureLabel={periodic_atomic:'Periodic atomic coordinates',structure_linked:'Linked structures / identifiers',composition_only:'Composition only',mixed:'Mixed availability or domains'};
  function updateURL(){
    const u=new URL(location.href);u.search='';
    for(const [k,v] of Object.entries(state))if(v!==DEFAULT_STATE[k]&&v)u.searchParams.set(k,v);
    try{history.replaceState(null,'',u);}catch{/* Standalone file viewers can restrict history. */}
  }
  const sourceList=d=>d.sources.map(s=>`<li>${external(s.url,esc(s.title))}<br>${esc(s.evidence)}<span class="source-date">Documentation checked ${esc(s.verified_date)}</span></li>`).join('');
  function detailHTML(d){
    const links=Object.entries(d.links).map(([key,url])=>external(url,({homepage:'Provider website',data:'Get data',paper:'Read paper',code:'Code',papers:'Papers CSV',samples:'Samples CSV',curves:'Curves CSV'}[key]||esc(key))+' ↗')).join('');
    const other=(d.additional_counts||[]).map(c=>`<li>${Number(c.value).toLocaleString('en-US')} ${esc(c.unit)} — ${esc(c.scope)}</li>`).join('');
    const math=d.count_derivation?`<p><strong>Count derivation:</strong> ${esc(d.count_derivation.method)}<br>${d.count_derivation.values.map(v=>v.toLocaleString('en-US')).join(' + ')} = ${d.count.toLocaleString('en-US')}</p>`:'';
    return `<div class="detail-panel"><div class="detail-top"><h3>${esc(d.name)}</h3><div class="detail-links">${links}${external(`${REPO}/blob/main/docs/catalog/${d.category}.md#${d.id}`,'Full dataset card ↗')}<a href="#${d.id}">Link to this release</a></div></div><div class="detail-grid"><div><h4>RELEASE &amp; COUNT SCOPE</h4><p>${esc(d.description)}</p><dl><dt>Release</dt><dd>${esc(d.version)}</dd><dt>Count</dt><dd>${esc(d.count_display)} ${esc(d.count_unit)}</dd><dt>Scope</dt><dd>${esc(d.count_scope)}</dd><dt>Structure data</dt><dd>${esc(structureLabel[d.structure_level])}</dd><dt>Provenance</dt><dd>${esc(d.provenance)}</dd><dt>Data license</dt><dd>${esc(d.license)}</dd></dl>${math}${other?`<div class="caveat-block"><h4>OTHER DENOMINATORS</h4><ul>${other}</ul></div>`:''}<div class="caveat-block"><h4>AVAILABLE LABELS &amp; CONTENT</h4><p>${d.properties.map(esc).join(' · ')}</p>${d.tags.length?`<p><strong>Tags:</strong> ${d.tags.map(esc).join(' · ')}</p>`:''}</div></div><div><h4>SOURCE EVIDENCE · ${d.sources.length}</h4><ul class="evidence-list">${sourceList(d)}</ul>${d.caveats.length?`<div class="caveat-block"><h4>REUSE &amp; INTERPRETATION</h4><ul>${d.caveats.map(c=>`<li>${esc(c)}</li>`).join('')}</ul></div>`:''}</div></div></div>`;
  }
  function datasetRow(d){
    const open=expanded.has(d.id);const provider=d.links.homepage||d.links.data||d.links.paper;
    return `<tr class="dataset-row${open?' expanded':''}" id="release-${d.id}" data-id="${d.id}"><td>${external(provider,esc(d.name)+'<span class="external-arrow" aria-hidden="true">↗</span>','dataset-link')}<p class="category-label">${d.year?`<span class="year-pill">${d.year}</span>`:''}${esc(categoryShort[d.category]||categories[d.category])}</p></td><td><span class="dataset-count${d.count===null?' unranked':''}">${formatCount(d)}</span><span class="count-unit">${esc(d.count_unit)}</span></td><td><div class="properties">${d.properties.slice(0,3).map(p=>`<span class="property-tag">${esc(p)}</span>`).join('')}${d.properties.length>3?`<span class="property-tag">+${d.properties.length-3}</span>`:''}</div><p class="dataset-description">${esc(d.description)}</p></td><td><span class="access-badge ${d.access}">${accessLabel[d.access]}</span><p class="license-text">${esc(d.license)}</p></td><td class="details-cell"><button class="details-toggle" type="button" aria-expanded="${open}" aria-controls="detail-${d.id}" aria-label="${open?'Close':'View'} details for ${esc(d.name)}" data-expand="${d.id}">${open?'−':'i'}</button></td></tr><tr class="detail-row" id="detail-${d.id}"${open?'':' hidden'}><td colspan="5">${detailHTML(d)}</td></tr>`;
  }
  function renderChips(){
    const chips=[];
    if(state.q)chips.push(['q',`Search: ${state.q}`]);
    if(state.view==='datasets')for(const k of ['category','access','structure','license','unit'])if(state[k]){
      const label=k==='category'?categoryShort[state[k]]:k==='access'?accessLabel[state[k]]:k==='structure'?structureLabel[state[k]]:k==='license'?(state[k]==='unknown'?'License unverified':'License terms documented'):({structures:'Structure counts',configurations:'Configuration counts',observations:'Property / literature counts',unknown:'Size unverified'}[state[k]]);
      chips.push([k,label||state[k]]);
    }
    $('active-filters').innerHTML=chips.map(([key,label])=>`<button type="button" class="filter-chip" data-clear="${key}" aria-label="Remove ${esc(label)} filter">${esc(label)} <span aria-hidden="true">×</span></button>`).join('');
    $('active-filters').hidden=chips.length===0;
    $('reset').disabled=chips.length===0&&state.sort===DEFAULT_STATE.sort;
  }
  function render(){
    const resourceMode=state.view==='resources';
    visible=resourceMode?filterResources(resources,state):filterDatasets(datasets,state,categories);
    $('search').value=state.q;
    for(const k of ['category','access','structure','license','sort'])$(k).value=state[k];
    $('clear-search').hidden=!state.q;
    document.querySelectorAll('.dataset-filter').forEach(el=>el.hidden=resourceMode);
    $('sort').parentElement.hidden=resourceMode;
    $('filters').classList.toggle('resource-mode',resourceMode);
    $('type-tabs').hidden=resourceMode;
    $('directory-title').textContent=resourceMode?'Repositories & portals':'Dataset directory';
    $('directory-description').textContent=resourceMode?'Find source collections, discovery tools, APIs and adjacent data resources.':'Search dataset names, properties, methods, tags and source evidence.';
    $('search').placeholder=resourceMode?'Repository, portal, topic…':'Name, property, method…';
    $('result-count').textContent=`${visible.length} of ${resourceMode?resources.length:datasets.length} ${resourceMode?'resources':'records'}`;
    for(const view of ['datasets','resources']){$('view-'+view).classList.toggle('selected',state.view===view);$('view-'+view).setAttribute('aria-pressed',String(state.view===view));}
    document.querySelectorAll('[data-unit]').forEach(btn=>{btn.classList.toggle('selected',btn.dataset.unit===state.unit);btn.setAttribute('aria-pressed',String(btn.dataset.unit===state.unit));});
    $('dataset-table-wrap').hidden=resourceMode||visible.length===0;
    document.querySelector('.mobile-table-hint').hidden=resourceMode||visible.length===0;
    $('resource-grid').hidden=!resourceMode||visible.length===0;
    $('empty-state').hidden=visible.length!==0;
    $('table-footnote').textContent=resourceMode?'Portals, APIs and collections are navigation resources, not additional independent crystal datasets.':'~ Approximate · ≥ Reported lower bound · Unranked = size unverified. “Public access” describes availability; data may still carry restrictions. Expand a release for its source evidence.';
    if(!resourceMode)$('dataset-rows').innerHTML=visible.map(datasetRow).join('');
    else $('resource-grid').innerHTML=visible.map(r=>`<article class="resource-card"><span class="resource-kind">${esc(r.kind)}</span><h3>${external(r.url,esc(r.name)+' <span class="external-arrow" aria-hidden="true">↗</span>')}</h3><p>${esc(r.description)}</p><details><summary>Source evidence · ${r.sources.length}</summary><ul>${sourceList(r)}</ul></details></article>`).join('');
    $('export-csv').disabled=$('export-json').disabled=visible.length===0;
    renderChips();updateURL();
  }
  function reset(){state={...DEFAULT_STATE,view:state.view};render();}
  function expand(id,force=false){
    const d=datasets.find(d=>d.id===id);if(!d)return;
    const open=force||!expanded.has(id);
    if(open)expanded.add(id);else expanded.delete(id);
    const row=$('release-'+id),panel=$('detail-'+id),button=row?.querySelector('[data-expand]');
    if(row&&panel&&button){row.classList.toggle('expanded',open);panel.hidden=!open;button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',`${open?'Close':'View'} details for ${d.name}`);button.textContent=open?'−':'i';if(open&&matchMedia('(max-width:700px)').matches){$('dataset-table-wrap').scrollTo({left:0});panel.scrollIntoView({block:'nearest'});}}
  }
  function openHash(){
    let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}
    if(!datasets.some(d=>d.id===id))return;
    if(state.view!=='datasets'||!visible.some(d=>d.id===id)){state={...DEFAULT_STATE};render();}
    expand(id,true);$('release-'+id)?.scrollIntoView({block:'start',behavior:'instant'});
  }
  for(const [id,title] of Object.entries(categories))$('category').insertAdjacentHTML('beforeend',`<option value="${id}">${esc(title)}</option>`);
  $('stat-datasets').textContent=$('dataset-view-count').textContent=datasets.length;
  $('stat-categories').textContent=Object.keys(categories).length;
  $('stat-sources').textContent=new Set(datasets.flatMap(d=>d.sources.map(s=>s.url))).size;
  $('stat-resources').textContent=$('resource-view-count').textContent=resources.length;
  $('checked-date').textContent=new Intl.DateTimeFormat('en-GB',{day:'2-digit',month:'short',year:'numeric',timeZone:'UTC'}).format(new Date(catalog.checkedDate+'T12:00:00Z')).toUpperCase();
  $('filters').addEventListener('submit',e=>e.preventDefault());
  $('search').addEventListener('input',e=>{state.q=e.target.value;render();});
  for(const k of ['category','access','structure','license','sort'])$(k).addEventListener('change',e=>{state[k]=e.target.value;render();});
  $('clear-search').addEventListener('click',()=>{state.q='';render();$('search').focus();});
  $('type-tabs').addEventListener('click',e=>{const b=e.target.closest('[data-unit]');if(b){state.unit=b.dataset.unit;render();}});
  $('active-filters').addEventListener('click',e=>{const b=e.target.closest('[data-clear]');if(b){state[b.dataset.clear]='';render();}});
  for(const v of ['datasets','resources'])$('view-'+v).addEventListener('click',()=>{state.view=v;render();});
  $('reset').addEventListener('click',reset);$('empty-reset').addEventListener('click',reset);
  $('dataset-rows').addEventListener('click',e=>{const b=e.target.closest('[data-expand]');if(b)expand(b.dataset.expand);});
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!e.ctrlKey&&!e.metaKey&&!e.altKey&&!['INPUT','SELECT','TEXTAREA'].includes(document.activeElement.tagName)){e.preventDefault();$('search').focus();}});
  document.addEventListener('click',e=>{const menu=document.querySelector('.export-menu');if(!menu.contains(e.target))menu.open=false;});
  window.addEventListener('hashchange',openHash);
  window.addEventListener('popstate',()=>{const p=new URLSearchParams(location.search);state={...DEFAULT_STATE};for(const k in state)if(p.has(k))state[k]=p.get(k);render();openHash();});
  function download(type){
    if(!visible.length)return;
    const content=type==='csv'?csvFor(visible,state.view):JSON.stringify(visible,null,2)+'\n';
    const blob=new Blob([content],{type:type==='csv'?'text/csv;charset=utf-8':'application/json;charset=utf-8'});
    const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=`matverse-${state.view}-${catalog.checkedDate}.${type}`;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);document.querySelector('.export-menu').open=false;
  }
  $('export-csv').addEventListener('click',()=>download('csv'));$('export-json').addEventListener('click',()=>download('json'));
  render();openHash();
}
if(typeof module!=='undefined'&&module.exports)module.exports={normalize,queryTokens,matchesQuery,unitKind,licenseUnknown,sortDatasets,filterDatasets,filterResources,csvFor,escapeHTML,formatCount,DEFAULT_STATE};
if(typeof document!=='undefined')startApp();
