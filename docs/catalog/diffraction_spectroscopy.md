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

<a id="mp-kedge-xanes-2018"></a>
## Materials Project K-edge XANES release

FEFF multiple-scattering XANES spectra for inequivalent absorber sites of MP crystal structures.

**Size:** ≥500,000 site-resolved K-edge XANES spectra (source wording: 500,000).

**Scope:** Paper reports more than500,000 spectra over more than40,000 materials

**Release:** 2018 paper cohort; deposit checked 2026-11-01. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** K-edge XANES energy-dependent absorption; absorber-site identity; calculation input parameters; site-averaged elemental spectra.

**Access:** open. **Dataset license:** CC0 1.0 (Figshare K-edge archive).

**Official routes:** [publication](https://doi.org/10.1038/sdata.2018.151) · [data](https://doi.org/10.6084/m9.figshare.5678998.v1)

Other denominators (not added to the ranking):

- 40,000 materials (lower bound): Descriptor reports more than40,000 unique materials

**Evidence:**

- [Materials Project K-edge XANES release — Scientific Data descriptor](https://doi.org/10.1038/sdata.2018.151) (checked 2026-11-01): Descriptor states>500,000 spectra and>40,000 materials; Figshare collection3946561 links this public xas.json.tgz archive.
- [Materials Project K-edge XANES release — primary deposit](https://doi.org/10.6084/m9.figshare.5678998.v1) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Count is a lower bound of spectra, not crystal structures.
- Public API/site-averaged spectra differ from individual-site archive records.
- Parent structures overlap Materials Project; preserve MP IDs, edge, absorber site and FEFF settings.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="simpod-powder-xrd"></a>
## SIMPOD simulated powder X-ray diffraction benchmark

Computed powder diffractograms and radial images linked to atomic crystal information.

**Size:** 467,861 COD structure/diffractogram pairs (source wording: 467,861).

**Scope:** COD-derived snapshot up to mid2023; one JSON and radial PNG per input structure

**Release:** Science Data BankV4;2025 paper cohort. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** powder XRD intensity versus2θ; radial diffraction PNG; atomic positions, occupancies and cell parameters; space group.

**Access:** open. **Dataset license:** CC0 1.0 (Science Data Bank depositor metadata).

**Official routes:** [publication](https://doi.org/10.1038/s41597-025-05534-3) · [data](https://doi.org/10.57760/sciencedb.09755)

**Evidence:**

- [SIMPOD simulated powder X-ray diffraction benchmark — Scientific Data descriptor](https://doi.org/10.1038/s41597-025-05534-3) (checked 2026-11-01): Publisher and deposit metadata agree on467,861 structures. Dataset registered asV4; JSON includes atoms, coordinates, occupancies, unit cells, space group and patterns.
- [SIMPOD simulated powder X-ray diffraction benchmark — primary deposit](https://doi.org/10.57760/sciencedb.09755) (checked 2026-11-01): Science Data Bank landing page and depositor-supplied DOI metadata identify V4, 467,861 structure/pattern pairs, atom/cell fields and CC0 1.0 rights.

**Reuse and interpretation notes:**

- Derived from COD;467,861 is not an independently measured or newly discovered crystal count.
- Simulated2θ5–90°,10,824 points,Cu wavelength 1.5406 Å, fixed0.01° width; no experimental background.
- Original author/publication metadata are omitted from simplified records; preserve COD IDs and recover parent provenance when needed.
- Distinct from existing opXRD, which contains experimental diffractograms.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mp-ledge-xanes-2021"></a>
## Materials Project L-edge XANES release

FEFF9 L-edge spectra linked to MP structures and absorber sites.

**Size:** ~140,000 site-wise L2 or L3 XANES spectra (source wording: 140,000).

**Scope:** Approximately140,000 site-wise spectra; not40,000 unique crystals

**Release:** 2021 paper cohort; deposit checked 2026-11-01. **Year:** 2021.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** L2/L3 XANES absorption; site-wise and site-averaged spectra; absorber and structural metadata.

**Access:** open. **Dataset license:** MIT (Figshare L-XAS archive).

**Official routes:** [publication](https://doi.org/10.1038/s41597-021-00936-5) · [data](https://doi.org/10.6084/m9.figshare.12824513.v1)

Other denominators (not added to the ranking):

- 22,000 structures (lower bound): Abstract reports more than22,000 structures

**Evidence:**

- [Materials Project L-edge XANES release — Scientific Data descriptor](https://doi.org/10.1038/s41597-021-00936-5) (checked 2026-11-01): Data Records describe approximately 140,000 site-wise L2/L3 spectra and 40,000 site-averaged elemental/structure counts; abstract says>22,000 structures.
- [Materials Project L-edge XANES release — primary deposit](https://doi.org/10.6084/m9.figshare.12824513.v1) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Each site-wise count is one edge at one absorbing site; site-averaged count is a completed structure/element L2,3 pair.
- Do not equate40,000 site-averaged counts with 40,000 unique material identities.
- Distinct property cohort from K-edge; underlying MP structure identities overlap.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="ins-crystals-10023"></a>
## Synthetic inelastic-neutron spectra — inorganic crystal subset

Simulated neutron S(Q,E), VISION/TOSCA spectra and phonon densities for PhononDB-derived crystal models.

**Size:** 10,023 inorganic crystal models with simulated INS (source wording: 10,023).

**Scope:** Inorganic subset of joint molecule/crystal deposit; molecular subset excluded

**Release:** Zenodo 1.0.1; 2023 descriptor inorganic subset. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** powder S(Q,E); INS spectra (cm⁻¹); phonon DOS and neutron-weighted DOS; structure CIF and Γ-point mode visualizations.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo 1.0.1).

**Official routes:** [publication](https://doi.org/10.1038/s41597-022-01926-x) · [data](https://doi.org/10.5281/zenodo.7438040)

**Evidence:**

- [Synthetic INS descriptor](https://www.nature.com/articles/s41597-022-01926-x) (checked 2026-11-01): Methods report 10,023 inorganic crystals after excluding nine Xe-containing cases from 10,032 PhononDB inputs. Models include CIF and simulated spectra.
- [Synthetic INS Zenodo 1.0.1](https://zenodo.org/records/7438040) (checked 2026-11-01): Open CC BY 4.0 deposit separates crystals.tar.gz and molecules.tar.gz; crystal/molecule indices are downloadable without full archives.

**Reuse and interpretation notes:**

- Structures/phonons derive from PhononDB, while INS spectra are new computed properties; do not add as novel crystals.
- The separate 21,693 gas-phase molecule cohort is outside this record.
- Crystal S(Q,E) uses 0–150 meV and 0–15 Å⁻¹ grids with generic instrument resolution; published files indicate 0 K.
- Γ-point mode visualizations are not the full-Brillouin-zone phonons used to compute spectra.

**Tags:** Scientific Data, characterization, computed, parent-database-derived, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="raman-oulu-5099"></a>
## Oulu computational Raman database

Raman tensors and vibrational data for a broad crystal cohort using PhononDB and Materials Project inputs.

**Size:** 5,099 materials with calculated Raman properties (source wording: 5,099).

**Scope:** Final calculated cohort, distinct from 8,382 flagged inputs

**Release:** 2023 paper cohort; deposit checked 2026-11-01. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** Raman tensors; Raman/IR mode activity; frequencies and eigenvectors; Born charges; dielectric properties.

**Access:** open. **Dataset license:** CC BY 4.0 (Materials Cloud deposit).

**Official routes:** [publication](https://doi.org/10.1038/s41597-023-01988-5) · [data](https://doi.org/10.24435/materialscloud:ze-58)

**Evidence:**

- [Oulu computational Raman database — Scientific Data descriptor](https://doi.org/10.1038/s41597-023-01988-5) (checked 2026-11-01): Paper reports 5,099 completed materials. Deposited JSON includes structures, symmetry, Raman tensors and source-database links.
- [Oulu computational Raman database — primary deposit](https://doi.org/10.24435/materialscloud:ze-58) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Input identities and imported phonon data overlap PhononDB/MP; this is a Raman-property release, not5,099 new crystal identities.
- Nonresonant Raman approximation; spectra shown at 300 K with normalization and mode broadening.
- Flagged-input, vibrational-mode and completed-material counts differ.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="qps-morphology-images"></a>
## Quaternary-phosphonium-salt image-to-molecule morphology benchmark

Molecular identity, acquisition metadata and multiscale salt-crystallization morphology images.

**Size:** 4,037 SEM and optical images (source wording: 4,037).

**Scope:** 3,649 SEM +388 optical images; includes foil controls

**Release:** 2026 paper cohort; deposit checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** SEM/optical morphology; compound/mixture identities; magnification, voltage and detector metadata.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare v2).

**Official routes:** [publication](https://doi.org/10.1038/s41597-026-06941-w) · [data](https://doi.org/10.6084/m9.figshare.31281778.v2)

**Count derivation:** Sum of SEM and optical image cohorts in Data Records; 3,649 + 388 = 4,037.

**Evidence:**

- [Quaternary-phosphonium-salt image-to-molecule morphology benchmark — Scientific Data descriptor](https://doi.org/10.1038/s41597-026-06941-w) (checked 2026-11-01): Paper reports 3,649 SEM and 388 optical images of 19 salts and binary mixtures; SEM collection also includes aluminum-foil controls.
- [Quaternary-phosphonium-salt image-to-molecule morphology benchmark — primary deposit](https://doi.org/10.6084/m9.figshare.31281778.v2) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Crystalline and amorphous solids are mixed; material-state filter is needed.
- Images are not resolved molecular-crystal atomic structures.
- Multiple magnifications and controls are not independent compounds.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="raman-2d-3504"></a>
## Two-dimensional materials ab initio Raman spectra

Harmonic Raman spectra and geometries computed from 2DMatPedia monolayer structures.

**Size:** 3,504 two-dimensional materials (source wording: 3,504).

**Scope:** Completed 2D Raman calculation cohort

**Release:** 2025 paper cohort; deposit checked 2026-11-01. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** Raman mode frequencies; Raman intensities; relaxed monolayer geometry.

**Access:** open. **Dataset license:** CC BY 4.0 (Materials Cloud deposit).

**Official routes:** [publication](https://doi.org/10.1038/s41597-025-04593-w) · [data](https://doi.org/10.24435/materialscloud:9g-1r)

**Evidence:**

- [Two-dimensional materials ab initio Raman spectra — Scientific Data descriptor](https://doi.org/10.1038/s41597-025-04593-w) (checked 2026-11-01): Publisher and primary deposit report 3,504 materials and provide geometry/frequency/intensity data.zip.
- [Two-dimensional materials ab initio Raman spectra — primary deposit](https://doi.org/10.24435/materialscloud:9g-1r) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Structures originate in 2DMatPedia; do not count as an independent set of novel structures.
- Harmonic, first-order Raman calculations omit substrate, excitonic and anharmonic effects.
- Paper cites deposit incompletely; actual Materials Cloud DOI resolved and title/count matched.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="lps-sulfur-kedge-xas"></a>
## Lithium-thiophosphate sulfur K-edge XAS

First-principles S-edge spectra with polarization components and atomic models for solid-electrolyte characterization.

**Size:** 2,681 site-resolved sulfur K-edge spectra (source wording: 2,681).

**Scope:** Spectra for 66 structure models:18 crystalline and 48 amorphous

**Release:** 2023 paper cohort; deposit checked 2026-11-01. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** S K-edge absorption versus energy; three polarization components; atomic positions and computational inputs.

**Access:** open. **Dataset license:** CC BY 4.0 (Materials Cloud deposit).

**Official routes:** [publication](https://doi.org/10.1038/s41597-023-02262-4) · [data](https://doi.org/10.24435/materialscloud:6z-qm)

Other denominators (not added to the ranking):

- 66 structure models: 18 crystalline and48 amorphous models

**Evidence:**

- [Lithium-thiophosphate sulfur K-edge XAS — Scientific Data descriptor](https://doi.org/10.1038/s41597-023-02262-4) (checked 2026-11-01): Paper reports 2,681 spectra across 66 models; deposited input/output set includes POSCAR, INCAR, KPOINTS and spectral mu.dat.
- [Lithium-thiophosphate sulfur K-edge XAS — primary deposit](https://doi.org/10.24435/materialscloud:6z-qm) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Mixed crystalline and amorphous models; keep18/48 structure-state distinction.
- POTCAR pseudopotentials omitted due VASP licensing.
- Raw calculated energies/intensities require appropriate alignment/broadening for experimental comparison.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="aachen-heerlen-steel-sem"></a>
## Aachen-Heerlen annotated steel microstructures

Steel SEM images with expert martensite-austenite island annotations and heat-treatment metadata.

**Size:** 2,580 SEM images (source wording: 2,580).

**Scope:** Full released image cohort; 1,705 images carry polygon annotations

**Release:** 2021 paper cohort; deposit checked 2026-11-01. **Year:** 2021.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** SEM morphology; MA-island polygons; area, perimeter, aspect ratio and compactness; transformation temperature (400 or 500 °C).

**Access:** open. **Dataset license:** CC0 1.0 (verified image and polygon deposits).

**Official routes:** [publication](https://doi.org/10.1038/s41597-021-00926-7) · [data](https://doi.org/10.6084/m9.figshare.c.5185004)

Other denominators (not added to the ranking):

- 1,705 polygon-annotated images: Subset of full image cohort
- 8,909 expert polygons: MA-island annotations, paper reported

**Evidence:**

- [Aachen-Heerlen annotated steel microstructures — Scientific Data descriptor](https://doi.org/10.1038/s41597-021-00926-7) (checked 2026-11-01): Data Records identify 2,580 TIFF images and PNG equivalents, of which 1,705 are polygon-annotated. Abstract reports 8,909 expert polygons.
- [Aachen-Heerlen annotated steel microstructures — primary deposit](https://doi.org/10.6084/m9.figshare.c.5185004) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- TIFF and PNG are representations of the same images; do not count both.
- Specific chemical compositions are withheld; only composition-type labels are supplied.
- Microstructure images and phase morphology do not provide atomic coordinates.
- Image conditions include4,000× magnification and 15 kV SEM operation.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="pd-carbon-sem-ordering"></a>
## Pd-on-carbon SEM ordering benchmark

Palladium nanoparticle spatial organization on carbon supports across several magnifications.

**Size:** 1,000 SEM images (source wording: 1,000).

**Scope:** 750 predominantly ordered plus250 predominantly disordered images

**Release:** 2020 paper cohort; deposit checked 2026-11-01. **Year:** 2020.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** SEM images; ordered/disordered labels; sample and area identifiers; acceleration voltage (V), working distance (µm), emission current (nA).

**Access:** open. **Dataset license:** CC BY 4.0 (both Figshare datasets).

**Official routes:** [publication](https://doi.org/10.1038/s41597-020-0439-1) · [data](https://doi.org/10.6084/m9.figshare.11783661)

Other denominators (not added to the ranking):

- 750 ordered images: Dataset1
- 250 disordered images: Dataset2;https://doi.org/10.6084/m9.figshare.11783667

**Evidence:**

- [Pd-on-carbon SEM ordering benchmark — Scientific Data descriptor](https://doi.org/10.1038/s41597-020-0439-1) (checked 2026-11-01): Data Records provide750 ordered and 250 disordered1,280×1,024-pixel TIFFs with instrument metadata; companion disordered deposit is11783667.
- [Pd-on-carbon SEM ordering benchmark — primary deposit](https://doi.org/10.6084/m9.figshare.11783661) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Multiple magnifications can show the same area; preserve area identifiers to prevent train/test leakage.
- Nanoparticle and support morphology is not a collection of resolved periodic crystal structures.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="jarvis-stm"></a>
## JARVIS-STM computational scanning-tunneling microscopy

DFT/Tersoff–Hamann constant-height STM images with raw electronic-density calculation outputs.

**Size:** 716 exfoliable two-dimensional materials (source wording: 716).

**Scope:** 716-material paper cohort; multiple biases/images per material

**Release:** 2021 descriptor cohort; repository checked 2026-11-01. **Year:** 2021.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** positive/negative-bias STM images; constant-height/current visualization; PARCHG and calculation input/output data; 2D Bravais-lattice labels.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare data items).

**Official routes:** [publication](https://doi.org/10.1038/s41597-021-00824-y) · [data](https://doi.org/10.6084/m9.figshare.11924070.v4) · [homepage](https://jarvis.nist.gov/jarvisstm) · [collection](https://doi.org/10.6084/m9.figshare.c.3883270)

**Evidence:**

- [Computational STM descriptor](https://www.nature.com/articles/s41597-021-00824-y) (checked 2026-11-01): Publisher reports 716 exfoliable 2D materials, positive/negative bias constant-height JPEG images and input/output data; JARVIS-STM app offers height/current variation.
- [JARVIS-STM Figshare v4 metadata](https://api.figshare.com/v2/articles/11924070) (checked 2026-11-01): Public STM database archive is version 4 under CC BY 4.0; related raw negative-bias archive item also declares CC BY 4.0.

**Reuse and interpretation notes:**

- Parent structures overlap JARVIS-DFT 2D; image/property release is independently useful but not a new material-identity universe.
- Only defect-free surfaces considered in paper cohort.
- Image appearance depends on bias, height/current and simulation approximation; preserve these conditions.
- Existing local JARVIS source inventory mentioned STM, but canonical catalog had no STM record at audit time.
- JARVIS-Tools documentation lists 1,132 for STM, an unreconciled later snapshot. The ranking retains the explicit 716-material 2021 descriptor cohort; the current archive population was not independently recounted.

**Tags:** Scientific Data, characterization, computed, parent-database-derived, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="amalgamatch-microscopy"></a>
## AmalgaMatch correlative materials microscopy benchmark

Cross-modal microscopy pairs with hand-annotated correspondences and structured image metadata.

**Size:** 187 annotated image pairs (source wording: 187).

**Scope:** 6 groups,19 material subsets and 35 scenes

**Release:** Fordatis1.0.0; Scientific Data accepted publication2026-08-14. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** optical/SEM/TEM/EBSD images; correspondence keypoints; acquisition and matching-task metadata.

**Access:** open. **Dataset license:** CC BY 4.0 (Fordatis repository license link).

**Official routes:** [publication](https://doi.org/10.1038/s41597-026-07961-2) · [data](https://doi.org/10.24406/fordatis/436)

Other denominators (not added to the ranking):

- 35 scenes: Correlative imaging scenes
- 19 material subsets: Grouped by imaged material

**Evidence:**

- [AmalgaMatch correlative materials microscopy benchmark — Scientific Data descriptor](https://doi.org/10.1038/s41597-026-07961-2) (checked 2026-11-01): Accepted descriptor and Fordatis v1.0.0 report 187 image pairs,35 scenes,19 subsets and 6 use-case groups; repository supplies4.13GB ZIP.
- [AmalgaMatch correlative materials microscopy benchmark — primary deposit](https://doi.org/10.24406/fordatis/436) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Image pairs and scenes are not independent material identities.
- Some image subsets derive from earlier shared studies; retain subset lineage.
- Microscopy supports microstructure characterization, not a complete atomic-coordinate catalog.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="hybrid-raman-crystal-2024"></a>
## Hybrid-functional inorganic-crystal Raman database

Hybrid-functional Raman/IR spectra and vibrational tensors calculated from ICSD-derived structures.

**Size:** 161 inorganic compounds (source wording: 161).

**Scope:** Paper-release cohort; live database can grow

**Release:** Paper 161-compound cohort; Zenodo1.1(2023-12-12). **Year:** 2024.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** Raman/IR frequencies (cm⁻¹); Raman intensities and tensors; Born charges; phonon properties.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo and primary code/data release).

**Official routes:** [publication](https://doi.org/10.1038/s41597-024-02924-x) · [data](https://doi.org/10.5281/zenodo.10360193)

**Evidence:**

- [Hybrid-functional inorganic-crystal Raman database — Scientific Data descriptor](https://doi.org/10.1038/s41597-024-02924-x) (checked 2026-11-01): Descriptor reports 161 compounds; data/code archive resolves to version 1.1, DOI 10360193. Web app supports CSV mode frequencies/intensities and structure visualization.
- [Hybrid-functional inorganic-crystal Raman database — primary deposit](https://doi.org/10.5281/zenodo.10360193) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- ICSD source identifiers and coordinate licensing must be retained; adding calculated properties does not create new independent experimental structures.
- Spectra depend on functional and convolution; plotted examples normalize maximum intensity to 1,000 arbitrary units.
- Archive has code/data; full per-file coordinate redistribution rights were not independently audited.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="usgs-rockjock-xrd-2021"></a>
## USGS updated geologic-materials XRD reference library

Measured powder diffractograms with reference intensity ratios, mineral-source metadata and paired corundum-spiked measurements.

**Size:** 156 pure-material reference diffractograms (source wording: 156).

**Scope:** Counted156 named intensity columns in RJ_ComparisonMaterials_purePatterns.csv and156 rows in values table; companion spike patterns are not additional phase identities.

**Release:** 2021 USGS release DOI10.5066/P9ID8IX1; metadata updated2021-12-09. **Year:** 2021.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** powder XRD intensity versus2theta; reference intensity ratio relative to corundum; integrated intensity; mineral specimen source; preparation comparison.

**Access:** open. **Dataset license:** CC0 1.0 Universal (USGS release rights).

**Official routes:** [homepage](https://www.usgs.gov/data/updated-x-ray-diffractogram-library-geologic-materials) · [data](https://doi.org/10.5066/P9ID8IX1)

Other denominators (not added to the ranking):

- 3,001 two-theta points per pure pattern: Actual CSV rows from5.00 to65.00 degrees

**Evidence:**

- [ScienceBase primary release metadata](https://www.sciencebase.gov/catalog/item/5fbc5aa6d34eb413d5e26d42?format=json) (checked 2026-11-01): Lists downloadable pure/spiked CSV patterns, RIR/source values, preparation-comparison data and FGDC XML; actual pure-pattern CSV has156 phase columns and3001 angle rows.
- [USGS FGDC methods and attribute metadata](https://www.sciencebase.gov/catalog/item/5fbc5aa6d34eb413d5e26d42) (checked 2026-11-01): Cu Kalpha patterns span5–65 degrees2theta at0.02degree spacing and at least5s/step. Instrument aligned with NIST-traceable quartz; corundum spikes define RIRs; trace impurity subtraction is documented.
- [USGS release rights](https://www.usgs.gov/data/updated-x-ray-diffractogram-library-geologic-materials) (checked 2026-11-01): Provider explicitly marks the data release CC0 1.0 Universal.

**Reuse and interpretation notes:**

- A single specimen/preparation represents each phase label; solid solution and crystallinity change peak positions/intensities.
- Measured reference patterns include documented trace-impurity subtraction and are not untouched detector output.
- Original RockJock2003 had169 patterns; the inspected2021 pure-pattern file contains156. Do not use169 as this release count.
- Mineral/source identities do not include solved atomic coordinates; repeated forms and natural/synthetic variants are separate references.

**Tags:** Data.gov-selection-20261101, verified-2026-11-01, specialist-experimental-data.

<a id="dl-add-tmd-stm-defects"></a>
## DL-ADD MoS2/WS2 atomic-defect STM benchmark

Experimental STM surface images and impurity/void annotations for defect segmentation in two transition-metal dichalcogenides.

**Size:** 105 original STM benchmark images (source wording: 105).

**Scope:** Published evaluation cohort:70 MoS2 training +20 MoS2 test +15 WS2 transfer-test images; augmented variants excluded

**Release:** 2023 descriptor cohort; deposit checked 2026-11-01. **Year:** 2023.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** STM topographic images; impurity/void segmentation labels; pixel defect locations; sample bias and tunneling-current conditions.

**Access:** open. **Dataset license:** CC BY 4.0 (OSF project license).

**Official routes:** [publication](https://doi.org/10.1038/s41597-023-02004-6) · [data](https://doi.org/10.17605/OSF.IO/ZXGTJ)

Other denominators (not added to the ranking):

- 90 MoS2 original images: 70 training +20 held-out test images
- 15 WS2 original images: Transfer-test cohort

**Count derivation:** Sum of published independent image cohorts; augmentation excluded; 70 + 20 + 15 = 105.

**Evidence:**

- [Deep learning based atomic defect detection framework for two-dimensional materials](https://www.nature.com/articles/s41597-023-02004-6) (checked 2026-11-01): Technical Validation reports 90 MoS2 images split 70/20 and15 WS2 transfer-test images. Images use50×50 or60×60 nm fields,256×256 px, constant-current−1 V sample bias and1 nA.
- [OSF DL-ADD primary project metadata](https://api.osf.io/v2/nodes/zxgtj/) (checked 2026-11-01): Public project titled TMD-FET defect autodetection at STM images has MoS2/WS2 data folders and a project-license relationship.
- [OSF dataset-associated license](https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96a/) (checked 2026-11-01): Associated project license is CC-By Attribution 4.0 International.

**Reuse and interpretation notes:**

- 105 counts original paper benchmark images, not all repository files, masks or augmented training examples.
- Training augmentation pastes defect crops onto backgrounds and applies image transforms; generated variants are not independent measurements.
- Image labels represent defect appearance, not fully resolved atomic coordinates or definitive impurity chemical identities.
- Underlying materials are MoS2 and WS2;105 images are not105 unique crystal structures.

**Tags:** Scientific Data, final-title-audit, characterization, condition-dependent, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="microlib-slicegan"></a>
## MicroLib SliceGAN microstructure library

Synthetic 3D microstructural volumes, trained models and metadata derived from 2D microscopy.

**Size:** 87 source microstructure entries (source wording: 87).

**Scope:** 87 DoITPoMS entries used to generate 3D microstructure volumes

**Release:** 2022 paper cohort; deposit checked 2026-11-01. **Year:** 2022.

**Provenance:** generated. **Structure availability:** `composition_only`.

**Labels/content:** generated 3D phase morphology; phase fractions and geometric validation metrics; 2D training micrographs.

**Access:** open. **Dataset license:** Not verified; Zenodo declares open access but no dataset license in retrieved metadata.

**Official routes:** [publication](https://doi.org/10.1038/s41597-022-01744-1) · [data](https://doi.org/10.5281/zenodo.7118559)

Other denominators (not added to the ranking):

- 32,768,000 voxels per illustrated volume: 320×320×320 example volume size; not material count

**Evidence:**

- [MicroLib SliceGAN microstructure library — Scientific Data descriptor](https://doi.org/10.1038/s41597-022-01744-1) (checked 2026-11-01): Paper and deposit describe 87 source entries; example generated volumes contain320³ voxels and release includes trained SliceGAN models.
- [MicroLib SliceGAN microstructure library — primary deposit](https://doi.org/10.5281/zenodo.7118559) (checked 2026-11-01): Zenodo API confirms 87 source microstructures, open access and ZIP file; no license field was present.

**Reuse and interpretation notes:**

- Generated microstructures are model outputs, not measured 3D volumes.
- Collection includes biological and noncrystalline materials; filter by material descriptors for crystal/alloy use.
- Voxels represent microstructural phases rather than periodic atomic coordinates.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mp-raman-2019"></a>
## Materials Project Raman tensor and RRUFF matching benchmark

Computed Raman tensors and spectra, paired with structure-matched RRUFF reference peaks.

**Size:** 55 computed inorganic compounds (source wording: 55).

**Scope:** 55-compound DFPT cohort with a separate experimental matching table

**Release:** 2019 paper cohort; deposit checked 2026-11-01. **Year:** 2019.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** Raman frequencies (cm⁻¹); Raman tensors and normalized intensities; normal modes; RRUFF-to-MP matched peak data.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare v2; source rights still apply).

**Official routes:** [publication](https://doi.org/10.1038/s41597-019-0138-y) · [data](https://doi.org/10.6084/m9.figshare.7427393.v2)

Other denominators (not added to the ranking):

- 205 matched peak/mode pairs: Technical-validation benchmark across55 compounds

**Evidence:**

- [Materials Project Raman tensor and RRUFF matching benchmark — Scientific Data descriptor](https://doi.org/10.1038/s41597-019-0138-y) (checked 2026-11-01): Paper reports 55 compounds and 205 matched peak/mode pairs; deposit contains computational/experimental JSON plus MP and RRUFF CIF archives.
- [Materials Project Raman tensor and RRUFF matching benchmark — primary deposit](https://doi.org/10.6084/m9.figshare.7427393.v2) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Computed data and RRUFF-derived measurements are separate evidence layers.
- RRUFF tables duplicate parent measurements; do not add them as new experiments.
- Reported spectra use 300 K and 532 nm excitation; intensities normalized to 100.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="battery-interphase-ir-raman-xrd"></a>
## Battery-interphase IR/Raman/XRD reference library

Experimental reference spectroscopy and diffraction collected with inert-atmosphere sample chambers.

**Size:** 10 reference compounds (source wording: 10).

**Scope:** Ten interphase-relevant compounds, with raw and processed spectral data

**Release:** 2024 paper cohort; deposit checked 2026-11-01. **Year:** 2024.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** ATR-FTIR spectra; Raman spectra; X-ray diffraction and d-spacings.

**Access:** open. **Dataset license:** CC0 1.0 (Dryad dataset).

**Official routes:** [publication](https://doi.org/10.1038/s41597-024-04236-6) · [data](https://doi.org/10.5061/dryad.v15dv421w)

**Evidence:**

- [Battery-interphase IR/Raman/XRD reference library — Scientific Data descriptor](https://doi.org/10.1038/s41597-024-04236-6) (checked 2026-11-01): Descriptor covers10 compounds; Dryad contains technique-specific XLSX workbooks with raw/final data; XRD wavelength 1.54 Å.
- [Battery-interphase IR/Raman/XRD reference library — primary deposit](https://doi.org/10.5061/dryad.v15dv421w) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- References represent isolated compounds, not measured heterogeneous working battery interphases.
- Processed Raman data for 6LiF and 7LiF are omitted, and raw/final Raman axes differ after interpolation/filtering.
- Spectral data are not a deposit of resolved periodic coordinates.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="nist-mgo-apt-spectra"></a>
## NIST MgO ultraviolet atom-probe mass spectra

Binned MgO atom-probe spectra comparing extreme- and near-ultraviolet pulsing, with uncorrected, corrected and estimated-background counts.

**Size:** 10 mass-spectrum condition files (source wording: 10).

**Scope:** Ten distinct CSV files linked by current release metadata; each has40000 mass-bin rows and four columns. Not a count of unique materials or independent specimens.

**Release:** NIST mds2-4005 v1.0.0; README2025, repository issued2026-01-16. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** mass-to-charge-state ratio(Da); uncorrected counts; corrected counts; background estimate(counts); pulse-source and acquisition-condition filename labels.

**Access:** open. **Dataset license:** NIST data-use terms explicitly linked by release metadata; not a Creative Commons license.

**Official routes:** [homepage](https://data.nist.gov/od/id/mds2-4005) · [data](https://doi.org/10.18434/mds2-4005)

Other denominators (not added to the ranking):

- 40,000 mass bins per spectrum: Inspected CSV, including0Da row

**Evidence:**

- [NIST primary release and checksums](https://data.nist.gov/od/id/mds2-4005) (checked 2026-11-01): Provides ten downloadable spectra and checksums. Downloaded CSVs each have40000 rows, four headers and a0–399.99Da grid with0.01Da spacing; README documents count columns and binning.
- [MgO spectra README](https://data.nist.gov/od/ds/ark:/88434/mds2-4005/4005_README.txt) (checked 2026-11-01): Names EUV/NUV CSVs and units; openly links NIST data-use terms. Filenames preserve energy/source/detection-rate/repetition-rate condition labels.

**Reuse and interpretation notes:**

- One material(MgO); useful for mass-spectrometry processing and source-condition comparisons, not broad composition–property learning.
- Negative corrected counts are present; preserve them and distinguish count correction/background modeling from raw counts.
- README lists EUV_5T_1DR twice; current release actually has10 distinct spectra.
- README says0.01–399.99Da, but each inspected payload includes a0Da row.
- Detailed specimen histories, per-bin statistical uncertainties and calibration/ranging procedures are not supplied in the short README; filename codes need paper-level context for full interpretation.

**Tags:** Data.gov-selection-20261101, verified-2026-11-01, specialist-experimental-data.

<a id="stem-nanomaterial-tomography-2016"></a>
## Nanomaterial STEM tomography reference collection

Experimental tomography for Co2P, supported Pt, atomic-resolution Pt/W and through-focal PtCu.

**Size:** 5 tomographic material systems (source wording: 5).

**Scope:** Five raw tilt-series/reconstruction benchmark cases

**Release:** 2016 paper cohort; deposit checked 2026-11-01. **Year:** 2016.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** STEM tilt-series intensities; 3D reconstructed volumes; tilt geometry and acquisition metadata.

**Access:** open. **Dataset license:** CC0 1.0 verified for sampled collection items; check per item for reuse.

**Official routes:** [publication](https://doi.org/10.1038/sdata.2016.41) · [data](https://doi.org/10.6084/m9.figshare.c.2185342)

**Evidence:**

- [Nanomaterial STEM tomography reference collection — Scientific Data descriptor](https://doi.org/10.1038/sdata.2016.41) (checked 2026-11-01): Descriptor defines five Tom_1–Tom_5 cases and 16-bit TIFF tilt-series/reconstructions; example Pt/W cases reach atomic resolution.
- [Nanomaterial STEM tomography reference collection — primary deposit](https://doi.org/10.6084/m9.figshare.c.2185342) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Tomography intensity volumes are not standardized periodic atomic structures.
- Tilt range, missing wedge, dose and alignment differ between cases.
- Several collection files derive from the same specimen; count five cases rather than files.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="zeolite13x-multimodal-tomography"></a>
## Zn-doped zeolite13X multimodal synchrotron benchmark

Co-registered XCT, spatial XRD-CT and powder XRD for multimodal data-fusion development.

**Size:** 1 bespoke two-phase sample (source wording: 1).

**Scope:** One partially Zn-doped13X sample studied at multiple resolutions/modalities

**Release:** 2025 paper cohort; deposit checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** multiresolution XCT; Na/Zn phase-resolved XRD-CT; powder diffraction; raw/reconstructed volumes.

**Access:** open. **Dataset license:** CC BY 4.0 verified for XRD-CT deposit; check linked deposits individually.

**Official routes:** [publication](https://doi.org/10.1038/s41597-025-04605-9) · [data](https://doi.org/10.5281/zenodo.13329639)

**Evidence:**

- [Zn-doped zeolite13X multimodal synchrotron benchmark — Scientific Data descriptor](https://doi.org/10.1038/s41597-025-04605-9) (checked 2026-11-01): Paper documents bespoke two-phase sample, four XCT resolutions and XRD-CT 25/50 µm spot sizes; multiple raw/processed Zenodo releases are linked.
- [Zn-doped zeolite13X multimodal synchrotron benchmark — primary deposit](https://doi.org/10.5281/zenodo.13329639) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Different imaging resolutions and reconstructions are not independent materials.
- XCT voxel sizes0.325–2.6 µm and XRD-CT spatial resolutions differ markedly.
- Full dataset spans several deposits; this row cites the core XRD-CT deposit and paper inventory.
- No periodic-coordinate release established.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="braggnn-hedm-datasets"></a>
## BraggNN high-energy diffraction microscopy training/validation data

Experimental diffraction frames and fitted peak locations for BraggNN localization benchmarks.

**Size:** Unranked diffraction frame/Bragg-peak records (source wording: Not reported).

**Scope:** Independent record count not established from available primary metadata

**Release:** 2022 paper cohort; deposit checked 2026-11-01. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** area-detector diffraction frames; Bragg peak row/column locations (pixels); frame identifiers.

**Access:** open. **Dataset license:** Not verified; no dataset license in retrieved MDF/DataCite metadata.

**Official routes:** [publication](https://doi.org/10.1038/s41597-022-01712-9) · [data](https://doi.org/10.18126/iftp-twz1) · [validation_data](https://doi.org/10.18126/hvny-s7ax)

**Evidence:**

- [BraggNN high-energy diffraction microscopy training/validation data — Scientific Data descriptor](https://doi.org/10.1038/s41597-022-01712-9) (checked 2026-11-01): Scientific Data releases separate training DOIiftp-twz1 and validation DOIhvny-s7ax in HDF5. Depositor metadata documents frames and fitted peak-row/column arrays.
- [BraggNN high-energy diffraction microscopy training/validation data — primary deposit](https://doi.org/10.18126/iftp-twz1) (checked 2026-11-01): MDF depositor DOI metadata describes HDF5 frame and peak arrays; current bulk download and license remain unverified.

**Reuse and interpretation notes:**

- Peak labels were obtained with conventional pseudo-Voigt fitting and are not independent ground-truth lattice coordinates.
- Training and validation releases should remain linked as one benchmark family.
- Public metadata verified; current bulk file access was not exercised.
- Globus group authorization mentioned for GPU model serving is separate from dataset rights.

**Tags:** Scientific Data, characterization, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="arpes-graphene-bp-2016"></a>
## Graphene/black-phosphorus ARPES simulation and HOPG reference data

Finite-cluster ARPES simulations, Gaussian geometries and direct experimental highly oriented pyrolytic graphite photoemission data.

**Size:** Unranked simulation/spectral records (source wording: Simulation and experimental spectral record count not verified).

**Scope:** Finite PAH/black-phosphorus simulation sets and experimental HOPG ARPES spectra; deposit packages are not treated as material counts.

**Release:** Dryad publication release, 2016. **Year:** 2016.

**Provenance:** mixed. **Structure availability:** `mixed`.

**Labels/content:** ARPES intensity; occupied energy levels; molecular Cartesian coordinates; photon/analyzer geometry; experimental HOPG spectra.

**Access:** open. **Dataset license:** CC0 1.0 (Dryad data metadata).

**Official routes:** [paper](https://doi.org/10.1038/sdata.2016.31) · [data](https://doi.org/10.5061/dryad.j2641)

**Evidence:**

- [Primary ARPES data descriptor](https://doi.org/10.1038/sdata.2016.31) (checked 2026-11-01): Data Record explicitly includes generated Gaussian/IAC simulation data and experimental HOPG ARPES tables; simulated PAHs span 24–864 carbon atoms, with 11 subfiles per molecular simulation set.
- [Dryad release and rights](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.j2641) (checked 2026-11-01): Dataset metadata identifies CC0 1.0. File inventory includes Dataset.zip, experimental ARPES data.zip, PES_program.zip and a program README; file count is not used as a material counter.

**Reuse and interpretation notes:**

- Simulation structures are finite molecules/clusters representing graphene/BP nanostructures, not periodic 2D crystal coordinates.
- Direct experimental bulk HOPG spectra make this a mixed materials-spectroscopy resource; filter out finite-model data for strictly periodic benchmarks.
- Simulated occupied energies are scaled/shifted against experiment or HOMO/LUMO midpoint; they are not unadjusted periodic DFT band structures.
- Payload size/metadata verified; simulation and measured-spectrum counts were not independently enumerated.

**Tags:** Scientific Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101, ARPES, experimental-reference, finite-cluster-models.

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
