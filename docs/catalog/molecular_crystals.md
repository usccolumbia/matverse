# Molecular crystals and ice

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="omc25"></a>
## Open Molecular Crystals 2025 (OMC25)

DFT relaxation trajectories of random molecular-crystal packings generated from OE62 molecules.

**Size:** 26,257,042 DFT configuration frames (source wording: 26,257,042 released train+validation frames; 218,841 starting crystals).

**Scope:** 24,870,226 train + 1,386,816 validation; test is not included in this public count.

**Release:** Public 250802 train and validation release; Scientific Data 2026. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic structure; total energy; forces; stress.

**Access:** mixed. **Dataset license:** Creative Commons Attribution 4.0 International (dataset).

**Official routes:** [data](https://huggingface.co/datasets/facebook/OMC25) · [paper](https://doi.org/10.1038/s41597-026-06628-2) · [code](https://github.com/facebookresearch/fairchem)

Other denominators (not added to the ranking):

- 218,841 initial molecular crystals: sum of public training207271 and validation11570 crystals

**Count derivation:** public training + validation frames; excludes the unreleased/held-out part of the study corpus; 24,870,226 + 1,386,816 = 26,257,042.

**Evidence:**

- [OMC25 official dataset card](https://huggingface.co/datasets/facebook/OMC25/blob/main/README.md) (checked 2026-11-01): Train has 24,870,226 frames and 207,271 starting crystals; validation has 1,386,816 frames and 11,570 starting crystals; CC BY 4.0 data.
- [OMC25 Scientific Data descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC12979844/) (checked 2026-11-01): Full study describes over 27 million frames, over 230,000 initial crystals and approximately 50,000 molecules.
- [OMC25 official access documentation](https://facebookresearch.github.io/fairchem/omc25/) (checked 2026-11-01): Hugging Face repository access is requested; ASE-compatible LMDB data and energy/force/stress labels are documented.
- [Open Molecular Crystals 2025 (OMC25) dataset and models — Scientific Data descriptor](https://doi.org/10.1038/s41597-026-06628-2) (checked 2026-11-01): Publisher DOI and Crossref metadata verify the corresponding Scientific Data descriptor; the selected release count is supported by the other evidence listed here.

**Reuse and interpretation notes:**

- Public train+validation sum is calculated directly from the card; the paper full-corpus 27M+ total includes other splits.
- Frames are not distinct molecular crystals or molecules.
- Hugging Face access is gated; the card also exposes direct data links.
- OMol25 and OE62 are isolated-molecule resources and are not counted as periodic datasets here.

**Tags:** molecular-crystal, DFT, MLIP, trajectory, Scientific Data.

<a id="osd-organic-superconductors"></a>
## Organic Superconductor Database (OSD)

Quasi-two-dimensional crystalline organic conductors and superconductors with literature measurements, CSD-linked crystal structures and tight-binding electronic calculations.

**Size:** 184 crystal structure entries (source wording: 184 CSD crystal structures associated with 110 materials and 440 measured properties (2022 paper)).

**Scope:** Historical 2022 publication cohort; 184 structures are not 184 independently confirmed superconductors or a current portal-total assertion

**Release:** 2022 publication cohort; public portal checked 2026-11-01. **Year:** 2022.

**Provenance:** mixed. **Structure availability:** `structure_linked`.

**Labels/content:** critical temperature; critical magnetic fields; experimental electromagnetic properties; crystal structure; tight-binding band structure; molecular packing.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](http://osd.clarku.edu/public/about) · [data](http://osd.clarku.edu/public/) · [paper](https://doi.org/10.3390/cryst12070919)

**Evidence:**

- [A Database for Crystalline Organic Conductors and Superconductors](https://www.mdpi.com/2073-4352/12/7/919) (checked 2026-11-01): 2022 paper reports 110 materials, 184 CSD structures and 440 measured properties; describes manual measurements and tight-binding calculations.
- [OSD official about page](http://osd.clarku.edu/public/about) (checked 2026-11-01): Confirms open public browsing, CSD-source CIFs, manually entered literature measurements and tight-binding electronic structures.

**Reuse and interpretation notes:**

- Includes organic conductors and other correlated electronic states as well as superconductors; not every material has superconducting Tc.
- Underlying CIFs originate from CSD; public links/viewers do not establish unrestricted coordinate redistribution.
- The 184-structure publication cohort overlaps CSD and can contain multiple structures for one material.
- Dataset-wide reuse licensing was not found; the paper’s article license is not substituted for data licensing.
- HTTP public pages were reachable in the direct retrieval; an HTTPS browser-tool request failed, so the observed HTTP route is retained.

**Tags:** superconductivity, organic, molecular crystal, CSD derivative, mixed provenance, superconductor, superconductors.

<a id="x23-dmc"></a>
## X23 diffusion Monte Carlo benchmark

High-accuracy lattice-energy reference values for the established X23 molecular-crystal set.

**Size:** 23 benchmark crystal systems (source wording: 23 molecular crystals).

**Scope:** All X23 molecular crystals evaluated by the 2024 DMC paper.

**Release:** 2024 DMC reference study. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** lattice energy; reference uncertainty; sublimation enthalpy comparisons.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [paper](https://doi.org/10.1103/PhysRevLett.133.046401)

**Evidence:**

- [Author abstract of 2024 X23 DMC paper](https://pubmed.ncbi.nlm.nih.gov/39121404/) (checked 2026-11-01): The primary paper reports diffusion Monte Carlo lattice energies for all 23 molecular crystals in X23.

**Reuse and interpretation notes:**

- An energy reference benchmark, not a new collection of 23 novel chemical structures.
- Separate reusable data license and machine-readable original coordinate package were not verified; periodic structures are identified by the benchmark.
- Original X23, revised X23b and DMC labels must be versioned separately.

**Tags:** molecular-crystal, benchmark, DMC, historical.

<a id="dmc-ice13"></a>
## DMC-ICE13

Diffusion Monte Carlo lattice-energy reference benchmark spanning ambient and high-pressure molecular ice.

**Size:** 13 benchmark periodic ice polymorphs (source wording: 13 ice polymorphs).

**Scope:** Thirteen phases in the 2022 DMC-ICE13 publication.

**Release:** 2022 JCP reference dataset. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; absolute lattice energy; relative lattice energy; DFT benchmark energies.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [paper](https://doi.org/10.1063/5.0102645) · [data](https://discovery.ucl.ac.uk/id/eprint/10162009/1/2207.01353v1.pdf)

**Evidence:**

- [DMC-ICE13 author paper](https://arxiv.org/abs/2207.01353) (checked 2026-11-01): Defines a 13-polymorph lattice-energy benchmark with DMC references.
- [DMC-ICE13 author supporting information](https://discovery.ucl.ac.uk/id/eprint/10162009/1/2207.01353v1.pdf) (checked 2026-11-01): Supporting information supplies all thirteen geometries in POSCAR format plus DFT/DMC input details.

**Reuse and interpretation notes:**

- Thirteen polymorphs of one chemical composition, not thirteen distinct compounds.
- Hydrogen ordering/disordering and geometry conventions affect comparisons.
- Explicit data redistribution license not verified.

**Tags:** molecular-crystal, ice, DMC, benchmark.
