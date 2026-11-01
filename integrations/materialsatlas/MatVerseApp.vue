<script setup lang="ts">
import { computed, onBeforeUnmount, ref } from 'vue'

const queryKeys = ['q', 'category', 'access', 'structure', 'license', 'unit', 'sort', 'view', 'collection', 'scope', 'api_kind', 'api_auth']
const revision = ref(0)
const loaded = ref(false)
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
  const frame = document.getElementById('matverse-frame') as HTMLIFrameElement | null
  // The locally hosted directory keeps its own filter URL in the frame.
  const href = frame?.contentWindow?.location.href || atlasUrl.value
  window.open(href, '_blank', 'noopener')
}
</script>

<template>
  <article class="matverse-app">
    <header class="matverse-toolbar">
      <div>
        <p class="eyebrow">MaterialsAtlas · Dataset discovery</p>
        <h1>MatVerse</h1>
        <p>Find crystal materials datasets, property tables, APIs and original sources.</p>
      </div>
      <div class="matverse-actions">
        <button class="outline-button" type="button" @click="openCurrentSearch">Open full page ↗</button>
        <a class="outline-button" href="https://github.com/usccolumbia/matverse" target="_blank" rel="noopener">Source &amp; survey ↗</a>
      </div>
    </header>
    <p v-if="!loaded" class="matverse-loading" role="status">Loading the dataset atlas…</p>
    <iframe
      id="matverse-frame"
      class="matverse-frame"
      title="MatVerse searchable materials dataset atlas"
      :src="atlasUrl"
      @load="loaded = true"
    ></iframe>
  </article>
</template>

<style scoped>
.matverse-app{min-width:0;width:100%}
.matverse-toolbar{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:16px}
.matverse-toolbar h1{margin:0 0 5px;font-size:28px}
.matverse-toolbar p{margin:0;color:#56706b;font-size:14px}
.matverse-toolbar .eyebrow{margin-bottom:5px;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.matverse-actions{display:flex;gap:8px;flex-wrap:wrap}
.matverse-frame{display:block;width:100%;height:calc(100vh - 190px);min-height:720px;border:1px solid #dce5e1;border-radius:12px;background:#f2f6f2}
.matverse-loading{color:#56706b;font-size:14px}
@media(max-width:700px){.matverse-toolbar h1{font-size:24px}.matverse-frame{height:85vh;min-height:600px}.matverse-actions{width:100%}}
</style>
