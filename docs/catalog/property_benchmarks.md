# Computed properties and prediction benchmarks

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="omdb-cod-bandgap-predictions"></a>
## OMDB-GAP1 models: COD band-gap prediction release

SOAP/kernel-ridge and SchNet band-gap predictions for a large COD-derived organic-crystal screening set, distinct from the DFT-labelled OMDB-GAP1 training corpus.

**Size:** 260,092 COD crystal prediction records (source wording: 260,092 COD crystal entries with model-predicted band gaps).

**Scope:** Named v1.1 COD prediction download, corresponding to the paper cohort of organic structures with at most 500 atoms per unit cell

**Release:** COD predictions v1.1 on the OMDB dataset page; 2019 paper cohort. **Year:** 2019.

**Provenance:** machine-learning predictions. **Structure availability:** `structure_linked`.

**Labels/content:** machine-learning predicted band gap; SOAP/kernel-ridge band-gap prediction; SchNet band-gap prediction; ensemble band-gap prediction.

**Access:** registration. **Dataset license:** Not verified.

**Official routes:** [homepage](https://omdb.mathub.io/dataset/) · [data](https://omdb.mathub.io/dataset/download/gap1-cod_v1.1) · [paper](https://doi.org/10.1002/qute.201900023)

**Evidence:**

- [OMDB official dataset downloads](https://omdb.mathub.io/dataset/) (checked 2026-11-01): Separately lists OMDB-GAP1 v1.1 at 12,500 materials and a COD v1.1 machine-learning prediction download at 260,092 materials.
- [Band Gap Prediction for Large Organic Crystal Structures with Machine Learning](https://onlinelibrary.wiley.com/doi/full/10.1002/qute.201900023) (checked 2026-11-01): Section 3.2 describes selecting organic COD structures containing C/H and supported elements, limiting cells to 500 atoms, and computing 260,092 model predictions; Data Availability identifies the release.
- [OMDB COD prediction download access check](https://omdb.mathub.io/dataset/download/gap1-cod_v1.1) (checked 2026-11-01): Public download link redirects to the login page, which offers free registration; payload was not obtained without an account.

**Reuse and interpretation notes:**

- Properties are machine-learning predictions, not 260,092 new DFT calculations or measured band gaps.
- The source crystal structures are COD-derived and overlap the COD family; no independent new-structure total is implied.
- Provider release count was not independently recounted because download currently requires login.
- Structure-linked classification denotes the named COD-source linkage; atomic-coordinate content and exact payload columns were not inspected.
- Dataset-specific reuse license was not identified in the inspected download and terms pages.

**Tags:** organic crystals, COD derivative, OMDB, band gap, machine-learning predictions, registration.

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

<a id="mp-graphs-2019"></a>
## Graphs of MP 2019

Contains 133,420 graph-target pairs for Materials Project structures which were used to train the MEGNet formation energy model.

**Size:** 133,420 graph–target records (source wording: 133,420).

**Scope:** MP Graphs: training release listed by Matbench Discovery; numerical count is source-reported, not a MatVerse payload recount.

**Release:** MP Graphs release as listed in Matbench Discovery at 8869a883a506. **Year:** 2019.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal CIF strings; graph features; formation energy (eV/atom).

**Access:** open. **Dataset license:** MIT (provider/benchmark release declaration).

**Official routes:** [homepage](https://figshare.com/articles/dataset/8097992) · [data](https://figshare.com/ndownloader/articles/8097992/versions/2) · [paper](https://doi.org/10.1021/acs.chemmater.9b01294)

Other denominators (not added to the ranking):

- 133,420 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MP Graphs: 133,420 configurations/structures; role training, created 2019-06-06, declared data license MIT. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MP Graphs entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [Graphs of Materials Project20190401 deposit](https://api.figshare.com/v2/articles/8097992) (checked 2026-11-01): Provider describes133,420 graph–target dictionaries, material_id, graph, formation_energy_per_atom(eV/atom) and CIF structure. Separate12,179-record elastic graphs are excluded. MIT declared in deposit metadata.

**Reuse and interpretation notes:**

- Counted 133,420 graph records with distinct material_id values in mp.2019.04.01.json.zip (https://figshare.com/files/15108200), one per material. The separately distributed elastic-property graphs are not added to this count.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Graph encodings depend on the5Å cutoff and preprocessing; these are derived MP structures rather than newly independent experiments.

**Tags:** Matbench-sets-20261101, MP Graphs, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

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

<a id="mdf-assorted-computed-band-gaps"></a>
## Foundry assorted computational band-gap cohort

Graph Network Based Deep Learning of Band Gaps - Assorted Computational Band Gaps

**Size:** 105,594 computed band-gap records (source wording: 105,594).

**Scope:** Foundry projects.foundry.n_items for foundry_assorted_computational_band_gaps_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** foundry_assorted_computational_band_gaps_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2021.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** band gap; calculation functional; band-gap type; declared crystal structure.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/foundry_assorted_computational_band_gaps_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/foundry_assorted_computational_band_gaps_v1.1/) · [release](https://doi.org/10.18126/7io9-1z9k) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=foundry_assorted_computational_band_gaps_v1.1) (checked 2026-11-01): Public subject response identifies foundry_assorted_computational_band_gaps_v1.1, DOI 10.18126/7io9-1z9k, n_items=105,594, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The JSON schema declares a structure field; atomic-coordinate completeness across the cohort was not audited.
- The archive filename is All_no_MP_Aflow_OQMD_new.json. Keep reported calculation methods and source references; do not merge labels as one uniform DFT protocol.

**Tags:** MDF, Foundry, MDF-property-20261101.

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

<a id="quantumdefects-semiconductor"></a>
## Quantum Defects Database — semiconductor point defects

Calculated point-defect structures and electronic/optical properties for quantum applications in diamond, silicon carbide and silicon.

**Size:** ≥50,000 point-defect calculations (source wording: >50,000).

**Scope:** Paper reports over 50,000 point-defect calculations. Charge states and excited states are not independent host materials.

**Release:** 2023 paper cohort; living public interface checked 2026-11-01. **Year:** 2023.

**Provenance:** High-throughput first-principles semiconductor defect calculations by Ivanov and collaborators. **Structure availability:** `periodic_atomic`.

**Labels/content:** relaxed defect structures; formation energies; spin states; zero-phonon lines; transition dipole moments.

**Access:** open. **Dataset license:** Not verified; public access does not establish a reuse licence.

**Official routes:** [Provider](https://quantumdefects.com/) · [Example](https://quantumdefects.com/c103) · [Paper](https://arxiv.org/abs/2303.16283)

**Evidence:**

- [Database of semiconductor point-defect properties for applications in quantum technologies](https://arxiv.org/abs/2303.16283) (checked 2026-11-01): Author abstract reports over 50,000 calculated defects and publicly available relaxed structures.
- [Live example: Ta substitution and Si interstitial](https://quantumdefects.com/c103) (checked 2026-11-01): Public example supplies charge-state controls, energies, spin information and a POSCAR-format structure download. A Si search returned 400 indexed results.

**Reuse and interpretation notes:**

- Paper-cohort lower bound is retained; live total was not verified.
- Distinct from QPOD, which focuses on intrinsic defects in two-dimensional materials.
- Properties are computed predictions and require application-specific validation.

**Tags:** point-defects, dopants, vacancies, quantum-defects, semiconductors, additional-materials-20261101.

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

**Tags:** transport, thermoelectric, MP derivative, Scientific Data, Scientific-Data-descriptor.

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

<a id="ecd-cubic"></a>
## ECD-cubic electronic charge-density database

Real-space DFT electronic charge densities for cubic inorganic periodic materials selected from Materials Project.

**Size:** 17,418 cubic material charge-density records (source wording: 17,418 cubic material charge-density records).

**Scope:** Publication dataset split across three Figshare payload parts; contains spin-polarized and unpolarized data.

**Release:** Publication-linked Figshare collection. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** electronic charge density; atomic structure; energy.

**Access:** open. **Dataset license:** CC0 1.0 (inspected Figshare payload metadata).

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01158-z) · [data](https://doi.org/10.6084/m9.figshare.c.5368343)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-022-01158-z) (checked 2026-11-01): Real-space DFT electronic charge densities for cubic inorganic periodic materials selected from Materials Project. Publication dataset split across three Figshare payload parts; contains spin-polarized and unpolarized data.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/14396414) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Restricted to cubic materials; not a general all-symmetry charge-density dataset.
- Underlying crystals overlap Materials Project; property grids are not new crystal materials.
- Large multi-part payloads were not downloaded; count comes from primary article.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="jarvis-wtbh-phonon"></a>
## JARVIS-WTBH phonon Hamiltonians

Phonon Hamiltonian subset associated with finite-difference JARVIS calculations.

**Size:** 15,502 phonon Hamiltonian entries (source wording: 15,502).

**Scope:** Selected wtbh_phonon release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS wtbh_phonon documentation / pinned downloader snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** phonon Hamiltonian; force constants; phonons; finite difference.

**Access:** open. **Dataset license:** Not verified for the Hamiltonian payloads.

**Official routes:** [homepage](https://jarvis.nist.gov/jarviswtb) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://ndownloader.figshare.com/files/25295732)

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named wtbh_phonon row reports 15,502 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the wtbh_phonon route or dedicated helper and the raw-file grouping.

**Reuse and interpretation notes:**

- Use get_wann_phonon(jid=...) and the FD-ELAST raw-file group; wtbh_phonon is not a current data(name) registry key. Documentation count was not independently recounted.
- The web portal may require registration; the linked public file route is separate.

**Tags:** JARVIS, wtbh_phonon, release-snapshot.

<a id="jarvis-efg-2020"></a>
## JARVIS electric-field-gradient tensor release

Computed site-resolved electric-field-gradient tensors with periodic atomic geometries for a JARVIS-DFT material subset.

**Size:** 15,202 material EFG records (source wording: 15,202 unique-JID JSON records; publication states 15,187 materials).

**Scope:** Independently counted v2 JSON payload, with one unique JARVIS identifier per row; publication/repository abstract count is retained as a separate discrepant cohort counter.

**Release:** Figshare 12307700 v2; inspected JARVIS-EFG4.json payload. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** site-resolved EFG tensor; diagonalized EFG tensor; periodic atomic structure; EFG asymmetry via accompanying CSV.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare v2 data licence).

**Official routes:** [paper](https://doi.org/10.1038/s41597-020-00707-8) · [data](https://doi.org/10.6084/m9.figshare.12307700.v2) · [homepage](https://jarvis.nist.gov/)

Other denominators (not added to the ranking):

- 15,187 materials: Original primary-paper and repository-abstract count; differs from inspected v2 payload

**Evidence:**

- [Primary EFG data descriptor](https://doi.org/10.1038/s41597-020-00707-8) (checked 2026-11-01): Reports EFG calculations for 15,187 JARVIS-DFT materials and a JSON file containing atoms plus raw/diagonalized tensors; uses calculated structures rather than experimental geometries.
- [Figshare v2 release metadata](https://api.figshare.com/v2/articles/12307700/versions/2) (checked 2026-11-01): Lists JARVIS-EFG4.csv, JARVIS-EFG4.json and parser example, with CC BY 4.0 rights. Downloaded JSON is 18,600,334 bytes; MD5 5877c7410a76e412a695925eb5b4cd27 matches provider metadata and contains 15,202 distinct JIDs.

**Reuse and interpretation notes:**

- Versioned downloadable JSON has 15,202 unique-JID rows, while both article and repository abstract state 15,187; the reason for this difference is unresolved.
- This property subset overlaps JARVIS-DFT; it is not 15,202 additional newly discovered compounds.
- EFGs are computed on DFT-relaxed geometries; experimental NQR frequency comparison additionally depends on nuclear quadrupole moments and measurement conditions.
- Site tensors and materials are different counting units.

**Tags:** Scientific Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101, JARVIS, EFG.

<a id="omdb-gap1"></a>
## OMDB-GAP1

Organic molecular-crystal structures paired with DFT band gaps for electronic-property learning.

**Size:** 12,500 materials (source wording: 12,500 materials).

**Scope:** v1.1

**Release:** v1.1. **Year:** 2019.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE band gap; molecular crystal structure.

**Access:** registration. **Dataset license:** Not verified.

**Official routes:** [homepage](https://omdb.mathub.io/) · [data](https://omdb.mathub.io/dataset/download/gap1_v1.1) · [paper](https://doi.org/10.1002/qute.201900023)

**Evidence:**

- [Organic Materials Database dataset downloads](https://omdb.mathub.io/dataset/) (checked 2026-11-01): Official download table lists OMDB-GAP1 v1.1, 12,500 materials, and DOI 10.1002/qute.201900023.
- [OMDB-GAP1 download access check](https://omdb.mathub.io/dataset/download/gap1_v1.1) (checked 2026-11-01): Named v1.1 download redirects to free-registration login. Limited public browsing does not establish anonymous bulk access; payload was not downloaded.

**Reuse and interpretation notes:**

- Periodic molecular crystals are in scope; these are not isolated-molecule HOMO–LUMO gaps.
- The 260,092 COD entry download on the same page contains ML predictions and is distinct from this DFT-labelled training corpus.
- Overlaps COD-origin molecular crystal structures.
- The current named download requires registration; public browsing and bulk-download access are separate.

**Tags:** molecular crystal, organic, electronic, band gap, COD derivative.

<a id="spse-ion-transport-2020"></a>
## SPSE hierarchical solid-electrolyte ion transport

Released SPSE ZIP contains 11,989 BVSE entries, 7,678 CAVD entries, 49 hierarchical calculation entries, 121 literature entries and 91,763 parent CIF records.

**Size:** 11,989 BVSE transport entries (source wording: 11,989).

**Scope:** Released SPSE ZIP contains 11,989 BVSE entries, 7,678 CAVD entries, 49 hierarchical calculation entries, 121 literature entries and 91,763 parent CIF records.

**Release:** Figshare 12011412 v1; JSONL archive recount. **Year:** 2020.

**Provenance:** mixed. **Structure availability:** `structure_linked`.

**Labels/content:** BVSE migration/activation-energy descriptors; geometric ion-path descriptors; hierarchical FP-NEB paths; experimental literature transport values; structure identifiers.

**Access:** open. **Dataset license:** CC BY 4.0 for deposit; underlying ICSD coordinate rights require separate review.

**Official routes:** [paper](https://doi.org/10.1038/s41597-020-0474-y) · [data](https://doi.org/10.6084/m9.figshare.12011412.v1) · [homepage](https://www.bmaterials.cn/)

**Evidence:**

- [High-throughput screening platform for solid electrolytes combining hierarchical ion-transport prediction algorithms](https://www.nature.com/articles/s41597-020-0474-y) (checked 2026-11-01): Paper separates source structures, empirical path/BVSE labels, hierarchical FP-NEB calculations and literature properties; exact archive BVSE count is 11,989 versus rounded 12,000 in paper.
- [SPSE Figshare v1](https://api.figshare.com/v2/articles/12011412) (checked 2026-11-01): CC BY 4.0 deposit; ZIP JSONL counts independently verified. Most parent CIFs identify ICSD origin.

**Reuse and interpretation notes:**

- Do not present every parent crystal or BVSE score as a full first-principles migration-barrier result.
- Most structures derive from ICSD; deposit license does not independently establish redistribution rights to third-party coordinates.
- FP-NEB output count is 49 calculation documents, not established as 49 unique compounds.
- Web workflow requires SPSE account although cited archive is public.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="phononmofdb"></a>
## PhononMOFdb

MACE-MP-MOF0-derived phonon, vibrational thermodynamic and mechanical properties linked to QMOF identifiers.

**Size:** 11,900 MOF thermal-property records (source wording: 11,900).

**Scope:** Unique QMOF-ID YAML files in Thermal.zip, excluding __MACOSX resource-fork files and directory entries

**Release:** Figshare 32050410; Thermal.zip inspected 2026-11-01. **Year:** 2026.

**Provenance:** MLIP-computed. **Structure availability:** `structure_linked`.

**Labels/content:** phonon DOS; phonon band structure; heat capacity; free energy; entropy; bulk modulus; simulated inelastic neutron scattering.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [dataset](https://figshare.com/articles/dataset/PhononMOFdb_Data-driven_Design_of_Metal-Organic_Frameworks/32050410) · [metadata](https://api.figshare.com/v2/articles/32050410) · [paper](https://arxiv.org/abs/2607.18594)

**Evidence:**

- [PhononMOFdb Figshare release metadata](https://api.figshare.com/v2/articles/32050410) (checked 2026-11-01): Describes approximately 12,000 QMOF-ID-labelled MOFs; lists Thermal.zip, DOS_data.zip, INS_spectra.zip, Band_data.zip, DFT_ZIF-8.zip and script.py under CC BY 4.0.
- [PhononMOFdb Thermal.zip payload](https://ndownloader.figshare.com/files/63887643) (checked 2026-11-01): Independently enumerated 11,900 non-resource-fork .yml files with 11,900 unique QMOF IDs. Sample YAML contains temperature, heat_capacity, free_energy, entropy and energy values.
- [Data-driven Design of MOFs with Tunable Negative Thermal Expansion](https://arxiv.org/html/2607.18594v1) (checked 2026-11-01): Methods specify applying MACE-MP-MOF0 v2 to QMOF structures, Phonopy thermal properties, equation-of-state bulk moduli and simulated INS; most corpus properties are model-computed.

**Reuse and interpretation notes:**

- Parent geometries overlap QMOF; this is a new property layer, not 11,900 new experimentally established compounds.
- 11,900 is the exact inspected thermal archive scope; other archives can have different membership and were not exhaustively enumerated.
- Main corpus predictions from an MLIP are distinct from the limited DFT and experimental validation data.

**Tags:** MOF, phonon, heat capacity, INS, MLIP, QMOF, additional-materials-20261101.

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

**Tags:** electronic, band gap, hybrid functional, Scientific Data, ICSD derivative, Scientific-Data-descriptor.

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

<a id="mdr-phonon-pbe-recalculation"></a>
## MDR Phonon PBE

PBE recalculations of the MDR Phonon dataset (https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019), introduced in the paper "Universal Machine Learning Interatomic Potentials are Ready for Phonons".

**Size:** 9,958 reference material phonon files (source wording: 9,958).

**Scope:** 9,958 unique mp-ID YAML.bz2 files counted in public PBE directory on2026-11-01; excludes displaced supercells and parent-directory link.

**Release:** MDR Phonon PBE release as listed in Matbench Discovery at 8869a883a506. **Year:** 2024.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE phonon force constants; phonon dispersions; reference crystal structures.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://alexandria.icams.rub.de/data/phonon_benchmark/pbe) · [data](https://alexandria.icams.rub.de/data/phonon_benchmark/) · [paper](https://doi.org/10.48550/arXiv.2412.16551)

Other denominators (not added to the ranking):

- 9,958 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MDR Phonon PBE: 9,958 configurations/structures; role test, created 2024-12-21, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MDR Phonon PBE entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [PBE recalculation directory of MDR phonons](https://alexandria.icams.rub.de/data/phonon_benchmark/pbe/) (checked 2026-11-01): Directory HTML contains9,958 unique mp-[ID].yaml.bz2 filenames; PFT paper reports9,959. This is a directory metadata recount, not full phonon payload validation.

**Reuse and interpretation notes:**

- Counted 9,958 distinct mp-ID files in the PBE release directory (https://alexandria.icams.rub.de/data/phonon_benchmark/pbe/) on 2026-09-13, one reference material per phonon calculation; the PFT paper reports 9,959. Displaced supercells are not added to this count.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- This is a PBE recalculation of the original MDR cohort, not the original PhononDB release or every displaced force calculation.

**Tags:** Matbench-sets-20261101, MDR Phonon PBE, Matbench Discovery, test, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="pft-mdr-pbe-training"></a>
## PFT MDR-PBE phonon training subset

Subset of the MDR Phonon PBE dataset to be used for phonon fine-tuning, as introduced in "PFT: Phonon Fine-tuning for Machine Learning Interatomic Potentials". This dataset was constructed by randomly sampling 8,510 structures with overlapping mp-id's with MPtrj and preprocessing into .aselmbd files with the Hessian stored in atoms.info["hessian"].

**Size:** 8,510 training materials with Hessians (source wording: 8,510).

**Scope:** 8,510 training materials in the benchmark metadata; validation and1,000-material test set separate. Source dataset is the MDR-PBE recalculation.

**Release:** MDR-MP PBE ω_q release as listed in Matbench Discovery at 8869a883a506. **Year:** 2026.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** reference unit cells; Hessians; phonon frequencies.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://figshare.com/articles/dataset/Preprocessed_data_for_Phonon_Fine-tuning_PFT_/31049869) · [data](https://figshare.com/files/60964675) · [paper](https://arxiv.org/abs/2601.07742)

Other denominators (not added to the ranking):

- 8,510 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MDR-MP PBE ω_q: 8,510 configurations/structures; role training, created 2026-01-08, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MDR-MP PBE ω_q entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [Preprocessed data for Phonon Fine-tuning deposit](https://api.figshare.com/v2/articles/31049869) (checked 2026-11-01): Provider distributes train/validation ASE-LMDB archives with hessian in atoms.info and separate1,000-material test archive; split by mp-ID. Registry reports8,510 training materials.

**Reuse and interpretation notes:**

- Counts 8,510 training materials, each represented by one reference cell and Hessian. The release (https://figshare.com/articles/dataset/Preprocessed_data_for_Phonon_Fine-tuning_PFT_/31049869) splits by mp-ID; validation and the 1,000-material test set are separate.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Subset overlaps the MDR-PBE parent and MPtrj IDs; no additional independent-material total.

**Tags:** Matbench-sets-20261101, MDR-MP PBE ω_q, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="fang-wannier-optical-transport-2025"></a>
## Fang Wannier optical and transport tensors

Structure-resolved optical conductivity, shift-current and electronic transport tensors from Wannier Hamiltonians.

**Size:** 7,301 material entries (source wording: 7,301).

**Scope:** 7,301 entries passing Wannier spread and band interpolation quality criteria.

**Release:** 2025 published release. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** optical conductivity tensor; shift-current tensor; electrical conductivity tensor; electronic thermal conductivity tensor; Seebeck tensor; electronic-only zT; crystal structure.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare data; article has a separate CC BY-NC-ND 4.0 license).

**Official routes:** [homepage](https://doi.org/10.6084/m9.figshare.28689059.v1) · [paper](https://doi.org/10.1038/s41597-025-05396-9) · [download](https://ndownloader.figshare.com/files/54595700)

**Evidence:**

- [Fang et al., Scientific Data 12, 1092](https://www.nature.com/articles/s41597-025-05396-9) (checked 2026-11-01): Describes 7,301 materials with per-material structures, first-principles/Wannier bands, optical tensors at 0–2.5 eV and transport at 100–1000 K.
- [Wannier dataset deposit metadata](https://api.figshare.com/v2/articles/28689059) (checked 2026-11-01): Deposit v1 offers data.zip and explicitly declares CC BY 4.0 for the dataset.

**Reuse and interpretation notes:**

- Transport uses intrinsic Fermi level and constant relaxation time of 10 fs; it does not represent doped optimization.
- Thermal conductivity is electronic only; reported zT excludes lattice conductivity and is not full experimental thermoelectric zT.
- MP source structures overlap the parent database; tensor components/temperature samples are not extra crystals.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="cmr-abse3"></a>
## CMR ABSe3 ternary selenides

Systematic ternary-selenide substitutions in six crystal prototypes for structure and energy prediction.

**Size:** 5,976 ASE calculation/structure rows (source wording: 5,976).

**Scope:** The released abse3.db systems table counted without adding spectra, property columns or functional results as independent materials.

**Release:** Provider ASE database snapshot 2026-11-01. **Year:** 2019.

**Provenance:** DFT / first-principles calculations. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBEsol-relaxed structures; PBE and PBEsol total energies; formation energies; prototype labels.

**Access:** open. **Dataset license:** Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification.

**Official routes:** [homepage](https://cmr.fysik.dtu.dk/abse3/abse3.html) · [download](https://wiki.fysik.dtu.dk/cmr-files/abse3.db)

**Evidence:**

- [CMR ABSe3 ternary selenides provider project page](https://cmr.fysik.dtu.dk/abse3/abse3.html) (checked 2026-11-01): Describes the property campaign and links its named ASE database.
- [CMR ABSe3 ternary selenides downloadable ASE database](https://wiki.fysik.dtu.dk/cmr-files/abse3.db) (checked 2026-11-01): Independently inspected SQLite systems table: 5,976 rows, all with populated positions, cell and atomic-number blobs; payload SHA-256 is preserved in the evidence manifest.
- [CMR repository terms](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): Repository-wide CC BY-SA 4.0 declaration; browser terms differ.
- [CMR ABSe3 ternary selenides browser](https://cmrdb.fysik.dtu.dk/abse3/) (checked 2026-11-01): Public browser provides record-level access; CC BY-NC 4.0 footer differs from the CMR index declaration.

**Reuse and interpretation notes:**

- The count includes structural polymorphs; it is not a unique-composition denominator.
- Atomic coordinate availability was checked in the released ASE database; cross-catalog structural overlap has not been deduplicated.

**Tags:** cmr, electronic-structure, semiconductors, additional-materials-20261101.

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

<a id="cu-dislocation-grain-boundary"></a>
## FCC Cu dislocation–grain-boundary interactions

Atomistic dislocation–grain-boundary interaction outcomes with periodic grain-boundary models and LAMMPS reproduction inputs.

**Size:** 5,234 dislocation–grain-boundary interaction outcomes (source wording: 5,234 interactions across 587 grain-boundary structures).

**Scope:** Final publication and v3 archive; edge, screw and 60-degree mixed dislocations with varied shear stress.

**Release:** Materials Cloud 2025.65, v3, 28 April 2025. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** interaction outcome; applied shear stress; grain-boundary energy; misorientation; atomic structure; LAMMPS inputs.

**Access:** open. **Dataset license:** CC BY 4.0 (provider declaration; metadata addendum also requests CC BY).

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-05256-6) · [data](https://doi.org/10.24435/materialscloud:sy-35) · [homepage](https://archive.materialscloud.org/record/2025.65)

Other denominators (not added to the ranking):

- 587 grain-boundary structures: 73 minimum-energy plus 514 metastable; reused across 5,234 interaction cases

**Evidence:**

- [Scientific Data final descriptor](https://doi.org/10.1038/s41597-025-05256-6) (checked 2026-11-01): Reports 5,234 interaction outcomes for 587 symmetric tilt grain-boundary structures, including 73 minimum-energy and 514 metastable structures; provides LAMMPS templates and GB geometry.
- [Materials Cloud v3 metadata](https://archive.materialscloud.org/api/records/59y2w-rap91) (checked 2026-11-01): Confirms final 5,234/587 counts, a public 6.6 GiB archive and CC BY 4.0 rights.

**Reuse and interpretation notes:**

- Older Materials Cloud 2024.191/v2 describes 5,593 outcomes and 449 GB structures; use final 2025.65/v3 for these counts.
- Interactions are repeated dislocation/stress cases on Cu grain boundaries, not 5,234 unique compositions or bulk compounds.
- Raw MD trajectories are omitted due to size; geometry/templates and outcome tables support reproduction.
- Large ZIP was not downloaded; structural content is established from primary descriptor and release inventory.

**Tags:** Scientific Data, survey:20261101, grain boundaries, dislocations, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mdf-wolverton-oxides"></a>
## Foundry Wolverton oxide perovskite stability and vacancies

Dataset containing DFT-calculated formation energy and convex hull energies of 4914 perovskite oxides

**Size:** 4,914 oxide perovskite records (source wording: 4,914).

**Scope:** Foundry projects.foundry.n_items for wolverton_oxides_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** wolverton_oxides_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** formation energy; energy above hull; oxygen vacancy formation energy; PBE band gap; magnetic moment; lattice parameters.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/wolverton_oxides_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/wolverton_oxides_v1.1/) · [release](https://doi.org/10.18126/h15n-7wu8) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=wolverton_oxides_v1.1) (checked 2026-11-01): Public subject response identifies wolverton_oxides_v1.1, DOI 10.18126/h15n-7wu8, n_items=4,914, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The tabular schema provides composition/site/prototype or lattice descriptors; a complete set of atomic coordinates is not established for this release.

**Tags:** MDF, Foundry, MDF-property-20261101.

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

<a id="zeodiff-diffusion"></a>
## ZeoDiff zeolite diffusion structure-property dataset

Zeolite geometry descriptors and diffusion targets packaged with CIF inputs and a diffusion-prediction application.

**Size:** 4,194 zeolite descriptor/diffusion rows (source wording: 4,194).

**Scope:** Unique first-column zeolite names in Dataset/zeolite_diffusion_dataset.xlsx; excludes header and demonstration predictions

**Release:** Zenodo 18858951 v1.0. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** self-diffusion target; pore-limiting diameter; pore diameter ratio; accessible void fraction; framework density; surface area; channel tortuosity; channel cross-section descriptors.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo archived release metadata).

**Official routes:** [dataset](https://zenodo.org/records/18858951) · [code](https://github.com/WangXiaobao-j/ZeoDiff_HTP/tree/v1.0) · [paper](https://doi.org/10.1038/s41467-026-71698-0)

**Evidence:**

- [ZeoDiff archived release metadata](https://zenodo.org/api/records/18858951) (checked 2026-11-01): Open v1.0 software/data release, CC BY 4.0, with a 14,263,821-byte repository archive.
- [ZeoDiff payload inspection](https://zenodo.org/api/records/18858951/files/WangXiaobao-j/ZeoDiff_HTP-v1.0.zip/content) (checked 2026-11-01): Dataset spreadsheet has 4,194 data rows and 4,194 distinct zeolite names; fields include PLD, PLD/LCD, Vacc, FDSi, ASA, Tort, cross-section statistics and Ds. Dataset/CIF/Zeolites.rar packages coordinates separately.
- [Harnessing confinement effect and interpretable ML to predict alkane diffusion](https://pubmed.ncbi.nlm.nih.gov/42000721/) (checked 2026-11-01): Primary paper abstract describes high-throughput molecular simulations of zeolite frameworks and methane diffusion with transfer to other small molecules. It reports a screening scale of approximately 100,000 frameworks, distinct from the released spreadsheet scope.

**Reuse and interpretation notes:**

- 4,194 is the inspected released descriptor spreadsheet scope, not the approximately 100,000 frameworks screened in the article.
- Spreadsheet target Ds scaling and simulation conditions require consulting the article and inputs before quantitative reuse.
- The separate nested RAR CIF collection was identified but not decompressed here; exact coordinate coverage for every row was not independently verified.
- Original parent framework topology collections overlap IZA and PCOD; new diffusion labels do not constitute new framework topologies.

**Tags:** zeolite, diffusion, methane, molecular dynamics, geometry, additional-materials-20261101.

<a id="wenzhou-te"></a>
## WenzhouTE computed thermoelectric database

Additional transport and thermomechanical calculations on Materials Project structures using deformation-potential transport and an elastic-model lattice conductivity.

**Size:** 3,607 calculated materials (source wording: 3,607).

**Scope:** Provider homepage cohorts: 1,915 class-1 + 1,692 class-2 calculations

**Release:** Provider homepage snapshot checked 2026-11-01. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** Seebeck coefficient (μV/K); electrical conductivity (kS/m in paper tables); electronic / lattice thermal conductivity (W/m/K); dimensionless ZT; carrier concentration (cm⁻³); elastic constants / moduli (GPa); Debye temperature and Grüneisen parameter.

**Access:** open. **Dataset license:** Not verified for database; article CC BY 4.0 does not establish data licensing.

**Official routes:** [homepage](https://hezhu2024.github.io/) · [search](https://hezhu2024.github.io/materials/search.html) · [publication](https://doi.org/10.3390/ma17102200)

**Count derivation:** Sum of disjoint K-means class-1 and class-2 calculated-material cohorts on provider homepage; 1,915 + 1,692 = 3,607.

**Evidence:**

- [WenzhouTE primary provider homepage](https://hezhu2024.github.io/) (checked 2026-11-01): Homepage states 1,915 calculated materials from class 1 and 1,692 from class 2; the sum is 3,607.
- [Wenzhou TE: A First-Principle-Calculated Thermoelectric Materials Database](https://www.mdpi.com/1996-1944/17/10/2200) (checked 2026-11-01): Methods specify PBE/VASP, BoltzTraP2, deformation-potential relaxation times and Slack-formula lattice conductivity; Table 2 labels 300 K transport properties.

**Reuse and interpretation notes:**

- The article reports 1,915 + 1,656 screened materials, while the live homepage reports 1,915 + 1,692. This row uses the homepage snapshot, not the paper total.
- Material identities overlap Materials Project; this is a new property calculation release, not 3,607 novel compounds.
- Lattice conductivity is a Slack-model estimate from elastic properties, not a full anharmonic BTE calculation.
- Carry temperature, carrier concentration, carrier type and approximation with transport values.
- Browser search page loads but a full row export was not audited.

**Tags:** thermoelectric, elastic, model-estimated-ltc, property-focused, OpenAlex-survey-20261101.

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

<a id="c1db"></a>
## Computational 1D Materials Database (C1DB)

Periodic-chain and parent-bulk structures with stability, electronic, magnetic and optical calculations; the current browser also includes machine-generated chains.

**Size:** 3,157 browser database rows (source wording: 3,157).

**Scope:** Total rows displayed by the live browser; includes multiple dimensionality, method and generation variants, not 3,157 unique 1D parent materials.

**Release:** Live browser snapshot 2026-11-01; original project 2022. **Year:** 2022.

**Provenance:** DFT, exfoliated experimental-parent crystals and machine-generated chains. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; energies and stability; band structures and gaps; magnetic and optical properties.

**Access:** open. **Dataset license:** Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification.

**Official routes:** [homepage](https://cmr.fysik.dtu.dk/c1db/c1db.html) · [browse](https://cmrdb.fysik.dtu.dk/c1db/) · [paper](https://doi.org/10.1103/PhysRevMaterials.6.064202)

**Evidence:**

- [C1DB project description](https://cmr.fysik.dtu.dk/c1db/c1db.html) (checked 2026-11-01): Describes bulk and isolated-chain calculations, GPAW workflows, functional and dimensionality keys.
- [C1DB live browser](https://cmrdb.fysik.dtu.dk/c1db/) (checked 2026-11-01): Displays 3,144 found rows out of 3,157 total and exposes dimension/method/source filters; footer says CC BY-NC 4.0.
- [C1DB representative public CIF](https://cmrdb.fysik.dtu.dk/c1db/material/ZrSe4Hf5Br10-6b6280765d7f/download/cif) (checked 2026-11-01): Public response includes unit cell and fractional atomic coordinates for a generated 1D chain.
- [CMR repository terms](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): Index declares all CMR databases CC BY-SA 4.0; this conflicts with the browser footer.

**Reuse and interpretation notes:**

- The original paper denominator of 820 1D materials must not be substituted for the expanded live row count.
- The browser found 3,144 rows out of 3,157; the completeness of the remaining rows is not established.
- The project download link c1db.db returned 404, while per-material CIF retrieval worked.
- The catalog has no dedicated 1D category, so this release is placed under computed-property datasets.

**Tags:** one-dimensional, low-dimensional, chains, electronic-structure, magnetism, additional-materials-20261101.

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

<a id="mdf-perovskite-opband"></a>
## Foundry perovskite O p-band centers

Dataset containing DFT-calculated O p-band center energies for 2912 perovskite oxides

**Size:** 2,912 perovskite composition records (source wording: 2,912).

**Scope:** Foundry projects.foundry.n_items for perovskite_opbandcenter_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** perovskite_opbandcenter_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** O p-band center; GGA; GGA+U; sublattice composition.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/perovskite_opbandcenter_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/perovskite_opbandcenter_v1.1/) · [release](https://doi.org/10.18126/f3p0-2c5f) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=perovskite_opbandcenter_v1.1) (checked 2026-11-01): Public subject response identifies perovskite_opbandcenter_v1.1, DOI 10.18126/f3p0-2c5f, n_items=2,912, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The tabular schema provides composition/site/prototype or lattice descriptors; a complete set of atomic coordinates is not established for this release.
- O p-band center values are referenced to the Fermi level and distinguish GGA from GGA+U.

**Tags:** MDF, Foundry, MDF-property-20261101.

<a id="mdf-semiconductor-defectlevels"></a>
## Foundry semiconductor impurity charge-state transitions

Dataset containing DFT-calculated defect charge state transition levels of 2910 semiconductor-impurity pairs

**Size:** 2,910 semiconductor-impurity records (source wording: 2,910).

**Scope:** Foundry projects.foundry.n_items for semiconductor_defectlevels_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** semiconductor_defectlevels_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** PBE charge-transition level; HSE charge-transition level; band alignment; host composition; impurity site; charge states.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/semiconductor_defectlevels_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/semiconductor_defectlevels_v1.1/) · [release](https://doi.org/10.18126/ite0-3iah) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=semiconductor_defectlevels_v1.1) (checked 2026-11-01): Public subject response identifies semiconductor_defectlevels_v1.1, DOI 10.18126/ite0-3iah, n_items=2,910, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The tabular schema provides composition/site/prototype or lattice descriptors; a complete set of atomic coordinates is not established for this release.
- The denominator is semiconductor-impurity records with charge-transition descriptors, not 2,910 unique semiconductor host structures.

**Tags:** MDF, Foundry, MDF-property-20261101.

<a id="oqmd-oxygen-vacancy-sites-2023"></a>
## OQMD-derived oxygen-vacancy formation energies

Site-resolved computed oxygen-vacancy energies and descriptors for oxide materials, indexed to OQMD pristine and defect entries.

**Size:** 2,677 oxygen-site property rows (source wording: 2,677).

**Scope:** Exact parsed Data.csv row count, excluding its header. Removing _v site suffixes gives 1,157 distinct pristine OQMD IDs.

**Release:** Zenodo v1, DOI 10.5281/zenodo.10028980. **Year:** 2023.

**Provenance:** Baldassarri–He–Wolverton high-throughput vacancy calculations on OQMD oxide hosts. **Structure availability:** `structure_linked`.

**Labels/content:** oxygen vacancy formation energy; OQMD pristine and defect identifiers; band gap; stability; site and composition descriptors.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo record metadata).

**Official routes:** [Release](https://zenodo.org/records/10028980) · [Paper](https://doi.org/10.1021/acs.chemmater.3c02251)

Other denominators (not added to the ranking):

- 1,157 pristine OQMD parent IDs: Distinct OQMD_ID_pristine values after stripping _v site suffix

**Evidence:**

- [Zenodo oxygen-vacancy release metadata](https://zenodo.org/api/records/10028980) (checked 2026-11-01): Open dataset with explicit cc-by-4.0 licence; Data.csv, Readme and example model code are distributed.
- [Released Data.csv](https://zenodo.org/records/10028980/files/Data.csv?download=1) (checked 2026-11-01): Parsed 2,677 data rows and 1,157 distinct parent IDs after removing _v site suffixes. Columns include OQMD_ID_defect and evf.

**Reuse and interpretation notes:**

- CSV provides structure identifiers and descriptors rather than self-contained coordinates.
- Do not interpret 2,677 as the number of distinct pristine materials.
- OQMD parent lineage is shared, but the released site-resolved vacancy labels are a distinct calculation corpus.

**Tags:** oxygen-vacancies, oxides, OQMD, redox, additional-materials-20261101.

<a id="jarvis-ff"></a>
## JARVIS-FF classical force-field calculations

Periodic-material calculations with multiple classical interatomic potentials.

**Size:** 2,538 force-field calculation records (source wording: 2,538).

**Scope:** Selected jff release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS jff documentation / pinned downloader snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; classical force field; energy; elastic properties.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare deposit).

**Official routes:** [homepage](https://jarvis.nist.gov/jarvisff) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://ndownloader.figshare.com/files/28937793) · [release](https://doi.org/10.6084/m9.figshare.14213522)

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named jff row reports 2,538 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the jff route or dedicated helper and the raw-file grouping.
- [Figshare release metadata](https://api.figshare.com/v2/articles/14213522) (checked 2026-11-01): Identifies the deposited files and reports the CC BY 4.0 dataset license.

**Reuse and interpretation notes:**

- Calculation records can repeat a material under different force fields; 2,538 is not asserted to be a deduplicated composition count.
- The web portal may require registration; the linked public file route is separate.

**Tags:** JARVIS, jff, release-snapshot.

<a id="superband"></a>
## SuperBand electronic-band / superconductivity dataset

DFT electronic bands, DOS and Fermi-surface representations linked to experimental superconducting-transition labels and crystal geometry.

**Size:** 2,474 materials (source wording: 1,362 superconductors plus 1,112 paper-designated nonsuperconductor entries = 2,474 band-data entries).

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
- The 1,112 negative labels are the paper’s designation, not an independent negative-experiment audit here. Review inherited SuperCon/3DSC missing-Tc conventions before treating zeros as confirmed negatives.

**Tags:** superconductivity, electronic, mixed provenance, Scientific Data, superconductor, superconductors, Scientific-Data-descriptor.

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

**Tags:** phonon, DFPT, MP derivative, Scientific Data, Scientific-Data-descriptor.

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

**Tags:** bonding, LOBSTER, Scientific-Data, collection-blaiszik, Scientific-Data-descriptor.

<a id="jarvis-wtbh-electron"></a>
## JARVIS-WTBH electron Hamiltonians

Electron Wannier Hamiltonian subset accessed through the raw-file index and dedicated helper.

**Size:** 1,440 electron Hamiltonian entries (source wording: 1,440).

**Scope:** Selected wtbh_electron release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS wtbh_electron documentation / pinned downloader snapshot 2026-11-01. **Year:** 2021.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** Wannier tight-binding Hamiltonian; spin-orbit coupling; electronic structure.

**Access:** open. **Dataset license:** Not verified for selected 1,440-entry index snapshot; original four-part Figshare Hamiltonian collection declares CC BY 4.0.

**Official routes:** [homepage](https://jarvis.nist.gov/jarviswtb) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://ndownloader.figshare.com/files/25295732) · [paper](https://doi.org/10.1038/s41597-021-00885-z) · [original_release](https://doi.org/10.6084/m9.figshare.c.5192276.v2)

Other denominators (not added to the ranking):

- 1,771 materials: 2021 publication cohort: 1,406 3D plus 365 2D; different from selected 1,440-entry documentation snapshot
- 1,772 unique material zip archives: Current four-part original Figshare collection inventory; 1,407 3D plus 365 2D

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named wtbh_electron row reports 1,440 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the wtbh_electron route or dedicated helper and the raw-file grouping.
- [Scientific Data electron-Wannier descriptor](https://doi.org/10.1038/s41597-021-00885-z) (checked 2026-11-01): Original article reports 1,771 materials: 1,406 3D and 365 2D. It describes archived Wannier90 input/output and Hamiltonian files and DFT-vs-Wannier comparison data.
- [Original Figshare Hamiltonian collection](https://api.figshare.com/v2/collections/5192276/articles) (checked 2026-11-01): Four listed partitions were inspected through their individual public metadata: all declare CC BY 4.0, and together they currently list 1,772 unique JVASP-*.zip files, including 365 2D archives.

**Reuse and interpretation notes:**

- Use get_wann_electron(jid=...) and the WANN raw-file group; wtbh_electron is not a current data(name) registry key. Homepage WannierTB total 1,771 has different scope.
- The web portal may require registration; the linked public file route is separate.
- The selected downloader/documentation snapshot count of 1,440 is preserved. Original 2021 paper count 1,771 and present original-collection inventory count 1,772 have different scope/version and must not replace it silently.
- The inspected original collection has 1,407 3D zip archives and 365 2D zip archives; the one-archive difference from the publication remains unexplained.

**Tags:** JARVIS, wtbh_electron, release-snapshot, Scientific-Data-descriptor.

<a id="cmr-a2bcx4"></a>
## CMR A2BCX4 quaternary chalcogenides

Six-phase screening of quaternary chalcogenides for larger-band-gap tandem photoelectrochemical absorbers.

**Size:** 1,368 ASE calculation/structure rows (source wording: 1,368).

**Scope:** The released a2bcx4.db systems table counted without adding spectra, property columns or functional results as independent materials.

**Release:** Provider ASE database snapshot 2026-11-01. **Year:** 2018.

**Provenance:** DFT / first-principles calculations. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; GLLB-SC band gaps; mBEEF energies and uncertainty; crystal prototypes.

**Access:** open. **Dataset license:** Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification.

**Official routes:** [homepage](https://cmr.fysik.dtu.dk/a2bcx4/a2bcx4.html) · [download](https://wiki.fysik.dtu.dk/cmr-files/a2bcx4.db)

**Evidence:**

- [CMR A2BCX4 quaternary chalcogenides provider project page](https://cmr.fysik.dtu.dk/a2bcx4/a2bcx4.html) (checked 2026-11-01): Describes the property campaign and links its named ASE database.
- [CMR A2BCX4 quaternary chalcogenides downloadable ASE database](https://wiki.fysik.dtu.dk/cmr-files/a2bcx4.db) (checked 2026-11-01): Independently inspected SQLite systems table: 1,368 rows, all with populated positions, cell and atomic-number blobs; payload SHA-256 is preserved in the evidence manifest.
- [CMR repository terms](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): Repository-wide CC BY-SA 4.0 declaration; browser terms differ.
- [CMR A2BCX4 quaternary chalcogenides browser](https://cmrdb.fysik.dtu.dk/a2bcx4/) (checked 2026-11-01): Public browser provides record-level access; CC BY-NC 4.0 footer differs from the CMR index declaration.

**Reuse and interpretation notes:**

- Different structural prototypes for the same chemistry are separate rows.
- Atomic coordinate availability was checked in the released ASE database; cross-catalog structural overlap has not been deduplicated.

**Tags:** cmr, electronic-structure, semiconductors, additional-materials-20261101.

<a id="mdf-double-perovskite-bandgaps"></a>
## Foundry double-perovskite oxide band gaps

Dataset containing DFT-calculated band gaps of 1306 double perovskite oxide materials

**Size:** 1,306 double-perovskite composition records (source wording: 1,306).

**Scope:** Foundry projects.foundry.n_items for double_perovskite_bandgap_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** double_perovskite_bandgap_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** GLLB-SC band gap; sublattice composition.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/double_perovskite_bandgap_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/double_perovskite_bandgap_v1.1/) · [release](https://doi.org/10.18126/lss6-o5x4) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=double_perovskite_bandgap_v1.1) (checked 2026-11-01): Public subject response identifies double_perovskite_bandgap_v1.1, DOI 10.18126/lss6-o5x4, n_items=1,306, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The tabular schema provides composition/site/prototype or lattice descriptors; a complete set of atomic coordinates is not established for this release.

**Tags:** MDF, Foundry, MDF-property-20261101.

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

**Tags:** elasticity, MP derivative, Scientific Data, Scientific-Data-descriptor.

<a id="mdf-heusler-magnetization"></a>
## Foundry / University of Alabama Heusler magnetization

Dataset containing saturation magnetization values of 1153 Heusler compounds

**Size:** 1,153 Heusler compound records (source wording: 1,153).

**Scope:** Foundry projects.foundry.n_items for heusler_magnetization_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** heusler_magnetization_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `composition_only`.

**Labels/content:** magnetic moment; saturation magnetization; formation energy; Fermi-level spin polarization; lattice parameters.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/heusler_magnetization_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/heusler_magnetization_v1.1/) · [release](https://doi.org/10.18126/un63-ohqv) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=heusler_magnetization_v1.1) (checked 2026-11-01): Public subject response identifies heusler_magnetization_v1.1, DOI 10.18126/un63-ohqv, n_items=1,153, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.
- [Matminer official dataset reference: Heusler magnetic properties](https://hackingmaterials.lbl.gov/matminer/dataset_summary.html#heusler-magnetic) (checked 2026-11-01): Describes 1,153 Heusler alloys with DFT-calculated magnetic/electronic properties and identifies the University of Alabama Heusler database source lineage.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The tabular schema provides composition/site/prototype or lattice descriptors; a complete set of atomic coordinates is not established for this release.
- Magnetic-moment and saturation-magnetization targets have different units (Bohr magneton versus emu/cc); they are not interchangeable.

**Tags:** MDF, Foundry, MDF-property-20261101.

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

**Tags:** dielectric, optical, MP derivative, Scientific Data, Scientific-Data-descriptor.

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

**Tags:** piezoelectric, MP derivative, Scientific Data, Scientific-Data-descriptor.

<a id="kumagai-oxygen-vacancies"></a>
## Kumagai oxygen-vacancy database

Charged oxygen-vacancy calculations in nonmagnetic insulating oxides, with defect geometry, formation energies and electronic information.

**Size:** 937 oxide hosts (source wording: 937).

**Scope:** Paper analyzes 937 oxide hosts, with inequivalent oxygen sites and three charge states. Host count is used instead of the approximate total defect calculations.

**Release:** 2021 paper cohort; repository master e310353ecbf698499c85a5ec5416b76e82dcecfd. **Year:** 2021.

**Provenance:** New PBEsol(+U) and non-self-consistent dielectric-dependent hybrid calculations; hosts selected from Materials Project. **Structure availability:** `periodic_atomic`.

**Labels/content:** defect formation energies; charge transition levels; vacancy structures; band structures; dielectric constants.

**Access:** open. **Dataset license:** CC BY 4.0 explicitly for all data in the author repository.

**Official routes:** [Release](https://github.com/kumagai-group/oxygen_vacancies_db) · [Paper](https://doi.org/10.1103/PhysRevMaterials.5.123803)

Other denominators (not added to the ranking):

- 5,047 filtered ML rows: Sum of charge0.csv (1745), charge1.csv (1689), charge2.csv (1613); overlapping hosts and sites

**Evidence:**

- [Oxygen vacancy database author release](https://github.com/kumagai-group/oxygen_vacancies_db) (checked 2026-11-01): README explicitly licenses all data CC BY 4.0; archive contains CIF supercells and defect results including relaxed CONTCAR geometry.
- [Insights into oxygen vacancies from high-throughput first-principles calculations](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.5.123803) (checked 2026-11-01): Primary paper reports 937 oxides and approximately 6,000 vacancy calculations across three charge states.

**Reuse and interpretation notes:**

- Released machine-learning CSVs have 1,745 neutral, 1,689 singly charged and 1,613 doubly charged rows; these filtered subsets are not the full calculation population.
- Distinct from Foundry Wolverton ABO3 vacancy data and JARVIS vacancy release.
- Later ML_charged_defects reuse of this oxygen corpus should not be added independently without new-data verification.

**Tags:** oxygen-vacancies, charged-defects, oxides, redox, additional-materials-20261101.

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

<a id="ternary-fluoride-electrode-pairs"></a>
## Ternary fluoride-ion battery electrode reaction pairs

Computed electrode reaction-pair properties including voltage, capacity, energy density and structural parent identifiers.

**Size:** 807 fluorinated/defluorinated reaction pairs (source wording: 807 reaction pairs; overlapping 168 direct-reaction subset).

**Scope:** All-pairs CSV; direct-reaction CSV is an overlapping subset, not additional materials.

**Release:** 2023 Figshare collection v1. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** voltage; gravimetric capacity; gravimetric energy density; volumetric energy density; volume expansion; diffusion barriers when available; space group; Materials Project IDs.

**Access:** open. **Dataset license:** CC0 (Figshare data-file metadata).

**Official routes:** [homepage](https://github.com/donmctaggart15/ternary_f_cathodes) · [data](https://doi.org/10.6084/m9.figshare.c.6231423.v1) · [paper](https://doi.org/10.1038/s41597-023-01954-1)

Other denominators (not added to the ranking):

- 168 direct-reaction pairs: Overlapping subset of the 807 all-pairs records

**Evidence:**

- [Primary data descriptor](https://www.nature.com/articles/s41597-023-01954-1) (checked 2026-11-01): Data Records specifies 807 all-reaction pairs and 168 direct pairs, with code and data on GitHub and Figshare.
- [Direct and indirect reaction data](https://api.figshare.com/v2/articles/21273111) (checked 2026-11-01): Metadata lists CSV columns for voltage, capacities, energy densities, MP IDs, space groups and barriers, with CC0 licence.

**Reuse and interpretation notes:**

- Counts are reaction pairs, not unique crystal materials.
- Properties derive from DFT energies and transformations of upstream Simmate/Materials Project records.
- Diffusion barriers are only included where available; release includes a few four/five-element pairs despite ternary label.
- Economic estimates are historical study inputs, not current prices.

**Tags:** battery-electrodes, fluoride-ion, voltage, Materials-Project-derivative, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="migration-barriers-literature-2025"></a>
## Literature-derived battery ionic migration barriers

Curated DFT-NEB barriers with periodic initial/final migration configurations, calculation metadata and source citations.

**Size:** 621 ionic migration pathways (source wording: 621 archived migration-barrier entries).

**Scope:** Zenodo JSON file independently counted; publication reports 443 compositions and 27 structural groups.

**Release:** Zenodo 17240095 archive; publication release. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** DFT-NEB migration barrier; initial and final periodic structures; chemical formula; space group; exchange-correlation functional; calculation metadata; literature BibTeX.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/sai-mat-group/migration-barrier-dataset) · [data](https://doi.org/10.5281/zenodo.17240095) · [paper](https://doi.org/10.1038/s41597-025-06196-x)

**Evidence:**

- [Migration-barrier data descriptor](https://www.nature.com/articles/s41597-025-06196-x?error=cookies_not_supported) (checked 2026-11-01): Reports 621 DFT-NEB barriers across 443 compositions and 27 structural groups, with initial/final configurations.
- [Versioned migration-barrier archive](https://zenodo.org/api/records/17240095) (checked 2026-11-01): Metadata lists CC BY 4.0 and a 9,108,391-byte JSON payload; downloaded checksum md5:878646be7126dd30175576a494b726b4 matches and array contains 621 entries.
- [Live repository snapshot](https://github.com/sai-mat-group/migration-barrier-dataset) (checked 2026-11-01): Public EM-COMPLETE-DATASET.json independently contains 619 entries, distinct from the 621-entry archived release.

**Reuse and interpretation notes:**

- The live GitHub and 2026 learning-paper subset contain 619 entries; retain the archive/version when reproducing 621.
- 621 pathways are not 621 unique materials; several systems have multiple migration paths.
- Barriers are literature DFT-NEB values across different functionals and calculation settings, not measured activation energies.
- Some endpoint structures were reconstructed or relaxed rather than copied from the original migration calculation.

**Tags:** ionic-transport, migration-barriers, NEB, battery-electrodes, solid-electrolytes, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="compsc-literature-epc"></a>
## CompSC literature-curated conventional-superconductor structures and EPC parameters

Literature-computed electron–phonon parameters linked to atomic structures curated by Tran and Vu for conventional-superconductor machine learning. The public corrected release contains periodic structures and pressure-dependent targets.

**Size:** 586 crystal structures (source wording: 586 atomic structures; 583 values of lambda and 566 values of omega_log after August 2024 duplicate removal).

**Scope:** Corrected CompSC/202305 public CSV and poscar.tgz at pinned repository revision; 586 rows and 586 regular POSCAR files, including multiple pressures/structures for a composition.

**Release:** May 2023 dataset; duplicate removed August 2024; repository revision ec5411ca41a0726cad01324609ed34940c9e20ab. **Year:** 2023.

**Provenance:** literature. **Structure availability:** `periodic_atomic`.

**Labels/content:** electron–phonon coupling lambda (literature-computed); logarithmic phonon frequency omega_log (literature-computed); pressure; lattice parameters; atomic species and fractional coordinates; literature references.

**Access:** open. **Dataset license:** Not verified; no repository license file or data license statement found..

**Official routes:** [homepage](https://github.com/huantd/matsdata/tree/main/CompSC/202305) · [data](https://raw.githubusercontent.com/huantd/matsdata/ec5411ca41a0726cad01324609ed34940c9e20ab/CompSC/202305/poscar.tgz) · [paper](https://doi.org/10.1103/PhysRevMaterials.7.054805) · [code](https://github.com/huantd/matsdata)

Other denominators (not added to the ranking):

- 583 numeric lambda records: corrected 586-row CSV
- 566 numeric omega_log records: corrected 586-row CSV

**Evidence:**

- [CompSC author README, corrected release](https://raw.githubusercontent.com/huantd/matsdata/ec5411ca41a0726cad01324609ed34940c9e20ab/CompSC/202305/README) (checked 2026-11-01): Author documents original 587 structures and the August 2024 duplicate removal, leaving 586 structures, 583 lambda values and 566 omega_log values.
- [CompSC released CSV](https://raw.githubusercontent.com/huantd/matsdata/ec5411ca41a0726cad01324609ed34940c9e20ab/CompSC/202305/supercond_May23.csv) (checked 2026-11-01): Direct parse: 586 rows with 272 distinct composition strings; 583 numeric Lambda values and 566 numeric omlog values. 584 pressures parse numerically, spanning 0–800; two pressure cells contain filename-like strings.
- [CompSC released periodic structures](https://raw.githubusercontent.com/huantd/matsdata/ec5411ca41a0726cad01324609ed34940c9e20ab/CompSC/202305/poscar.tgz) (checked 2026-11-01): In-memory archive listing contains exactly 586 regular files named struct-*.vasp; no extraction needed.
- [Machine-learning approach for discovery of conventional superconductors](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.7.054805) (checked 2026-11-01): Tran and Vu, Physical Review Materials 7, 054805 (31 May 2023): predicts lambda and omega_log from structures; Tc is computed afterward rather than supplied as experimental ground truth.

**Reuse and interpretation notes:**

- Targets are literature-computed EPC parameters, not experimental Tc measurements; composition repeats across pressure and structural cases.
- The 2024 ACS review reports the earlier 587-structure cohort; the public corrected denominator is 586.
- The pressure column has two nonnumeric cells (IDs 567 and 568: 270Pa.vasp and 300Pa.vasp). Numeric values reach 800; do not impose the review’s historical up-to-500-GPa description on the released file.
- Missing lambda and omega_log labels are distinct from zero. A downstream Tc estimate requires a specified formula and Coulomb pseudopotential.
- Public downloading does not establish redistribution rights.

**Tags:** superconductivity, electron-phonon, EPC, high-pressure, hydrides, literature-curated, POSCAR, CompSC, superconductor, superconductors.

<a id="trinquet-shg-2024"></a>
## Trinquet nonlinear-optical SHG tensor dataset

Static second-harmonic generation and electronic dielectric tensors computed for inorganic semiconductor crystals.

**Size:** 579 inorganic semiconductor structures (source wording: 579).

**Scope:** 579 noncentrosymmetric inorganic semiconductors in the released computed database.

**Release:** 2024 published release. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** static SHG tensor (pm/V); electronic dielectric tensor; band gap; crystal structure.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://archive.materialscloud.org/records/004k3-s0p94) · [paper](https://doi.org/10.1038/s41597-024-03590-9) · [download](https://doi.org/10.24435/materialscloud:w5-d6) · [api](https://contribs.materialsproject.org/projects/shg)

**Evidence:**

- [Materials Cloud 2024.87](https://archive.materialscloud.org/records/004k3-s0p94) (checked 2026-11-01): Open CC BY 4.0 record supplies nlodb.json, README and rotation code for 579 inorganic semiconductors.
- [Trinquet et al., Scientific Data 11, 757](https://www.nature.com/articles/s41597-024-03590-9) (checked 2026-11-01): ABINIT LDA/DFPT static conventional SHG and electronic dielectric tensors; MPContribs supplies associated pymatgen Structure.

**Reuse and interpretation notes:**

- Static electronic response excludes frequency dispersion and ionic contributions.
- LDA band gap errors can inflate SHG components; ranking does not prove device performance.
- The same dataset is mirrored at Materials Cloud, UCLouvain Dataverse and MPContribs; count once.
- Parent structures overlap MP and earlier optical semiconductor cohorts.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="jarvis-vacancydb"></a>
## JARVIS vacancy formation-energy release

Paired bulk and defective crystal structures with vacancy-energy labels.

**Size:** 464 defect calculation records (source wording: 464).

**Scope:** Selected vacancydb release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS vacancydb documentation / pinned downloader snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** bulk structure; defective structure; vacancy formation energy; chemical potential.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare deposit).

**Official routes:** [homepage](https://pages.nist.gov/jarvis/databases/) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://figshare.com/ndownloader/files/40750811) · [release](https://doi.org/10.6084/m9.figshare.23000573)

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named vacancydb row reports 464 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the vacancydb route or dedicated helper and the raw-file grouping.
- [Figshare release metadata](https://api.figshare.com/v2/articles/23000573) (checked 2026-11-01): Identifies the deposited files and reports the CC BY 4.0 dataset license.
- [Independent small-archive row count](https://figshare.com/ndownloader/files/40750811) (checked 2026-11-01): Complete ZIP archive parsed locally on 2026-11-01: 464 JSON records. Hash and record-key receipt: research/provenance/optimade_discovery_20261101.json.

**Reuse and interpretation notes:**

- This is the downloader-selected 40750811 archive, not a recount of newer files listed on the deposit page.
- The web portal may require registration; the linked public file route is separate.

**Tags:** JARVIS, vacancydb, release-snapshot.

<a id="ricci-polar-ferroelectrics-2024"></a>
## Ricci polar-material ferroelectric screening dataset

Pseudosymmetry-generated nonpolar references and DFT polarization screening of polar Materials Project compounds.

**Size:** 447 polar materials with computed polarization (source wording: 447).

**Scope:** Paper reports polarization calculations for 447 polar materials; 1,978 initial structures were screened and a ranked subset contains 182 potential ferroelectrics.

**Release:** 2024 published release. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** polarization (µC/cm²); polar–nonpolar energy difference (meV/atom); screening tier; synthesizability score; phonon assessment.

**Access:** open. **Dataset license:** CC BY 4.0 (paper and its supplementary tables).

**Official routes:** [homepage](https://www.nature.com/articles/s41524-023-01193-3) · [paper](https://doi.org/10.1038/s41524-023-01193-3)

**Evidence:**

- [Ricci et al., Candidate ferroelectrics via ab initio high-throughput screening of polar materials](https://www.nature.com/articles/s41524-023-01193-3) (checked 2026-11-01): Full paper states polarization calculated for 447 materials; data availability identifies manuscript and supplementary tables, and says future MP/API availability.

**Reuse and interpretation notes:**

- Data release is manuscript/supplementary tables; current Materials Project API coverage was not verified.
- Structure-linked through parent MP records; standalone atomic coordinate archive not verified.
- 182 ranked candidates use ΔE of 1–200 meV/atom and polarization above 10 µC/cm²; initial-screen denominator 1,978 is not a count of successful polarization labels.
- Overlaps the Smidt search and Materials Project; do not add counts as independent crystals.

**Tags:** property-focused, OpenAlex-survey-20261101.

<a id="predicted-high-dielectric-oxides"></a>
## Predicted high-dielectric ternary oxide structures

441 low-energy ternary oxide candidates with dielectric tensors; 33 high-performance candidates are a selected subset.

**Size:** 441 computed ternary-oxide structures (source wording: 441).

**Scope:** 441 low-energy ternary oxide candidates with dielectric tensors; 33 high-performance candidates are a selected subset.

**Release:** Figshare 10482707 v2; 441-entry JSON. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** electronic/ionic/total dielectric tensors; polycrystalline dielectric constant; band gap (eV); energy above hull; periodic atomic structure.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-020-0418-6) · [data](https://doi.org/10.6084/m9.figshare.10482707.v2) · [archive](https://doi.org/10.24435/materialscloud:2020.0010/v1)

**Evidence:**

- [High dielectric ternary oxides from crystal structure prediction and high-throughput screening](https://www.nature.com/articles/s41597-020-0418-6) (checked 2026-11-01): Paper combines crystal structure prediction and DFPT; Data Records lists tensor/property keys and calculation metadata.
- [Predicted dielectric data deposit](https://api.figshare.com/v2/articles/10482707) (checked 2026-11-01): CC BY 4.0; downloaded JSON independently has 441 entries, each with embedded POSCAR data.

**Reuse and interpretation notes:**

- Computed screening candidates are not experimentally validated dielectrics or proven stable at operating conditions.
- 33 is a subset, not an additional release population.
- May overlap source crystal prototypes/MP records; parent-database novelty not independently audited.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** education, diffusion, derived, composition-only, Scientific-Data-descriptor.

<a id="uw-cmg-dilute-solute-diffusion"></a>
## UW CMG dilute-solute diffusion database

DFT vacancy-mediated solute diffusion coefficients, activation barriers and attempt frequencies across metallic crystal hosts.

**Size:** ≥400 host-solute diffusion systems (source wording: more than 400 host–solute systems).

**Scope:** Expanded Figshare release across FCC/BCC/HCP hosts; original 2016 article described more than 230 systems.

**Release:** Figshare v10 expanded release. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** Arrhenius diffusion prefactor; diffusion activation energy; jump barriers; attempt frequencies; host crystal type.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://matmodapp.engr.wisc.edu/https-only/dsd_calculated/cmg_dilute_solute_diffusion_main.php) · [data](https://doi.org/10.6084/m9.figshare.1546772.v10) · [paper](https://doi.org/10.1038/sdata.2016.54)

**Evidence:**

- [Expanded author diffusion release](https://api.figshare.com/v2/articles/1546772) (checked 2026-11-01): v10 describes more than 400 systems in 15 metallic hosts and provides a DFT diffusivity workbook plus experimental comparison data; metadata licence CC BY 4.0.
- [UW CMG provider table](https://matmodapp.engr.wisc.edu/https-only/dsd_calculated/cmg_dilute_solute_diffusion_main.php) (checked 2026-11-01): Provider gives Arrhenius parameters for vacancy-mediated diffusion and distinguishes paramagnetic BCC Fe treatment.

**Reuse and interpretation notes:**

- Host-solute systems and directional coefficients are not distinct bulk crystal counts.
- Uses vacancy-mediated models and host self-diffusion corrections; do not treat as direct measured diffusivity.
- Expanded release overlaps the original six-host paper and existing MAST-ML educational slice; do not sum them.
- Atomic-coordinate package was not verified for this table.

**Tags:** diffusion, metals, Arrhenius, DFT, overlap:mastml-dilute-diffusion-education, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="smidt-ferroelectric-2020"></a>
## Smidt first-principles ferroelectric candidate database

Symmetry-paired polar and nonpolar structures with computed polarization paths and electronic properties.

**Size:** 255 completed polar–nonpolar structure pairs (source wording: 255).

**Scope:** 255 completed candidate workflows; 200 pass the paper’s high-quality assessment and 126 are newly proposed within that subset.

**Release:** 2020 published release. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** spontaneous polarization (µC/cm²); polarization path; band gap (eV); relative energy; atomic structures.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://blondegeek.github.io/ferroelectric_search_site/) · [paper](https://doi.org/10.1038/s41597-020-0407-9) · [download](https://doi.org/10.6084/m9.figshare.6025634.v4) · [repository](https://github.com/blondegeek/ferroelectric_search_site)

**Evidence:**

- [Smidt et al., Scientific Data 7, 72](https://www.nature.com/articles/s41597-020-0407-9) (checked 2026-11-01): Paper reports 255 successfully completed pairs after screening over 67,000 MP materials; provides atomic structures, VASP files, polarization and energies.
- [Ferroelectric data deposit metadata](https://api.figshare.com/v2/articles/6025634) (checked 2026-11-01): Version 4 provides distortions.json.gz, workflow_data.json.gz and per-workflow VASP archives under CC BY 4.0.

**Reuse and interpretation notes:**

- Candidate ferroelectricity is a computational designation; it does not establish experimental switching.
- Overlaps Materials Project structures; the 255 pairs are not 510 unique materials.
- The paper’s metadata-only Figshare record 11702073 is distinct from the actual data deposit.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="porous-heat-capacity-2022"></a>
## Nanoporous-material heat-capacity DFT and prediction dataset

DFT heat capacities and local atomic contributions for MOFs, COFs and zeolites, with larger model-predicted heat-capacity tables.

**Size:** 232 DFT-labelled parent structures (source wording: 232).

**Scope:** Rows excluding header in DFT/DFT_cp_allstructures.csv inside database_heat_capacity.zip

**Release:** Materials Cloud 2022.53 v1. **Year:** 2022.

**Provenance:** computed and model-predicted. **Structure availability:** `periodic_atomic`.

**Labels/content:** DFT heat capacity; site-projected heat capacity; model-predicted heat capacity; prediction uncertainty; crystal structure; phonon calculation outputs.

**Access:** open. **Dataset license:** CC BY 4.0 (Materials Cloud dataset metadata).

**Official routes:** [dataset](https://archive.materialscloud.org/records/7p3z3-t3q91) · [metadata](https://archive.materialscloud.org/api/records/7p3z3-t3q91) · [paper](https://doi.org/10.1038/s41563-022-01374-3) · [experimental_companion](https://zenodo.org/records/7215247)

Other denominators (not added to the ranking):

- 31,420 model-predicted parent-database rows: Sum of five ML table row counts; not deduplicated across parent collections
- 17,619 site-projected DFT heat-capacity rows: Atomic-site contributions, distinct from parent structures

**Evidence:**

- [Nanoporous heat-capacity release metadata](https://archive.materialscloud.org/api/records/7p3z3-t3q91) (checked 2026-11-01): Release files include DFT_calculations.zip, ML.zip and database_heat_capacity.zip; dataset rights are explicitly CC BY 4.0.
- [Provider file descriptions](https://archive.materialscloud.org/api/records/7p3z3-t3q91/files/files_description.md/content) (checked 2026-11-01): States DFT_calculations.zip contains heat capacity, crystal structure and phonon outputs for MOFs/COFs/zeolites; larger tables cover 250–400 K in parent databases.
- [Heat-capacity table payload inspection](https://archive.materialscloud.org/api/records/7p3z3-t3q91/files/database_heat_capacity.zip/content) (checked 2026-11-01): DFT_cp_allstructures.csv has 232 data rows; DFT_site_projected_cp.csv 17,619 rows. Model tables have QMOF 20,373, IZA 229, CURATEDMOFs 3,257, CURATEDCOFs 656 and CoREMOFs_ASR 6,905 rows.

**Reuse and interpretation notes:**

- Parent structures overlap CoRE, QMOF, CURATED and IZA; this adds property labels rather than new chemical identities.
- 31,420 model table rows are not DFT measurements and can overlap across parent databases.
- 232 DFT rows are the released table scope; paper describes approximately 230 selected structures.
- Experimental electronic-lab-notebook data are a linked companion on Zenodo, not included in the DFT count.

**Tags:** MOF, COF, zeolite, heat capacity, DFT, uncertainty, additional-materials-20261101.

<a id="mint-atlas"></a>
## MINT-ATLAS atomistic magnetic interactions

Structure-linked atomistic magnetic interaction data with downloadable interaction tables and precomputed magnetic spectra.

**Size:** 209 OPTIMADE structure records (source wording: 209).

**Scope:** Unfiltered live API meta.data_available; different records can share a formula or magnetic system.

**Release:** Public OPTIMADE snapshot 2026-11-01. **Year:** 2026.

**Provenance:** Compiled atomistic magnetic-interaction calculations with per-record method and literature provenance. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; scalar exchange interactions; anisotropy and moments where provided; stored adiabatic magnon spectra; Fourier-transformed exchange eigenvalues; q=0 scalar-exchange mean-field temperatures.

**Access:** open. **Dataset license:** Not verified: client MIT license covers software; no dataset-specific license established.

**Official routes:** [homepage](https://mintatlas.org/) · [api](https://mintatlas.org/optimade/info) · [client](https://github.com/mintatlas-org/mintatlas)

**Evidence:**

- [MINT-ATLAS public OPTIMADE structures](https://mintatlas.org/optimade/v1/structures?page_limit=1) (checked 2026-11-01): Unfiltered metadata reports 209 records; sample mi-0 has cell vectors, site coordinates, method and reference fields, and availability flags.
- [MINT-ATLAS material/download metadata](https://mintatlas.org/optimade/v1/extensions/mintatlas/materials/mi-0) (checked 2026-11-01): Advertises HDF5, exchange CSV and structure exports with byte counts and SHA-256 values.
- [Official MINT-ATLAS client documentation](https://github.com/mintatlas-org/mintatlas) (checked 2026-11-01): Documents public token-free read-only access and explicitly identifies MIT as a client-software license; describes spectra and mean-field conventions.

**Reuse and interpretation notes:**

- The API uses 3D periodic simulation cells even for physically lower-dimensional systems.
- Availability differs by record; absent interaction/spectrum fields are not zero.
- Mean-field temperature is a q=0 scalar-exchange estimate, not an experimental ordering temperature or a full-Brillouin-zone ground-state search.
- The first response reports data_returned=209 despite page_limit=1; the count uses meta.data_available, not page-array length.
- Compiled sources can overlap other magnetic databases; the record count is not a distinct-compound deduplication.

**Tags:** magnetism, exchange, magnons, optimade, additional-materials-20261101.

<a id="gb-solute-interaction-spectra"></a>
## Bond-focused grain-boundary solute interaction spectra

Spectral grain-boundary thermodynamic parameters for binary alloy segregation and solute interactions.

**Size:** ~200 binary alloy systems (source wording: ~200).

**Scope:** Provider describes approximately 200 binary systems with EAM potentials available from NIST.

**Release:** Mendeley Data v1, DOI 10.17632/hrv39bz4k6.1. **Year:** 2024.

**Provenance:** EAM calculations of grain-boundary segregation and interaction spectra; not DFT or experimental measurements. **Structure availability:** `composition_only`.

**Labels/content:** solvent excess boundary enthalpy; dilute segregation energy; solute interaction energy; bulk interaction parameter.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [Release](https://data.mendeley.com/datasets/hrv39bz4k6/1)

**Evidence:**

- [Bond-Focused Local Atomic Environment Representation supplemental data](https://data.mendeley.com/datasets/hrv39bz4k6/1) (checked 2026-11-01): Provider describes approximately 200 binary systems, a downloadable spectral database and CC BY 4.0 licensing.

**Reuse and interpretation notes:**

- Binary-system count is not atom count or the number of segregation-site energy labels.
- Atomic-coordinate payload availability was not verified; this record represents released property spectra.

**Tags:** grain-boundaries, segregation, alloys, EAM, solute-interactions, additional-materials-20261101.

<a id="altermagnet-spin-splitting-2026"></a>
## Sufyan altermagnetic spin-splitting screening release

Calculated spin-splitting summaries linked to MAGNDATA/ICSD structures, with separate symmetry and broader candidate tables.

**Size:** 171 ranked material records (source wording: 171).

**Scope:** 171 nonempty rows in one ranked worksheet; a second worksheet repeats the same cohort with extra ICSD identifiers and is not added.

**Release:** Zenodo v1, 2026-03-19; ranked spreadsheet snapshot 2026-11-01. **Year:** 2026.

**Provenance:** DFT screening of MAGNDATA-derived magnetic structures; some candidates use forced-collinear variants. **Structure availability:** `structure_linked`.

**Labels/content:** maximum and mean spin splitting; band gap; spin-splitting percentage; magnetic structure identifiers; symmetry classification.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo metadata).

**Official routes:** [homepage](https://zenodo.org/records/19109715) · [paper](https://doi.org/10.1103/mmdm-hrj4) · [download](https://zenodo.org/records/19109715/files/Altermagnet_Screening_MaxSS_Ranked_v1..xlsx)

Other denominators (not added to the ranking):

- 295 candidate-table rows: Nonempty material rows in Altermagnet_HTS_Full_Candidate_Pool.xlsx; includes a broader cohort, not added to ranked count.

**Evidence:**

- [Altermagnetic band-splitting data release](https://zenodo.org/records/19109715) (checked 2026-11-01): Deposits ranked/candidate spreadsheets plus collinear and converted-noncollinear MAGNDATA symmetry tables.
- [Altermagnet Zenodo metadata](https://zenodo.org/api/records/19109715) (checked 2026-11-01): Declares CC BY 4.0 and public downloadable files with checksums.
- [Altermagnet ranked spreadsheet](https://zenodo.org/api/records/19109715/files/Altermagnet_Screening_MaxSS_Ranked_v1..xlsx/content) (checked 2026-11-01): Independent OOXML inspection finds 171 nonempty data rows in each of two sheets; columns contain MAGNDATA/ICSD identifiers and spin-splitting properties.

**Reuse and interpretation notes:**

- This deposited ranked cohort has 171 records; the associated paper/current application describes 180 materials, so the catalog does not assign 180 to this file.
- The broader candidate spreadsheet has 295 nonempty material rows and is a different denominator.
- Structure identifiers establish linkage; this small Zenodo package does not independently establish release of all atomic coordinates or the claimed raw DFT calculation files.
- MAGNDATA parent structures overlap the parent database; computed spin splitting is the additional content.
- Forced-collinear variants do not establish stability relative to noncollinear ground states.

**Tags:** altermagnetism, spintronics, magndata-derived, band-splitting, additional-materials-20261101.

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

<a id="hh130-mathub"></a>
## HH130 half-Heusler thermal-transport / MLIP release

Compound-specific interatomic potentials and configuration datasets supporting anharmonic thermal transport of half-Heusler crystals.

**Size:** 130 half-Heusler compounds (source wording: 130).

**Scope:** HH130 material-level cohort; thermal-transport study performed on an 80-compound subset

**Release:** 2024 paper release, checked 2026-11-01. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** DFT energies and forces; interatomic force constants; phonon properties; lattice thermal conductivity including four-phonon scattering (W/m/K).

**Access:** open. **Dataset license:** Not verified for downloadable data/model archive; article is CC BY-NC 3.0.

**Official routes:** [publication](https://doi.org/10.1039/D4DD00240G) · [homepage](http://www.mathub3d.net) · [download](http://www.mathub3d.net/static/database/HH130.zip)

Other denominators (not added to the ranking):

- 31,891 configurations: HH130 training dataset, as reported by paper
- 390 MLIP models: Three models for each of 130 compounds
- 80 compounds: Thermal-transport analysis subset

**Evidence:**

- [HH130 primary Digital Discovery paper](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d4dd00240g) (checked 2026-11-01): Paper describes 130 half-Heuslers, 31,891 configurations and 390 compound-specific models; data-availability statement gives provider ZIP and thermal conductivity analysis for 80 compounds at 300 K.

**Reuse and interpretation notes:**

- Keep material, configuration and model counts separate.
- Thermal conductivities include MLIP-based higher-order force constants; they are computed estimates, not measurements.
- Only 80 of the 130 compounds enter the reported thermal-transport analysis.
- Temperature and phonon-scattering order must accompany conductivity.
- Live provider archive accessibility is documented in primary/hh_download_access.json; no archive was downloaded or inspected.
- Potential training configurations are a specialized property-supporting release and should not be added to other MLIP datasets as unique structures.
- Live provider homepage and archive both returned HTTP 502 during this audit; paper gives a public release route, but current download availability is unresolved.

**Tags:** phonons, thermal-conductivity, half-heusler, mlip, property-focused, OpenAlex-survey-20261101.

<a id="cmr-abx2"></a>
## CMR ABX2 photovoltaic polytypes

Computed II–IV–V2 and III–III–V2 polymorphs for visible-light absorption and photovoltaic applications.

**Size:** 123 ASE calculation/structure rows (source wording: 123).

**Scope:** The released abx2.db systems table counted without adding spectra, property columns or functional results as independent materials.

**Release:** Provider ASE database snapshot 2026-11-01. **Year:** 2017.

**Provenance:** DFT / first-principles calculations. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; GLLB-SC and TB09 band gaps; carrier effective masses; hull energies and uncertainty.

**Access:** open. **Dataset license:** Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification.

**Official routes:** [homepage](https://cmr.fysik.dtu.dk/abx2/abx2.html) · [download](https://wiki.fysik.dtu.dk/cmr-files/abx2.db)

**Evidence:**

- [CMR ABX2 photovoltaic polytypes provider project page](https://cmr.fysik.dtu.dk/abx2/abx2.html) (checked 2026-11-01): Describes the property campaign and links its named ASE database.
- [CMR ABX2 photovoltaic polytypes downloadable ASE database](https://wiki.fysik.dtu.dk/cmr-files/abx2.db) (checked 2026-11-01): Independently inspected SQLite systems table: 123 rows, all with populated positions, cell and atomic-number blobs; payload SHA-256 is preserved in the evidence manifest.
- [CMR repository terms](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): Repository-wide CC BY-SA 4.0 declaration; browser terms differ.
- [CMR ABX2 photovoltaic polytypes browser](https://cmrdb.fysik.dtu.dk/abx2/) (checked 2026-11-01): Public browser provides record-level access; CC BY-NC 4.0 footer differs from the CMR index declaration.

**Reuse and interpretation notes:**

- Polytypes are separate rows; model gaps and effective masses are calculated properties.
- Atomic coordinate availability was checked in the released ASE database; cross-catalog structural overlap has not been deduplicated.

**Tags:** cmr, electronic-structure, semiconductors, additional-materials-20261101.

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

<a id="cmr-perovskite-absorption"></a>
## CMR perovskite optical-absorption spectra

Optical spectra for oxide, oxynitride and organometal-halide perovskite phases.

**Size:** 79 ASE calculation/structure rows (source wording: 79).

**Scope:** The released absorption_perovskites.db systems table counted without adding spectra, property columns or functional results as independent materials.

**Release:** Provider ASE database snapshot 2026-11-01. **Year:** 2015.

**Provenance:** DFT / first-principles calculations. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; frequency-resolved dielectric/absorption spectra; GLLB-SC gaps; calculated absorption efficiency.

**Access:** open. **Dataset license:** Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification.

**Official routes:** [homepage](https://cmr.fysik.dtu.dk/absorption_perovskites/absorption_perovskites.html) · [download](https://wiki.fysik.dtu.dk/cmr-files/absorption_perovskites.db)

**Evidence:**

- [CMR perovskite optical-absorption spectra provider project page](https://cmr.fysik.dtu.dk/absorption_perovskites/absorption_perovskites.html) (checked 2026-11-01): Describes the property campaign and links its named ASE database.
- [CMR perovskite optical-absorption spectra downloadable ASE database](https://wiki.fysik.dtu.dk/cmr-files/absorption_perovskites.db) (checked 2026-11-01): Independently inspected SQLite systems table: 79 rows, all with populated positions, cell and atomic-number blobs; payload SHA-256 is preserved in the evidence manifest.
- [CMR repository terms](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): Repository-wide CC BY-SA 4.0 declaration; browser terms differ.
- [CMR perovskite optical-absorption spectra browser](https://cmrdb.fysik.dtu.dk/absorption_perovskites/) (checked 2026-11-01): Public browser provides record-level access; CC BY-NC 4.0 footer differs from the CMR index declaration.

**Reuse and interpretation notes:**

- The paper describes around 80 phases; the released ASE database contains exactly 79 records.
- Atomic coordinate availability was checked in the released ASE database; cross-catalog structural overlap has not been deduplicated.

**Tags:** cmr, electronic-structure, optics, additional-materials-20261101.

<a id="oxygen-migration-perovskites-2016"></a>
## Oxygen migration barriers in perovskites

DFT oxygen migration barriers and descriptor data for perovskite ionic conductors, with archived raw calculation data.

**Size:** ≥40 perovskite systems (source wording: over 40 perovskites).

**Scope:** Lower bound in primary publication; exact row/material count of archived workbook not independently recounted.

**Release:** 2016 study; Figshare v2 archive (2018). **Year:** 2016.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** oxygen migration barrier; oxygen vacancy formation energy; oxygen p-band center; bond-strength descriptors.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://doi.org/10.6084/m9.figshare.7180817.v2) · [data](https://doi.org/10.6084/m9.figshare.7180817.v2) · [paper](https://doi.org/10.1016/j.ssi.2016.09.007)

**Evidence:**

- [Mayeshiba and Morgan primary article](https://www.sciencedirect.com/science/article/pii/S0167273816304088) (checked 2026-11-01): Authors describe ab initio oxygen migration barriers for over 40 perovskites and compare vacancy formation and oxygen-band descriptors.
- [Author dataset archive](https://api.figshare.com/v2/articles/7180817) (checked 2026-11-01): v2 metadata links study DOI and provides a workbook and 4.19 GB raw-data archive, with CC BY 4.0 licence.

**Reuse and interpretation notes:**

- This is a defect/pathway property collection, not a count of measured oxygen conductivities.
- Large raw-data archive was not downloaded; reusable periodic-coordinate coverage has not been inspected.
- Barriers reflect specific vacancy and calculation conventions.

**Tags:** oxygen-ion, perovskites, migration-barriers, defects, property-focused, OpenAlex-survey-20261101.

<a id="ins-exchange-magnetic-2025"></a>
## INS-derived magnetic exchange and Monte Carlo dataset

Paper describes nearly 100 magnetic materials, while deposit description says over 70; exact archived compound count has not been reconciled.

**Size:** Unranked magnetic compounds with exchange models (source wording: Not verified).

**Scope:** Paper describes nearly 100 magnetic materials, while deposit description says over 70; exact archived compound count has not been reconciled.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** Heisenberg exchange parameters (meV); spin quantum numbers; experimental transition temperature; Monte Carlo transition temperature; exchange pathways; VESTA structures.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-06099-x) · [data](https://doi.org/10.5281/zenodo.17160565) · [repository](https://github.com/malaei/Magnetic_data/tree/main/INS_SW_MC)

**Evidence:**

- [Experimental Exchange Interaction Dataset for Magnetic Materials: Spin Waves to MC Simulations](https://www.nature.com/articles/s41597-025-06099-x) (checked 2026-11-01): Data Records says per-compound directories contain VESTA structures, exchange tables, experimental and MC transition temperatures, references, and MC inputs/outputs.
- [Magnetic exchange archive](https://zenodo.org/api/records/17160565) (checked 2026-11-01): CC BY 4.0; Magnetic_data-main.zip is public and description identifies exchange fits and MC data.

**Reuse and interpretation notes:**

- INS-fitted exchange parameters are model-inferred experimental quantities; MC transition temperatures are computed.
- Heisenberg double-counting, signs, spin normalization and (S+1)/S correction must remain explicit.
- Do not substitute archive description count for a reconciled unique-compound count; bulk 445 MB archive not audited.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="materialscloud-fast-li-ion-conductors"></a>
## Materials Cloud fast Li-ion conductor screening

First-principles molecular-dynamics trajectories and periodic structures for lithium solid-electrolyte screening, with one complete AiiDA provenance example.

**Size:** Unranked released crystal systems / trajectories (source wording: ~60 shortlisted FPMD candidates described; exact released structure/trajectory count not recounted).

**Scope:** Release includes fpmd_structures.aiida, fpmd_trajectories.aiida and one complete screening archive; the >30,000 starting structures are not the released dataset count.

**Release:** Materials Cloud 2025.199 v1, 18 December 2025. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic structure; Li-ion diffusivity; temperature-dependent molecular dynamics; activation barrier; calculation provenance.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://archive.materialscloud.org/records/5zenj-34e64) · [data](https://doi.org/10.24435/materialscloud:zh-cn) · [paper](https://doi.org/10.1039/d5ee07336g)

**Evidence:**

- [Materials Cloud author archive](https://archive.materialscloud.org/records/5zenj-34e64) (checked 2026-11-01): Release describes >30,000 source structures, ~1,000 pinball-screened insulators and ~60 FPMD shortlist candidates; includes FPMD structures/trajectories and one complete Li7NbO6 provenance archive.
- [Materials Cloud release metadata](https://archive.materialscloud.org/api/records/5zenj-34e64) (checked 2026-11-01): Lists four public files totaling 17,645,859,671 bytes with checksums, including structures, trajectories, README and provenance; CC BY 4.0 rights.

**Reuse and interpretation notes:**

- The >30,000 source-pool size is not a count of released FPMD systems or new materials.
- Pinball-model screening and full first-principles MD labels must remain distinct.
- AiiDA trajectory/provenance archives total about 16.4 GiB; bulk payloads were not downloaded or counted in this survey.
- Source experimental databases overlap COD, ICSD and MPDS.

**Tags:** solid-electrolytes, diffusivity, AiiDA, molecular-dynamics, Materials-Cloud, property-focused, OpenAlex-survey-20261101.

<a id="mp-charge-density-pyrho"></a>
## Materials Project representation-independent charge densities

Periodic electronic charge densities and tools for Fourier-based changes of cell/grid representation.

**Size:** Unranked charge-density records (source wording: Not verified charge-density records).

**Scope:** The publication describes a growing API collection without a verified fixed record count in this audit.

**Release:** 2022 publication / API-based collection. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** electronic charge density; periodic structure; grid transformations; calculation metadata.

**Access:** registration. **Dataset license:** Not verified separately for the charge-density endpoint; consult Materials Project data terms.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01746-z) · [data](https://doi.org/10.17188/1833409)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-022-01746-z) (checked 2026-11-01): Periodic electronic charge densities and tools for Fourier-based changes of cell/grid representation. The publication describes a growing API collection without a verified fixed record count in this audit.
- [Primary repository release metadata](https://api.datacite.org/dois/10.17188/1833409) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Derivative property layer for Materials Project structures, not an independent material count.
- Figshare 19908193 is a re-gridding validation example, not the entire density corpus.
- Current record count and authenticated API availability were not tested.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="topohse-db"></a>
## TopoHSE-DB

Hybrid-functional topological classifications of nonmagnetic crystalline materials, compared with semilocal calculations.

**Size:** Unranked classified crystalline-material entries (source wording: Not verified).

**Scope:** Dataset-level release verified; exact entry count and standalone atomic coordinate coverage were not verified.

**Release:** 2026 published release. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** HSE06 topological classification; semilocal topological classification; electronic symmetry traces.

**Access:** open. **Dataset license:** CC BY 2.0.

**Official routes:** [homepage](https://rodare.hzdr.de/record/4935) · [paper](https://doi.org/10.1088/2632-2153/ae97d8) · [download](https://doi.org/10.14278/rodare.4935)

**Evidence:**

- [OpenAlex primary publication metadata](https://api.openalex.org/works/https://doi.org/10.1088/2632-2153/ae97d8) (checked 2026-11-01): Verified published article title/authors and abstract: HSE06 and semilocal calculations share relaxed structures and are classified using topological quantum chemistry.
- [TopoHSE-DB data release](https://rodare.hzdr.de/record/4935) (checked 2026-11-01): RODARE open dataset published 2026-08-14 provides trace_files.zip under CC BY 2.0; version DOI 10.14278/rodare.4935.

**Reuse and interpretation notes:**

- A separate hybrid-functional computed cohort from existing TQC catalogs; overlap with source crystals remains possible.
- Only trace archive availability was directly verified; structure files, count and archive contents were not audited.
- Topological classes depend on functional and ideal bulk/symmetry assumptions; experimental topological claims are not equivalent labels.

**Tags:** property-focused, OpenAlex-survey-20261101.

<a id="wurtzite-piezoml-dryad"></a>
## Wurtzite solid-solution PiezoML data

DFT structures, screening descriptors and explicit piezoelectric calculations for doped wurtzite solid solutions.

**Size:** Unranked candidate/DFT calculation records (source wording: Not verified).

**Scope:** Deposit describes >3,000 generated candidates, about 500 proxy-screened candidates, 30 promising selections and 11 enhanced-response predictions; exact released row count unverified.

**Release:** 2026 published release. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** piezoelectric e33 (C/m²); lattice c/a ratio; formation energy; DFT relaxed structures; screening descriptors.

**Access:** open. **Dataset license:** CC0 1.0 (Dryad data terms; bundled software licenses need separate checking).

**Official routes:** [homepage](https://datadryad.org/dataset/doi%3A10.5061/dryad.vmcvdnd6s) · [download](https://doi.org/10.5061/dryad.vmcvdnd6s)

**Evidence:**

- [Behrendt et al., Dryad data and code release](https://datadryad.org/dataset/doi%3A10.5061/dryad.vmcvdnd6s) (checked 2026-11-01): Published 2026-05-28; README lists relaxed base structures, doped calculation directories, finite-strain Berry-phase e33, formation-energy calculations and CSVs. Nine base systems are AlN, BeO, CdS, CdSe, GaN, ZnO, ZnS, ZnSe and AgI.
- [Dryad data terms](https://datadryad.org/terms#copyright) (checked 2026-11-01): Dryad terms identify CC0 as the data publication license.

**Reuse and interpretation notes:**

- Generated candidates, proxy-screened candidates and explicit e33 calculations have different denominators; total candidate count is not a piezoelectric label count.
- README lists 2×2×1 16-atom wurtzite supercells and two cation substitutions.
- Some relaxed candidates lose wurtzite structure; failure markers must not be treated as valid computed responses.
- Deposit date is 2026; README refers to a 2024 publication without a verified journal DOI.

**Tags:** property-focused, OpenAlex-survey-20261101.
