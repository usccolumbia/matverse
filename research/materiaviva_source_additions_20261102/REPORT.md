# MateriaViva source coverage additions — 2026-11-02

Added **16 dataset/release records**, increasing MatVerse from **532 to 548**, and 14 bulk-file routes (35 to 49). All 38 supplied source rows are searchable: 36 map to source-family or release cards, while two grouped aliases have explicit unranked cards because their exact component manifests remain unresolved.

The four Materials Cloud deposits are represented separately. Original dataset families, repackaged releases, imported membership and CIF-file counts remain distinct; none of these totals is additive across overlapping sources. Existing cards are preserved.

## Added records

| Dataset / release | Count | Counted unit |
|---|---:|---|
| [CSLLM non-synthesizable screening set](../../docs/catalog/generation_benchmarks.md#csllm-negatives) | 106470 | CIF files |
| [FAIR-MOFs experimental and optimized structures](../../docs/catalog/porous_frameworks.md#fair-mofs) | 45699 | curated experimental MOF structures |
| [Predicted Crystallography Open Database (PCOD)](../../docs/catalog/bulk_computed.md#pcod) | 1062771 | predicted database entries |
| [Wren prospective coordinate-free discovery dataset](../../docs/catalog/generation_benchmarks.md#wren) | 4721 | converged DFT structures |
| [NovoMag magnetic materials database](../../docs/catalog/property_benchmarks.md#novomag) | 3826 | provider-reported database entries |
| [AFLOW Encyclopedia of Crystallographic Prototypes](../../docs/catalog/experimental_crystallography.md#aflow-prototypes) | 2127 | prototype CIF files |
| [Deem PCOD v2.1 SLC-good — Zenodo release](../../docs/catalog/porous_frameworks.md#deem-zeolites-zenodo-8035241) | 331000 | hypothetical zeolite frameworks |
| [hMOF — JARVIS-Atoms Figshare release](../../docs/catalog/porous_frameworks.md#jarvis-hmof) | 137651 | MOF records |
| [SNUMAT hybrid band gaps — JARVIS Figshare release](../../docs/catalog/property_benchmarks.md#jarvis-snumat) | 10481 | structure-property records |
| [CoRE MOF 2019 — public ASR and FSR release](../../docs/catalog/porous_frameworks.md#core-mof-2019) | 12020 | public ASR structure entries |
| [CMR static collections — MateriaViva source group](../../docs/catalog/aggregated_crystals.md#cmr-static) | Unranked | source-group structures |
| [JARVIS specialized structures — MateriaViva source group](../../docs/catalog/aggregated_crystals.md#jarvis-specialized-structures) | Unranked | source-group structures |
| [A2BC2 ternary electride discovery — Materials Cloud](../../docs/catalog/property_benchmarks.md#mcloud-a2bc2-electrides) | 290 | CIF files |
| [Active-learning nonlinear optical crystals — Materials Cloud](../../docs/catalog/property_benchmarks.md#mcloud-nonlinear-optics) | 2233 | CIF files |
| [Federated optical materials discovery — Materials Cloud](../../docs/catalog/property_benchmarks.md#mcloud-optical-discovery) | 2413 | CIF files |
| [Machine learning on topological materials datasets — Materials Cloud](../../docs/catalog/property_benchmarks.md#mcloud-topological-ml) | 35608 | materials records |

## Remaining evidence limits

- CMR static collections and JARVIS specialized structures: searchable group cards, but no independently resolved component/version manifest. Their MateriaViva membership counts (48,080 and 3,443) are supplemental values only.
- PCOD: 1,062,771 is explicitly the provider’s historical November 2009 total, not a newly measured live count.
- NovoMag: the provider describes 3,826 entries; the downloaded JSON Lines payload contains 3,827 records. Both are recorded and the discrepancy remains unresolved.
- Deem: approximately 331,000 is inherited from the author’s SLC-good description; the three Zenodo archives were not re-counted.
- hMOF: 137,651 comes from the pinned JARVIS documentation inventory; the full ZIP was not parsed.
- CoRE MOF: public ASR 12,020 and FSR 7,061 are declared in the deposited filenames; overlapping variants are not summed.
- FAIR-MOFs: 45,699 experimental and 33,361 optimized structures are deposit-declared, overlapping representations.

## Verification and provenance

- [Original pre-addition audit](../materiaviva_source_coverage_20261102/REPORT.md) is preserved unchanged.
- [Added catalog records](added-records.json), [38-row crosswalk and integration receipt](integration-receipt.json).
- [Deposit metadata](metadata-summary.json), [downloaded payload counts and hashes](payload-inspection.json), [Materials Cloud archive counts and hashes](mcloud-payload-inspection.json).
- [AFLOW pinned tree](aflow-tree.json), [follow-up metadata retrieval receipts](followup-fetch.json).
- New cards include source URLs, verification dates, release-specific license declarations, count scope and overlap caveats. No credentials or source payload datasets are bundled.
