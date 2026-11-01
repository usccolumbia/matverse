# Diffraction, spectroscopy and characterization

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="icdd-pdf5"></a>
## ICDD Powder Diffraction File PDF-5+

Commercial phase-identification reference combining diffraction and crystal-structure information.

**Size:** ≥1,126,200 reference entries (source wording: 1,126,200+ entries).

**Scope:** PDF-5+ 2026 product headline total; 651200+ coordinate-bearing entries are a subset

**Release:** PDF-5+ 2026. **Year:** 2026.

**Provenance:** mixed. **Structure availability:** `mixed`.

**Labels/content:** powder diffraction; phase identification; reference intensities; atomic coordinates for subset.

**Access:** commercial. **Dataset license:** Limited, nonexclusive, and nontransferable license.

**Official routes:** [homepage](https://www.icdd.com/) · [data](https://www.icdd.com/pdf-5/)

**Evidence:**

- [ICDD 2026 product booklet](https://www.icdd.com/assets/files/2026-Product-Booklet.pdf) (checked 2026-11-01): PDF-5+ 2026 advertises 1126200+ entries and 651200+ with atomic coordinates.
- [ICDD licensing process](https://www.icdd.com/licensing-process/) (checked 2026-11-01): Licensed access; restrictions include redistribution and derivative works involving ML or AI, except as expressly authorized.

**Reuse and interpretation notes:**

- Reference entries include calculated as well as measured diffraction information.
- Coordinate-bearing entries are a subset, not an additional dataset.
- Terms restrict derivative ML/AI works and redistribution; do not assume training rights from subscription access.

**Tags:** commercial, XRD, ML-restrictions.

<a id="opxrd"></a>
## opXRD: Open Experimental Powder X-ray Diffraction Database

Labeled and unlabeled experimental powder diffractograms contributed by multiple research institutions.

**Size:** 92,552 diffraction patterns (source wording: 92,552 diffractograms, 2179 of them labeled).

**Scope:** Count described in author preprint; not independently recounted in v11 archive

**Release:** 2025 paper; downloadable archive v11 (2025-04-28). **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** experimental powder XRD; phase labels for subset; partial structure information.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://xrd.aimat.science/) · [data](https://zenodo.org/records/15298026) · [paper](https://doi.org/10.1002/aidi.202500044) · [code](https://github.com/aimat-lab/opXRD)

**Evidence:**

- [opXRD author preprint v2](https://arxiv.org/html/2503.05577v2) (checked 2026-11-01): Reports 92552 collected diffractograms, 2179 labeled, with broad material coverage.
- [opXRD archive v11](https://zenodo.org/records/15298026) (checked 2026-11-01): Author archive provides experimental single- and multiphase pXRD data.
- [opXRD Zenodo metadata](https://zenodo.org/api/records/15298026) (checked 2026-11-01): Metadata identifies v11 and CC BY 4.0 licence.

**Reuse and interpretation notes:**

- Most patterns are unlabeled.
- Not a database of 92552 resolved atomic structures.
- Count is paper-reported; archive payload was not downloaded or independently enumerated.

**Tags:** XRD, experimental, open, labels-sparse.

<a id="mdr-xafs"></a>
## MDR XAFS DB

Integrated experimental X-ray absorption fine-structure spectra with standardized metadata and source DOIs.

**Size:** 2,264 collection items (source wording: 2264 items).

**Scope:** MDR collection items; a work may include sample/reference spectra and metadata

**Release:** Live collection, accessed 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** XAFS spectra; absorption edges; measurement metadata; local structure probes.

**Access:** open. **Dataset license:** CC BY-NC-SA 4.0 for whole database; individual data CC BY or CC BY-NC-SA.

**Official routes:** [homepage](https://mdr.nims.go.jp/collections/a0f3fbf1-f94a-4be7-8a66-6b91a24f6b54) · [data](https://doi.org/10.48505/nims.1447) · [paper](https://doi.org/10.1080/27660400.2023.2197518)

**Evidence:**

- [MDR XAFS DB collection](https://mdr.nims.go.jp/collections/a0f3fbf1-f94a-4be7-8a66-6b91a24f6b54) (checked 2026-11-01): Shows 2264 items, metadata/API facilities, and distinct whole-database and item-level licences.

**Reuse and interpretation notes:**

- Item count is not necessarily a unique-material or individual-spectrum count.
- Inspect each record licence; whole-database reuse has noncommercial/share-alike conditions.
- Local spectroscopy does not guarantee a full atomic structure.

**Tags:** NIMS, XAFS, spectroscopy, API.

<a id="raman-open-database"></a>
## Raman Open Database (ROD)

Open Raman spectra collection interconnected with crystallographic records.

**Size:** 1,133 entries (source wording: 1133 entries).

**Scope:** ROD live counter; latest deposition shown 2025-10-30

**Release:** Live provider homepage, accessed 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `structure_linked`.

**Labels/content:** Raman spectra; sample identity; linked diffraction structure information.

**Access:** open. **Dataset license:** CC0.

**Official routes:** [homepage](https://solsa.crystallography.net/rod/) · [paper](https://journals.iucr.org/j/issues/2019/03/00/nb5236/)

**Evidence:**

- [ROD homepage](https://solsa.crystallography.net/rod/) (checked 2026-11-01): Shows 1133 entries and CC0 public-domain dedication.
- [ROD primary descriptor](https://journals.iucr.org/j/issues/2019/03/00/nb5236/) (checked 2026-11-01): Describes the interconnected Raman and X-ray diffraction identification resource.

**Reuse and interpretation notes:**

- Spectrum entries are not a count of unique atomic structures or compositions.

**Tags:** Raman, CC0, structure-linked.

<a id="remi-fe-co-ni-combinatorial"></a>
## REMI Fe-Co-Ni combinatorial library

Experimental composition-spread alloy library with aligned X-ray diffraction and magnetic measurements.

**Size:** 921 composition-spread sample points (source wording: 921).

**Scope:** Released REMI library files at nist-pages commit 596b04435fb577175264a70c4434f5539b809510

**Release:** REMI nist-pages source snapshot2026-11-01. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** composition; X-ray diffraction; magnetic coercivity; Kerr rotation.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://pages.nist.gov/remi/data/) · [data](https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni) · [paper](https://arxiv.org/abs/2204.05838)

**Evidence:**

- [REMI direct data list](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md) (checked 2026-11-01): Identifies this library as composition-spread data for discovery/optimization benchmarking.
- [Library data description](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni/data%20description.txt) (checked 2026-11-01): Documents sample-wise correspondence of composition, diffraction and magnetic measurements.
- [Official release files](https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni) (checked 2026-11-01): MATLAB arrays C(921,3), XRD(921,89), Coer(921,1), Kerr(921,1) align across921 samples.

**Reuse and interpretation notes:**

- Sample points are not unique fully solved atomic crystal structures; atomic coordinates are absent.
- Combinatorial alloy phases can include mixtures or amorphous regions; the crystalline state is not uniform across the library.
- Release-specific data license was not verified; a general NIST/software license is not silently assigned.
- Shared source experiments may appear in later active-learning studies; benchmark versions must preserve their provenance.

**Tags:** experimental, combinatorial-library, diffraction, composition-only.

<a id="remi-fe-ga-pd-combinatorial"></a>
## REMI Fe-Ga-Pd combinatorial library

Composition-spread alloy library combining measured diffraction/magnetic response with computed phase-region labels.

**Size:** 278 composition-spread sample points (source wording: 278).

**Scope:** Released REMI library files at nist-pages commit 596b04435fb577175264a70c4434f5539b809510

**Release:** REMI nist-pages source snapshot2026-11-01. **Year:** 2020.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** composition; X-ray diffraction; SQUID voltage; computed DFT phase-region label.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://pages.nist.gov/remi/data/) · [data](https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd) · [paper](https://doi.org/10.1038/s41467-020-19597-w)

**Evidence:**

- [REMI direct data list](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md) (checked 2026-11-01): Identifies this library as composition-spread data for discovery/optimization benchmarking.
- [Library data description](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/data%20description.txt) (checked 2026-11-01): Documents sample-wise correspondence of composition, diffraction and magnetic measurements.
- [Official release files](https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd) (checked 2026-11-01): Composition(278,3), XRD(278,551), magnetic(278,2), DFT label(278,) arrays align across278 samples.

**Reuse and interpretation notes:**

- Sample points are not unique fully solved atomic crystal structures; atomic coordinates are absent.
- Combinatorial alloy phases can include mixtures or amorphous regions; the crystalline state is not uniform across the library.
- Release-specific data license was not verified; a general NIST/software license is not silently assigned.
- Shared source experiments may appear in later active-learning studies; benchmark versions must preserve their provenance.

**Tags:** experimental, combinatorial-library, diffraction, composition-only.

<a id="rruff"></a>
## RRUFF mineral spectroscopy and diffraction

Mineral specimen chemistry, Raman/IR spectra, powder XRD and structural metadata.

**Size:** Unranked samples (source wording: Current primary sample or spectrum count not verified).

**Scope:** RRUFF empirical mineral collection; modality counts differ

**Release:** Current provider documentation. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `structure_linked`.

**Labels/content:** Raman spectra; infrared spectra; powder XRD; chemistry; cell parameters.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.rruff.net/) · [data](https://www.rruff.net/about/download-data/)

**Evidence:**

- [RRUFF home](https://www.rruff.net/) (checked 2026-11-01): Lists empirical mineral chemistry, cell parameters and multiple spectroscopic modalities.
- [RRUFF data downloads](https://www.rruff.net/about/download-data/) (checked 2026-11-01): Offers ZIP collections for chemistry, Raman, IR and powder XRD.
- [RRUFF download documentation](https://www.rruff.net/help/zip-download/) (checked 2026-11-01): Distinguishes raw and processed spectra; calculated XRD profiles are labeled processed.

**Reuse and interpretation notes:**

- No current count repeated from third-party catalogues.
- Modalities and repeated measurements do not equal unique minerals.
- Processed XRD may include calculated profiles; do not treat every profile as measured.
- Data licence not independently verified.

**Tags:** minerals, Raman, XRD, IR, bulk-download.
