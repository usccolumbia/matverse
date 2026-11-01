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

**Count derivation:** superconductor + nonsuperconductor band cohorts; 1,362 + 1,112 = 2,474.

**Evidence:**

- [SuperBand: an Electronic-band and Fermi surface structure database of superconductors](https://pmc.ncbi.nlm.nih.gov/articles/PMC12056090/) (checked 2026-11-01): Data Records gives 1,362 superconductors and 1,112 verified nonsuperconductors with band calculations and crystal parameters.
- [SuperBand official repository](https://github.com/ljcj007/SuperBand) (checked 2026-11-01): Training set has 2,474 band entries; database CC BY 4.0, code MIT; GitHub includes four band-data examples and links the full archive.
- [SuperBand: an Electronic-band and Fermi surface structure database of superconductors — Scientific Data descriptor](https://doi.org/10.1038/s41597-025-05015-7) (checked 2026-11-01): Publisher DOI and Crossref metadata verify the corresponding Scientific Data descriptor; the selected release count is supported by the other evidence listed here.

**Reuse and interpretation notes:**

- 2,474 is the successful DFT band-data cohort, not the larger initial literature/CIF collection.
- Tc labels are experimental; electronic features are computed.
- Repository text informally calls all 2,474 entries superconductors; the paper explicitly separates 1,362 positive and 1,112 negative entries.

**Tags:** superconductivity, electronic, mixed provenance, Scientific Data.

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

**Tags:** superconductivity, 3d, JARVIS derivative, electron–phonon.

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

**Tags:** superconductivity, 2d, JARVIS derivative, electron–phonon.

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
