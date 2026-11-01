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

**Tags:** None assigned.

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
