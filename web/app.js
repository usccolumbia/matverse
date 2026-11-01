/* MatVerse UI. MIT; catalog metadata retains CC BY 4.0 and upstream terms. */
'use strict';
const REPO = 'https://github.com/usccolumbia/matverse';
const DEFAULT_STATE = {q:'', category:'', access:'', structure:'', license:'', unit:'', sort:'category', view:'datasets', collection:'', scope:'',api_kind:'',api_auth:''};
const API_KINDS={optimade:'OPTIMADE',native_api:'Native API',bulk_sdk:'Bulk SDK',bulk_files:'Bulk files'};
const API_AUTH={none:'Anonymous public route',api_key:'API key',account:'Account / authorization',mixed:'Depends on operation or dataset'};
const API_STATUS={sample_verified:'Small record sample verified',metadata_verified:'Metadata response verified',empty_response:'JSON response · empty sample',auth_required:'Authentication required',unavailable:'Probe unsuccessful',documented:'Documented · not queried'};
const SCOPE_LABELS = {crystal_related:'Crystal-related',adjacent:'Adjacent domains',navigation:'Portals & navigation',uncertain:'Scope uncertain'};
function normalize(value){return String(value ?? '').normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[‐‑–—_-]/g,' ').replace(/\s+/g,' ').trim();}
function normalizeSearch(value){return normalize(value).replace(/\b(?:superconductors?|superconductivity|superconducting|superconductive|supercon)\b/g,'superconductivity').replace(/\bcritical temperatures?\b|\bt c\b/g,'tc');}
function queryTokens(query){return (normalizeSearch(query).match(/"[^"]+"|\S+/g)||[]).map(t=>t.replace(/^"|"$/g,'')).filter(Boolean);}
function searchable(record,categories={}){const raw=JSON.stringify(record)+' '+(categories[record.category]||'');return normalize(raw)+' '+normalizeSearch(raw);}
function matchesQuery(record,query,categories={}){const text=searchable(record,categories);return queryTokens(query).every(token=>token==='tc'?/\btc\b/.test(text):text.includes(token));}
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
function filterAPIs(data,state){return filterResources(data.filter(r=>(!state.api_kind||r.kind===state.api_kind)&&(!state.api_auth||r.auth===state.api_auth)),state);}
function filterSourceEntries(data,state){return data.filter(e=>(!state.collection||e.collection===state.collection)&&(!state.scope||e.scope===state.scope)&&matchesQuery(e,state.q)).sort((a,b)=>a.collection_name.localeCompare(b.collection_name,'en',{sensitivity:'base'})||a.position-b.position);}
function globalSearchState(query,view='datasets'){return {...DEFAULT_STATE,q:query,view};}
function searchOverview(catalog,query){
  const state=globalSearchState(query);
  return {datasets:filterDatasets(catalog.datasets,{...state,sort:'name'},catalog.categories),resources:filterResources(catalog.resources,state),sources:filterSourceEntries(catalog.sourceEntries,state),apis:filterAPIs(catalog.apiSources||[],state)};
}
function csvFor(rows,kind='datasets'){
  const fields=kind==='apis'?['id','name','kind','entrypoint','auth','auth_notes','description','formats','catalog_ids','verification','sources','limitations']:kind==='sources'?['id','label','url','collection','collection_name','collection_url','position','section','scope']:kind==='resources'?['name','kind','url','description','sources']:['id','name','category','version','year','count','count_display','count_unit','count_scope','count_precision','structure_level','provenance','properties','access','license','links','sources','caveats','tags','property_dataset'];
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
function propertyAccessHTML(d){
  const p=d.property_dataset;if(!p)return '';
  const esc=escapeHTML;
  const link=(url,label)=>`<a href="${esc(safeURL(url))}" target="_blank" rel="noopener">${esc(label)} ↗</a>`;
  return `<section class="property-access" aria-label="Property dataset access and original sources"><h4>DIRECT ACCESS SOURCE</h4><p>${link(p.direct_access,p.provider+' · '+p.property_key)} · ${link(p.direct_download,'Download Parquet')}</p><dl><dt>Property unit</dt><dd>${esc(p.unit??'Not specified / unitless')}</dd><dt>Value type</dt><dd>${esc({num:'Numeric',bool:'Boolean (0/1)',text:'Text descriptor'}[p.value_kind])}</dd><dt>Linked structures</dt><dd>${p.structures.toLocaleString('en-US')}</dd></dl><h4>ORIGINAL SOURCES / INDIRECT ACCESS · ${p.upstream_sources.length}</h4><ul>${p.upstream_sources.map(u=>`<li>${link(u.url,u.name)} <span class="upstream-count">${u.values.toLocaleString('en-US')} values</span><br><code>${esc(u.source_id)}</code> · provider-declared ${esc(u.license_class)}${u.notes?`<p>${esc(u.notes)}</p>`:''}</li>`).join('')}</ul><p class="property-provenance-note">Values retain original source, native ID, method and per-row license. Property subsets overlap their parent datasets.</p></section>`;
}
function startApp(){
  const catalog=JSON.parse(document.getElementById('catalog-data').textContent);
  const {datasets,resources,categories,collections,sourceEntries,apiSources}=catalog;
  const params=new URLSearchParams(location.search);
  let state={...DEFAULT_STATE};
  for(const k of Object.keys(DEFAULT_STATE))if(params.has(k))state[k]=params.get(k);
  if(!Object.keys(categories).includes(state.category))state.category='';
  if(!['datasets','resources','sources','apis'].includes(state.view))state.view='datasets';
  if(!Object.hasOwn(API_KINDS,state.api_kind))state.api_kind='';
  if(!Object.hasOwn(API_AUTH,state.api_auth))state.api_auth='';
  if(!collections.some(c=>c.id===state.collection))state.collection='';
  if(!Object.hasOwn(SCOPE_LABELS,state.scope))state.scope='';
  if(!['category','largest','smallest','name','newest'].includes(state.sort))state.sort='category';
  if(!['','structures','configurations','observations','unknown'].includes(state.unit))state.unit='';
  const expanded=new Set();
  let visible=[];
  const $=id=>document.getElementById(id);
  const esc=escapeHTML;
  const external=(url,label,cls='')=>`<a href="${esc(safeURL(url))}" target="_blank" rel="noopener"${cls?` class="${cls}"`:''}>${label}</a>`;
  const categoryShort={aggregated_crystals:'Aggregated crystal collections',bulk_computed:'Computed bulk crystals',experimental_crystallography:'Crystallography & reference data',mlip_configurations:'MLIP configurations',two_dimensional:'2D & layered materials',porous_frameworks:'MOFs, COFs & zeolites',molecular_crystals:'Molecular crystals & ice',surfaces_catalysis:'Surfaces & catalysis',materials_properties:'Materials properties',property_benchmarks:'Property benchmarks',generation_benchmarks:'Generation & discovery',experimental_properties:'Experimental properties & literature',diffraction_spectroscopy:'Diffraction & spectroscopy'};
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
    return `<div class="detail-panel"><div class="detail-top"><h3>${esc(d.name)}</h3><div class="detail-links">${links}${external(`${REPO}/blob/main/docs/catalog/${d.category}.md#${d.id}`,'Full dataset card ↗')}<a href="#${d.id}">Link to this release</a></div></div><div class="detail-grid"><div><h4>RELEASE &amp; COUNT SCOPE</h4><p>${esc(d.description)}</p><dl><dt>Release</dt><dd>${esc(d.version)}</dd><dt>Count</dt><dd>${esc(d.count_display)} ${esc(d.count_unit)}</dd><dt>Scope</dt><dd>${esc(d.count_scope)}</dd><dt>Structure data</dt><dd>${esc(structureLabel[d.structure_level])}</dd><dt>Provenance</dt><dd>${esc(d.provenance)}</dd><dt>Data license</dt><dd>${esc(d.license)}</dd></dl>${propertyAccessHTML(d)}${math}${other?`<div class="caveat-block"><h4>OTHER DENOMINATORS</h4><ul>${other}</ul></div>`:''}<div class="caveat-block"><h4>AVAILABLE LABELS &amp; CONTENT</h4><p>${d.properties.map(esc).join(' · ')}</p>${d.tags.length?`<p><strong>Tags:</strong> ${d.tags.map(esc).join(' · ')}</p>`:''}</div></div><div><h4>SOURCE EVIDENCE · ${d.sources.length}</h4><ul class="evidence-list">${sourceList(d)}</ul>${d.caveats.length?`<div class="caveat-block"><h4>REUSE &amp; INTERPRETATION</h4><ul>${d.caveats.map(c=>`<li>${esc(c)}</li>`).join('')}</ul></div>`:''}</div></div></div>`;
  }
  function datasetRow(d){
    const open=expanded.has(d.id);const provider=d.links.homepage||d.links.data||d.links.paper;
    return `<tr class="dataset-row${open?' expanded':''}" id="release-${d.id}" data-id="${d.id}"><td>${external(provider,esc(d.name)+'<span class="external-arrow" aria-hidden="true">↗</span>','dataset-link')}<p class="category-label">${d.year?`<span class="year-pill">${d.year}</span>`:''}${esc(categoryShort[d.category]||categories[d.category])}</p></td><td><span class="dataset-count${d.count===null?' unranked':''}">${formatCount(d)}</span><span class="count-unit">${esc(d.count_unit)}</span></td><td><div class="properties">${d.properties.slice(0,3).map(p=>`<span class="property-tag">${esc(p)}</span>`).join('')}${d.properties.length>3?`<span class="property-tag">+${d.properties.length-3}</span>`:''}</div><p class="dataset-description">${esc(d.description)}</p>${d.property_dataset?`<p class="property-route-label">Via MateriaViva · ${d.property_dataset.upstream_sources.length} original source${d.property_dataset.upstream_sources.length===1?'':'s'}</p>`:''}</td><td><span class="access-badge ${d.access}">${accessLabel[d.access]}</span><p class="license-text">${esc(d.license)}</p></td><td class="details-cell"><button class="details-toggle" type="button" aria-expanded="${open}" aria-controls="detail-${d.id}" aria-label="${open?'Close':'View'} details for ${esc(d.name)}" data-expand="${d.id}">${open?'−':'i'}</button></td></tr><tr class="detail-row" id="detail-${d.id}"${open?'':' hidden'}><td colspan="5">${detailHTML(d)}</td></tr>`;
  }
  function sourceEntryCard(e){
    return `<article class="resource-card source-entry"><span class="resource-kind">${esc(SCOPE_LABELS[e.scope])}</span><h3>${external(e.url,esc(e.label)+' <span class="external-arrow" aria-hidden="true">↗</span>')}</h3><p class="entry-section">${esc(e.section)}</p><p class="entry-url">${external(e.url,esc(e.url))}</p><div class="entry-origin"><span>FROM SOURCE COLLECTION</span>${external(e.collection_url,esc(e.collection_name))}<small>Original link occurrence ${e.position} · imported discovery lead</small></div></article>`;
  }
  function apiCard(r){
    const v=r.verification;
    const covered=r.catalog_ids.map(id=>datasets.find(d=>d.id===id)).filter(Boolean).map(d=>`<button type="button" data-open-api-dataset="${esc(d.id)}">${esc(d.name)} ↗</button>`).join('');
    return `<article class="resource-card api-card"><span class="resource-kind">${esc(API_KINDS[r.kind])}</span><h3>${external(r.entrypoint,esc(r.name)+' ↗')}</h3><p>${esc(r.description)}</p><p class="api-endpoint">${external(r.entrypoint,esc(r.entrypoint))}</p><dl class="api-facts"><dt>AUTHENTICATION</dt><dd>${esc(API_AUTH[r.auth])}</dd><dt>FORMATS</dt><dd>${r.formats.map(esc).join(' · ')}</dd><dt>CHECKED ${esc(v.checked_date)}</dt><dd class="api-status ${esc(v.status)}">${esc(API_STATUS[v.status])}</dd></dl><details><summary>Access, evidence &amp; limits</summary><p>${esc(r.auth_notes)}</p><p>${esc(v.note)}${v.http_status?` · HTTP ${esc(v.http_status)}`:''}</p><ul>${r.limitations.map(s=>`<li>${esc(s)}</li>`).join('')}</ul><ul>${sourceList(r)}</ul></details>${covered?`<div class="api-coverage"><span>RELATED CATALOG RELEASES</span>${covered}</div>`:''}</article>`;
  }
  function renderChips(){
    const chips=[];
    if(state.q)chips.push(['q',`Search: ${state.q}`]);
    if(state.view==='datasets')for(const k of ['category','access','structure','license','unit'])if(state[k]){
      const label=k==='category'?categoryShort[state[k]]:k==='access'?accessLabel[state[k]]:k==='structure'?structureLabel[state[k]]:k==='license'?(state[k]==='unknown'?'License unverified':'License terms documented'):({structures:'Structure counts',configurations:'Configuration counts',observations:'Property / literature counts',unknown:'Size unverified'}[state[k]]);
      chips.push([k,label||state[k]]);
    }
    if(state.view==='sources')for(const k of ['collection','scope'])if(state[k])chips.push([k,k==='collection'?collections.find(c=>c.id===state[k])?.name||state[k]:SCOPE_LABELS[state[k]]]);
    if(state.view==='apis')for(const k of ['api_kind','api_auth'])if(state[k])chips.push([k,(k==='api_kind'?API_KINDS:API_AUTH)[state[k]]]);
    $('active-filters').innerHTML=chips.map(([key,label])=>`<button type="button" class="filter-chip" data-clear="${key}" aria-label="Remove ${esc(label)} filter">${esc(label)} <span aria-hidden="true">×</span></button>`).join('');
    $('active-filters').hidden=chips.length===0;
    $('reset').disabled=chips.length===0&&state.sort===DEFAULT_STATE.sort;
  }
  function renderSearchOverview(){
    const panel=$('search-overview');
    if(!state.q.trim()){panel.hidden=true;panel.innerHTML='';return;}
    const matches=searchOverview(catalog,state.q);
    const current=state.view==='sources'?'this source-entry view':state.view==='resources'?'the portal view':state.view==='apis'?'the API view':'the dataset view';
    const labels={datasets:'dataset records',resources:'portals & resources',sources:'source entries',apis:'API / SDK routes'};
    const switches=Object.entries(matches).map(([view,rows])=>`<button type="button" data-search-view="${view}">${rows.length} ${labels[view]} <span aria-hidden="true">↗</span></button>`).join('');
    const previews=state.view!=='datasets'?matches.datasets.slice(0,8).map(d=>`<button type="button" data-open-dataset="${esc(d.id)}">${esc(d.name)} <span aria-hidden="true">↗</span></button>`).join(''):'';
    panel.innerHTML=`<p><strong>Search across MatVerse.</strong> Results below use ${current} and its selected filters. Open a result group to search it without those filters.</p><div class="search-view-links">${switches}</div>${previews?`<div class="search-dataset-previews"><span>DATASET MATCHES ELSEWHERE IN THE ATLAS</span>${previews}</div>`:''}`;
    panel.hidden=false;
  }
  function render(){
    const resourceMode=state.view==='resources',sourceMode=state.view==='sources',datasetMode=state.view==='datasets',apiMode=state.view==='apis';
    visible=apiMode?filterAPIs(apiSources,state):sourceMode?filterSourceEntries(sourceEntries,state):resourceMode?filterResources(resources,state):filterDatasets(datasets,state,categories);
    $('search').value=state.q;
    for(const k of ['category','access','structure','license','sort','collection','scope','api_kind','api_auth'])$(k).value=state[k];
    $('clear-search').hidden=!state.q;
    document.querySelectorAll('.dataset-filter').forEach(el=>el.hidden=!datasetMode);
    document.querySelectorAll('.source-filter').forEach(el=>el.hidden=!sourceMode);
    document.querySelectorAll('.api-filter').forEach(el=>el.hidden=!apiMode);
    $('source-note').hidden=!sourceMode;
    $('api-note').hidden=!apiMode;
    $('sort').parentElement.hidden=!datasetMode;
    $('filters').classList.toggle('resource-mode',resourceMode);
    $('filters').classList.toggle('api-mode',apiMode);
    $('filters').classList.toggle('source-mode',sourceMode);
    $('type-tabs').hidden=!datasetMode;
    $('directory-title').textContent=apiMode?'API-accessible / Agent-ready sources':sourceMode?'Source collection entries':resourceMode?'Repositories & portals':'Dataset directory';
    $('directory-description').textContent=apiMode?'Search query APIs, OPTIMADE endpoints, bulk SDKs and structured file downloads.':sourceMode?'Search every imported link by its original name, URL, section or collection.':resourceMode?'Find source collections, discovery tools, APIs and adjacent data resources.':'Search dataset names, properties, methods, tags and source evidence.';
    $('search').placeholder=apiMode?'Provider, OPTIMADE, format…':sourceMode?'Source name, URL, section…':resourceMode?'Repository, portal, topic…':'Name, property, method…';
    $('result-count').textContent=`${visible.length} of ${apiMode?apiSources.length:sourceMode?sourceEntries.length:resourceMode?resources.length:datasets.length} ${apiMode?'access routes':sourceMode?'source entries':resourceMode?'resources':'records'}`;
    for(const view of ['datasets','resources','sources','apis']){$('view-'+view).classList.toggle('selected',state.view===view);$('view-'+view).setAttribute('aria-pressed',String(state.view===view));}
    document.querySelectorAll('[data-unit]').forEach(btn=>{btn.classList.toggle('selected',btn.dataset.unit===state.unit);btn.setAttribute('aria-pressed',String(btn.dataset.unit===state.unit));});
    $('dataset-table-wrap').hidden=!datasetMode||visible.length===0;
    document.querySelector('.mobile-table-hint').hidden=!datasetMode||visible.length===0;
    $('resource-grid').hidden=datasetMode||visible.length===0;
    $('empty-state').hidden=visible.length!==0;
    $('table-footnote').textContent=apiMode?'Verification is dated: a small record sample, metadata response, empty response, authentication requirement or unsuccessful probe are different outcomes. Interface access does not establish scientific quality or data reuse rights.':sourceMode?'Entries preserve source context; exact-URL deduplication is documented per collection. Scope labels aid discovery; destinations, counts and licenses require their own evidence. Source entries are excluded from dataset size rankings.':resourceMode?'Portals, APIs and collections are navigation resources, not additional independent crystal datasets.':'~ Approximate · ≥ Reported lower bound · Unranked = size unverified. “Public access” describes availability; data may still carry restrictions. Expand a release for its source evidence.';
    if(datasetMode)$('dataset-rows').innerHTML=visible.map(datasetRow).join('');
    else $('resource-grid').innerHTML=apiMode?visible.map(apiCard).join(''):sourceMode?visible.map(sourceEntryCard).join(''):visible.map(r=>`<article class="resource-card"><span class="resource-kind">${esc(r.kind)}</span><h3>${external(r.url,esc(r.name)+' <span class="external-arrow" aria-hidden="true">↗</span>')}</h3><p>${esc(r.description)}</p><details><summary>Source evidence · ${r.sources.length}</summary><ul>${sourceList(r)}</ul></details></article>`).join('');
    $('export-csv').disabled=$('export-json').disabled=visible.length===0;
    renderChips();renderSearchOverview();updateURL();
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
  for(const c of collections)$('collection').insertAdjacentHTML('beforeend',`<option value="${esc(c.id)}">${esc(c.name)} (${c.entry_count})</option>`);
  $('source-view-count').textContent=sourceEntries.length;
  $('api-view-count').textContent=apiSources.length;
  $('stat-datasets').textContent=$('dataset-view-count').textContent=datasets.length;
  $('stat-categories').textContent=Object.keys(categories).length;
  $('stat-sources').textContent=new Set(datasets.flatMap(d=>d.sources.map(s=>s.url))).size;
  $('stat-resources').textContent=$('resource-view-count').textContent=resources.length;
  $('checked-date').textContent=new Intl.DateTimeFormat('en-GB',{day:'2-digit',month:'short',year:'numeric',timeZone:'UTC'}).format(new Date(catalog.checkedDate+'T12:00:00Z')).toUpperCase();
  $('filters').addEventListener('submit',e=>e.preventDefault());
  $('search').addEventListener('input',e=>{state.q=e.target.value;render();});
  for(const k of ['category','access','structure','license','sort','collection','scope','api_kind','api_auth'])$(k).addEventListener('change',e=>{state[k]=e.target.value;render();});
  $('clear-search').addEventListener('click',()=>{state.q='';render();$('search').focus();});
  $('type-tabs').addEventListener('click',e=>{const b=e.target.closest('[data-unit]');if(b){state.unit=b.dataset.unit;render();}});
  $('active-filters').addEventListener('click',e=>{const b=e.target.closest('[data-clear]');if(b){state[b.dataset.clear]='';render();}});
  $('search-overview').addEventListener('click',e=>{
    const viewButton=e.target.closest('[data-search-view]');
    if(viewButton){state=globalSearchState(state.q,viewButton.dataset.searchView);render();return;}
    const datasetButton=e.target.closest('[data-open-dataset]');
    if(datasetButton){const id=datasetButton.dataset.openDataset;state=globalSearchState(state.q);render();expand(id,true);$('release-'+id)?.scrollIntoView({block:'start'});}
  });
  for(const v of ['datasets','resources','sources','apis'])$('view-'+v).addEventListener('click',()=>{state.view=v;render();});
  $('resource-grid').addEventListener('click',e=>{const b=e.target.closest('[data-open-api-dataset]');if(b){state=globalSearchState('');render();expand(b.dataset.openApiDataset,true);$('release-'+b.dataset.openApiDataset)?.scrollIntoView({block:'start'});}});
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
if(typeof module!=='undefined'&&module.exports)module.exports={propertyAccessHTML,normalize,normalizeSearch,queryTokens,matchesQuery,unitKind,licenseUnknown,sortDatasets,filterDatasets,filterResources,filterAPIs,filterSourceEntries,searchOverview,globalSearchState,csvFor,escapeHTML,formatCount,DEFAULT_STATE};
if(typeof document!=='undefined')startApp();
