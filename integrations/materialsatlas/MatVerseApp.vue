<script setup lang="ts">
import { computed, onBeforeUnmount, ref } from 'vue'

const queryKeys = ['q', 'category', 'access', 'structure', 'license', 'unit', 'sort', 'view', 'collection', 'scope', 'api_kind', 'api_auth']
const revision = ref(0)
const loaded = ref(false)
const frame = ref<HTMLIFrameElement | null>(null)
// Applied only to this same-origin embedded document; full-page MatVerse keeps its normal layout.
const compactStyles = `
.hero,.stats,.count-note,.reading-strip,body>footer{display:none!important}
main.shell{width:100%;max-width:none;margin:0}
#directory{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:12px;padding:10px 14px 18px;scroll-margin-top:10px}
#directory>:not(.directory-heading):not(.view-switch){grid-column:1/-1}
.directory-heading{grid-column:2;grid-row:1;align-self:start}
.directory-heading>div{display:none}
.export-menu summary{min-height:32px;padding:7px 10px;font-size:11px;gap:8px}
.view-switch{grid-column:1;grid-row:1;margin:0 0 10px;gap:8px 14px;align-items:start;min-width:0}
.view-switch>button{font-size:11px;padding:7px 0 9px}
.filters{grid-template-columns:minmax(170px,1.45fr) repeat(5,minmax(95px,1fr));gap:8px}
.filters.api-mode,.filters.source-mode{grid-template-columns:minmax(170px,1.5fr) repeat(3,minmax(120px,1fr))}
.filters.resource-mode:not(.api-mode):not(.source-mode){grid-template-columns:minmax(200px,2fr) 1fr}
.filters label{margin-bottom:4px;min-height:14px;font-size:9px}
.filters input,.filters select{height:36px}
.input-wrap>svg{top:9px}.input-wrap>button{top:6px}
.source-note{margin:0 0 10px;padding:8px 10px;font-size:11px}
.source-note p{font-size:11px;line-height:1.45}
.results-toolbar{margin:10px 0 8px;gap:8px;flex-direction:row;align-items:center;flex-wrap:wrap}
.results-actions{width:auto;justify-content:flex-end}
.type-tabs{gap:3px}.type-tabs button{padding:6px 8px;font-size:10px}
.search-overview{margin-top:10px;padding:8px 10px;font-size:11px;line-height:1.45}
.search-overview p{margin:0 0 5px}
.active-filters{gap:5px;margin:0 0 8px}.filter-chip{padding:4px 7px}
th{padding:10px 12px}td{padding:12px}
.details-cell{padding:12px 0}.category-label{margin-top:4px}
.dataset-link{font-size:13px}.dataset-count{font-size:15px}
.dataset-description,.license-text{margin-top:5px}
.table-footnote{margin:8px 0 0}
@media(max-width:850px){.filters{grid-template-columns:minmax(160px,1.4fr) 1fr 1fr}.filters.api-mode,.filters.source-mode{grid-template-columns:1fr 1fr}}
@media(max-width:620px){
 #directory{grid-template-columns:minmax(0,1fr);padding:8px 10px 12px}
 .directory-heading{grid-column:1;grid-row:1;justify-self:end;margin-bottom:6px}
 .view-switch{grid-column:1;grid-row:2;margin-bottom:8px;gap:5px 12px}
 .filters,.filters.api-mode,.filters.source-mode{grid-template-columns:1fr 1fr}
 .filters .search-field{grid-column:1/-1}
 .filters .api-filter{grid-column:auto}.api-mode>div:last-child{grid-column:auto}
 .results-toolbar{align-items:start;flex-wrap:wrap}.results-actions{margin-left:auto}
}
`
function compactFrame() {
  const doc = frame.value?.contentDocument
  if (!doc) return
  let style = doc.getElementById('materialsatlas-compact-layout') as HTMLStyleElement | null
  if (!style) {
    style = doc.createElement('style')
    style.id = 'materialsatlas-compact-layout'
    doc.head.appendChild(style)
  }
  style.textContent = compactStyles
  loaded.value = true
}
function refreshRoute() { revision.value += 1 }
window.addEventListener('popstate', refreshRoute)
onBeforeUnmount(() => window.removeEventListener('popstate', refreshRoute))
const atlasUrl = computed(() => {
  void revision.value
  const route = window.location.hash.startsWith('#/')
    ? new URL(window.location.hash.slice(1), window.location.origin)
    : new URL(window.location.href)
  const url = new URL('/matverse/index.html', window.location.origin)
  for (const key of queryKeys) {
    const value = route.searchParams.get(key)
    if (value) url.searchParams.set(key, value)
  }
  return `${url.pathname}${url.search}`
})
function openCurrentSearch() {
  const href = frame.value?.contentWindow?.location.href || atlasUrl.value
  window.open(href, '_blank', 'noopener')
}
</script>

<template>
  <article class="matverse-app">
    <header class="matverse-toolbar">
      <h1>MatVerse <span>Dataset search</span></h1>
      <div class="matverse-actions">
        <button class="outline-button" type="button" @click="openCurrentSearch">Open full page ↗</button>
        <a class="outline-button" href="https://github.com/usccolumbia/matverse" target="_blank" rel="noopener">Source &amp; survey ↗</a>
      </div>
    </header>
    <p v-if="!loaded" class="matverse-loading" role="status">Loading the dataset atlas…</p>
    <iframe
      id="matverse-frame"
      ref="frame"
      :class="['matverse-frame', { ready: loaded }]"
      title="MatVerse searchable materials dataset atlas"
      :src="atlasUrl"
      @load="compactFrame"
    ></iframe>
  </article>
</template>

<style scoped>
.matverse-app{position:relative;min-width:0;width:100%}
.matverse-toolbar{display:flex;align-items:center;justify-content:space-between;gap:8px 16px;flex-wrap:wrap;margin-bottom:8px;min-height:32px}
.matverse-toolbar h1{display:flex;align-items:baseline;flex-wrap:wrap;gap:10px;margin:0;font-size:20px;line-height:1.2}
.matverse-toolbar h1 span{font-size:12px;font-weight:400;color:#56706b}
.matverse-actions{display:flex;gap:6px;flex-wrap:wrap}
.matverse-actions .outline-button{padding:6px 9px;min-height:30px;font-size:12px}
.matverse-frame{display:block;width:100%;height:calc(100dvh - 160px);min-height:360px;border:1px solid #dce5e1;border-radius:8px;background:#f2f6f2;opacity:0}
.matverse-frame.ready{opacity:1}
.matverse-loading{position:absolute;top:65px;left:16px;margin:0;color:#56706b;font-size:14px}
@media(max-width:700px){.matverse-toolbar h1{font-size:18px}.matverse-toolbar h1 span{display:none}.matverse-actions .outline-button{font-size:11px;padding:6px 8px}.matverse-frame{height:calc(100dvh - 140px)}}
</style>
