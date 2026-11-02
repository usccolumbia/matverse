# Experimental crystallography and reference collections

[Back to MatVerse](../../README.md)

Checked 2026-11-02. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="csd"></a>
## Cambridge Structural Database (CSD)

Curated experimental three-dimensional organic and metal-organic crystal structures.

**Size:** 1,431,347 crystal structures (source wording: 1,431,347 (arithmetic sum of published-structure table)).

**Scope:** Sum of 63 rows in official Structures column, publications 1923–2026, cutoff 2026-01-01; not a November live counter

**Release:** CCDC publication-year statistics, 2026-01-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; molecular conformation; crystal packing.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.ccdc.cam.ac.uk/solutions/software/csd/) · [data](https://www.ccdc.cam.ac.uk/structures/)

**Count derivation:** sum of 63 Structures-column rows in CCDC January-2026 publication-year statistics; incomplete at cutoff; 4,045 + 656 + 690 + 942 + 977 + 1,133 + 1,268 + 1,552 + 1,981 + 1,995 + 2,145 + 2,180 + 2,749 + 3,101 + 3,425 + 3,885 + 4,257 + 4,667 + 5,241 + 5,255 + 6,516 + 6,924 + 6,875 + 7,500 + 7,699 + 7,826 + 8,965 + 9,975 + 10,737 + 12,082 + 12,304 + 13,030 + 15,615 + 15,971 + 17,370 + 18,928 + 20,098 + 21,915 + 24,478 + 26,462 + 28,277 + 31,950 + 34,940 + 36,901 + 37,292 + 41,546 + 42,467 + 45,008 + 48,190 + 49,115 + 52,105 + 55,285 + 56,901 + 59,633 + 58,390 + 61,172 + 64,116 + 60,934 + 60,952 + 60,892 + 61,927 + 58,600 + 1,340 = 1,431,347.

**Evidence:**

- [CCDC CSD Publication Year Statistics, 1 January 2026](https://www.ccdc.cam.ac.uk/media/CSD-Publication-Year-Statistics-2026.pdf) (checked 2026-11-01): Summing 63 published-structure counts gives 1431347. Source marks 2025 as incomplete at the January-2026 cutoff; atom averages are a different column.
- [CCDC: Access Structures downloads](https://support.ccdc.cam.ac.uk/support/solutions/articles/103000306361/) (checked 2026-11-01): Individual CIF downloads are free after accepting conditions of use.
- [CCDC/FIZ Access Structures](https://www.ccdc.cam.ac.uk/structures/) (checked 2026-11-01): Distinguishes free retrieval from advanced licensed CSD-Core and ICSD functionality.

**Reuse and interpretation notes:**

- Count is an explicitly computed sum of the provider publication-year table, not an independently deduplicated or live November-2026 total.
- Individual retrieval is free; advanced curated database products require licences.
- Calculated non-CSD depositions are outside the curated experimental CSD remit.

**Tags:** CIF, molecular-crystals, mixed-access, foundational, dated-provider-statistics.

<a id="cod"></a>
## Crystallography Open Database (COD)

Open CIF collection spanning inorganic, organic, metal-organic and mineral crystals.

**Size:** 535,025 entries (source wording: 535025 entries).

**Scope:** Live COD mirror counter; latest deposition shown 2026-10-23

**Release:** Live homepage, accessed 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; unit cells; space groups.

**Access:** open. **Dataset license:** CC0.

**Official routes:** [homepage](https://www.crystallography.net/cod/) · [data](https://www.crystallography.net/cod/archives/)

**Evidence:**

- [COD official mirror](https://cod.psdi.ac.uk/) (checked 2026-11-01): Shows 535025 entries, crystal-family coverage excluding biopolymers, and CC0 public-domain dedication.

**Reuse and interpretation notes:**

- Entries are database records, not deduplicated compositions or independently validated new materials.
- Scope and data quality must be checked per CIF; reference patterns calculated from CIFs are not measured XRD.

**Tags:** CIF, open, experimental, foundational.

<a id="mpds-pauling-file"></a>
## Materials Platform for Data Science (MPDS / PAULING FILE)

Literature-curated inorganic structures, physical properties and phase diagrams exposed through GUI and API.

**Size:** 424,820 crystalline structures (source wording: 424 820 crystalline structures).

**Scope:** Structural counter only, not the sum of datasheets and physical-property records

**Release:** Live provider counters, accessed 2026-11-01. **Year:** 2026.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structures; physical properties; phase diagrams.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://mpds.io/) · [data](https://mpds.io/#start) · [code](https://mpds.io/developer/)

**Evidence:**

- [MPDS provider home](https://mpds.io/) (checked 2026-11-01): Displays 424820 crystalline structures and distinct counters for 1101574 physical properties and 140255 phase diagrams.
- [MPDS introduction](https://mpds.io/tutorial/) (checked 2026-11-01): Online PAULING FILE edition; subscription provides full data, with limited free and open subsets.

**Reuse and interpretation notes:**

- The platform additionally contains explicitly marked in-house calculated or ML data.
- Free logged-in open access covers a limited subset; full GUI/API require subscription.
- PAULING FILE-derived products overlap and must not be summed.

**Tags:** PAULING-FILE, API, mixed-access, literature.

<a id="atomwork-adv"></a>
## NIMS AtomWork-Adv

Expert-curated inorganic single-phase structure, property and phase-diagram data.

**Size:** 409,723 crystal structures (source wording: 409,723 crystal structures).

**Scope:** NIMS statistics as of 2026-03-31, not a live November counter

**Release:** 2026-03-31 NIMS statistics. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structures; X-ray diffraction; phase diagrams; physical properties.

**Access:** commercial. **Dataset license:** Commercial licensed access under NIMS provider terms; limited downloads; trial has no download permission..

**Official routes:** [homepage](https://atomwork-adv.nims.go.jp/) · [data](https://atomwork-adv.nims.go.jp/en/service.html)

Other denominators (not added to the ranking):

- 746,888 XRD records: Provider-displayed counter; not additional structures
- 568,195 property records: Provider-displayed counter; not additional structures
- 49,650 phase diagrams: Provider-displayed counter; not additional structures

**Evidence:**

- [MEXT/NIMS materials data infrastructure presentation](https://www.mext.go.jp/content/20260522-mxt_jyohoka01-000050160_3.pdf) (checked 2026-11-01): NIMS statistics dated 2026-03-31 give AtomWork-Adv 409723 crystal structures.
- [AtomWork-Adv provider service terms](https://atomwork-adv.nims.go.jp/service.html?lan=jp) (checked 2026-11-01): Purchased licence follows a limited browsing-only trial; licensed use allows limited downloads.
- [A comprehensive data network for data-driven study of battery materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC11573338/) (checked 2026-11-01): Describes expert literature extraction and annual updating of AtomWork-Adv.
- [AtomWork-Adv provider counters and service limits](https://atomwork-adv.nims.go.jp/en/service.html?lan=en) (checked 2026-11-01): Corroborates 409,723 structures, 746,888 XRD records, 568,195 properties and 49,650 phase diagrams. Paid license permits 5,000 downloads/year; the 72-hour/1,000-page-view trial excludes downloads.

**Reuse and interpretation notes:**

- Do not conflate property-value counts with structures or materials.
- Limited trial is not an open bulk dataset.
- Shared PAULING FILE lineage creates overlap with other products.
- Provider permits 5,000 downloads/year under a paid license; the 72-hour/1,000-page trial is browsing-only. This does not establish bulk redistribution rights.

**Tags:** NIMS, commercial, literature.

<a id="pearsons-crystal-data"></a>
## Pearson's Crystal Data

Critically evaluated inorganic structural datasets rooted in PAULING FILE.

**Size:** ~395,000 structural datasets (source wording: about 395,000 structural data sets).

**Scope:** 2023/24 offline release; not a live ASM-MPDS total

**Release:** Release 2023/24. **Year:** 2023.

**Provenance:** literature. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates when determined; displacement parameters; diffraction references.

**Access:** commercial. **Dataset license:** Not verified.

**Official routes:** [homepage](https://crystalimpact.com/pcd/) · [data](https://asm.mpds.io/)

**Evidence:**

- [Pearson's Crystal Data publisher page](https://crystalimpact.com/pcd/) (checked 2026-11-01): 2023/24 release has about 395000 structural datasets; announces transition to ASM online MPDS after final offline release.

**Reuse and interpretation notes:**

- Some datasets lack determined atom coordinates.
- Shares PAULING FILE provenance with MPDS and related products; counts are not additive.
- Publisher page is historical; future access is directed to ASM MPDS.

**Tags:** commercial, PAULING-FILE, historical-release.

<a id="icsd"></a>
## Inorganic Crystal Structure Database (ICSD)

Curated inorganic crystal structures with experimental and separately searchable theoretical collections.

**Size:** 347,985 crystal structures (source wording: 347,985 crystal structures).

**Scope:** Entire ICSD total announced 2026-10-30, including theoretical structures

**Release:** 2026-10-30 announcement. **Year:** 2026.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; space groups; unit cells; experimental metadata.

**Access:** commercial. **Dataset license:** Not verified.

**Official routes:** [homepage](https://icsd.products.fiz-karlsruhe.de/en) · [data](https://icsd.fiz-karlsruhe.de/)

**Evidence:**

- [ICSD home](https://icsd.products.fiz-karlsruhe.de/en) (checked 2026-11-01): News dated 30.10.2026 reports 347,985 crystal structures.
- [About ICSD](https://icsd.products.fiz-karlsruhe.de/en/about/about-icsd) (checked 2026-11-01): Theoretical structures are included and can be searched separately from experimental structures.
- [ICSD products](https://icsd.products.fiz-karlsruhe.de/en/products/icsd-products) (checked 2026-11-01): Provides licensed Web and desktop access options.

**Reuse and interpretation notes:**

- The headline count is not an experimental-only count.
- Free individual deposited structures via CCDC/FIZ Access Structures do not establish bulk redistribution rights.

**Tags:** CIF, commercial, experimental-and-theoretical, foundational.

<a id="atomwork"></a>
## NIMS AtomWork

Inorganic crystal structures, phase diagrams and properties curated from literature.

**Size:** 82,000 crystal structures (source wording: 82,000 crystal structures).

**Scope:** Provider homepage displays 82000 structures for the base 2010/06 release; not a new November release or AtomWork-Adv total

**Release:** NIMS AtomWork base data release 2010/06; provider counters checked 2026-11-01. **Year:** 2010.

**Provenance:** literature. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structures; phase diagrams; physical properties.

**Access:** registration. **Dataset license:** NIMS proprietary terms: written permission required for reproduction, republication or third-party distribution; bulk acquisition and scraping prohibited..

**Official routes:** [homepage](https://crystdb.nims.go.jp/) · [data](https://crystdb.nims.go.jp/)

Other denominators (not added to the ranking):

- 55,000 property records: Displayed base AtomWork counter; not additional structures
- 15,000 phase diagrams: Displayed base AtomWork counter; not additional structures

**Evidence:**

- [MEXT materials data reference, NIMS-provided table](https://www.mext.go.jp/content/20200602-mxt_nanozai-000007507_6_2.pdf) (checked 2026-11-01): NIMS table separates AtomWork 82000 structures, 15000 phase diagrams and 55000 properties from AtomWork-Adv.
- [NIMS MatNavi](https://mits.nims.go.jp/en/) (checked 2026-11-01): Free registered browsing; mass acquisition and web scraping prohibited.
- [NIMS AtomWork provider release and access terms](https://crystdb.nims.go.jp/) (checked 2026-11-01): Displays data release 2010/06, 82,000 crystal structures, 55,000 property records and 15,000 phase diagrams. Registered access; bulk acquisition/scraping prohibited; written permission required for reproduction or third-party distribution.

**Reuse and interpretation notes:**

- MatNavi access does not authorize bulk scraping.
- Related PAULING FILE/AtomWork products overlap.
- Primary provider page corroborates displayed counters; records were not independently deduplicated. The underlying base release remains 2010/06.

**Tags:** NIMS, registration, historical-count, Inorganic Materials Database, NMIS (user-listed spelling).

<a id="aflow-prototypes"></a>
## AFLOW Encyclopedia of Crystallographic Prototypes

Reference crystal prototypes with parameterized structures, symmetry labels and literature references.

**Size:** 2,127 prototype CIF files (source wording: 2,127).

**Scope:** Files ending /aflow.cif in the non-truncated repository tree at fb7421bb2522888b6a0a4ff91e124c6c65191096; not AFLOW calculation records.

**Release:** Repository tree fb7421bb2522888b6a0a4ff91e124c6c65191096. **Year:** Not verified.

**Provenance:** curated. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal prototype; space group; Pearson symbol; Strukturbericht designation.

**Access:** open. **Dataset license:** Apache-2.0 (repository license).

**Official routes:** [homepage](https://github.com/aflow-org/aflow_prototype_encyclopedia) · [data](https://github.com/aflow-org/aflow_prototype_encyclopedia/tree/fb7421bb2522888b6a0a4ff91e124c6c65191096/data)

Other denominators (not added to the ranking):

- 629 structures represented in MateriaViva: MateriaViva source alias aflow-prototypes; overlapping imported membership, not the source-release total

**Evidence:**

- [AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (checked 2026-11-02): Pinned recursive Git tree fb7421bb2522888b6a0a4ff91e124c6c65191096 contains 2,127 aflow.cif paths; repository declares Apache-2.0.
- [MateriaViva source database table](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) (checked 2026-11-02): Source alias aflow-prototypes reports 629 represented structures. This imported denominator is separate from the source-release count.

**Reuse and interpretation notes:**

- Prototype representatives are not a count of experimentally distinct compounds or DFT calculations.
- Overlaps MateriaViva and potentially other catalog releases; counts must not be added across these records.

**Tags:** MateriaViva source coverage, aflow-prototypes.

<a id="magndata"></a>
## MAGNDATA

Published commensurate and incommensurate magnetic structures with atomic positions and magnetic moments in magCIF.

**Size:** ≥2,000 magnetic structures (source wording: more than 2000 published ... magnetic structures).

**Scope:** Landing-page lower bound, not an enumerated release

**Release:** Live landing page, accessed 2026-11-01. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `periodic_atomic`.

**Labels/content:** magnetic moments; magnetic symmetry; atomic coordinates.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://cryst.ehu.es/magndata/) · [data](https://cryst.ehu.es/magndata/magndata_download.html)

**Evidence:**

- [MAGNDATA landing page](https://cryst.ehu.es/magndata/) (checked 2026-11-01): Reports more than 2000 structures and downloadable .mcif information defining positions and moments.
- [MAGNDATA bulk download instructions](https://test2.cryst.ehu.eus/magndata/magndata_download.html) (checked 2026-11-01): Bulk repository download requires an approved account; currently academic or educational institutions only.

**Reuse and interpretation notes:**

- Individual entries are downloadable; bulk access has registration and institutional restrictions.
- Magnetic structures may be multiple measurements or phases of one composition.

**Tags:** magCIF, magnetism, experimental, registration-for-bulk.

<a id="amcsd"></a>
## American Mineralogist Crystal Structure Database (AMCSD)

Published mineral and synthetic-phase structure refinements with coordinates, cells, symmetry and references.

**Size:** Unranked crystal structures (source wording: Not verified).

**Scope:** Current AMCSD collection; no current primary total verified

**Release:** Current RRUFF documentation. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; unit cells; space groups; mineral identity.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.rruff.net/) · [data](https://www.rruff.net/about/download-data/)

**Evidence:**

- [RRUFF FAQ: AMCSD](https://www.rruff.net/help/faq/) (checked 2026-11-01): Identifies AMCSD as peer-reviewed mineral and synthetic-phase crystallographic refinements.
- [RRUFF: ZIP download](https://www.rruff.net/help/zip-download/) (checked 2026-11-01): AMCSD archives include full structural .amc and minimal CIF files.

**Reuse and interpretation notes:**

- Do not infer a permissive data licence from free ZIP availability.
- Overlaps mineral structures in COD and data linked to RRUFF specimens.

**Tags:** CIF, minerals, bulk-download.
