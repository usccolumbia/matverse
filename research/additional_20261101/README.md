# Additional materials dataset discoveries

Completed locally on 2026-11-01. **50 new dataset/release records** extend the 304-record baseline to **354 records**. This is a targeted domain expansion, not an exhaustive inventory of materials data online. No GitHub commit or push is authorized.

- [Frozen research brief](BRIEF.md)
- [Generated comparison survey](../../docs/additional-datasets.md)
- [Integration receipt, canonical IDs, input hashes and year corrections](integration_receipt.json)
- [Source inventory: 243 route/lead occurrences](../collection_additional_20261101.json)

## Research packages

| Perspective | Integrated records | Evidence and dispositions |
|---|---:|---|
| Atomistic references and experimental properties | 16 | [Notes](coordinator/notes.md) · [Leads](coordinator/leads.json) · [Queries](coordinator/queries.json) · [Count receipts](coordinator/count_receipts.json) |
| Defects, disorder and irradiation | 12 | [Notes](defects/notes.md) · [Leads](defects/leads.json) · [Queries](defects/queries.json) · [Validation](defects/validation.json) |
| Porous materials, adsorption and thermal labels | 9 | [Notes](porous/notes.md) · [Leads](porous/leads.json) · [Queries](porous/queries.json) · [Payload inspection](porous/payload_inspection.json) |
| Functional and low-dimensional materials | 13 | [Notes](functional/notes.md) · [Leads](functional/leads.json) · [Validation](functional/validation.json) |

The staging files preserve the original handoff and source scope. `data/datasets.json` is maintained canonical metadata; tags and normalized terms added during integration live there. Staging is not an automatic replacement for canonical data.

Primary evidence spans actual provider tables, author repositories, named releases, selected coordinate/CSV/Excel/SQLite/extXYZ payloads, DOI metadata and papers. Compact receipts retain request status, versions, bytes and SHA-256 hashes; unsuccessful probes remain failures. Raw responses and payloads remain exclusively under ignored `research/cache/additional_20261101/` paths. No downloaded source code or pickle was executed.

Counts distinguish parent systems, calculations, sites, frames, observations, generated CIFs and model predictions. Overlap/derivation is explicit: MOF parents, Si/SiO2/SiOx references, original/revised carbon data and merged thermoelectric sources are not additive. Article or software licenses are not assumed to govern separate data. Some terms remain unverified or conflicting; ULTERA files remain provider-restricted. The revised SoLiD26 public release supersedes the early preprint's by-request access statement.

The preview review also exposed 23 previous journal-import years incorrectly parsed as 2002. Each was corrected using the retained journal DOI/publication date. The integration receipt records all before/after values and sources without overwriting historical staging.

The search-page header was made compact locally: smaller headline and vertical padding, no forced headline line break, shorter supporting description and tighter provenance badges. Lab attribution remains visible. The local native browser preview was visually checked; screenshot retained under ignored `research/cache/compact-banner-preview.png`.
