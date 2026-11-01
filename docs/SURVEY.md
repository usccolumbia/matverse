# Crystal materials datasets: volume, coverage and reusable evidence

## Abstract

Materials dataset sizes describe different things: distinct crystallographic determinations, optimized structures, trajectory frames, property observations, or source publications. This survey maps their uses and limitations through a categorized catalog with release-scoped counts and primary-source evidence. It covers inorganic bulk crystals, experimental crystallography, interatomic-potential data, two-dimensional solids, porous frameworks, molecular crystals, surfaces, discovery benchmarks and crystal-related experimental properties. The central finding is methodological: volume becomes interpretable only after identifying the counted object, computational or measurement protocol, structure availability, and overlap with other releases. Large integrated crystal indexes help retrieval and coverage, while non-equilibrium configurations constrain interatomic models and experimentally linked records connect predictions to material behavior. These resources support different tasks and should not be compressed into one ranking of “materials.” The accompanying cards preserve those distinctions and flag unresolved count, access and license questions.

## 1. Questions and scope

An equilibrium structure repository, a relaxation archive and a literature property collection cannot be compared using an unlabeled row count. This survey asks: **RQ1**, which dataset families cover crystal materials and their relevant observations; **RQ2**, what each reported size counts; and **RQ3**, how provenance, access, overlap and label coverage affect reuse. The [catalog](../README.md#ranked-catalog) supplies descending volume tables within categories. The [methods](METHODOLOGY.md) define the evidence and counting rules.

The requested [ACS Perspective](review-crosswalk.md) extends the coverage check to integrated experimental and computational platforms. The present survey adds release-level accounting for the named recent datasets and keeps numerical evidence attached to provider documentation.

## 2. Search, evidence and taxonomy

Independent research perspectives searched provider sites, repositories, dataset cards, release APIs, original papers and data descriptors. Follow-up searches examined newer versions, subsets, access restrictions and discrepancies. The catalog includes commercial reference databases to describe the landscape, but hosts only metadata and links. This is a broad, living survey; it is not a PRISMA systematic review and does not claim exhaustive retrieval. The [research log](../research/search_log.json) and record-level sources document the search and evidence trail.

The primary categories follow the data's main scientific use. Secondary tags describe chemistry, method and lineage. Structure availability is a separate axis: full periodic atomic coordinates, structural identifiers or links, composition-only records, and mixed availability. Provenance is also separate from availability: a generated crystal can have precise atomic coordinates without experimental validation, while a measured conductivity may lack a resolved crystal structure.

| Evidence type | What it establishes | What it does not establish |
|---|---|---|
| Release metadata or independently counted files | Defined rows/files and distribution scope | Unique valid structures or scientific correctness |
| Experimentally resolved crystallography | A reported structure under its measurement/refinement conditions | All properties, every synthesis route, or universal phase stability |
| DFT-labeled structures/configurations | Results under a specified electronic-structure protocol | Experimental synthesis or error-free transfer between protocols |
| MLIP predictions | Model outputs under a documented model and settings | Equivalent evidence to a DFT calculation or experiment |
| Extracted literature observations | Reported observations with publication context | Uniform measurement conditions, error-free extraction or unique materials |

## 3. Integrated indexes and computed bulk structures

[LeMat-Bulk](https://huggingface.co/datasets/LeMaterial/LeMat-Bulk) standardizes records from MP, OQMD and Alexandria, whereas [MateriaViva Open](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) spans a wider set of sources, properties and curves. Their counts therefore characterize integrated releases rather than independent additions to their parents. Their deduplication definitions and source-coordinate provenance need to travel with exports. A fingerprint match is useful structural evidence, but it does not by itself establish that all associated calculations used interchangeable numerical settings or that a material was experimentally synthesized.

[Alexandria](https://alexandria.icams.rub.de/datasets.html), [AFLOW](https://aflow.org/API/aflowlib_stats/), [OQMD](https://oqmd.org/) and [Materials Project](https://materialsproject.org/) share high-throughput structure-centered computation, but differ in release scope and calculation conventions. They are suitable starting points for property prediction and stability screening when versions and labels are controlled. [MC3D](https://arxiv.org/abs/2508.19223) instead emphasizes automated, reproducible optimization of curated crystallographic inputs. [GNoME](https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md) illustrates another denominator problem: the public novel stable-structure set differs from the much larger discovery-candidate headline. Each card ranks the documented release it actually describes.

## 4. Experimental crystallography and reference collections

[COD](https://www.crystallography.net/cod/), [ICSD](https://icsd.products.fiz-karlsruhe.de/en) and [CSD](https://www.ccdc.cam.ac.uk/solutions/software/csd/) are structural reference resources, but their chemistry, curation and access models differ. An entry may represent a distinct determination, temperature, refinement, disorder treatment or polymorph rather than a new composition. ICSD also maintains a theoretical-structure collection; its headline counter should not be presented as an experimental-only total. [MPDS](https://mpds.io/) links structures with separately counted properties and phase diagrams, so its platform-wide entry count should not be used as its crystal-structure count.

Public browsing does not establish open bulk reuse. COD's data policy and commercial collections' contractual terms create materially different routes for reproducible data distribution. A dataset using identifiers from a restricted parent may distribute only labels and links. The [3DSC paper](https://www.nature.com/articles/s41597-023-02721-y) and the linked release records are an example of why structure access should be checked independently of a superconductivity label table. This distinction is recorded in the catalog rather than inferred from an article's open-access status.

## 5. Non-equilibrium data for interatomic models

[LeMat-Traj](https://huggingface.co/datasets/LeMaterial/LeMat-Traj), [OMat24](https://huggingface.co/datasets/facebook/OMAT24), [MPtrj](https://doi.org/10.6084/m9.figshare.23713842), and [MatPES](https://github.com/materialyzeai/matpes) supply configuration-level energy, force or stress information. Their frames constrain environments beyond a collection of equilibrium minima, but many related frames can come from one parent crystal. A release's frame count should therefore be accompanied by parent-system counts where available. Training on randomly separated neighboring frames can provide a much easier test than holding out parent materials or structural families.

Sampling pools also need separation from labeled releases. [MP-ALOE](https://doi.org/10.1038/s41524-025-01834-9) selects DFT calculations from a much larger generated pool, while MatPES selects configurations from extensive MD. [ELEMENTA](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) distinguishes its public archives from a larger full corpus. [MAD](https://arxiv.org/abs/2603.02089) mixes periodic and isolated systems under a consistent calculation approach. These examples show why a model's training-size headline, its released subset and its number of distinct crystals are separate quantities. A checkpoint download alone is not a verified release of its training data.

## 6. Low-dimensional, porous and molecular crystals

[C2DB](https://2dhub.org/c2db/c2db.html), [MC2D](https://archive.materialscloud.org/records/17gf6-84915) and [2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910) cover two-dimensional structures through different extraction, generation and calculation pipelines. A monolayer candidate, a defect charge state and a bilayer stacking are distinct observation units. Ranking them numerically remains useful for navigation when those units stay explicit, but does not measure the number of experimentally exfoliable compounds.

[CoRE MOF](https://zenodo.org/records/15621349) curates experimental-derived frameworks, whereas [QMOF](https://github.com/Andrew-S-Rosen/QMOF) emphasizes computed quantum properties and hypothetical framework datasets explore broader design spaces. Full family counts can include restricted branches or multiple solvent-removal variants; the publicly downloadable computation-ready subset may be much smaller. Molecular-crystal resources present a similar scale split: [OMC25](https://arxiv.org/abs/2508.02651) offers extensive configuration data, while the X23 and ice benchmark cards describe small, higher-level reference sets. Broad training coverage and careful reference benchmarks serve complementary roles.

## 7. Surfaces and coupled environments

The [Open Catalyst datasets](https://opencatalystproject.org/) provide large atomistic training sets, while [Catalysis-Hub](https://www.catalysis-hub.org/) organizes reaction and adsorption studies. A relaxation system, a frame within that relaxation and a reaction-energy record are not interchangeable. [ODAC](https://opencatalystproject.org/odac/) extends adsorption data to porous frameworks. Its placement in the framework category is a navigation choice, not a claim that adsorption frames are distinct MOFs.

More detailed environments increase the importance of metadata. Surface termination, adsorbate coverage, solvent configuration and electronic-structure settings can all define separate learning problems. The [ACS review crosswalk](review-crosswalk.md) captures the requested paper's connection to experimental catalysis and integrated portals. MatVerse consequently keeps reaction portals, measured performance collections and atomic configuration corpora identifiable instead of combining their headline counts.

## 8. Property, generation and discovery benchmarks

[Matbench](https://github.com/materialsproject/matbench) organizes property tasks, whereas [Matbench Discovery](https://matbench-discovery.materialsproject.org/data/sets) evaluates discovery-style stability prediction. Paired Matbench tasks can reuse the same structures and should not be summed as independent corpora. The [WBM processing documentation](https://github.com/janosh/matbench-discovery/blob/main/data/wbm/readme.md) distinguishes original, cleaned and prototype-filtered sets. The catalog uses an explicit processed denominator and preserves those alternatives in its card.

[CDVAE's MP-20, Perov-5 and Carbon-24](https://github.com/txie-93/cdvae/tree/main/data) are benchmark derivatives, while [MatterGen](https://github.com/microsoft/mattergen/tree/main/data-release) supplies larger generation-oriented collections. Training and testing across these families require parentage checks. Small-cell filters, prototype reuse, energy thresholds and database versions alter the evaluated task. Specialized phonon, transport, dielectric, magnetic and elastic datasets add different labels, often for subsets of the same parent repositories. A property's advertised presence does not imply that every structure has that label.

## 9. Experimental properties and extracted literature

[Starrydata](https://starrydata.github.io/starrydata_datasets/) stores digitized observations with paper and sample context, whereas [DigBat](https://www.digbat.org/) focuses on electrolyte information and [DigHyd](https://www.dighyd.org/) on hydrogen-storage observations. Their sample, curve, conductivity-entry and paper counters describe different levels of evidence. Composition alone may not identify phase, processing history, porosity, defects or test conditions, which can all matter when connecting these records to ideal crystal structures.

The [Scientific Data index](scientific-data.md) includes measured-property extraction, synthesis and characterization descriptors as well as computed structure/property datasets. Extraction errors and reporting bias remain relevant even when the source articles are real. In particular, [impurity-aware synthesis records](https://www.nature.com/articles/s41597-025-06222-y) distinguish explicit secondary phases from their absence in the reported account; an unmentioned impurity is not proof of phase purity. Dataset cards retain the observation unit and original publication route so users can check such distinctions.

The [superconductivity supplement](superconductivity.md) examines a focused instance of this distinction: experimental transition measurements, matched structure proxies, electronic-band collections and computed electron–phonon labels support different learning tasks. Hennig-group training releases add useful supervised inputs, but their public file coverage, train/test manifests and parent datasets must be checked independently of the paper's model-training headline. Pressure, repeated compositions and shared SuperCon ancestry are central to this comparison; the supplement records these limits alongside the reported sizes.

## 10. Cross-family implications and open work

The catalog supports three practical conclusions. First, scale should be reported at multiple levels when possible: source structures, parent systems, configurations and observations. Second, joins should carry identifiers, versions and measurement/calculation context; matching a formula or structure fingerprint is not enough to make labels scientifically interchangeable. Third, a training set's value depends on coverage, information content and validation conditions, not solely its row count. These are synthesis conclusions from the different data designs represented above, not claims that every dataset has been audited for each failure mode.

Several concrete improvements remain. The community would benefit from machine-readable count manifests that distinguish converged outputs from input pools, immutable release snapshots, license fields tied to each source contribution, column-level label coverage, and parent/family-aware benchmark splits. Experimentally linked records need phase and processing context as well as negative or unsuccessful results. Computed labels need method provenance and documented unit conventions. The catalog itself needs continued primary-source updates: some sizes and terms remain unverified, current websites can be inaccessible, and file recounts do not certify uniqueness or physical validity. The [additional perspective papers](related-perspectives.md) were checked for coverage and interpretation, with their review/preview evidence limits stated separately.

## 11. Answers to the research questions

**RQ1:** The relevant ecosystem extends from equilibrium and experimental crystal structures to non-equilibrium atomistic data, domain-specific periodic systems, and structure-linked or composition-only observations. The categories make these resources discoverable without claiming they all contain the same kind of object.

**RQ2:** The release and counted unit determine the meaning of size. Category tables sort reported volumes in descending order, preserving rounded figures, lower bounds and unknowns. Overlapping releases, aggregates and observation levels prevent a meaningful additive total of materials.

**RQ3:** Reuse depends on source provenance, actual structure availability, label coverage, measurement or calculation protocol, access rights and evaluation split. MatVerse contributes a maintained evidence trail for those choices; the original providers and data descriptors remain the sources to cite when using the data.

## References and data citations

Every specific dataset cited above links to its primary documentation, paper or release. Full claim-level evidence and check dates are in the [dataset cards](../README.md#ranked-catalog) and [JSON](../data/datasets.json). The requested review is cited in the [ACS crosswalk](review-crosswalk.md); navigation resources have a separate [source directory](resources.md). This linked reference system preserves download routes and release context without inventing bibliographic metadata.
