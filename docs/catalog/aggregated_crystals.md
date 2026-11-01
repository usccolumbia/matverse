# Aggregated and deduplicated crystal collections

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="materiaviva-open"></a>
## MateriaViva Open

Cross-database crystal index with structures, source-linked property values, curves and separate model predictions.

**Size:** 10,903,588 deduplicated crystal structures (source wording: 10,903,588).

**Scope:** Release described by the cited source

**Release:** Provider page snapshot, checked 2026-11-01. **Year:** 2026.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; 148 property types; spectra and curves; separate model predictions.

**Access:** open. **Dataset license:** Per row: CC BY 4.0, CC0 1.0, CC BY-SA 4.0, public domain, or MIT (provider declarations).

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open)

Other denominators (not added to the ranking):

- 113,459,302 property values: 148 property types across included structures
- 850,417 curves: Spectra, DOS and band structure records; separate from structure count

**Evidence:**

- [MateriaViva Open — primary documentation](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) (checked 2026-11-01): Card reports 10,903,588 included structures from a 14,590,485-structure pool spanning 55 databases; 290,118 included structures are tagged experimental.

**Reuse and interpretation notes:**

- An aggregate overlapping most parent databases; never add it to their totals.
- Provider reports 2,471,566 stored CIFs with origin_open=false: a matching fingerprint exists in an open source, but the actual stored coordinates came from another or unrecorded source. Filter origin_open for coordinate-source traceability.
- Fingerprint deduplication and per-row licensing are provider claims, not independently audited here.
- Model predictions are distinct from measured or DFT-computed property values.
- Structure-release licensing is separate from property-row terms: the property manifest reports 97,837,513 open, 15,215,145 unclear, 313,041 noncommercial and 93,603 restricted value rows. Preserve each row’s licence and licence_class; these global totals do not determine each property’s class distribution.

**Tags:** MateriaViva, MaterialViva, Matvina, 148 property tables.

<a id="lemat-bulk"></a>
## LeMat-Bulk

Standardized outputs from Materials Project, Alexandria and OQMD, with functional-compatibility subsets.

**Size:** 6,725,590 structure records (source wording: 6,725,590).

**Scope:** Release described by the cited source

**Release:** Main card/config metadata snapshot (2025 release). **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/LeMaterial/LeMat-Bulk)

**Evidence:**

- [LeMat-Bulk — primary documentation](https://huggingface.co/datasets/LeMaterial/LeMat-Bulk) (checked 2026-11-01): Dataset card and config metadata report 6,725,590 structure records representing 5,860,446 materials; PBE compatible subset has 5,335,299 rows.

**Reuse and interpretation notes:**

- 6,725,590 records are not 6,725,590 distinct materials.
- Combines upstream databases; energy corrections and computational settings need subset-aware handling.
- This is the non-unique collection; use BulkUnique for the corresponding fingerprint-deduplicated release.

**Tags:** PBE, PBEsol, SCAN, harmonization.

<a id="lemat-bulkunique"></a>
## LeMat-BulkUnique

Fingerprint-deduplicated companion to LeMat-Bulk.

**Size:** 5,438,436 functional-specific unique records (source wording: 5,438,436).

**Scope:** Release described by the cited source

**Release:** December 2024 card snapshot. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY 4.0 (card license section).

**Official routes:** [homepage](https://huggingface.co/datasets/LeMaterial/LeMat-BulkUnique)

**Evidence:**

- [LeMat-BulkUnique — primary documentation](https://huggingface.co/datasets/LeMaterial/LeMat-BulkUnique) (checked 2026-11-01): Card table lists 5,438,436 all records: 5,005,017 PBE, 15,753 PBEsol, and 417,666 SCAN.

**Reuse and interpretation notes:**

- Includes functional-specific subsets; the sum must not be described as a count of experimentally known compounds.
- Overlaps LeMat-Bulk and all three source databases.

**Tags:** deduplication, BAWL.

<a id="mpdd"></a>
## Material-Property-Descriptor Database (MPDD)

Atomic structures organized for high-throughput material featurizers and machine-learning models, maintained by the Phases Research Lab.

**Size:** 4,457,640 atomic structure records (source wording: 4,457,640).

**Scope:** Unfiltered OPTIMADE meta.data_available for the named child database, one-record sample only.

**Release:** Provider/API snapshot, checked 2026-11-01. **Year:** Not verified.

**Provenance:** aggregated; inspect individual source provenance. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; material descriptors and featurizer inputs.

**Access:** open. **Dataset license:** Not verified; inspect collection and original-source terms before redistribution.

**Official routes:** [homepage](https://optimade.mpdd.org/) · [documentation](https://optimade.mpdd.org/) · [api_index](https://providers.optimade.org/index-metadbs/mpdd)

**Evidence:**

- [Material-Property-Descriptor Database (MPDD) provider documentation](https://optimade.mpdd.org/) (checked 2026-11-01): Atomic structures organized for high-throughput material featurizers and machine-learning models, maintained by the Phases Research Lab.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [Material-Property-Descriptor Database (MPDD) bounded API sample](http://mpddoptimade.phaseslab.org/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.

**Reuse and interpretation notes:**

- Database/provider snapshot checked 2026-11-01; overlapping records and releases must not be summed as unique materials.
- Public availability is distinct from reuse permissions; per-record provenance and rights may differ.
- API meta.data_available reports the total; meta.data_returned also contains that total despite only one data object. Use actual data-array length for downloaded sample size.

**Tags:** Repository-coverage-20261101, mpdd, Material-Property-Descriptor Database (MPDD).
