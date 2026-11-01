# Crystal generation and discovery benchmarks

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="openlam-crystal-philately"></a>
## OpenLAM Crystal Philately challenge collection

Competition crystal collection combining participant submissions and reused open-repository structures, relaxed and scored with OpenLAM models.

**Size:** ≥19,800,000 valid structures (source wording: over 19.8 million valid structures (January 2025 report)).

**Scope:** January 2025 first-round challenge-report snapshot

**Release:** January 2025 first-round challenge-report snapshot. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; MLIP energy; model-relative hull membership.

**Access:** registration. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/deepmodeling/openlam) · [data](https://github.com/deepmodeling/openlam#query-crystal-structures-from-openlam-database) · [paper](https://arxiv.org/abs/2501.16358) · [code](https://github.com/deepmodeling/openlam)

**Evidence:**

- [The OpenLAM Challenges](https://arxiv.org/abs/2501.16358) (checked 2026-11-01): Full paper reports over 19.8 million valid structures, including 12.8 million uploaded by participants; the rest come from open repositories.
- [OpenLAM official repository](https://github.com/deepmodeling/openlam) (checked 2026-11-01): Documents crystal-structure and hull queries through an authenticated API.

**Reuse and interpretation notes:**

- 19.8 million is not entirely new generated material coverage: 12.8 million are participant uploads and the rest reuse open repositories.
- Historical challenge count; current total and complete bulk archive were not verified.
- OpenLAM model-based hull membership is not DFT ground-state stability or experimental synthesis.
- API queries require a Bohrium account access key; no key was used in this audit.
- Validity, uniqueness, and novelty definitions must be checked before comparison with SUN metrics.

**Tags:** generation, OpenLAM, challenge, MLIP labels.

<a id="alex-mp-mattergen-reference"></a>
## Alex-MP reference dataset (MatterGen public release)

Combined reference structures and energies distributed to assess novelty and stability of generated crystals.

**Size:** 845,997 structures (source wording: 845,997 structures with DFT energies).

**Scope:** Public MatterGen Alex-MP reference release

**Release:** Public MatterGen Alex-MP reference release. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; DFT energy; reference convex hull.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/microsoft/mattergen) · [data](https://github.com/microsoft/mattergen/tree/main/data-release/alex-mp) · [paper](https://doi.org/10.1038/s41586-025-08628-5) · [code](https://github.com/microsoft/mattergen)

**Evidence:**

- [MatterGen official README](https://raw.githubusercontent.com/microsoft/mattergen/main/README.md) (checked 2026-11-01): Public Alex-MP reference has 845,997 structures and DFT energies; ICSD structures used in the paper cannot be shared for licensing reasons.

**Reuse and interpretation notes:**

- Overlaps Alex-MP-20 and parent databases.
- Public reference differs from the paper’s Alex-MP-ICSD reference: licensed ICSD components are omitted.
- Correction scheme and MLIP-versus-DFT evaluation affect the hull and stability labels.

**Tags:** generation, reference hull, MatterGen.

<a id="alex-mp20-mattergen"></a>
## Alex-MP-20 (MatterGen)

DFT-recomputed Materials Project and Alexandria structures filtered for small cells and energy above hull below 0.1 eV/atom, for generative-model training.

**Size:** 607,684 structures (source wording: 607,684 crystal structures (model data summary)).

**Scope:** MatterGen publication training corpus

**Release:** MatterGen publication training corpus. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; DFT energy; energy above hull; band gap; bulk modulus; magnetic density.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International (upstream MP-20 and Alexandria data-release READMEs).

**Official routes:** [homepage](https://github.com/microsoft/mattergen) · [data](https://github.com/microsoft/mattergen/tree/main/data-release/alex-mp) · [paper](https://doi.org/10.1038/s41586-025-08628-5) · [code](https://github.com/microsoft/mattergen)

**Evidence:**

- [Microsoft MatterGen data summary card](https://huggingface.co/microsoft/mattergen/blob/main/data_summary_card.md) (checked 2026-11-01): Reports 607,684 DFT-relaxed crystal structures from MP v2022.10.28 and Alexandria.
- [MatterGen Alex-MP data-release README](https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/alex-mp/README.md) (checked 2026-11-01): Re-relaxes with PBE; removes Tc, Pm and atomic numbers 84 or higher; training cells have at most twenty atoms and hull energy at most 0.1 eV/atom.

**Reuse and interpretation notes:**

- Includes/recomputes MP-20 and Alexandria; not additive with its parent databases.
- 607,684 is the publication/model-card corpus count; a local file-row recount was not performed.
- Property labels are sparse and not all structures have every listed property.
- Below a 0.1 eV/atom hull threshold does not mean experimentally synthesized.

**Tags:** generation, MatterGen, Alexandria derivative, MP derivative.

<a id="mp20-cdvae"></a>
## MP-20 (CDVAE benchmark)

Materials Project / ICSD-derived crystal benchmark with one to twenty atoms per unit cell and fixed train/validation/test splits.

**Size:** 45,231 structures (source wording: 45,231 general inorganic materials).

**Scope:** CDVAE ICLR 2022 release

**Release:** CDVAE ICLR 2022 release. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; formation energy; energy above hull.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/txie-93/cdvae/tree/main/data/mp_20) · [data](https://github.com/txie-93/cdvae/tree/main/data/mp_20) · [paper](https://arxiv.org/abs/2110.06197) · [code](https://github.com/txie-93/cdvae)

**Evidence:**

- [CDVAE MP-20 dataset documentation](https://raw.githubusercontent.com/txie-93/cdvae/main/data/mp_20/README.md) (checked 2026-11-01): 45,231 entries; 1–20 atoms per unit cell; selected from ICSD-origin Materials Project structures with energy filters.

**Reuse and interpretation notes:**

- DFT-relaxed structures inherit experimental parentage; this does not establish dynamical or finite-temperature stability of every entry.
- Different downstream MP-20 repackagings can remove entries or alter standardization; retain split/version provenance.
- Overlaps Materials Project, ICSD-derived corpora and MatterGen datasets.

**Tags:** generation, CSP, MP derivative, small cells.

<a id="perov5-cdvae-matbench"></a>
## Perov-5 / Matbench perovskites

Castelli computational perovskite screening corpus reused by CDVAE for generation and by Matbench for formation-energy regression.

**Size:** 18,928 structures (source wording: 18,928 five-atom perovskite materials).

**Scope:** Castelli corpus / CDVAE and Matbench benchmark derivatives

**Release:** Castelli corpus / CDVAE and Matbench benchmark derivatives. **Year:** 2012.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; formation energy.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/txie-93/cdvae/tree/main/data/perov_5) · [data](https://github.com/txie-93/cdvae/tree/main/data/perov_5) · [paper](https://doi.org/10.1039/C2EE22341D) · [code](https://github.com/txie-93/cdvae)

**Evidence:**

- [CDVAE Perov-5 dataset documentation](https://raw.githubusercontent.com/txie-93/cdvae/main/data/perov_5/README.md) (checked 2026-11-01): 18,928 structures, all with five atoms; all original corpus entries are included.
- [Matminer dataset metadata](https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json) (checked 2026-11-01): matbench_perovskites has 18,928 structure/formation-energy samples adapted from Castelli et al.

**Reuse and interpretation notes:**

- Perov-5 and Matbench perovskites are task derivatives of the same parent corpus; not independent materials collections.
- Many hypothetical candidates are thermodynamically unstable.
- Formation energy in Matbench is eV per unit cell.

**Tags:** generation, perovskite, Matbench, hypothetical.

<a id="carbon24-cdvae"></a>
## Carbon-24 (CDVAE benchmark)

Carbon allotrope benchmark selected from AIRSS calculations at 10 GPa; six to twenty-four atoms per unit cell.

**Size:** 10,153 structures (source wording: 10,153 lowest-energy carbon structures selected from 101,529 AIRSS structures).

**Scope:** CDVAE ICLR 2022 release, from Pickard 2020 AIRSS archive

**Release:** CDVAE ICLR 2022 release, from Pickard 2020 AIRSS archive. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy per atom.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) · [data](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) · [paper](https://arxiv.org/abs/2110.06197) · [code](https://github.com/txie-93/cdvae)

**Evidence:**

- [CDVAE Carbon-24 dataset documentation](https://raw.githubusercontent.com/txie-93/cdvae/main/data/carbon_24/README.md) (checked 2026-11-01): Selects the lowest-energy ten percent, 10,153 of 101,529 AIRSS carbon structures at 10 GPa.

**Reuse and interpretation notes:**

- Single composition, many structures; not 10,153 chemical compounds.
- High-pressure source; diamond is most stable at the specified pressure, while the remaining entries are metastable or unstable.
- Overlaps the larger AIRSS carbon source archive.

**Tags:** generation, carbon, AIRSS, 10 GPa.
