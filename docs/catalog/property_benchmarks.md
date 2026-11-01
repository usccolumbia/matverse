# Computed properties and prediction benchmarks

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="wbm-matbench-discovery"></a>
## WBM / Matbench Discovery stability test set

Element-substitution candidates with initial structures, DFT-relaxed structures and energies for discovery-style stability evaluation.

**Size:** 256,963 structure entries (source wording: 256,963 filtered WBM ComputedStructureEntries; 215,488 after unique-prototype filtering).

**Scope:** Full cleaned WBM test set; original unfiltered WBM has 257,487 entries; unique-prototype subset has 215,488

**Release:** Matbench Discovery filtered WBM release. **Year:** 2021.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** formation energy; energy above convex hull; DFT energy; band gap; relaxed structure.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://matbench-discovery.materialsproject.org/) · [data](https://figshare.com/articles/dataset/22715158) · [paper](https://doi.org/10.1038/s41524-020-00481-6) · [code](https://github.com/janosh/matbench-discovery)

**Evidence:**

- [WBM benchmark test-set documentation](https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/wbm/readme.md) (checked 2026-11-01): 257,487 original entries become 256,963 after suspicious-data filtering; unique-prototype subset has 215,488.
- [Matbench Discovery data-file release metadata](https://api.figshare.com/v2/articles/22715158) (checked 2026-11-01): Current Figshare data-file release metadata specifies CC BY 4.0.

**Reuse and interpretation notes:**

- Generated substitutions followed by DFT relaxation; not experimentally discovered compounds.
- Full and unique-prototype subsets are overlapping alternatives, not additive.
- Stability depends on the DFT reference hull and energy corrections.

**Tags:** benchmark, stability, WBM, Materials Project derivative.

<a id="matbench-mp-e-form"></a>
## Matbench mp_e_form

Fixed Matbench v0.1 structure-to-property prediction task dataset.

**Size:** 132,752 task samples (source wording: 132,752 samples per task).

**Scope:** Matbench mp_e_form; fixed released task sample count

**Release:** Matbench v0.1. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** formation energy (eV/atom).

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://matbench.materialsproject.org/) · [data](https://github.com/materialsproject/matbench/tree/main/matbench) · [paper](https://doi.org/10.1038/s41524-020-00406-3) · [code](https://github.com/materialsproject/matbench)

**Evidence:**

- [Official Matbench v0.1 task metadata](https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json) (checked 2026-11-01): mp_e_form: 132,752 structure inputs; formation-energy target.
- [Official Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): MP snapshot retrieved 2019-04-02; excludes noble gases and formation energies above 2.5 eV.

**Reuse and interpretation notes:**

- MP snapshot retrieved 2019-04-02; excludes noble gases and formation energies above 2.5 eV.
- Task samples reuse parent datasets; do not sum Matbench tasks as unique crystals.
- Preserve the official order and folds for benchmark comparability.

**Tags:** Matbench, benchmark, structure-based, derived dataset.

<a id="matbench-mp-electronic"></a>
## Matbench mp_gap / mp_is_metal (shared source cohort)

Fixed Matbench v0.1 structure-to-property prediction task dataset.

**Size:** 106,113 task samples (source wording: 106,113 samples per task).

**Scope:** Matbench mp_gap / mp_is_metal (shared source cohort); fixed released task sample count

**Release:** Matbench v0.1. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE band gap; metallicity.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://matbench.materialsproject.org/) · [data](https://github.com/materialsproject/matbench/tree/main/matbench) · [paper](https://doi.org/10.1038/s41524-020-00406-3) · [code](https://github.com/materialsproject/matbench)

**Evidence:**

- [Official Matbench v0.1 task metadata](https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json) (checked 2026-11-01): mp_gap and mp_is_metal each contain 106,113 structure samples.
- [Official Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): These are two prediction tasks over the same MP-derived source cohort; the count is per task, not their sum.

**Reuse and interpretation notes:**

- These are two prediction tasks over the same MP-derived source cohort; the count is per task, not their sum.
- Task samples reuse parent datasets; do not sum Matbench tasks as unique crystals.
- Preserve the official order and folds for benchmark comparability.

**Tags:** Matbench, benchmark, structure-based, derived dataset.

<a id="tqc-topological-materials-2022"></a>
## Topological Quantum Chemistry all-band materials catalog

DFT and symmetry-based catalog of stable and fragile electronic band topology in nonmagnetic stoichiometric ICSD entries.

**Size:** 96,196 ICSD structure entries (source wording: 96,196 processable ICSD entries).

**Scope:** Historical 2022 all-band topological classification cohort; the count is processable ICSD entries, not unique formulas or exclusively topological materials

**Release:** Science 2022 / arXiv 2105.09954v2 publication cohort. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** electronic band structure; symmetry representations; stable topology; fragile topology; Fermi-level topology.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.topologicalquantumchemistry.com/) · [data](https://www.topologicalquantumchemistry.fr/) · [paper](https://doi.org/10.1126/science.abg9094)

**Evidence:**

- [All Topological Bands of All Nonmagnetic Stoichiometric Materials](https://arxiv.org/abs/2105.09954) (checked 2026-11-01): Authors report a publicly accessible all-band topology catalog for 96,196 processable ICSD entries; the abstract provides official portal and mirror links.
- [All Topological Bands, full author manuscript](https://arxiv.org/html/2105.09954v2) (checked 2026-11-01): Workflow filters ICSD entries for stoichiometry and valid atomic coordinates and calculates symmetry-indicated band topology by DFT.

**Reuse and interpretation notes:**

- This is an ICSD-derived property cohort and overlaps experimental crystal-structure databases.
- The 96,196 entries include both topological and trivial classifications; they are not 96,196 topological discoveries.
- Public classification access does not establish unrestricted redistribution rights to underlying ICSD coordinates.
- Primary portal timed out during this audit; scope and count are verified from the authors’ paper, and current portal availability is not confirmed.
- Nonmagnetic and stoichiometric scope omits disordered and magnetic materials.

**Tags:** topological materials, electronic structure, TQC, ICSD derivative, historical cohort, collection:sedaoturak.

<a id="lemat-rho"></a>
## LeMat-Rho

r2SCAN crystal structures with charge density grids and atom-resolved charge labels.

**Size:** 69,117 materials (source wording: 69,117).

**Scope:** Release described by the cited source

**Release:** 2026-10-19 card revision. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** charge density; Bader charge; energy; forces; stress.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/LeMaterial/LeMat-Rho)

**Evidence:**

- [LeMat-Rho — primary documentation](https://huggingface.co/datasets/LeMaterial/LeMat-Rho) (checked 2026-11-01): Card reports 69,117 materials, Bader charges for 59,613 and unsmoothed charge density for 65,960.

**Reuse and interpretation notes:**

- Label coverage differs by column; 69,117 does not imply complete Bader labels.
- Derived from structures with AFLOW, OQMD and MP identifiers.

**Tags:** None assigned.

<a id="mp-boltztrap-transport"></a>
## Materials Project / Ricci electronic transport database

BoltzTraP electronic transport from MP band structures with temperature/doping dependence under a constant-relaxation-time approximation.

**Size:** ~48,000 materials (source wording: approximately 48,000 inorganic materials).

**Scope:** Publication release

**Release:** Publication release. **Year:** 2017.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** Seebeck coefficient; electrical conductivity divided by relaxation time; electronic thermal conductivity divided by relaxation time; effective mass; carrier concentration.

**Access:** open. **Dataset license:** Creative Commons Zero v1.0 Universal (CC0-1.0).

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://doi.org/10.5061/dryad.gn001) · [paper](https://doi.org/10.1038/sdata.2017.85) · [code](https://github.com/materialsproject/pymatgen)

**Evidence:**

- [An ab initio electronic transport database for inorganic materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC5496472/) (checked 2026-11-01): Data Records reports about 48,000 inorganic crystals; GGA and GGA+U can coexist for the same compound; higher-level and detailed records form two representations.
- [Dryad electronic-transport dataset metadata](https://datadryad.org/dataset/doi:10.5061/dryad.gn001) (checked 2026-11-01): Dataset JSON-LD specifies Creative Commons Zero v1.0 Universal.

**Reuse and interpretation notes:**

- Two record-detail datasets and multiple functionals are not additional independent materials.
- Constant relaxation time; transport coefficients are often normalized by tau.
- Electronic thermal conductivity is not lattice thermal conductivity.
- The 8,924-entry matminer boltztrap_mp convenience dataset is only a derivative subset at 300 K and 10^18 cm^-3.

**Tags:** transport, thermoelectric, MP derivative, Scientific Data.

<a id="mp-phonon-2026"></a>
## Materials Project Phonon database v1.1

Versioned Materials Project phonon archive associated with the expanded phonon-calculation program.

**Size:** 26,413 materials (source wording: 26,413 compounds (archive title)).

**Scope:** v1.1, 2026-06-08

**Release:** v1.1, 2026-06-08. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** phonon calculations.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://doi.org/10.5281/zenodo.20196565)

**Evidence:**

- [Materials Project Phonon database v1.1 - (26,413 compounds)](https://zenodo.org/records/20196565) (checked 2026-11-01): Zenodo release title states 26,413 compounds; version v1.1, published 2026-06-08; metadata specifies open access and CC BY 4.0.

**Reuse and interpretation notes:**

- Count is the versioned archive’s compound count, not all displaced configurations or raw calculation files.
- The multi-terabyte payload was not downloaded; label completeness per compound was not audited.
- Shares parent MP materials with earlier phonon subsets; not additive.

**Tags:** phonon, MP derivative, 2026 release.

<a id="uci-superconductivity-2018"></a>
## UCI Superconductivity Data (Hamidieh 2018)

Composition-based superconducting critical-temperature regression benchmark derived from the original NIMS SuperCon database.

**Size:** 21,263 tabular material records (source wording: 21,263 tabular instances, 81 input features plus critical temperature).

**Scope:** Rows in the UCI regression release; train.csv and unique_m.csv are two representations of the same 21,263 samples

**Release:** 2018 UCI release; official metadata checked 2026-11-01. **Year:** 2018.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** superconducting critical temperature; chemical formula; composition-derived elemental descriptors.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International (CC BY 4.0).

**Official routes:** [homepage](https://archive.ics.uci.edu/dataset/464/superconductivty+data) · [data](https://doi.org/10.24432/C53P47) · [paper](https://doi.org/10.1016/j.commatsci.2018.07.052) · [code](https://github.com/khamidieh/predict_tc)

**Evidence:**

- [UCI Superconductivty Data](https://archive.ics.uci.edu/dataset/464/superconductivty+data) (checked 2026-11-01): Official page reports 21,263 instances, 81 features, a formula companion file, NIMS SuperCon parentage and CC BY 4.0.
- [UCI dataset 464 official metadata](https://archive.ics.uci.edu/api/dataset?id=464) (checked 2026-11-01): Confirms instance/feature counts, 2018 release and dataset DOI 10.24432/C53P47.
- [A data-driven statistical model for predicting the critical temperature of a superconductor](https://doi.org/10.1016/j.commatsci.2018.07.052) (checked 2026-11-01): Primary paper describes formula-derived features, preprocessing of NIMS SuperCon data and the regression scope.

**Reuse and interpretation notes:**

- Derived from NIMS SuperCon; not an independent experimental acquisition or an additive expansion of the original/MDR collection.
- No periodic atomic coordinates are included; repeated compositions and sample variants need not be unique compounds.
- The two CSV files contain the same sample cohort and must not be added together.
- Elemental thermal-conductivity and similar descriptors are computed feature aggregates, not measured compound properties.
- The original regression task concerns known superconductors and does not establish classification of superconductors versus nonsuperconductors.

**Tags:** superconductivity, Tc, UCI, composition-only, SuperCon derivative, benchmark, Superconductivty Data (provider spelling), superconductor, superconductors.

<a id="phonix"></a>
## Phonix anharmonic phonon database

Automated first-principles database of anharmonic phonon interactions and thermal transport for inorganic nonmetallic, nonmagnetic compounds.

**Size:** 20,912 unique materials (source wording: 20,912 unique materials; 6,812 unique materials with thermal conductivity).

**Scope:** Full release: 20,912 unique materials, of which 6,812 have kappa; 28,211 total records include duplicates

**Release:** v2026.03.28. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** anharmonic force constants; phonon interactions; thermal conductivity; phonon lifetimes.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://phonix-db.org/) · [data](https://phonix-db.org/ver2026.03.28/index.html) · [paper](https://www.nature.com/articles/s41524-026-02033-w) · [code](https://github.com/phonix-db/auto-kappa)

**Evidence:**

- [Phonix v2026.03.28 release statistics](https://phonix-db.org/ver2026.03.28/index.html) (checked 2026-11-01): 28,211 data records include 7,299 duplicates, leaving 20,912 unique materials; 6,812 unique materials have kappa.
- [Phonix official database documentation](https://phonix-db.org/) (checked 2026-11-01): Documents anharmonic phonon scope, MP/PhononDB parentage and CC BY 4.0 licensing.

**Reuse and interpretation notes:**

- Only 6,812 of the 20,912 unique materials have thermal-conductivity labels.
- 28,211 raw data records contain duplicates and are not unique-material coverage.
- Parent MP/PhononDB structures overlap other collections.
- Nonmetallic/nonmagnetic selection restricts chemistry coverage.

**Tags:** phonon, anharmonic, thermal transport, 2026 release.

<a id="omdb-gap1"></a>
## OMDB-GAP1

Organic molecular-crystal structures paired with DFT band gaps for electronic-property learning.

**Size:** 12,500 materials (source wording: 12,500 materials).

**Scope:** v1.1

**Release:** v1.1. **Year:** 2019.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE band gap; molecular crystal structure.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://omdb.mathub.io/) · [data](https://omdb.mathub.io/dataset/) · [paper](https://doi.org/10.1002/qute.201900023)

**Evidence:**

- [Organic Materials Database dataset downloads](https://omdb.mathub.io/dataset/) (checked 2026-11-01): Official download table lists OMDB-GAP1 v1.1, 12,500 materials, and DOI 10.1002/qute.201900023.

**Reuse and interpretation notes:**

- Periodic molecular crystals are in scope; these are not isolated-molecule HOMO–LUMO gaps.
- The 260,092 COD entry download on the same page contains ML predictions and is distinct from this DFT-labelled training corpus.
- Overlaps COD-origin molecular crystal structures.

**Tags:** molecular crystal, organic, electronic, band gap, COD derivative.

<a id="matbench-elastic"></a>
## Matbench log_gvrh / log_kvrh (shared source cohort)

Fixed Matbench v0.1 structure-to-property prediction task dataset.

**Size:** 10,987 task samples (source wording: 10,987 samples per task).

**Scope:** Matbench log_gvrh / log_kvrh (shared source cohort); fixed released task sample count

**Release:** Matbench v0.1. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** log10 VRH shear modulus; log10 VRH bulk modulus.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://matbench.materialsproject.org/) · [data](https://github.com/materialsproject/matbench/tree/main/matbench) · [paper](https://doi.org/10.1038/s41524-020-00406-3) · [code](https://github.com/materialsproject/matbench)

**Evidence:**

- [Official Matbench v0.1 task metadata](https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json) (checked 2026-11-01): log_gvrh and log_kvrh each have 10,987 structure samples.
- [Official Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): Two tasks share the MP elasticity cohort; positive-modulus and Voigt/Reuss consistency filters were applied.

**Reuse and interpretation notes:**

- Two tasks share the MP elasticity cohort; positive-modulus and Voigt/Reuss consistency filters were applied.
- Task samples reuse parent datasets; do not sum Matbench tasks as unique crystals.
- Preserve the official order and folds for benchmark comparability.

**Tags:** Matbench, benchmark, structure-based, derived dataset.

<a id="snumat-hybrid-gap"></a>
## SNUMAT hybrid-functional band-gap dataset

HSE and GGA electronic gaps, relaxed structures, density of states and magnetic-order information from an automated ICSD-based computation workflow.

**Size:** 10,481 materials (source wording: 10,481 materials with finite band gap).

**Scope:** 10,481 nonmetallic materials released with the descriptor, not all portal calculations

**Release:** Publication finite-gap release (Figshare v7 update 2021). **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** HSE band gap; GGA band gap; direct/indirect gap; density of states; magnetic ordering.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](http://www.snumat.com/) · [data](https://figshare.com/articles/dataset/hybrid_bandgap_200821_v1_zip/12839240) · [paper](https://doi.org/10.1038/s41597-020-00723-8) · [code](https://github.com/MDIL-SNU/AMP2)

**Evidence:**

- [A band-gap database for semiconducting inorganic materials calculated with hybrid functional](https://www.nature.com/articles/s41597-020-00723-8) (checked 2026-11-01): Publication releases 10,481 finite-gap compounds on Figshare; the full portal also includes metals; records contain relaxed POSCAR structures.
- [SNUMAT Figshare publication-release metadata](https://api.figshare.com/v2/articles/12839240) (checked 2026-11-01): Version 7 describes 10,481 inorganic compounds and the 2021-04-13 magnetic-property update; license CC BY 4.0.

**Reuse and interpretation notes:**

- Full SNUMAT and repackaged JARVIS counts can differ because metals and updates are included.
- ICSD-derived selection, finite-gap screening and primitive-cell size limit bias coverage.
- Open Figshare archive; SNUMAT API authorization is a separate access route.

**Tags:** electronic, band gap, hybrid functional, Scientific Data, ICSD derivative.

<a id="phonondb-mdr"></a>
## PhononDB / MDR harmonic phonon calculation database

Harmonic phonon calculations made with VASP and phonopy, migrated from the former Kyoto University phonon database to NIMS MDR.

**Size:** 10,034 material calculation entries (source wording: 10,034 collection items / author-index materials).

**Scope:** Kyoto v2018-04-07 parent; migrated MDR collection checked 2026-11-01

**Release:** Kyoto v2018-04-07 parent; migrated MDR collection checked 2026-11-01. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** harmonic force constants; phonon dispersion; phonon DOS; phonon thermal properties.

**Access:** open. **Dataset license:** Creative Commons BY Attribution 4.0 International.

**Official routes:** [homepage](https://github.com/atztogo/phonondb) · [data](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) · [code](https://github.com/phonopy/phonopy)

**Evidence:**

- [MDR phonon calculation database](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): Collection lists 10,034 items, VASP/phonopy calculations and CC BY 4.0 rights.
- [Phonondb author repository](https://github.com/atztogo/phonondb) (checked 2026-11-01): Confirms Kyoto website closure and migration to NIMS MDR; links the PBEsol material index.

**Reuse and interpretation notes:**

- The Kyoto URL is retired; use the author-maintained MDR migration index.
- Harmonic phonons do not provide lattice thermal conductivity by themselves.
- MDR is the host, not an additional independent phonon dataset.

**Tags:** phonon, PBEsol, Kyoto, MDR, NIMS.

<a id="cerqueira-conventional-epc"></a>
## Cerqueira–Sanna–Marques conventional-superconductor EPC archive

Open ground-state and electron–phonon calculations used upstream of Hennig BEE-NET, with structures, spectra and theoretical Tc estimates.

**Size:** ~7,000 electron–phonon calculations (source wording: around 7,000 model-data calculations; paper reports >8,250 total EPC calculations).

**Scope:** Approximate model-data cohort described by archive; broader public batch archive includes additional calculations and was not enumerated

**Release:** Materials Cloud 2023.163 v1; 2024 Advanced Materials paper. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** optimized crystal structure; Eliashberg alpha2F; phonon bands; electron–phonon coupling; Allen–Dynes Tc; isotropic Eliashberg Tc.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://archive.materialscloud.org/records/3kbt5-r3n56) · [data](https://doi.org/10.24435/materialscloud:qv-bq) · [paper](https://doi.org/10.1002/adma.202307085)

**Evidence:**

- [Cerqueira EPC archive metadata](https://archive.materialscloud.org/api/records/3kbt5-r3n56) (checked 2026-11-01): Around 7000 electron–phonon calculations; 17 batch archives; rights metadata CC BY 4.0.
- [Cerqueira EPC archive README](https://archive.materialscloud.org/api/records/3kbt5-r3n56/files/README.txt/content) (checked 2026-11-01): Documents optimized CIF, alpha2F by smearing, phonon outputs and separate McMillan/Allen–Dynes and isotropic-Eliashberg Tc files.
- [Sampling the Materials Space for Conventional Superconducting Compounds](https://doi.org/10.1002/adma.202307085) (checked 2026-11-01): Paper distinguishes a broader total exceeding 8250 ab initio EPC calculations from ML screening over 191528 candidates.
- [Sampling the materials space for conventional superconducting compounds — data archive](https://archive.materialscloud.org/records/3kbt5-r3n56) (checked 2026-11-01): Author deposit describes around 7,000 electron–phonon calculations used to train a model, followed by screening approximately 200,000 compounds and DFPT validation of selected candidates.

**Reuse and interpretation notes:**

- Created by Cerqueira, Sanna and Marques, not the Hennig group; included because BEE-NET directly reuses a subset.
- Do not sum the archive with the overlapping BEE-NET subset or parent Alexandria structures.
- The approximate 7000 model-data figure and >8250 total calculations are distinct denominators; all raw archive records were not counted.
- Tc values are computed conventional-superconductivity estimates, not experimental confirmations.
- The reused BEE domain is ambient pressure; no pressure-resolved hydride benchmark is implied for all records.
- Approximately 200,000 screened compounds carry model predictions and must not be counted as 200,000 DFPT-labeled superconductors.
- The ranked count is approximate and denotes calculation cases; an independent exact unique-structure recount was not performed.
- Computed Tc and stability screening do not establish experimental superconductivity.
- Training data can overlap other published high-throughput electron–phonon collections; no cross-family deduplication was performed.

**Tags:** superconductivity, electron–phonon, upstream source, Hennig-associated reuse, computed Tc, superconductor, superconductors.

<a id="hennig-bee-net-structures"></a>
## Hennig BEE-NET public structures and split files

Public structural subset and split metadata for BEE-NET, trained on DFT Eliashberg spectra reused from the Cerqueira superconductivity archive.

**Size:** 5,241 public CIF structures (source wording: 5,241 CIF files; documented pool 4,192 train / 1,049 test).

**Scope:** Public Git structures plus split files; full target database and model checkpoints are explicitly not tracked

**Release:** Git revision f21c260a9117830f2d74f2c5ac844ab671c0c606 (2026-10-05); journal paper 2026. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structures; train/test partitions; upstream-linked computed Eliashberg spectra; documented Allen–Dynes Tc targets.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/henniggroup/BEE-NET) · [data](https://github.com/henniggroup/BEE-NET/tree/f21c260a9117830f2d74f2c5ac844ab671c0c606/structures) · [paper](https://doi.org/10.1038/s41524-026-01964-8) · [code](https://github.com/henniggroup/BEE-NET)

Other denominators (not added to the ranking):

- 4,192 training-pool entries: Author README, prior to bootstrap sampling; not additional structures
- 1,049 test entries: Author README and released test-ID file; included in 5241 total

**Evidence:**

- [BEE-NET immutable public file inventory](https://api.github.com/repos/henniggroup/BEE-NET/git/trees/f21c260a9117830f2d74f2c5ac844ab671c0c606?recursive=1) (checked 2026-11-01): Non-truncated public tree contains exactly 5241 CIFs and split indices; no database.json or licence file.
- [BEE-NET author release documentation](https://raw.githubusercontent.com/henniggroup/BEE-NET/f21c260a9117830f2d74f2c5ac844ab671c0c606/README.md) (checked 2026-11-01): States 5241 entries, 1049 test and 4192 training-pool entries; database.json and model ensembles are not tracked; points to Cerqueira upstream.
- [BEE-NET author preprint](https://arxiv.org/html/2503.20005v1) (checked 2026-11-01): Training is ambient-pressure and Tc comparison uses DFT-derived Allen–Dynes values; high-pressure hydrides are outside its stated domain.
- [BEE-NET journal paper](https://www.nature.com/articles/s41524-026-01964-8) (checked 2026-11-01): Describes the AI-assisted discovery workflow; training-data availability points to BEE-NET GitHub.

**Reuse and interpretation notes:**

- Structure files and split metadata are open; a complete ready-to-train target database was not present in the public Git snapshot or GitHub Releases.
- The 5241 entries are a curated subset of upstream calculations, not an independent set of newly computed or experimentally measured superconductors.
- A large screened candidate pool and DFT-selected hits are different denominators from this training-structure release.
- Two experimentally confirmed examples in the study do not convert all training labels into experimental Tc.
- Ambient-pressure training and the stated 100 meV spectral ceiling limit use for high-pressure/high-frequency hydrides.
- No data licence was located in the public repository.

**Tags:** superconductivity, Hennig, partial release, ambient pressure, upstream derivative, superconductor, superconductors, Richard G. Hennig, Hennig group, University of Florida.

<a id="phonondb-mdr-ltc"></a>
## PhononDB lattice thermal conductivity (MDR)

Lattice thermal conductivity release using per-material polynomial machine-learning potentials fitted to VASP PBEsol displaced-supercell data, then phonopy/phono3py force constants.

**Size:** 4,811 listed material calculation entries (source wording: 4,811 material rows counted in the author-maintained release index).

**Scope:** 4,811 unique material-ID rows in release index; independently counted, not a paper-reported size

**Release:** Author release index snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** lattice thermal conductivity; second-order force constants; third-order force constants; DFT training energies and forces; polynomial MLP.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/atztogo/phonondb) · [data](https://github.com/atztogo/phonondb/tree/main/mdr/phonondb_LTC) · [code](https://github.com/phonopy/phono3py)

**Evidence:**

- [Phonondb lattice thermal conductivity data on MDR at NIMS](https://raw.githubusercontent.com/atztogo/phonondb/main/mdr/phonondb_LTC/README.md) (checked 2026-11-01): Counted 4,811 linked material rows in the cached author index; methodology uses 200 random-displacement VASP supercells per crystal to fit polynomial potentials.

**Reuse and interpretation notes:**

- An overlapping subset/extension of harmonic PhononDB.
- Force constants and transport are evaluated with fitted polynomial MLPs, not exclusively direct finite-displacement DFT forces.
- Count comes from the current linked index; individual files and successful-LTC completeness were not audited.
- The index says a methodology manuscript is forthcoming.

**Tags:** phonon, thermal transport, MDR, PBEsol, MLP-assisted.

<a id="matbench-dielectric"></a>
## Matbench dielectric

Fixed Matbench v0.1 structure-to-property prediction task dataset.

**Size:** 4,764 task samples (source wording: 4,764 samples per task).

**Scope:** Matbench dielectric; fixed released task sample count

**Release:** Matbench v0.1. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** refractive index.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://matbench.materialsproject.org/) · [data](https://github.com/materialsproject/matbench/tree/main/matbench) · [paper](https://doi.org/10.1038/s41524-020-00406-3) · [code](https://github.com/materialsproject/matbench)

**Evidence:**

- [Official Matbench v0.1 task metadata](https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json) (checked 2026-11-01): dielectric: 4,764 structure samples; target is refractive index n.
- [Official Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): MP-derived refractive-index task, not the original 1,056-compound dielectric-tensor release; retrieved 2019-04-02.

**Reuse and interpretation notes:**

- MP-derived refractive-index task, not the original 1,056-compound dielectric-tensor release; retrieved 2019-04-02.
- Task samples reuse parent datasets; do not sum Matbench tasks as unique crystals.
- Preserve the official order and folds for benchmark comparability.

**Tags:** Matbench, benchmark, structure-based, derived dataset.

<a id="mc3d-superconductivity"></a>
## MC3D conventional-superconductivity screening and Eliashberg dataset

Electron–phonon and superconductivity calculations on experimental-derived MC3D metal structures, with refined isotropic and anisotropic Migdal–Eliashberg subsets.

**Size:** 4,533 screened metal structures (source wording: 4,533 nonmagnetic metals screened; refined subsets of 250 isotropic and 140 anisotropic Eliashberg calculations).

**Scope:** Version 4 initial Allen–Dynes screening cohort; refined subsets are nested

**Release:** Materials Cloud 2025.175, version 4 (2025-11-04). **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; electron–phonon coupling; Eliashberg spectral function; calculated critical temperature; superconducting gap; prediction sensitivity.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://mc3d.materialscloud.org/?preset=superconductivity) · [data](https://doi.org/10.24435/materialscloud:x2-ap) · [paper](https://doi.org/10.1103/sb28-fjc9)

Other denominators (not added to the ranking):

- 250 structures: Version 4 refined dynamically stable isotropic Migdal–Eliashberg subset
- 140 structures: Version 4 anisotropic Migdal–Eliashberg subset of the refined cohort

**Evidence:**

- [Charting the landscape of Bardeen-Cooper-Schrieffer superconductors in experimentally known compounds — version 4](https://archive.materialscloud.org/records/0kqen-w8h90) (checked 2026-11-01): Archive describes 4,533 initial metals, 250 refined dynamically stable structures and 140 anisotropic cases; supplies AiiDA archives and tables.
- [Materials Cloud version 4 metadata](https://archive.materialscloud.org/api/records/0kqen-w8h90) (checked 2026-11-01): Confirms publication date 2025-11-04 and CC BY 4.0 deposit rights.

**Reuse and interpretation notes:**

- Tc labels are calculated; experimental provenance of the starting crystal structures does not make Tc experimental.
- The 250 and 140 cases are subsets, not additional structures to add to 4,533.
- Earlier preprint/archive versions quote smaller refined subsets; these counts refer specifically to version 4.
- Overlaps the broad MC3D structural family; count this as a property release, not an independent sum of new structures.

**Tags:** superconductivity, DFPT, electron-phonon coupling, Eliashberg, MC3D, high-throughput, superconductor, superconductors.

<a id="aflow-ael-agl-2017"></a>
## AFLOW AEL–AGL thermomechanical cohort (2017)

Combined Automatic Elasticity Library and Automatic GIBBS Library computed property cohort in AFLOW.

**Size:** ≥3,500 materials (source wording: over 3,500 unique materials (2017 publication)).

**Scope:** 2017 publication cohort; current count not asserted

**Release:** 2017 publication cohort; current count not asserted. **Year:** 2017.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** elastic tensor; bulk modulus; shear modulus; Poisson ratio; Debye temperature; Gruneisen parameter; Debye-model thermal conductivity.

**Access:** open. **Dataset license:** Free for scientific, academic and non-commercial purposes; any other use prohibited (AFLUX documentation).

**Official routes:** [homepage](https://aflow.org/) · [data](https://aflow.org/documentation/) · [paper](https://doi.org/10.1103/PhysRevMaterials.1.015401)

**Evidence:**

- [Combining the AFLOW GIBBS and elastic libraries to efficiently and robustly screen thermomechanical properties of solids](https://doi.org/10.1103/PhysRevMaterials.1.015401) (checked 2026-11-01): Abstract reports over 3,500 unique materials; paper describes DFT stress–strain elasticity combined with quasiharmonic Debye thermal estimates.
- [AFLOW REST/AFLUX documentation](https://aflow.org/documentation/) (checked 2026-11-01): Documents AEL/AGL properties and limits data reuse to scientific, academic and non-commercial purposes.

**Reuse and interpretation notes:**

- Historical cohort count, not current AFLOW property coverage.
- Subset of the broad AFLOW parent database; not additive.
- AGL thermal conductivity is a Debye-model estimate, not full third-order force-constant/Boltzmann transport.

**Tags:** elasticity, thermal transport, AFLOW derivative, historical release.

<a id="hennig-xie-eliashberg-benchmark"></a>
## Hennig–Xie Eliashberg / Allen–Dynes symbolic-regression benchmark

Public descriptor and Tc tables combining artificial spectra, computed material cases, literature hydrides and an Allen–Dynes comparison baseline.

**Size:** 3,046 descriptor/Tc table rows (source wording: 3,046 CSV rows across five tables; 3,017 excluding the 29-row comparison table).

**Scope:** Direct CSV count: artificial 2819 + calculated 30 + literature 149 + hydrides 19 + AD29 baseline 29; not unique materials

**Release:** Materials Cloud 2021.150 v1 (2021-09-18); journal paper 2022. **Year:** 2022.

**Provenance:** mixed. **Structure availability:** `mixed`.

**Labels/content:** Eliashberg Tc; Allen–Dynes Tc; lambda; omega_log; omega_2; Coulomb pseudopotential mu*; symbolic-regression prefactors.

**Access:** open. **Dataset license:** Apache-2.0.

**Official routes:** [homepage](https://archive.materialscloud.org/records/skdzy-kyx54) · [data](https://archive.materialscloud.org/api/records/skdzy-kyx54/files/data_tables.zip/content) · [paper](https://doi.org/10.1038/s41524-021-00666-7) · [code](https://github.com/henniggroup/symbolic-regression-utilities)

Other denominators (not added to the ranking):

- 2,874 spectral functions/cases: Paper total: 55 physical cases plus 2819 artificial spectra; not all unique crystals
- 55 physical material spectral functions: 13 in-house calculated + 29 literature classic + 13 literature hydrides
- 2,819 artificial spectral cases: Synthetic trimodal model subset
- 19 hydride table rows: 13 hydride cases resampled across mu*

**Evidence:**

- [Hennig–Xie Materials Cloud metadata](https://archive.materialscloud.org/api/records/skdzy-kyx54) (checked 2026-11-01): Authors include Hennig and Xie; archive contains data_tables.zip plus SISSO records; rights metadata explicitly declares Apache-2.0.
- [Hennig–Xie public numerical tables](https://archive.materialscloud.org/api/records/skdzy-kyx54/files/data_tables.zip/content) (checked 2026-11-01): 429059-byte ZIP matches published MD5 86c68504d1780b6fc7eaccbd4116706c. Direct counts: AD29 29, artificial 2819, calculated 30, hydrides 19, literature 149.
- [Xie et al. Eliashberg theory paper](https://www.nature.com/articles/s41524-021-00666-7) (checked 2026-11-01): Separates 13 calculated, 29 classic and 13 hydride material spectra from 2819 artificial spectra; physical cases are resampled across mu*.
- [Earlier Hennig–Xie analytical-form study (2019)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.100.174513) (checked 2026-11-01): Provides the prior Allen–Dynes-based formula context; no standalone 2018 data release was verified.

**Reuse and interpretation notes:**

- 3046 counts all public table rows, including an overlapping comparison baseline; it does not mean 3046 distinct crystals.
- The primary spectral collection comprises 55 physical material cases plus 2819 artificial spectra; resampling mu* expands numerical rows.
- Hydride validation has 13 material spectral functions / 19 table rows, not 19 unique hydride crystals.
- Tables provide numerical theoretical targets and comparison values; no full CIF collection is deposited here.
- Hydride pressures and full raw spectral inputs are not uniformly encoded in the public descriptor tables; consult original references. The paper says raw data are available upon request.
- The 2019 analytical-form paper and the 2021 archive / 2022 successor paper are related; do not advertise an unverified separate 2018 release.

**Tags:** superconductivity, Hennig, Eliashberg, Allen–Dynes, artificial spectra, hydride validation, superconductor, superconductors, Richard G. Hennig, Hennig group, University of Florida.

<a id="superband"></a>
## SuperBand electronic-band / superconductivity dataset

DFT electronic bands, DOS and Fermi-surface representations linked to experimental superconducting-transition labels and crystal geometry.

**Size:** 2,474 materials (source wording: 1,362 superconductors + 1,112 verified nonsuperconductors = 2,474 band-structure entries).

**Scope:** Scientific Data 2025 band-data release

**Release:** Scientific Data 2025 band-data release. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** DFT band structure; density of states; Fermi surface; experimental Tc; crystal structure.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 (database); MIT (software).

**Official routes:** [homepage](https://www.superband.work/) · [data](https://doi.org/10.57760/sciencedb.16728) · [paper](https://doi.org/10.1038/s41597-025-05015-7) · [code](https://github.com/ljcj007/SuperBand)

Other denominators (not added to the ranking):

- 8,625 reference catalogue CSV rows: Official GitHub superband.csv snapshot 2026-11-01; excludes header; not the 2,474 band-data cohort

**Count derivation:** superconductor + nonsuperconductor band cohorts; 1,362 + 1,112 = 2,474.

**Evidence:**

- [SuperBand: an Electronic-band and Fermi surface structure database of superconductors](https://pmc.ncbi.nlm.nih.gov/articles/PMC12056090/) (checked 2026-11-01): Data Records gives 1,362 superconductors and 1,112 verified nonsuperconductors with band calculations and crystal parameters.
- [SuperBand official repository](https://github.com/ljcj007/SuperBand) (checked 2026-11-01): Training set has 2,474 band entries; database CC BY 4.0, code MIT; GitHub includes four band-data examples and links the full archive.
- [SuperBand: an Electronic-band and Fermi surface structure database of superconductors — Scientific Data descriptor](https://doi.org/10.1038/s41597-025-05015-7) (checked 2026-11-01): Publisher DOI and Crossref metadata verify the corresponding Scientific Data descriptor; the selected release count is supported by the other evidence listed here.
- [SuperBand official reference CSV snapshot](https://raw.githubusercontent.com/ljcj007/SuperBand/main/superband.csv) (checked 2026-11-01): CSV parser counted 8,625 nonheader rows, of which 8,598 have nonempty formula fields; SHA-256 0ab0d37a1dee14146b0d94daf4745df90d73122c6f34c3c2c7d65d8af57ccfb5.
- [SuperBand primary article full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12056090/fullTextXML) (checked 2026-11-01): Data Records confirms 1,362 superconductors plus 1,112 nonsuperconductors; pressure-limited exclusions explain why catalogue references can exceed the band cohort.

**Reuse and interpretation notes:**

- 2,474 is the successful DFT band-data cohort, not the larger initial literature/CIF collection.
- Tc labels are experimental; electronic features are computed.
- Repository text informally calls all 2,474 entries superconductors; the paper explicitly separates 1,362 positive and 1,112 negative entries.
- Official superband.csv contains 8,625 nonheader reference/catalogue rows in the audited snapshot; this is not a replacement for the 2,474 computed-band cohort.
- The snapshot has 8,598 nonempty formula fields and 27 blank formula fields; row counts are not a cleaned unique-material total.
- The paper excludes extreme-pressure hydrides without suitable ambient-pressure structural data from the band cohort, while retaining such formulas in the reference catalogue.

**Tags:** superconductivity, electronic, mixed provenance, Scientific Data, superconductor, superconductors.

<a id="mastml-perovskite-education"></a>
## MAST-ML perovskite stability educational slice

Perovskite-oxide composition and crystallographic site identities paired with DFT stability/property labels and descriptors.

**Size:** 1,929 perovskite composition/feature rows (source wording: 1,929).

**Scope:** Educational Figshare v5 CSV, excluding header; independently parsed1929 rows.

**Release:** Figshare7017254 v5, 2018-09-11. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** energy above hull; formation energy; A/B/X site identities; elemental descriptors.

**Access:** open. **Dataset license:** MIT.

**Official routes:** [homepage](https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254) · [data](https://ndownloader.figshare.com/files/12978425) · [paper](https://doi.org/10.1016/j.commatsci.2018.04.033)

**Evidence:**

- [MAST-ML educational release metadata](https://api.figshare.com/v2/articles/7017254) (checked 2026-11-01): v5 declares MIT licensing and identifies the perovskite CSV as DFT stability data.
- [Educational dataset README](https://ndownloader.figshare.com/files/13008500) (checked 2026-11-01): Defines energy-above-hull and formation-energy targets and site-based elemental descriptors.
- [Official perovskite educational CSV](https://ndownloader.figshare.com/files/12978425) (checked 2026-11-01): Independent parse gives1929 non-header data rows; payload hash retained.

**Reuse and interpretation notes:**

- No complete periodic atomic coordinates are present.
- Educational slice and source-study dataset may have different denominators; this is explicitly the packaged row count.
- Computed convex-hull distance is a screening measure, not experimental proof of synthesis or finite-temperature stability.

**Tags:** education, perovskite, DFT, composition-only.

<a id="mp-dfpt-phonons-2018"></a>
## Materials Project / Petretto DFPT phonons (2018)

ABINIT PBEsol harmonic phonon dispersions and DOS, thermodynamic functions, Born effective charges and dielectric tensors.

**Size:** 1,521 materials (source wording: 1,521 semiconducting inorganic crystals).

**Scope:** Publication release

**Release:** Publication release. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** phonon dispersion; phonon DOS; Born effective charges; dielectric tensor; vibrational thermodynamics.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://doi.org/10.6084/m9.figshare.c.3938023) · [paper](https://doi.org/10.1038/sdata.2018.65)

**Evidence:**

- [High-throughput density-functional perturbation theory phonons for inorganic materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC5928854/) (checked 2026-11-01): Data Records provides 1,521 materials; ABINIT DDB and processed JSON; 1,508 have fewer than thirteen atomic sites.

**Reuse and interpretation notes:**

- Harmonic approximation; not third-order anharmonic force constants or lattice thermal conductivity.
- Includes negative-mode warning flags and omits thermodynamic integration when severe negative frequencies occur.
- Parent of Matbench phonons; overlaps newer MP phonon collections.

**Tags:** phonon, DFPT, MP derivative, Scientific Data.

<a id="lobster-bonding-2023"></a>
## Quantum-Chemical Bonding Database for Solid-State Materials (2023)

LOBSTER bonding descriptors and computational outputs for insulating and semiconducting solids linked to Materials Project IDs.

**Size:** 1,520 compounds (source wording: 1520 solid-state compounds).

**Scope:** Original 2023 release; two archive parts cover one 1520-compound cohort

**Release:** Published 2023 Zenodo parts 1 and 2. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** chemical bonding; COHP-derived descriptors; LOBSTER outputs.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://zenodo.org/records/8091844) · [data](https://zenodo.org/records/8091844) · [paper](https://www.nature.com/articles/s41597-023-02477-5) · [code](https://github.com/naik-aakash/lobster-database-paper-analysis-scripts)

**Evidence:**

- [LOBSTER database Part 1 author deposit](https://zenodo.org/api/records/8091844) (checked 2026-11-01): Describes all 1520 compounds in lightweight JSON, larger outputs for 700, CC BY 4.0.
- [LOBSTER database Part 2 author deposit](https://zenodo.org/api/records/8092187) (checked 2026-11-01): Provides remaining 820 large-output records; same cohort and CC BY 4.0.

**Reuse and interpretation notes:**

- Parts 1 and 2 overlap through the common lightweight cohort; do not sum them as separate materials.
- The collection also links a newer 2026 NOMAD DOI with a claimed larger scope; its count was not independently verified and is not substituted here.
- Structures are linked to source IDs; this is chiefly a bonding-property dataset.

**Tags:** bonding, LOBSTER, Scientific-Data, collection-blaiszik.

<a id="matbench-phonons"></a>
## Matbench phonons

Fixed Matbench v0.1 structure-to-property prediction task dataset.

**Size:** 1,265 task samples (source wording: 1,265 samples per task).

**Scope:** Matbench phonons; fixed released task sample count

**Release:** Matbench v0.1. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** highest-frequency optical phonon DOS peak.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://matbench.materialsproject.org/) · [data](https://github.com/materialsproject/matbench/tree/main/matbench) · [paper](https://doi.org/10.1038/s41524-020-00406-3) · [code](https://github.com/materialsproject/matbench)

**Evidence:**

- [Official Matbench v0.1 task metadata](https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json) (checked 2026-11-01): phonons: 1,265 structure samples; highest-frequency phonon DOS peak target.
- [Official Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): Filtered derivative of the Petretto 1,521-compound DFPT corpus; this scalar target is not a full phonon dispersion or thermal conductivity.

**Reuse and interpretation notes:**

- Filtered derivative of the Petretto 1,521-compound DFPT corpus; this scalar target is not a full phonon dispersion or thermal conductivity.
- Task samples reuse parent datasets; do not sum Matbench tasks as unique crystals.
- Preserve the official order and folds for benchmark comparability.

**Tags:** Matbench, benchmark, structure-based, derived dataset.

<a id="mp-elastic-2015"></a>
## Materials Project elastic tensor release (2015)

Historical frozen release of DFT elastic tensors, compliance tensors and derived moduli, linked to relaxed CIF/POSCAR structures.

**Size:** 1,181 materials (source wording: 1,181 inorganic compounds).

**Scope:** Publication release

**Release:** Publication release. **Year:** 2015.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** elastic tensor; compliance tensor; bulk modulus; shear modulus; elastic anisotropy.

**Access:** open. **Dataset license:** Creative Commons Zero v1.0 Universal (CC0-1.0).

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://doi.org/10.5061/dryad.h505v) · [paper](https://doi.org/10.1038/sdata.2015.9) · [code](https://github.com/materialsproject/pymatgen)

**Evidence:**

- [Charting the complete elastic properties of inorganic crystalline compounds](https://pmc.ncbi.nlm.nih.gov/articles/PMC4432655/) (checked 2026-11-01): Data Records specifies 1,181 materials and structure metadata in CIF/POSCAR form.
- [Dryad elastic-tensor dataset metadata](https://datadryad.org/dataset/doi:10.5061/dryad.h505v) (checked 2026-11-01): Dataset JSON-LD specifies Creative Commons Zero v1.0 Universal.

**Reuse and interpretation notes:**

- Historical descriptor release; not the current total of MP elasticity calculations.
- Overlaps MP and later Matbench elastic cohorts.

**Tags:** elasticity, MP derivative, Scientific Data.

<a id="jarvis-supercon-3d"></a>
## JARVIS superconductivity 3D DFT cohort

Distinct downloadable JARVIS electron–phonon-coupling superconductivity cohort for 3D materials.

**Size:** 1,058 materials (source wording: 1,058 entries).

**Scope:** JARVIS-Tools named supercon_3d release

**Release:** JARVIS-Tools named supercon_3d release. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** electron–phonon coupling; logarithmic phonon frequency; computed superconducting transition temperature.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://jarvis.nist.gov/supercon) · [data](https://figshare.com/ndownloader/files/38307921) · [paper](https://doi.org/10.1038/s41524-022-00933-1) · [code](https://github.com/usnistgov/jarvis)

**Evidence:**

- [JARVIS-Tools database inventory](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): supercon_3d: 1058 entries; explicitly listed as a superconductivity DFT dataset.
- [Official JARVIS dataset loader](https://raw.githubusercontent.com/usnistgov/jarvis/master/jarvis/db/figshare.py) (checked 2026-11-01): supercon_3d maps to the corresponding Figshare JSON, count 1058, and primary paper.
- [JARVIS-SuperconDB Figshare metadata](https://api.figshare.com/v2/articles/21370572) (checked 2026-11-01): v4 groups 3D and 2D electron–phonon files, defines Tc through the McMillan–Allen–Dynes formula, and specifies CC BY 4.0.

**Reuse and interpretation notes:**

- Computed phonon-mediated/BCS-oriented superconductivity estimates, not experimental Tc labels.
- A named property cohort overlapping parent JARVIS materials.
- Do not combine with the experimental/composition-only supercon_chem collection.

**Tags:** superconductivity, 3d, JARVIS derivative, electron–phonon, superconductor, superconductors.

<a id="mp-dielectric-2017"></a>
## Materials Project dielectric tensor release (2017)

DFPT electronic and ionic dielectric tensors, total dielectric response, refractive-index estimates and relaxed structures.

**Size:** 1,056 materials (source wording: 1,056 inorganic ordered compounds).

**Scope:** Publication release

**Release:** Publication release. **Year:** 2017.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** dielectric tensor; electronic dielectric constant; ionic dielectric constant; refractive index.

**Access:** open. **Dataset license:** Creative Commons Zero v1.0 Universal (CC0-1.0).

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://doi.org/10.5061/dryad.ph81h) · [paper](https://doi.org/10.1038/sdata.2016.134) · [code](https://github.com/materialsproject/pymatgen)

**Evidence:**

- [High-throughput screening of inorganic compounds for the discovery of novel dielectric and optical materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC5315501/) (checked 2026-11-01): Reports 1,056 compounds with DFPT dielectric tensors and structure metadata.
- [Dryad dielectric-tensor dataset metadata](https://datadryad.org/dataset/doi:10.5061/dryad.ph81h) (checked 2026-11-01): Dataset JSON-LD specifies Creative Commons Zero v1.0 Universal.

**Reuse and interpretation notes:**

- Historical frozen release, overlapping MP; the later 4,764-sample Matbench task is a different cohort and target.
- Includes hypothetical compounds; refractive index is a computational estimate far from optical resonance.

**Tags:** dielectric, optical, MP derivative, Scientific Data.

<a id="mp-piezo-2015"></a>
## Materials Project piezoelectric tensor release (2015)

DFPT intrinsic piezoelectric tensors with crystal structures and maximum longitudinal piezoelectric response.

**Size:** 941 materials (source wording: 941 inorganic crystalline compounds).

**Scope:** Publication release

**Release:** Publication release. **Year:** 2015.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** piezoelectric tensor; maximum longitudinal piezoelectric modulus.

**Access:** open. **Dataset license:** Creative Commons Zero v1.0 Universal (CC0-1.0).

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://doi.org/10.5061/dryad.n63m4) · [paper](https://doi.org/10.1038/sdata.2015.53) · [code](https://github.com/materialsproject/pymatgen)

**Evidence:**

- [A database to enable discovery and design of piezoelectric materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587372/) (checked 2026-11-01): Reports 941 compounds; CIF/POSCAR structures, tensors and warning flags are released.
- [Dryad piezoelectric-tensor dataset metadata](https://datadryad.org/dataset/doi:10.5061/dryad.n63m4) (checked 2026-11-01): Dataset JSON-LD specifies Creative Commons Zero v1.0 Universal.

**Reuse and interpretation notes:**

- 0 K, bulk, defect-free and strain-free intrinsic response; not measured ceramic/device coefficients.
- 134 of 941 compounds carry one or more consistency-filter warnings; retain flags.
- Overlaps MP; historical release is not the current property count.

**Tags:** piezoelectric, MP derivative, Scientific Data.

<a id="jarvis-high-pressure-hydride-2024"></a>
## JARVIS high-pressure hydride superconductivity campaign

Pressure-resolved DFT/DFPT hydride calculations, superconductivity labels and accompanying ALIGNN models released by the authors.

**Size:** ≥900 structure-pressure calculation cases (source wording: Over 900 high-pressure hydride electron–phonon/DFT calculation cases).

**Scope:** Author paper v4 calculation campaign; repeated pressures per candidate are not unique compounds

**Release:** Figshare version 1 (2024-02-23); paper arXiv v4 (2024-05-31). **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; pressure; phonons; electron–phonon coupling; calculated critical temperature; phase energy; machine-learning predictions.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://figshare.com/articles/dataset/Data-driven_Design_of_High_Pressure_Hydride_Superconductors_using_DFT_and_Deep_Learning/25270012) · [data](https://doi.org/10.6084/m9.figshare.25270012.v1) · [paper](https://arxiv.org/abs/2312.12694)

Other denominators (not added to the ranking):

- 122 structure-pressure cases: Dynamically stable computed cases reported above MgB2 reference Tc of 39 K

**Evidence:**

- [Data-driven Design of High Pressure Hydride Superconductors using DFT and Deep Learning — author version 4](https://arxiv.org/html/2312.12694v4) (checked 2026-11-01): Latest author version describes over 900 EPC/DFT cases spanning multiple pressures and 122 dynamically stable cases above the MgB2 reference Tc.
- [High-pressure hydride dataset Figshare metadata](https://api.figshare.com/v2/articles/25270012) (checked 2026-11-01): Version 1 deposit contains raw DFT hydride data, ALIGNN data/models, a notebook and phase energies; license is CC BY 4.0.

**Reuse and interpretation notes:**

- The same candidate is evaluated at multiple pressures; over 900 is not a unique-composition count.
- This pressure-resolved release is distinct from the existing JARVIS ambient 3D and 2D superconductivity cohorts, but source structures overlap JARVIS, 3DSC and earlier hydride work.
- Calculated Tc labels and model predictions coexist in the package; model predictions are not additional DFT validation.
- Earlier manuscript versions used different training-set wording; the selected lower-bound count follows author version 4.

**Tags:** superconductivity, JARVIS, hydrides, high pressure, DFPT, ALIGNN, superconductor, superconductors.

<a id="superhydra"></a>
## Superhydra binary-hydride database

Template-generated binary hydrides with calculated electronic, vibrational and chemical descriptors at high pressure.

**Size:** 880 hypothetical hydride structures (source wording: 880 hypothetical structures; 139 superconducting cases in the McMillan–Allen–Dynes approximation).

**Scope:** Binary-hydride template cohort at 200 GPa, not 880 independent Tc-positive observations

**Release:** 2023 Physical Review Materials release; 2022 preprint dataset. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** structural template; pressure; electronic descriptors; vibrational descriptors; electron–phonon coupling; calculated critical temperature.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://arxiv.org/abs/2205.02554) · [data](https://journals.aps.org/prmaterials/supplemental/10.1103/PhysRevMaterials.7.054806) · [paper](https://doi.org/10.1103/PhysRevMaterials.7.054806)

Other denominators (not added to the ranking):

- 139 calculated superconducting structures: McMillan–Allen–Dynes superconducting subset of the 880-case cohort

**Evidence:**

- [Mapping Superconductivity in High-Pressure Hydrides: The Superhydra Project](https://arxiv.org/abs/2205.02554) (checked 2026-11-01): Authors report 880 hypothetical binary-hydride structures and 139 superconducting cases under the McMillan–Allen–Dynes approximation.
- [Superhydra Physical Review Materials article and Supplemental Material](https://doi.org/10.1103/PhysRevMaterials.7.054806) (checked 2026-11-01): Published article identifies the supplemental CSV release; the cohort is generated by element substitution into structural templates.

**Reuse and interpretation notes:**

- The main count includes the full hypothetical-structure cohort, not just calculated superconductors.
- Structure-linked classification is conservative: complete atomic coordinates in the supplemental CSV were not independently audited.
- Dataset-specific reuse license was not verified.
- The campaign is pressure-specific and calculated; it does not establish synthesis, experimental Tc or ambient-pressure stability.

**Tags:** superconductivity, hydrides, high pressure, template generation, electron-phonon coupling, superconductor, superconductors.

<a id="hennig-bete-net"></a>
## Hennig BETE-NET released EPC cohort

DFT electron–phonon spectral data, phonon descriptors and CIFs released with the tempered-learning superconductivity study.

**Size:** 806 released crystal structures (source wording: 806 released composition rows and 806 CIF files; paper cohort: 818).

**Scope:** Public Git snapshot: complete comp column and matching CIF inventory; distinct from the paper-described 818-material cohort

**Release:** Git revision 56bc783908a60e8a15e31b60018e6f3c3e48f593 (2024-08-20); journal paper 2025. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** Eliashberg spectral function alpha2F; phonon DOS; electron–phonon coupling lambda; phonon frequency moments; computed superconducting Tc.

**Access:** open. **Dataset license:** Apache-2.0 (repository declaration).

**Official routes:** [homepage](https://github.com/henniggroup/BETE-NET) · [data](https://github.com/henniggroup/BETE-NET/blob/56bc783908a60e8a15e31b60018e6f3c3e48f593/database.json) · [paper](https://doi.org/10.1038/s41524-024-01475-4) · [code](https://github.com/henniggroup/BETE-NET)

Other denominators (not added to the ranking):

- 818 materials: Journal-described dynamically stable cohort; differs from current public file count
- 1,265 converged calculations: 2024 author-preprint denominator before filtering, not the released cohort
- 1,600 attempted calculations: 2024 author-preprint submitted calculations, not successful records

**Evidence:**

- [BETE-NET immutable public file inventory](https://api.github.com/repos/henniggroup/BETE-NET/git/trees/56bc783908a60e8a15e31b60018e6f3c3e48f593?recursive=1) (checked 2026-11-01): Non-truncated tree has 806 CIFs and an 89104840-byte database.json.
- [BETE-NET released data header](https://raw.githubusercontent.com/henniggroup/BETE-NET/56bc783908a60e8a15e31b60018e6f3c3e48f593/database.json) (checked 2026-11-01): Complete first JSON field comp contains 806 row labels; only a 256 KiB prefix was retrieved.
- [BETE-NET journal paper](https://www.nature.com/articles/s41524-024-01475-4) (checked 2026-11-01): Describes high-quality calculations for 818 dynamically stable materials, selected from a larger attempted/converged pool.
- [BETE-NET author release documentation](https://raw.githubusercontent.com/henniggroup/BETE-NET/56bc783908a60e8a15e31b60018e6f3c3e48f593/README.md) (checked 2026-11-01): Identifies database, corresponding CIFs, split indices and predictions as paper data.
- [BETE-NET repository licence](https://raw.githubusercontent.com/henniggroup/BETE-NET/56bc783908a60e8a15e31b60018e6f3c3e48f593/LICENSE) (checked 2026-11-01): Repository licence file declares Apache License 2.0.

**Reuse and interpretation notes:**

- 806 is a public-file denominator, not a correction to the paper's 818-material scientific cohort. The discrepancy remains unresolved.
- Published train/test index files contain 824 labels; 18 do not occur in the released comp row labels. Match indices to the intended data version before reuse.
- Tc targets are calculated from electron–phonon spectra; these are not 806 measured superconductors.
- A pressure-resolved release field was not verified; do not treat this as a high-pressure hydride benchmark.
- Repository licensing is recorded independently of the journal article licence.

**Tags:** superconductivity, Hennig, electron–phonon, computed Tc, release discrepancy, superconductor, superconductors, Richard G. Hennig, Hennig group, University of Florida.

<a id="matbench-jdft2d"></a>
## Matbench jdft2d

Fixed Matbench v0.1 structure-to-property prediction task dataset.

**Size:** 636 task samples (source wording: 636 samples per task).

**Scope:** Matbench jdft2d; fixed released task sample count

**Release:** Matbench v0.1. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** exfoliation energy.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://matbench.materialsproject.org/) · [data](https://github.com/materialsproject/matbench/tree/main/matbench) · [paper](https://doi.org/10.1038/s41524-020-00406-3) · [code](https://github.com/materialsproject/matbench)

**Evidence:**

- [Official Matbench v0.1 task metadata](https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json) (checked 2026-11-01): jdft2d: 636 structure samples; exfoliation-energy target.
- [Official Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): Adapted from the JARVIS-DFT two-dimensional dataset; an overlapping benchmark subset, not all JARVIS 2D materials.

**Reuse and interpretation notes:**

- Adapted from the JARVIS-DFT two-dimensional dataset; an overlapping benchmark subset, not all JARVIS 2D materials.
- Task samples reuse parent datasets; do not sum Matbench tasks as unique crystals.
- Preserve the official order and folds for benchmark comparability.

**Tags:** Matbench, benchmark, structure-based, derived dataset.

<a id="mastml-dilute-diffusion-education"></a>
## MAST-ML dilute-solute diffusion educational slice

DFT dilute-solute diffusion barriers in host crystals, packaged with host/solute elemental descriptors for teaching.

**Size:** 408 host–solute feature/property rows (source wording: 408).

**Scope:** Educational Figshare v5 CSV, excluding header; independently parsed408 rows.

**Release:** Figshare7017254 v5, 2018-09-11. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** normalized activation energy; raw activation energy; host and solute composition; elemental descriptors.

**Access:** open. **Dataset license:** MIT.

**Official routes:** [homepage](https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254) · [data](https://ndownloader.figshare.com/files/13007075) · [paper](https://doi.org/10.1038/sdata.2016.54)

**Evidence:**

- [MAST-ML educational release metadata](https://api.figshare.com/v2/articles/7017254) (checked 2026-11-01): v5 package declares MIT licensing and identifies the diffusion CSV as DFT-based.
- [Educational dataset README](https://ndownloader.figshare.com/files/13008500) (checked 2026-11-01): Defines normalization relative to host self diffusion and a separate raw-energy target.
- [Official diffusion educational CSV](https://ndownloader.figshare.com/files/13007075) (checked 2026-11-01): Independent parse gives408 non-header data rows; source SHA-256 retained in collection inventory.

**Reuse and interpretation notes:**

- Educational packaging derived from a prior diffusion corpus; do not add it to the parent as unique new materials.
- Host/solute identities and descriptors are provided; periodic coordinates are absent.
- Normalized and raw activation energies are different targets.

**Tags:** education, diffusion, derived, composition-only.

<a id="antiperovskite-superconductivity-dfpt"></a>
## Antiperovskite superconductivity DFPT dataset

Electron–phonon calculations for cubic antiperovskites XYZ3 with metal X/Z and H, B, C, N, O or P on the Y site.

**Size:** 384 material calculation cases (source wording: Electron–phonon calculations for 384 antiperovskites).

**Scope:** Starting DFPT cohort in the 2022 archive, including dynamically unstable cases

**Release:** Materials Cloud 2022.49, version 1. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; phonons; electron–phonon coupling; calculated critical temperature; electronic descriptors.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://archive.materialscloud.org/records/2hg1p-63427) · [data](https://doi.org/10.24435/materialscloud:6g-az)

Other denominators (not added to the ranking):

- 16 calculated material cases: Initial DFPT cohort with calculated Tc above 5 K

**Evidence:**

- [Superconductivity in antiperovskites — data archive](https://archive.materialscloud.org/records/2hg1p-63427) (checked 2026-11-01): Describes 384 starting DFPT cases, approximately 40% with imaginary phonons, and 16 calculated cases above 5 K.
- [Materials Cloud 2022.49 metadata](https://archive.materialscloud.org/api/records/2hg1p-63427) (checked 2026-11-01): Confirms 2022-04-06 release, downloadable calculation archives and CC BY 4.0 rights.

**Reuse and interpretation notes:**

- The cohort includes dynamically unstable materials; 384 is not a count of stable superconductors.
- The further 44 materials above 5 K are model predictions and are not added to the DFPT cohort count.
- All superconducting temperatures in this release are theoretical.

**Tags:** superconductivity, DFPT, antiperovskites, electron-phonon coupling, high-throughput, superconductor, superconductors.

<a id="jarvis-supercon-2d"></a>
## JARVIS superconductivity 2D DFT cohort

Distinct downloadable JARVIS electron–phonon-coupling superconductivity cohort for 2D materials.

**Size:** 161 materials (source wording: 161 entries).

**Scope:** JARVIS-Tools named supercon_2d release

**Release:** JARVIS-Tools named supercon_2d release. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** electron–phonon coupling; logarithmic phonon frequency; computed superconducting transition temperature.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://jarvis.nist.gov/supercon) · [data](https://figshare.com/ndownloader/files/38950433) · [paper](https://doi.org/10.1021/acs.nanolett.2c04420) · [code](https://github.com/usnistgov/jarvis)

**Evidence:**

- [JARVIS-Tools database inventory](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): supercon_2d: 161 entries; explicitly listed as a superconductivity DFT dataset.
- [Official JARVIS dataset loader](https://raw.githubusercontent.com/usnistgov/jarvis/master/jarvis/db/figshare.py) (checked 2026-11-01): supercon_2d maps to the corresponding Figshare JSON, count 161, and primary paper.
- [JARVIS-SuperconDB Figshare metadata](https://api.figshare.com/v2/articles/21370572) (checked 2026-11-01): v4 groups 3D and 2D electron–phonon files, defines Tc through the McMillan–Allen–Dynes formula, and specifies CC BY 4.0.

**Reuse and interpretation notes:**

- Computed phonon-mediated/BCS-oriented superconductivity estimates, not experimental Tc labels.
- A named property cohort overlapping parent JARVIS materials.
- Do not combine with the experimental/composition-only supercon_chem collection.

**Tags:** superconductivity, 2d, JARVIS derivative, electron–phonon, superconductor, superconductors.

<a id="htsc-2025"></a>
## HTSC-2025 ambient-pressure BCS superconductor benchmark

A curated benchmark of crystal CIFs and literature theoretical Tc values for recent ambient-pressure conventional-superconductor candidates.

**Size:** 140 material records (source wording: 140 material records with CIF structures and Tc values).

**Scope:** 140 top-level material keys independently counted in official HTSC-2025.json

**Release:** ScienceDB V1; official Hugging Face JSON snapshot 2026-11-01. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; calculated critical temperature.

**Access:** open. **Dataset license:** MIT License (ScienceDB V1 registrant metadata).

**Official routes:** [homepage](https://huggingface.co/datasets/xiao-qi/HTSC-2025) · [data](https://doi.org/10.57760/sciencedb.j00113.00259) · [paper](https://doi.org/10.1088/1674-1056/adf042)

**Evidence:**

- [HTSC-2025 official dataset card](https://huggingface.co/datasets/xiao-qi/HTSC-2025/raw/main/README.md) (checked 2026-11-01): Describes 140 ambient-pressure BCS materials compiled from recent theoretical studies, grouped into six material families.
- [HTSC-2025 official JSON data](https://huggingface.co/datasets/xiao-qi/HTSC-2025/raw/main/HTSC-2025.json) (checked 2026-11-01): Independently parsed 140 material keys; entries contain CIF text and a tc field. SHA-256 fba2681d115fcd131e0e09086bf0a271d6ecb5ef9e46f238be98d3faac0f92a3.
- [ScienceDB HTSC-2025 V1 DOI metadata](https://api.datacite.org/dois/10.57760/sciencedb.j00113.00259) (checked 2026-11-01): Registrant metadata gives version V1, MIT rights and the theoretical-superconductor benchmark description.

**Reuse and interpretation notes:**

- The cohort primarily compiles predicted superconductors, not 140 experimentally demonstrated high-Tc materials; MgB2 also appears as a reference.
- The dataset viewer can display one row because the JSON is a single dictionary; 140 is the number of material entries inside it.
- Literature-calculated Tc values can use different computational assumptions and should not be treated as a uniformly recomputed experimental benchmark.

**Tags:** superconductivity, ambient pressure, BCS, hydrides, crystal benchmark, superconductor, superconductors.

<a id="phonondb-103-pbesol"></a>
## Phono3py 103-compound finite-displacement dataset (PBEsol)

Finite-displacement force data for lattice thermal conductivity calculations, supporting the Phonopy/Phono3py methods reference.

**Size:** 103 compounds (source wording: 103 binary compounds).

**Scope:** PBEsol finite-displacement release

**Release:** PBEsol finite-displacement release. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** lattice thermal conductivity; displaced-supercell forces; anharmonic phonons.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/atztogo/phonondb) · [data](https://github.com/atztogo/phonondb/tree/main/mdr/phono3py_103compounds_fd) · [paper](https://doi.org/10.7566/JPSJ.92.012001) · [code](https://github.com/phonopy/phono3py)

**Evidence:**

- [Lattice thermal conductivity calculation datasets for 103 binary compounds by finite displacement method](https://mdr.nims.go.jp/collections/e85f8f40-d810-42ae-91c4-0a07b9641219?locale=en) (checked 2026-11-01): Collection identifies 103 binary compounds and phono3py inputs used for Fig. 17 of JPSJ 92, 012001.
- [Phonondb author repository](https://github.com/atztogo/phonondb) (checked 2026-11-01): Separately identifies PBEsol and PBE 103-compound finite-displacement releases.

**Reuse and interpretation notes:**

- PBEsol and PBE versions largely share compounds and are not independent chemistry coverage.
- Different from the larger polynomial-MLP-assisted PhononDB LTC release.

**Tags:** phonon, thermal transport, PBEsol, MDR.
