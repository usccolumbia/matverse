<h1>
  <a href="http://mleg.cse.sc.edu"><img src="assets/mleg-logo-readme.svg" alt="Machine Learning and Evolution Lab (MLEG)" width="154" height="40" align="right"></a>
  <img src="assets/matverse-logo.png" alt="MatVerse logo" width="40" height="40" align="absmiddle">&nbsp;MatVerse
  <a href="https://usccolumbia.github.io/matverse/?q=thermoelectric"><img src="assets/search-box.svg" alt="Search MatVerse datasets" width="230" height="24" align="absmiddle"></a>
</h1>

**A source-verified atlas of crystal materials datasets.**

**[Search the interactive directory](https://usccolumbia.github.io/matverse/)** · [Download the standalone HTML](https://github.com/usccolumbia/matverse/raw/refs/heads/main/index.html) · [All source links](sources.md)

523 dataset and release records · 13 categories · 748 distinct dataset evidence URLs · checked **November 1, 2026**

MatVerse surveys periodic crystal structures and their associated data: experimental crystallography, computed inorganic solids, machine-learning interatomic potential (MLIP) configurations, 2D materials, porous frameworks, molecular crystals, surfaces, and property and discovery benchmarks. It also includes crystal-related experimental property collections that supply compositions or measurements without complete atomic coordinates.

The catalog includes **LeMat, MateriaViva Open, Alexandria, OMat24, Matbench Discovery/WBM, Scientific Data descriptors and Starrydata**, alongside established databases and newer releases. It is a broad, living survey rather than an exhaustive census. A record can be a dataset, a named subset, or a release; records are not necessarily independent corpora.

[Read the survey](docs/SURVEY.md) · [Full JSON](data/datasets.json) · [CSV export](data/datasets.csv) · [Repository and resource directory](docs/resources.md) · [Scientific Data index](docs/scientific-data.md) · [ACS paper crosswalk](docs/review-crosswalk.md) · [Lineage and overlap](docs/overlap.md) · [Methods and schema](docs/METHODOLOGY.md)

## Read the counts correctly

- **Structures/materials:** usually equilibrium or curated structural records. Polymorphs, temperatures, disorder models and functional variants can create several records per composition.
- **Configurations/frames:** snapshots from relaxation, molecular dynamics or perturbation. Millions of frames can originate from far fewer parent crystals.
- **Property records/samples/patterns:** observations, literature samples or characterization data. These may have no atom-resolved structure.
- **Aggregates and derivatives overlap.** LeMat, MateriaViva, parent databases, benchmark subsets and format mirrors cannot be added into one material total.
- **Access and licensing are separate.** A free website, model license or open-access paper does not establish a dataset's redistribution rights. Unverified terms remain explicit.

Each linked dataset card records the release, unit, count evidence, available structure level, provenance, labels, access, license and caveats. There are 22 records with unverified size; these remain unranked. Counts are mostly provider-reported, with selected metadata sums and small-file recounts identified explicitly. “Checked” means the documentation was inspected; it does not mean every payload was downloaded, every row audited, or each claim independently reproduced.

The [HTML directory](https://usccolumbia.github.io/matverse/) searches names, properties, methods, tags and source evidence. Filter by category, access, structure availability, license status or counted data type; expand a release for its evidence and caveats. Export the current results as CSV or JSON. The standalone `index.html` also works offline.

The separate **[Source entries view](https://usccolumbia.github.io/matverse/?view=sources)** searches all 3433 imported link entries from 15 inspected collections. This includes every extracted entry from [Blaiszik's list](https://usccolumbia.github.io/matverse/?view=sources&collection=blaiszik) (274 occurrences, 218 URLs) and [Seda Oturak's list](https://usccolumbia.github.io/matverse/?view=sources&collection=sedaoturak) (90 occurrences, 87 URLs). Filter by collection and scope; export labels, URLs and original sections. All are included in [sources.md](sources.md). The [coverage audit](docs/collection-coverage.md) records revisions, extraction boundaries and hashes. Imported links include adjacent domains and discovery resources; individual counts and licenses need their own evidence before entering the ranked dataset table.

**[All 14 Starrydata project datasets](docs/starrydata.md)** are individually searchable, with separate sample/curve/figure/paper counts and download links. The [45-file manifest](data/starrydata_files.json) retains file sizes and SHA-256 values corroborated against release asset metadata. Projects overlap and are subsets of the combined Starrydata entry.

**[Superconductivity datasets and resources](docs/superconductivity.md)** compare experimental critical temperatures, matched crystal structures, electronic bands, computed electron–phonon data and model-training releases, including Hennig-group contributions. Search recognizes “superconductor,” “superconducting,” “superconductivity” and “SuperCon.” When a source-list filter hides a catalog dataset, the search overview exposes matching dataset records and opens them with the query preserved.

The [requested-resource crosswalk](docs/requested-resources.md) maps the November resource list to existing datasets, newly added platforms, polymer/model resources and supporting papers. Original legacy URLs remain in the [source-entry inventory](https://usccolumbia.github.io/matverse/?view=sources&collection=user_resources_20261101).

## Materials dataset search tools

| Search tool | What to search |
|---|---|
| [Materials Data Facility (MDF)](https://www.materialsdatafacility.org/search) · [Homepage](https://www.materialsdatafacility.org/) | Search deposited materials datasets, metadata and properties. Access and licenses vary by deposit. |
| [Foundry-ML](https://foundry-ml.org/) | Discover structured, schema-described ML datasets within the MDF ecosystem; use the supported client to inspect and load data. |
| [Materials Cloud OPTIMADE Client](https://optimadeclient.materialscloud.io/) | Select a provider and child database, filter crystal structures, and inspect or download results. |
| [OPTIMADE provider registry](https://providers.optimade.org/) | Find provider index APIs and discover child structure databases; listing does not guarantee endpoint availability. |
| [NIST REMI](https://pages.nist.gov/remi/) | Discover materials informatics resources and example datasets; a resource guide rather than a uniform property database. |
| [OpenAlex](https://openalex.org/) | Find dataset papers and follow references/citations. Scholarly works are discovery leads, not materials-data payloads. |

The **[MDF property-dataset audit](docs/mdf-property-datasets.md)** selects eight structured releases with explicit record counts, target/unit schemas, stable identifiers and declared data rights. Ten targeted MDF searches returned 244 distinct deposits; existing-source mirrors and unverified leads remain distinguishable from new catalog entries. [Search the eight MDF additions](https://usccolumbia.github.io/matverse/?q=MDF-property-20261101).

## Materials properties: direct and original sources

**[All 148 MateriaViva property tables](docs/materiaviva-properties.md)** are separate searchable entries in [Materials properties](https://usccolumbia.github.io/matverse/?category=materials_properties). Find a specific property by its common name, abbreviation or source key. Each entry links directly to its pinned MateriaViva Parquet file and lists every contributing original provider separately, with value counts, linked structure counts, units and source/method provenance. Property subsets overlap their parent datasets; per-row licenses remain explicit.

## Specialized materials property datasets

The **[OpenAlex property-dataset survey](docs/specialized-properties.md)** adds 35 paper-backed releases spanning ionic conductivity and migration, ferroic/optical response, thermal and magnetic properties, alloy mechanics, hydrogen storage and combustion. Its 41 keyword searches and DDSE citation/reference traversal returned 1,761 distinct works; only releases with their own evidence enter the catalog. [Search these additions](https://usccolumbia.github.io/matverse/?q=property-focused).

The original **DDSE** paper is now linked explicitly to the existing **DigBat** record, with historical 2023/2024 counts separate from the June 2026 material and measurement totals. The survey compares structural coverage, experimental versus calculated labels, conditions, access, licenses and overlapping source lineages. [Query receipts and coverage limits](research/openalex_property_20261101/search_manifest.json).

## Materials datasets from Scientific Data

The **[Scientific Data survey](docs/scientific-data.md)** covers structure/DFT collections, property measurements, synthesis, spectroscopy and microstructure data. The journal-index metadata harvest retrieved 9,304 records through November 1, 2026; broad title screening yielded 1,514 candidates. Verified releases enter the ranked catalog; unresolved candidates stay in a separate searchable source inventory. [Search the new additions](https://usccolumbia.github.io/matverse/?q=%22Scientific-Data-survey-20261101%22) · [Browse all journal candidates](https://usccolumbia.github.io/matverse/?view=sources&collection=sdata_20261101). The report records release counts, structure availability, parentage, rights and search limits.

## Curated Data.gov materials datasets

The **[Data.gov selection report](docs/datagov-selection.md)** checks the supplied 320-result attachment and adds eight structured or evaluated datasets, including USGS XRD references, IUPAC solid–liquid equilibrium, cryogenic and ceramic properties, hafnia metrology, dielectric measurements and MgO spectra. Existing adsorption data remain linked; conditional development tables, polymers, software and handbooks stay separately labeled resources. [Search the shortlist](https://usccolumbia.github.io/matverse/?q=Data.gov-selection-20261101).

## Further dataset discoveries

The **[additional-dataset survey](docs/additional-datasets.md)** extends coverage to solid–liquid interfaces, one-dimensional materials, carbon allotropes, point defects, grain boundaries, irradiation, porous thermal/adsorption data, Heusler/spin transport, atomistic reference cohorts and experimental properties. Counts retain their units, parent overlaps and release-specific rights. [Search these additions](https://usccolumbia.github.io/matverse/?q=%22additional-materials-20261101%22).

## Matbench Discovery dataset-directory coverage

**[All 46 rows](docs/matbench-coverage.md)** in the [Matbench Discovery dataset directory](https://matbench-discovery.materialsproject.org/data/sets) are preserved in the [searchable source inventory](https://usccolumbia.github.io/matverse/?view=sources&collection=matbench_discovery_20261101). The audit adds 13 named releases/subsets and eight adjacent or unavailable-data resources. Existing family matches retain exact-release and counting limits; isolated-molecule data and unreleased training corpora are explicitly labeled.

## API-accessible / Agent-ready data sources

**[Search 20 API, SDK and bulk-file routes](https://usccolumbia.github.io/matverse/?view=apis)** · [Access guide and examples](docs/api-access.md) · [Machine-readable API registry](data/api_sources.json)

Find programmatic access to Materials Project, OQMD, AFLOW, COD, Alexandria, JARVIS, NOMAD, Materials Cloud, MPDS and other sources. Each route records its interface type, authentication, formats, scope, documentation and verification status. “Agent-ready” means a documented software access path; it does not certify data quality, complete labels or unrestricted reuse. Query APIs, metadata APIs, bulk SDKs and static downloads remain distinguishable.

**[OPTIMADE](https://www.optimade.org/)** (Open Databases Integration for Materials Design) standardizes structure queries, response attributes and pagination across participating databases. The [API guide](docs/api-access.md#optimade-one-standard-across-materials-databases) explains provider discovery, version checks, filters, coordinate fields and provider-specific property extensions. Standard access preserves each provider's authentication and licensing requirements.

Try the **[Materials Cloud OPTIMADE Client](https://optimadeclient.materialscloud.io/)** to select a provider and search its structures. The **[official clients directory](https://www.optimade.org/clients)** compares browser and Python clients. The [provider crosswalk](docs/api-access.md#providers-visible-in-the-supplied-screenshot) records all 17 provider options visible in the supplied screenshot, including Materials Cloud Archive, MPDD, Matterverse, NOMAD, ODBX, Open Materials Database, PSDI, TCOD, 2DMatpedia and AtomGPT.

**[Complete JARVIS audit](docs/jarvis-coverage.md):** all 13 rows in the homepage Databases table (numbered 1–7 and 9–14), all 65 named entries in its linked Figshare table, and all 66 current downloader names are included in the [searchable JARVIS source inventory](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_databases). Newly cataloged releases include QETB, FF, interfaces, surfaces, vacancies and electron/phonon Hamiltonians. Alternate portals and mirrors are identified without adding duplicate corpus totals.

## Browse by category

- [Aggregated and deduplicated crystal collections](#aggregated-crystals) (3)
- [Computed bulk inorganic crystals](#bulk-computed) (25)
- [Experimental crystallography and reference collections](#experimental-crystallography) (9)
- [Bulk and mixed-domain MLIP configurations](#mlip-configurations) (41)
- [Two-dimensional and layered materials](#two-dimensional) (12)
- [MOFs, COFs and zeolites](#porous-frameworks) (24)
- [Molecular crystals and ice](#molecular-crystals) (5)
- [Surfaces, interfaces and catalysis](#surfaces-catalysis) (18)
- [Materials properties](#materials-properties) (148)
- [Computed properties and prediction benchmarks](#property-benchmarks) (87)
- [Crystal generation and discovery benchmarks](#generation-benchmarks) (7)
- [Experimental properties and literature extraction](#experimental-properties) (114)
- [Diffraction, spectroscopy and characterization](#diffraction-spectroscopy) (30)

## Ranked catalog

Sizes descend **within each category**. Approximate figures use `~`, source lower bounds use `≥`, and unverified sizes appear last. Units remain explicit: these are volume rankings, not quality rankings. Click a dataset for its release, official download links, evidence and caveats.

<a id="aggregated-crystals"></a>
### Aggregated and deduplicated crystal collections

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [MateriaViva Open](docs/catalog/aggregated_crystals.md#materiaviva-open) | 10,903,588 | deduplicated crystal structures | open | Per row: CC BY 4.0, CC0 1.0, CC BY-SA 4.0, public domain, or MIT (provider declarations) |
| [LeMat-Bulk](docs/catalog/aggregated_crystals.md#lemat-bulk) | 6,725,590 | structure records | open | CC BY 4.0 |
| [LeMat-BulkUnique](docs/catalog/aggregated_crystals.md#lemat-bulkunique) | 5,438,436 | functional-specific unique records | open | CC BY 4.0 (card license section) |

<a id="bulk-computed"></a>
### Computed bulk inorganic crystals

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Alexandria](docs/catalog/bulk_computed.md#alexandria) | ~5,800,000 | DFT-relaxed structures | open | CC BY 4.0 (provider About page) |
| [AFLOW](docs/catalog/bulk_computed.md#aflow) | 3,929,948 | database entries | open | Provider terms: free for scientific, academic and non-commercial use; other use prohibited |
| [OQMD](docs/catalog/bulk_computed.md#oqmd) | 1,407,395 | materials entries | open | CC BY 4.0 (OQMD download terms) |
| [JARVIS-QETB / TB3PY DFT database](docs/catalog/bulk_computed.md#jarvis-qetb) | 829,574 | DFT structure records | open | CC BY 4.0 (Figshare deposit) |
| [GNoME released stable-materials set](docs/catalog/bulk_computed.md#gnome) | ~381,000 | novel structure records | open | CC BY-NC 4.0 (data); Apache 2.0 applies to code |
| [Materials Project](docs/catalog/bulk_computed.md#materials-project) | 271,325 | crystal structure records | registration | CC BY 4.0 for core data; GNoME-origin data carry separate BY-NC acceptance |
| [Carolina Materials Database](docs/catalog/bulk_computed.md#carolina) | 214,436 | inorganic materials entries | open | CC BY 4.0 (provider Terms of Use) |
| [PBEsol/SCAN 175k crystalline-material reference cohort](docs/catalog/bulk_computed.md#pbesol-scan-175k-2022) | ~175,000 | crystalline material records | open | CC BY 4.0 |
| [MP v2022.10.28](docs/catalog/bulk_computed.md#mp-frozen-2022) | 154,718 | relaxed material entries | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [DXMag Computational HeuslerDB — quaternary ML](docs/catalog/bulk_computed.md#dxmag-heusler-quaternary) | 131,544 | provider-reported compounds | open | CC BY 4.0 (explicit database declaration) |
| [DXMag Computational HeuslerDB — ternary DFT](docs/catalog/bulk_computed.md#dxmag-heusler-ternary) | 106,235 | DFT calculation rows | open | CC BY 4.0 (explicit database declaration) |
| [DXMag Computational HeuslerDB — all-d ML](docs/catalog/bulk_computed.md#dxmag-heusler-alld) | 105,763 | provider-reported compounds | open | CC BY 4.0 (explicit database declaration) |
| [CAMD autonomous crystal discovery corpus](docs/catalog/bulk_computed.md#camd-crystal-discoveries-2022) | 96,640 | crystal structure records | open | CC BY 4.0 |
| [JARVIS-DFT 3D](docs/catalog/bulk_computed.md#jarvis-dft-3d) | ~75,993 | structure records | open | CC BY 4.0 (3D Figshare dataset) |
| [Theoretical multinary perovskite oxides](docs/catalog/bulk_computed.md#multinary-perovskite-66516) | 66,516 | optimized oxide entries | open | Provider displays CCA4 (Creative Commons Attribution 4.0); exact linked licence text not exposed in parsed page |
| [MIP-3d materials informatics release](docs/catalog/bulk_computed.md#mip3d-release) | 33,078 | metadata/property records | open | CC BY 4.0 |
| [Materials Cloud 3D (MC3D)](docs/catalog/bulk_computed.md#mc3d) | 32,013 | unique optimized structures | open | CC BY 4.0 (Materials Cloud record) |
| [Layered intercalation crystal band structures](docs/catalog/bulk_computed.md#layered-intercalation-bandstructures) | 9,024 | intercalated crystal records | open | CC BY 4.0 |
| [Double-transition-metal MAX-phase precursors](docs/catalog/bulk_computed.md#dtm-max-phases-8712) | 8,712 | MAX-phase configuration records | open | CC BY 4.0 |
| [All-electron hybrid-functional materials database](docs/catalog/bulk_computed.md#all-electron-hybrid-7024) | 7,024 | inorganic material records | open | CC BY 4.0 |
| [SACADA three-periodic carbon allotropes](docs/catalog/bulk_computed.md#sacada) | 1,661 | carbon allotrope table entries | open | Not verified; public browsing/download does not establish redistribution rights |
| [Hybrid organic–inorganic perovskite DFT dataset](docs/catalog/bulk_computed.md#hoip-2017) | 1,346 | optimized hybrid-perovskite compounds | open | CC0 1.0 |
| [HEX high-pressure elemental crystals](docs/catalog/bulk_computed.md#hex-high-pressure-elements) | 228 | element-pressure ground-state cases | open | CC0 1.0 |
| [NIST MRAS amorphous structural models](docs/catalog/bulk_computed.md#nist-mras-amorphous) | 50 | final amorphous structure files | open | NIST Open License; see linked dataset-specific metadata and NIST terms |
| [NLR MatDB (formerly NRELMatDB)](docs/catalog/bulk_computed.md#nlr-matdb) | Unranked | materials | open | Not verified |

<a id="experimental-crystallography"></a>
### Experimental crystallography and reference collections

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Cambridge Structural Database (CSD)](docs/catalog/experimental_crystallography.md#csd) | 1,431,347 | crystal structures | mixed | Not verified |
| [Crystallography Open Database (COD)](docs/catalog/experimental_crystallography.md#cod) | 535,025 | entries | open | CC0 |
| [Materials Platform for Data Science (MPDS / PAULING FILE)](docs/catalog/experimental_crystallography.md#mpds-pauling-file) | 424,820 | crystalline structures | mixed | Not verified |
| [NIMS AtomWork-Adv](docs/catalog/experimental_crystallography.md#atomwork-adv) | 409,723 | crystal structures | commercial | Commercial licensed access under NIMS provider terms; limited downloads; trial has no download permission. |
| [Pearson's Crystal Data](docs/catalog/experimental_crystallography.md#pearsons-crystal-data) | ~395,000 | structural datasets | commercial | Not verified |
| [Inorganic Crystal Structure Database (ICSD)](docs/catalog/experimental_crystallography.md#icsd) | 347,985 | crystal structures | commercial | Not verified |
| [NIMS AtomWork](docs/catalog/experimental_crystallography.md#atomwork) | 82,000 | crystal structures | registration | NIMS proprietary terms: written permission required for reproduction, republication or third-party distribution; bulk acquisition and scraping prohibited. |
| [MAGNDATA](docs/catalog/experimental_crystallography.md#magndata) | ≥2,000 | magnetic structures | mixed | Not verified |
| [American Mineralogist Crystal Structure Database (AMCSD)](docs/catalog/experimental_crystallography.md#amcsd) | Unranked | crystal structures | open | Not verified |

<a id="mlip-configurations"></a>
### Bulk and mixed-domain MLIP configurations

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [COSMOSDataset](docs/catalog/mlip_configurations.md#cosmos-sevennet-omni) | 242,788,218 | aggregate configurations | mixed | CC-BY-4.0 declared for assembly/deposit; individual parent terms retained |
| [LeMat-Traj](docs/catalog/mlip_configurations.md#lemat-traj) | 121,274,458 | atomic configurations | open | CC BY 4.0 |
| [Open Materials 2024 (OMat24)](docs/catalog/mlip_configurations.md#omat24) | 101,849,946 | atomic configurations | open | CC BY 4.0 |
| [ELEMENTA public core release](docs/catalog/mlip_configurations.md#elementa-public) | ~39,000,000 | atomic configurations | open | CC BY-NC 4.0 |
| [SoLiD26 solid–liquid interface configurations](docs/catalog/mlip_configurations.md#solid26) | 15,379,823 | atomic configuration frames | open | CC BY 4.0 |
| [sAlex25](docs/catalog/mlip_configurations.md#salex25) | ~14,000,000 | out-of-equilibrium configurations | open | CC BY 4.0 (Alexandria provider terms) |
| [sAlex (OMat24 distribution)](docs/catalog/mlip_configurations.md#salex-omat24) | 11,000,983 | atomic configurations | open | CC BY 4.0 |
| [ELEMENTA Spin](docs/catalog/mlip_configurations.md#elementa-spin) | ~4,700,000 | magnetic configuration frames | open | CC BY-NC 4.0 |
| [Materials Project Trajectory (MPtrj)](docs/catalog/mlip_configurations.md#mptrj) | 1,580,395 | atomic configurations | open | MIT (Figshare dataset record) |
| [MP-ALOE](docs/catalog/mlip_configurations.md#mp-aloe) | 909,792 | DFT configuration frames | open | Not verified for downloadable dataset |
| [Subsampled Alexandria Validation Set](docs/catalog/mlip_configurations.md#salex-omat24-validation) | 553,218 | configurations | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [MatPES2025.1 — PBE](docs/catalog/mlip_configurations.md#matpes-pbe-2025-1) | 434,712 | configurations | open | Not verified for frozen2025.1 payload: current Hugging Face dataset card declares BSD-3-Clause; Matbench registry lists MIT. Verify release-specific data terms. |
| [MatPES](docs/catalog/mlip_configurations.md#matpes) | ~400,000 | sampled configurations | open | BSD 3-Clause (current Hugging Face dataset card); Matbench directory lists MIT, so verify historical frozen-release terms separately. |
| [MatPES2025.1 — r2SCAN](docs/catalog/mlip_configurations.md#matpes-r2scan-2025-1) | 387,897 | configurations | open | Not verified for frozen2025.1 payload: current Hugging Face dataset card declares BSD-3-Clause; Matbench registry lists MIT. Verify release-specific data terms. |
| [ALIGNN-FF training dataset](docs/catalog/mlip_configurations.md#alignn-ff) | 307,113 | energy-labeled configurations | open | Not verified for training download |
| [Polyanion sodium cathode atomic structure and dynamics](docs/catalog/mlip_configurations.md#polyanion-sodium-cathode-2025) | 298,144 | periodic atomic configurations | open | CC BY 4.0 |
| [Massive Atomic Diversity (MAD-1.5)](docs/catalog/mlip_configurations.md#mad15) | 216,803 | atomic configurations | open | Not verified for this archived version |
| [MPF.2021.2.8](docs/catalog/mlip_configurations.md#mpf2021) | 187,687 | ionic-step configurations | open | CC BY 4.0 (Figshare record) |
| [SevenNet-Omni domain-bridging set (DBS)](docs/catalog/mlip_configurations.md#sevennet-omni-dbs) | ~125,000 | cross-domain DFT configuration records | open | CC BY 4.0 |
| [Carbon-data synthetic atomistic trajectories](docs/catalog/mlip_configurations.md#carbon-data-gap17) | 114,660 | MD snapshots | open | Not verified |
| [Massive Atomic Diversity](docs/catalog/mlip_configurations.md#mad-original-2025) | 95,595 | configurations | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [Nb–Ta–V BCC solid-solution DFT configurations](docs/catalog/mlip_configurations.md#nb-ta-v-bcc-dft) | 19,800 | sampled starting alloy configurations | open | CC BY 4.0 (inspected Figshare mirrors) |
| [IAEA CascadesDB collision-cascade simulations](docs/catalog/mlip_configurations.md#iaea-cascadesdb) | 17,024 | collision-cascade simulations | open | CC BY 4.0 for data and metadata unless individually stated otherwise |
| [Carbon GAP-20 DFT reference database](docs/catalog/mlip_configurations.md#carbon-gap20) | ~17,000 | DFT atomic configurations | open | CC BY 4.0 |
| [Multiphase Ti and Ti-6Al-4V MLIP configurations](docs/catalog/mlip_configurations.md#ti-ti64-multiphase) | 15,563 | selected training configurations | open | CC BY 4.0; British Crown Owned Copyright attribution retained in metadata |
| [SiOx-ACE-24 silicon–oxygen reference configurations](docs/catalog/mlip_configurations.md#siox-ace24) | 11,428 | normalized training configurations | open | CC BY 4.0 |
| [Carbon GAP-20U revised training configurations](docs/catalog/mlip_configurations.md#carbon-gap20u) | 6,088 | DFT reference configurations | open | GPL-3.0 |
| [Materials Project non-crystalline AIMD and diffusivity database](docs/catalog/mlip_configurations.md#mp-noncrystalline-aimd) | 5,120 | 5000 K AIMD parent systems | open | Not verified for dataset files; MPContribs labels project CCA4, but release-file terms were not independently checked |
| [P-GAP-20 phosphorus reference configurations](docs/catalog/mlip_configurations.md#p-gap20) | 4,798 | normalized training configurations | open | CC BY 4.0 |
| [MACE-MP-MOF0 DFT training configurations](docs/catalog/mlip_configurations.md#mace-mp-mof0-training) | 4,311 | DFT configuration frames | open | CC BY 4.0 (explicit mace-mof-0 folder data license) |
| [GO-MACE-23 graphene-oxide reference cohort](docs/catalog/mlip_configurations.md#go-mace23) | 3,816 | normalized training configurations | open | CC BY 4.0 |
| [SiO2-GAP-22 silica training cohort](docs/catalog/mlip_configurations.md#sio2-gap22) | 3,074 | normalized training configurations | open | CC BY 4.0 |
| [Paracrystalline/amorphous silicon structural models](docs/catalog/mlip_configurations.md#asi-paracrystalline-models) | 3,069 | final melt–quench configuration frames | open | CC BY 4.0 |
| [GST-GAP-22 PBE reference cohort](docs/catalog/mlip_configurations.md#gst-gap22-pbe) | 2,692 | normalized training configurations | open | CC BY 4.0 |
| [Si-GAP-18 silicon training cohort](docs/catalog/mlip_configurations.md#si-gap18) | 2,475 | normalized training configurations | open | CC BY-NC-SA 4.0 (load-atoms distribution; original Zenodo metadata uses other-open) |
| [Chalcogenide vacancy structure-reconstruction dataset](docs/catalog/mlip_configurations.md#chalcogenide-vacancy-reconstructions) | ~130 | neutral cation-vacancy defects | open | Not verified; Zenodo metadata did not expose an explicit dataset licence |
| [ElectroFace electrochemical interface trajectories](docs/catalog/mlip_configurations.md#electroface-trajectories) | 71 | trajectory archive packages | open | CC BY 4.0 |
| [Fe–Ni–Cr irradiated and relaxed atomistic configurations](docs/catalog/mlip_configurations.md#fenicr-irradiated-relaxed-md) | 2 | released atomistic sample configurations | open | CC BY 4.0 (explicit file-level licences) |
| [Amorphous alumina bulk/surface DFT training release](docs/catalog/mlip_configurations.md#amorphous-alumina-deep-potential) | Unranked | DFT reference configurations | open | GPL-3.0 as explicitly applied to the repository containing data; inspect downstream distribution obligations |
| [Massive Atomic Diversity (MAD-1.6)](docs/catalog/mlip_configurations.md#mad16) | Unranked | atomic configurations | open | CC BY 4.0 (Materials Cloud archive metadata) |
| [OpenLAM TrainingSet](docs/catalog/mlip_configurations.md#openlam-training) | Unranked | atomic configurations | mixed | Not verified |

<a id="two-dimensional"></a>
### Two-dimensional and layered materials

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Computational 2D Materials Database (C2DB)](docs/catalog/two_dimensional.md#c2db) | 16,789 | database rows | mixed | Not verified |
| [van der Waals Bilayer Database (BiDB)](docs/catalog/two_dimensional.md#bidb) | 8,451 | homobilayer configurations | open | Not verified |
| [2DMatPedia](docs/catalog/two_dimensional.md#2dmatpedia) | 6,351 | monolayer structures | open | CC BY 4.0 |
| [Materials Cloud Two-Dimensional Structure Database (MC2D)](docs/catalog/two_dimensional.md#mc2d) | 3,077 | monolayer compounds | open | Creative Commons Attribution 4.0 International |
| [Quantum Point Defects Database (QPOD)](docs/catalog/two_dimensional.md#qpod) | 2,061 | defect-charge-state rows | open | Not verified |
| [JARVIS-DFT 2D snapshot](docs/catalog/two_dimensional.md#jarvis-2d) | 1,103 | 2D material records | open | CC BY 4.0 |
| [BMDS bilayer electronic and transport dataset](docs/catalog/two_dimensional.md#bmds-bilayers-760) | 760 | bilayer materials | open | CC BY 4.0 |
| [CMR C2DM transition-metal monolayer electronic structures (2015)](docs/catalog/two_dimensional.md#cmr-c2dm-2015) | 494 | ASE calculation/structure rows | open | Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification |
| [Zhou–Poncé–Charlier 2D spin-Hall / Wannier dataset](docs/catalog/two_dimensional.md#zhou-2d-spin-hall-426) | 426 | nonmagnetic monolayers | open | CC BY 4.0 (record metadata) |
| [2D-Alloy Database](docs/catalog/two_dimensional.md#2d-alloys) | 400 | alloy monolayers | open | Not verified |
| [van der Waals 2D Heterostructure Database (HetDB)](docs/catalog/two_dimensional.md#hetdb) | 336 | heterobilayer structures | open | Not verified |
| [AC-2D-22 amorphous graphene benchmark subset](docs/catalog/two_dimensional.md#ac2d-amorphous-graphene) | 150 | selected 200-atom configurations | open | CC BY 4.0 original deposit; CC BY-NC-SA 4.0 normalized load-atoms distribution |

<a id="porous-frameworks"></a>
### MOFs, COFs and zeolites

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Open Direct Air Capture 2025 (ODAC25)](docs/catalog/porous_frameworks.md#odac25) | ~70,000,000 | DFT configuration frames | registration | Creative Commons Attribution 4.0 International (dataset) |
| [Open Direct Air Capture 2023 (ODAC23)](docs/catalog/porous_frameworks.md#odac23) | 38,983,748 | DFT configuration frames | open | Creative Commons Attribution 4.0 International |
| [PORMAKE hypothetical MOFs for MOFTransformer](docs/catalog/porous_frameworks.md#pormake-moftransformer-1m) | 1,118,074 | hypothetical MOF structures | open | CC BY 4.0 |
| [Deem hypothetical zeolites / PCOD SLC-good](docs/catalog/porous_frameworks.md#pcod-zeolites) | ~331,000 | hypothetical zeolite frameworks | open | Not verified |
| [Boyd-Woo hypothetical MOFs for wet flue-gas capture](docs/catalog/porous_frameworks.md#boyd-woo) | 324,426 | generated MOF structures | open | Creative Commons Attribution 4.0 International |
| [ab initio REPEAT Charge MOF Database (ARC-MOF)](docs/catalog/porous_frameworks.md#arc-mof) | ~280,000 | MOF structures | open | Creative Commons Attribution 4.0 International |
| [ReDD-COFFEE](docs/catalog/porous_frameworks.md#redd-coffee) | 268,687 | generated COF structures | open | Creative Commons Attribution Non Commercial Share Alike 4.0 International |
| [MOFX-DB computational adsorption database](docs/catalog/porous_frameworks.md#mofx-db) | 168,534 | parent-database structure records | open | Not verified: open API and bulk downloads; no dataset-wide reuse license confirmed |
| [Wilmer hypothetical MOF database (hMOF)](docs/catalog/porous_frameworks.md#hmof-wilmer) | 137,953 | generated MOF structures | mixed | Not verified |
| [MOSAEC MOF Database (MOSAEC-DB)](docs/catalog/porous_frameworks.md#mosaec-db) | ~124,000 | processed MOF structures | mixed | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International; CIF access also requires CSD license |
| [Mercado hypothetical 2D and 3D COFs](docs/catalog/porous_frameworks.md#hcof-mercado) | 69,840 | generated COF structures | open | Creative Commons Attribution 4.0 International |
| [SymGNN aluminum-substituted zeolite adsorption dataset](docs/catalog/porous_frameworks.md#symgnn-zeolite-adsorption) | 57,084 | substitution/property cases | open | CC BY 4.0 (Zenodo archived release metadata) |
| [CoRE MOF Database](docs/catalog/porous_frameworks.md#core-mof) | 43,439 | MOF structure records | mixed | CC BY 4.0 for Zenodo SI deposit; CSD-derived files have additional CCDC access terms |
| [Zeo-1](docs/catalog/porous_frameworks.md#zeo-1) | 32,550 | geometry-optimization frames | open | Creative Commons Attribution 4.0 International |
| [Quantum MOF Database (QMOF)](docs/catalog/porous_frameworks.md#qmof) | ≥20,000 | DFT-optimized structures | open | CC BY 4.0 |
| [ToBaCCo hypothetical MOF structure database](docs/catalog/porous_frameworks.md#tobacco-mofs) | 13,511 | valid hypothetical MOF structures | open | Not verified: public MOFX-DB structure downloads; reuse license not confirmed |
| [TBHubbard MOF Hamiltonians](docs/catalog/porous_frameworks.md#tbhubbard-mofs) | 10,000 | MOF tight-binding cases | open | Custom dataset terms, contents not verified; DataCite links a v4.1 custom licence (not CC0) |
| [AdsZeo equilibrium methane adsorption configurations](docs/catalog/porous_frameworks.md#adszeo-equilibrium-configurations) | 4,775 | zeolite framework realizations | open | CC BY 4.0 (Zenodo data metadata) |
| [MOFSimplify stability-labelled MOFs](docs/catalog/porous_frameworks.md#mofsimplify-stability) | 3,132 | thermal-stability-labelled MOFs | open | CC BY 4.0 |
| [Computation-Ready Experimental COF Database (CoRE COF)](docs/catalog/porous_frameworks.md#core-cof) | 1,242 | COF structure files | open | Not verified |
| [CURATED covalent organic frameworks](docs/catalog/porous_frameworks.md#curated-cofs) | 871 | valid COF structures | open | Creative Commons Attribution 4.0 International (Materials Cloud files) |
| [CRAFTED MOF adsorption isotherms](docs/catalog/porous_frameworks.md#crafted-mof-isotherms) | 690 | parent MOF structures | open | CDLA-Sharing-1.0 for generated data; CC BY 4.0 for all CIF folders; MIT for CO2/N2 force-field definitions |
| [Open-framework aluminophosphate structure database](docs/catalog/porous_frameworks.md#alpo-open-framework) | 312 | crystal structures | open | CC BY 4.0 |
| [IZA Database of Zeolite Structures](docs/catalog/porous_frameworks.md#iza-zeolites) | 270 | framework topology types | open | Not verified |

<a id="molecular-crystals"></a>
### Molecular crystals and ice

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Open Molecular Crystals 2025 (OMC25)](docs/catalog/molecular_crystals.md#omc25) | 26,257,042 | DFT configuration frames | mixed | Creative Commons Attribution 4.0 International (dataset) |
| [Organic Superconductor Database (OSD)](docs/catalog/molecular_crystals.md#osd-organic-superconductors) | 184 | crystal structure entries | mixed | Not verified |
| [PAH101 molecular-crystal GW+BSE dataset](docs/catalog/molecular_crystals.md#pah101-gwbse) | 101 | molecular crystal records | open | Not verified separately for deposited data; article/preprint CC BY is not used as an external data licence |
| [X23 diffusion Monte Carlo benchmark](docs/catalog/molecular_crystals.md#x23-dmc) | 23 | benchmark crystal systems | open | Not verified |
| [DMC-ICE13](docs/catalog/molecular_crystals.md#dmc-ice13) | 13 | benchmark periodic ice polymorphs | open | Not verified |

<a id="surfaces-catalysis"></a>
### Surfaces, interfaces and catalysis

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Open Catalyst 2020 (OC20)](docs/catalog/surfaces_catalysis.md#oc20) | 133,934,018 | DFT configuration frames | open | Creative Commons Attribution 4.0 International |
| [Open Catalyst 2020 Multiple Adsorbates](docs/catalog/surfaces_catalysis.md#oc20-mads) | 21,804,758 | configurations | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [Open Catalyst 2020 Clean Slabs](docs/catalog/surfaces_catalysis.md#oc20-slabs) | 18,323,074 | configurations | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [AQCat25 heterogeneous-catalysis dataset](docs/catalog/surfaces_catalysis.md#aqcat25) | ~13,500,000 | DFT records/frames | registration | CC BY-NC-SA 4.0 |
| [Open Catalyst 2022 (OC22)](docs/catalog/surfaces_catalysis.md#oc22) | ~9,854,504 | DFT configuration frames | open | Creative Commons Attribution 4.0 International |
| [Open Catalyst 2025 (OC25)](docs/catalog/surfaces_catalysis.md#oc25) | 7,801,261 | DFT configuration evaluations | registration | Creative Commons Attribution 4.0 International (dataset) |
| [Open Catalyst 2020 Nudged Elastic Band Benchmark](docs/catalog/surfaces_catalysis.md#oc20-neb) | 1,375,930 | configurations | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [SUNCAT bimetallic adsorption calculations](docs/catalog/surfaces_catalysis.md#bimetallic-catalysis-2019) | ≥90,000 | DFT calculations | open | CC BY 4.0 |
| [Open Catalyst 2020 Dense Adsorbate Sampling](docs/catalog/surfaces_catalysis.md#oc20-dense) | 85,658 | initial adsorption configurations | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [Work function and cleavage energy surface database](docs/catalog/surfaces_catalysis.md#work-function-cleavage-surfaces) | 58,332 | surface configuration records | open | Creative Commons Attribution Non Commercial 4.0 International (CC BY-NC 4.0) |
| [BEAST DB](docs/catalog/surfaces_catalysis.md#beast-db) | ≥20,000 | electrochemical DFT calculations | open | Not verified |
| [Homer aluminum grain-boundary structures across 5D space](docs/catalog/surfaces_catalysis.md#homer-aluminum-gb-7304) | 7,304 | minimum-energy grain-boundary structures | open | CC BY 4.0 |
| [Computational Single-Atom Catalyst Database (NCEPU)](docs/catalog/surfaces_catalysis.md#sac-ncepu) | 1,197 | optimized catalyst configurations | open | Not verified |
| [Organic chains chemisorbed on silicon surfaces](docs/catalog/surfaces_catalysis.md#si-organic-chain-slab-2026) | ≥700 | optimized adsorbate–slab configurations | open | CC BY 4.0 |
| [JARVIS / InterMat surface release](docs/catalog/surfaces_catalysis.md#jarvis-surfacedb) | 607 | surface calculation records | open | CC BY 4.0 (Figshare deposit) |
| [JARVIS InterfacDB / InterMat interface release](docs/catalog/surfaces_catalysis.md#jarvis-interfacedb) | 593 | interface calculation records | open | CC BY 4.0 (Figshare deposit) |
| [GBDB elemental-metal grain-boundary DFT database](docs/catalog/surfaces_catalysis.md#gbdb-elemental-metals) | 327 | grain-boundary structures | open | Not verified for released data |
| [Elemental crystal surface energies and Wulff shapes](docs/catalog/surfaces_catalysis.md#elemental-surface-energy-2016) | ≥100 | elemental crystal polymorphs | open | CC0 1.0 |

<a id="materials-properties"></a>
### Materials properties

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [MateriaViva — Electronic band gap](docs/catalog/materials_properties.md#materiaviva-property-band-gap) | 13,943,575 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Formation energy per atom](docs/catalog/materials_properties.md#materiaviva-property-formation-energy-per-atom) | 12,377,989 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Total energy per atom](docs/catalog/materials_properties.md#materiaviva-property-total-energy-per-atom) | 12,091,066 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Space group number](docs/catalog/materials_properties.md#materiaviva-property-spacegroup-number) | 9,658,652 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Energy above convex hull](docs/catalog/materials_properties.md#materiaviva-property-energy-above-hull) | 8,895,858 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Total magnetization](docs/catalog/materials_properties.md#materiaviva-property-total-magnetization) | 7,064,021 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Density of states at Fermi level](docs/catalog/materials_properties.md#materiaviva-property-dos-at-fermi) | 6,794,075 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Direct electronic band gap](docs/catalog/materials_properties.md#materiaviva-property-band-gap-direct) | 6,719,595 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Phase separation energy](docs/catalog/materials_properties.md#materiaviva-property-phase-separation-energy) | 6,715,271 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Volume per atom](docs/catalog/materials_properties.md#materiaviva-property-volume-per-atom) | 5,303,898 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Maximum residual force](docs/catalog/materials_properties.md#materiaviva-property-max-residual-force) | 3,235,999 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Structure prototype](docs/catalog/materials_properties.md#materiaviva-property-structure-prototype) | 3,007,443 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Mass density](docs/catalog/materials_properties.md#materiaviva-property-density) | 2,675,966 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Carbon dioxide uptake](docs/catalog/materials_properties.md#materiaviva-property-co2-uptake) | 1,405,390 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Carbon dioxide heat of adsorption](docs/catalog/materials_properties.md#materiaviva-property-co2-heat-of-adsorption) | 1,142,345 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Magnetization per atom](docs/catalog/materials_properties.md#materiaviva-property-magnetization-per-atom) | 960,839 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Poisson ratio](docs/catalog/materials_properties.md#materiaviva-property-poisson-ratio) | 882,331 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Largest cavity diameter](docs/catalog/materials_properties.md#materiaviva-property-largest-cavity-diameter) | 493,874 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Pore limiting diameter](docs/catalog/materials_properties.md#materiaviva-property-pore-limiting-diameter) | 493,874 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Void fraction](docs/catalog/materials_properties.md#materiaviva-property-void-fraction) | 468,330 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Gravimetric surface area](docs/catalog/materials_properties.md#materiaviva-property-surface-area-gravimetric) | 426,130 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Structural dimensionality](docs/catalog/materials_properties.md#materiaviva-property-dimensionality) | 419,324 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Young's modulus](docs/catalog/materials_properties.md#materiaviva-property-youngs-modulus) | 406,893 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Pore volume](docs/catalog/materials_properties.md#materiaviva-property-pore-volume) | 297,226 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Nitrogen uptake](docs/catalog/materials_properties.md#materiaviva-property-n2-uptake) | 289,129 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Carbon dioxide / nitrogen selectivity](docs/catalog/materials_properties.md#materiaviva-property-co2-n2-selectivity) | 287,610 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Temperature-swing working capacity](docs/catalog/materials_properties.md#materiaviva-property-working-capacity-temperature-swing) | 287,610 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Vacuum-swing working capacity](docs/catalog/materials_properties.md#materiaviva-property-working-capacity-vacuum-swing) | 287,610 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Nitrogen heat of adsorption](docs/catalog/materials_properties.md#materiaviva-property-n2-heat-of-adsorption) | 285,827 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Direct band gap flag](docs/catalog/materials_properties.md#materiaviva-property-is-gap-direct) | 264,982 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Electronic dielectric constant](docs/catalog/materials_properties.md#materiaviva-property-dielectric-constant-electronic) | 262,400 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Measurement temperature](docs/catalog/materials_properties.md#materiaviva-property-measurement-temperature) | 244,260 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Bulk modulus — Voigt–Reuss–Hill](docs/catalog/materials_properties.md#materiaviva-property-bulk-modulus-vrh) | 202,894 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Shear modulus — Voigt–Reuss–Hill](docs/catalog/materials_properties.md#materiaviva-property-shear-modulus-vrh) | 199,927 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Experimentally observed flag](docs/catalog/materials_properties.md#materiaviva-property-experimentally-observed) | 192,278 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Volumetric surface area](docs/catalog/materials_properties.md#materiaviva-property-surface-area-volumetric) | 180,462 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Fermi energy](docs/catalog/materials_properties.md#materiaviva-property-fermi-energy) | 173,661 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Magnetization per volume](docs/catalog/materials_properties.md#materiaviva-property-magnetization-per-volume) | 170,211 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Stability flag](docs/catalog/materials_properties.md#materiaviva-property-is-stable) | 170,211 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Metallicity flag](docs/catalog/materials_properties.md#materiaviva-property-is-metal) | 170,153 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Magnetic ordering](docs/catalog/materials_properties.md#materiaviva-property-magnetic-ordering) | 155,422 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Decomposition energy](docs/catalog/materials_properties.md#materiaviva-property-decomposition-energy) | 153,566 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Total dielectric constant](docs/catalog/materials_properties.md#materiaviva-property-dielectric-constant-total) | 152,653 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Bulk modulus — Voigt](docs/catalog/materials_properties.md#materiaviva-property-bulk-modulus-voigt) | 151,596 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Bulk modulus — Reuss](docs/catalog/materials_properties.md#materiaviva-property-bulk-modulus-reuss) | 151,536 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Longitudinal sound velocity](docs/catalog/materials_properties.md#materiaviva-property-sound-velocity-longitudinal) | 151,400 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Shear modulus — Voigt](docs/catalog/materials_properties.md#materiaviva-property-shear-modulus-voigt) | 149,937 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Transverse sound velocity](docs/catalog/materials_properties.md#materiaviva-property-sound-velocity-transverse) | 148,518 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Framework T-atom density](docs/catalog/materials_properties.md#materiaviva-property-framework-density) | 148,197 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Shear modulus — Reuss](docs/catalog/materials_properties.md#materiaviva-property-shear-modulus-reuss) | 146,626 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Chemical name](docs/catalog/materials_properties.md#materiaviva-property-chemical-name) | 141,432 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Energy per framework T atom](docs/catalog/materials_properties.md#materiaviva-property-energy-per-t-atom) | 136,008 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Decomposition products](docs/catalog/materials_properties.md#materiaviva-property-decomposes-to) | 130,373 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Topological class](docs/catalog/materials_properties.md#materiaviva-property-topology-class) | 126,094 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Average oxidation states](docs/catalog/materials_properties.md#materiaviva-property-average-oxidation-states) | 124,820 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Oxidation states](docs/catalog/materials_properties.md#materiaviva-property-oxidation-states) | 124,820 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Predicted synthesizability flag](docs/catalog/materials_properties.md#materiaviva-property-predicted-synthesizable) | 98,303 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Conduction band minimum](docs/catalog/materials_properties.md#materiaviva-property-cbm) | 95,095 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Valence band maximum](docs/catalog/materials_properties.md#materiaviva-property-vbm) | 95,095 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Topological invariant](docs/catalog/materials_properties.md#materiaviva-property-topology-invariant) | 82,861 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Magnetic species](docs/catalog/materials_properties.md#materiaviva-property-magnetic-species) | 69,385 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Seebeck coefficient](docs/catalog/materials_properties.md#materiaviva-property-seebeck-coefficient) | 67,176 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Thermoelectric power factor](docs/catalog/materials_properties.md#materiaviva-property-power-factor) | 67,172 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Imaginary phonon flag](docs/catalog/materials_properties.md#materiaviva-property-has-imaginary-phonon) | 64,437 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Minimum phonon frequency](docs/catalog/materials_properties.md#materiaviva-property-phonon-min-frequency) | 64,437 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Maximum phonon frequency](docs/catalog/materials_properties.md#materiaviva-property-phonon-max-frequency) | 64,394 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Largest free path diameter](docs/catalog/materials_properties.md#materiaviva-property-largest-free-path-diameter) | 51,554 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Pore channel count](docs/catalog/materials_properties.md#materiaviva-property-pore-channel-count) | 41,942 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Lattice thermal conductivity](docs/catalog/materials_properties.md#materiaviva-property-lattice-thermal-conductivity) | 39,461 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Symmetry indicators](docs/catalog/materials_properties.md#materiaviva-property-symmetry-indicators) | 36,516 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Maximum residual stress](docs/catalog/materials_properties.md#materiaviva-property-max-residual-stress) | 30,230 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Superconducting critical temperature](docs/catalog/materials_properties.md#materiaviva-property-tc-superconducting) | 26,613 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Heat of formation](docs/catalog/materials_properties.md#materiaviva-property-heat-of-formation) | 24,944 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Mineral name](docs/catalog/materials_properties.md#materiaviva-property-mineral-name) | 24,103 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Debye temperature](docs/catalog/materials_properties.md#materiaviva-property-debye-temperature) | 23,387 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Heat capacity](docs/catalog/materials_properties.md#materiaviva-property-heat-capacity) | 21,761 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Average battery voltage](docs/catalog/materials_properties.md#materiaviva-property-average-voltage) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Battery formula](docs/catalog/materials_properties.md#materiaviva-property-battery-formula) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Charged electrode stability](docs/catalog/materials_properties.md#materiaviva-property-electrode-stability-charged) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Discharged electrode stability](docs/catalog/materials_properties.md#materiaviva-property-electrode-stability-discharged) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Electrode volume change](docs/catalog/materials_properties.md#materiaviva-property-electrode-volume-change) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Gravimetric battery capacity](docs/catalog/materials_properties.md#materiaviva-property-capacity-gravimetric) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Gravimetric battery energy density](docs/catalog/materials_properties.md#materiaviva-property-energy-density-gravimetric) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Maximum battery voltage step](docs/catalog/materials_properties.md#materiaviva-property-max-voltage-step) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Number of battery voltage steps](docs/catalog/materials_properties.md#materiaviva-property-num-voltage-steps) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Volumetric battery capacity](docs/catalog/materials_properties.md#materiaviva-property-capacity-volumetric) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Volumetric battery energy density](docs/catalog/materials_properties.md#materiaviva-property-energy-density-volumetric) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Working battery ion](docs/catalog/materials_properties.md#materiaviva-property-working-ion) | 20,671 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Framework bond dissociation energy](docs/catalog/materials_properties.md#materiaviva-property-framework-bond-dissociation-energy) | 20,243 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Elastic anisotropy](docs/catalog/materials_properties.md#materiaviva-property-elastic-anisotropy) | 18,255 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Maximum electric field gradient](docs/catalog/materials_properties.md#materiaviva-property-nmr-efg-max) | 17,636 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Ionic dielectric constant](docs/catalog/materials_properties.md#materiaviva-property-dielectric-constant-ionic) | 17,104 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Spin–orbit spillage](docs/catalog/materials_properties.md#materiaviva-property-spillage) | 16,656 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Refractive index](docs/catalog/materials_properties.md#materiaviva-property-refractive-index) | 15,273 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Spectroscopic limited maximum efficiency](docs/catalog/materials_properties.md#materiaviva-property-slme) | 13,715 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Structure-prediction R factor](docs/catalog/materials_properties.md#materiaviva-property-structure-prediction-r-factor) | 12,415 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Piezoelectric modulus](docs/catalog/materials_properties.md#materiaviva-property-piezoelectric-modulus) | 10,974 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Lattice thermal conductivity — coherence contribution](docs/catalog/materials_properties.md#materiaviva-property-lattice-thermal-conductivity-coherence) | 8,434 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Lattice thermal conductivity — particle contribution](docs/catalog/materials_properties.md#materiaviva-property-lattice-thermal-conductivity-particle) | 8,420 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Equation-of-state bulk modulus](docs/catalog/materials_properties.md#materiaviva-property-eos-bulk-modulus) | 8,350 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Thermal conductivity](docs/catalog/materials_properties.md#materiaviva-property-thermal-conductivity) | 7,867 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Thermal expansion coefficient](docs/catalog/materials_properties.md#materiaviva-property-thermal-expansion) | 7,865 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Maximum Born effective charge](docs/catalog/materials_properties.md#materiaviva-property-born-effective-charge-max) | 7,741 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Exfoliation energy](docs/catalog/materials_properties.md#materiaviva-property-exfoliation-energy) | 6,815 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — GLLB-SC derivative discontinuity](docs/catalog/materials_properties.md#materiaviva-property-gllbsc-derivative-discontinuity) | 6,571 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Birefringence](docs/catalog/materials_properties.md#materiaviva-property-birefringence) | 6,050 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Electron effective mass](docs/catalog/materials_properties.md#materiaviva-property-effective-mass-electron) | 5,701 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Hole effective mass](docs/catalog/materials_properties.md#materiaviva-property-effective-mass-hole) | 5,687 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Superconductor class](docs/catalog/materials_properties.md#materiaviva-property-superconductor-class) | 5,540 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Magnetic polarization](docs/catalog/materials_properties.md#materiaviva-property-magnetic-polarization) | 5,434 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Interlayer binding energy](docs/catalog/materials_properties.md#materiaviva-property-interlayer-binding-energy) | 4,712 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Measurement pressure](docs/catalog/materials_properties.md#materiaviva-property-measurement-pressure) | 4,443 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Work function](docs/catalog/materials_properties.md#materiaviva-property-work-function) | 4,225 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Direction of maximum piezoelectric response](docs/catalog/materials_properties.md#materiaviva-property-piezoelectric-max-direction) | 4,053 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Continuous symmetry measure](docs/catalog/materials_properties.md#materiaviva-property-continuous-symmetry-measure) | 3,940 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Coordination environments](docs/catalog/materials_properties.md#materiaviva-property-coordination-environments) | 3,940 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Second-harmonic generation coefficient](docs/catalog/materials_properties.md#materiaviva-property-shg-coefficient) | 3,429 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Ion migration barrier](docs/catalog/materials_properties.md#materiaviva-property-migration-barrier) | 2,985 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Electron–phonon coupling](docs/catalog/materials_properties.md#materiaviva-property-electron-phonon-coupling) | 1,526 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Logarithmic average phonon frequency](docs/catalog/materials_properties.md#materiaviva-property-phonon-log-average-frequency) | 1,526 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Magnetic anisotropy constant](docs/catalog/materials_properties.md#materiaviva-property-magnetic-anisotropy-constant) | 1,521 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Magnetic easy axis](docs/catalog/materials_properties.md#materiaviva-property-easy-axis) | 1,521 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Argon uptake](docs/catalog/materials_properties.md#materiaviva-property-ar-uptake) | 1,519 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Hydrogen uptake](docs/catalog/materials_properties.md#materiaviva-property-h2-uptake) | 1,160 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Dynamical stability flag](docs/catalog/materials_properties.md#materiaviva-property-dynamically-stable) | 1,049 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Layer group number](docs/catalog/materials_properties.md#materiaviva-property-layer-group-number) | 1,049 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Pearson symbol](docs/catalog/materials_properties.md#materiaviva-property-pearson-symbol) | 957 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Surface energy](docs/catalog/materials_properties.md#materiaviva-property-surface-energy) | 695 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Bulk modulus from equation of state](docs/catalog/materials_properties.md#materiaviva-property-bulk-modulus-eos) | 428 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Pressure derivative of bulk modulus](docs/catalog/materials_properties.md#materiaviva-property-bulk-modulus-pressure-derivative) | 428 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Strukturbericht designation](docs/catalog/materials_properties.md#materiaviva-property-strukturbericht) | 356 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Mohs hardness](docs/catalog/materials_properties.md#materiaviva-property-mohs-hardness) | 267 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Surface reconstruction flag](docs/catalog/materials_properties.md#materiaviva-property-has-reconstructed-surface) | 237 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Surface anisotropy](docs/catalog/materials_properties.md#materiaviva-property-surface-anisotropy) | 229 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Wulff shape factor](docs/catalog/materials_properties.md#materiaviva-property-wulff-shape-factor) | 229 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Measured chemistry](docs/catalog/materials_properties.md#materiaviva-property-measured-chemistry) | 201 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Crystallographic R factor](docs/catalog/materials_properties.md#materiaviva-property-r-factor) | 185 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Grain boundary energy](docs/catalog/materials_properties.md#materiaviva-property-grain-boundary-energy) | 164 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Maximum electron localization function](docs/catalog/materials_properties.md#materiaviva-property-elf-max) | 145 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Grain boundary types](docs/catalog/materials_properties.md#materiaviva-property-grain-boundary-types) | 106 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Work of separation](docs/catalog/materials_properties.md#materiaviva-property-work-of-separation) | 106 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Energy relative to diamond](docs/catalog/materials_properties.md#materiaviva-property-relative-energy-to-diamond) | 23 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Altermagnetic splitting fraction](docs/catalog/materials_properties.md#materiaviva-property-altermagnetic-split-fraction) | 22 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Average altermagnetic splitting](docs/catalog/materials_properties.md#materiaviva-property-altermagnetic-splitting-avg) | 22 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Maximum altermagnetic splitting](docs/catalog/materials_properties.md#materiaviva-property-altermagnetic-splitting-max) | 22 | property values | open | Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources. |
| [MateriaViva — Vickers hardness](docs/catalog/materials_properties.md#materiaviva-property-hardness-vickers) | 20 | property values | open | Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. |
| [MateriaViva — Curie temperature](docs/catalog/materials_properties.md#materiaviva-property-curie-temperature) | 6 | property values | open | Per-row upstream terms; retain licence and licence_class. |
| [MateriaViva — Ionic conductivity](docs/catalog/materials_properties.md#materiaviva-property-ionic-conductivity) | 5 | property values | open | Per-row upstream terms; retain licence and licence_class. |

<a id="property-benchmarks"></a>
### Computed properties and prediction benchmarks

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [OMDB-GAP1 models: COD band-gap prediction release](docs/catalog/property_benchmarks.md#omdb-cod-bandgap-predictions) | 260,092 | COD crystal prediction records | registration | Not verified |
| [WBM / Matbench Discovery stability test set](docs/catalog/property_benchmarks.md#wbm-matbench-discovery) | 256,963 | structure entries | open | CC BY 4.0 |
| [Graphs of MP 2019](docs/catalog/property_benchmarks.md#mp-graphs-2019) | 133,420 | graph–target records | open | MIT (provider/benchmark release declaration) |
| [Matbench mp_e_form](docs/catalog/property_benchmarks.md#matbench-mp-e-form) | 132,752 | task samples | open | Not verified |
| [Matbench mp_gap / mp_is_metal (shared source cohort)](docs/catalog/property_benchmarks.md#matbench-mp-electronic) | 106,113 | task samples | open | Not verified |
| [Foundry assorted computational band-gap cohort](docs/catalog/property_benchmarks.md#mdf-assorted-computed-band-gaps) | 105,594 | computed band-gap records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [Topological Quantum Chemistry all-band materials catalog](docs/catalog/property_benchmarks.md#tqc-topological-materials-2022) | 96,196 | ICSD structure entries | open | Not verified |
| [LeMat-Rho](docs/catalog/property_benchmarks.md#lemat-rho) | 69,117 | materials | open | CC BY 4.0 |
| [Quantum Defects Database — semiconductor point defects](docs/catalog/property_benchmarks.md#quantumdefects-semiconductor) | ≥50,000 | point-defect calculations | open | Not verified; public access does not establish a reuse licence |
| [Materials Project / Ricci electronic transport database](docs/catalog/property_benchmarks.md#mp-boltztrap-transport) | ~48,000 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Materials Project Phonon database v1.1](docs/catalog/property_benchmarks.md#mp-phonon-2026) | 26,413 | materials | open | Creative Commons Attribution 4.0 International |
| [UCI Superconductivity Data (Hamidieh 2018)](docs/catalog/property_benchmarks.md#uci-superconductivity-2018) | 21,263 | tabular material records | open | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| [Phonix anharmonic phonon database](docs/catalog/property_benchmarks.md#phonix) | 20,912 | unique materials | open | Creative Commons Attribution 4.0 International |
| [ECD-cubic electronic charge-density database](docs/catalog/property_benchmarks.md#ecd-cubic) | 17,418 | cubic material charge-density records | open | CC0 1.0 (inspected Figshare payload metadata) |
| [JARVIS-WTBH phonon Hamiltonians](docs/catalog/property_benchmarks.md#jarvis-wtbh-phonon) | 15,502 | phonon Hamiltonian entries | open | Not verified for the Hamiltonian payloads |
| [JARVIS electric-field-gradient tensor release](docs/catalog/property_benchmarks.md#jarvis-efg-2020) | 15,202 | material EFG records | open | CC BY 4.0 (Figshare v2 data licence) |
| [OMDB-GAP1](docs/catalog/property_benchmarks.md#omdb-gap1) | 12,500 | materials | registration | Not verified |
| [SPSE hierarchical solid-electrolyte ion transport](docs/catalog/property_benchmarks.md#spse-ion-transport-2020) | 11,989 | BVSE transport entries | open | CC BY 4.0 for deposit; underlying ICSD coordinate rights require separate review |
| [PhononMOFdb](docs/catalog/property_benchmarks.md#phononmofdb) | 11,900 | MOF thermal-property records | open | CC BY 4.0 |
| [Matbench log_gvrh / log_kvrh (shared source cohort)](docs/catalog/property_benchmarks.md#matbench-elastic) | 10,987 | task samples | open | Not verified |
| [SNUMAT hybrid-functional band-gap dataset](docs/catalog/property_benchmarks.md#snumat-hybrid-gap) | 10,481 | materials | open | CC BY 4.0 |
| [PhononDB / MDR harmonic phonon calculation database](docs/catalog/property_benchmarks.md#phonondb-mdr) | 10,034 | material calculation entries | open | Creative Commons BY Attribution 4.0 International |
| [MDR Phonon PBE](docs/catalog/property_benchmarks.md#mdr-phonon-pbe-recalculation) | 9,958 | reference material phonon files | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [PFT MDR-PBE phonon training subset](docs/catalog/property_benchmarks.md#pft-mdr-pbe-training) | 8,510 | training materials with Hessians | open | CC-BY-4.0 (provider/benchmark release declaration) |
| [Fang Wannier optical and transport tensors](docs/catalog/property_benchmarks.md#fang-wannier-optical-transport-2025) | 7,301 | material entries | open | CC BY 4.0 (Figshare data; article has a separate CC BY-NC-ND 4.0 license) |
| [Cerqueira–Sanna–Marques conventional-superconductor EPC archive](docs/catalog/property_benchmarks.md#cerqueira-conventional-epc) | ~7,000 | electron–phonon calculations | open | CC BY 4.0 |
| [CMR ABSe3 ternary selenides](docs/catalog/property_benchmarks.md#cmr-abse3) | 5,976 | ASE calculation/structure rows | open | Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification |
| [Hennig BEE-NET public structures and split files](docs/catalog/property_benchmarks.md#hennig-bee-net-structures) | 5,241 | public CIF structures | mixed | Not verified |
| [FCC Cu dislocation–grain-boundary interactions](docs/catalog/property_benchmarks.md#cu-dislocation-grain-boundary) | 5,234 | dislocation–grain-boundary interaction outcomes | open | CC BY 4.0 (provider declaration; metadata addendum also requests CC BY) |
| [Foundry Wolverton oxide perovskite stability and vacancies](docs/catalog/property_benchmarks.md#mdf-wolverton-oxides) | 4,914 | oxide perovskite records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [PhononDB lattice thermal conductivity (MDR)](docs/catalog/property_benchmarks.md#phonondb-mdr-ltc) | 4,811 | listed material calculation entries | open | Not verified |
| [Matbench dielectric](docs/catalog/property_benchmarks.md#matbench-dielectric) | 4,764 | task samples | open | Not verified |
| [MC3D conventional-superconductivity screening and Eliashberg dataset](docs/catalog/property_benchmarks.md#mc3d-superconductivity) | 4,533 | screened metal structures | open | Creative Commons Attribution 4.0 International |
| [ZeoDiff zeolite diffusion structure-property dataset](docs/catalog/property_benchmarks.md#zeodiff-diffusion) | 4,194 | zeolite descriptor/diffusion rows | open | CC BY 4.0 (Zenodo archived release metadata) |
| [WenzhouTE computed thermoelectric database](docs/catalog/property_benchmarks.md#wenzhou-te) | 3,607 | calculated materials | open | Not verified for database; article CC BY 4.0 does not establish data licensing |
| [AFLOW AEL–AGL thermomechanical cohort (2017)](docs/catalog/property_benchmarks.md#aflow-ael-agl-2017) | ≥3,500 | materials | open | Free for scientific, academic and non-commercial purposes; any other use prohibited (AFLUX documentation) |
| [Computational 1D Materials Database (C1DB)](docs/catalog/property_benchmarks.md#c1db) | 3,157 | browser database rows | open | Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification |
| [Hennig–Xie Eliashberg / Allen–Dynes symbolic-regression benchmark](docs/catalog/property_benchmarks.md#hennig-xie-eliashberg-benchmark) | 3,046 | descriptor/Tc table rows | open | Apache-2.0 |
| [Foundry perovskite O p-band centers](docs/catalog/property_benchmarks.md#mdf-perovskite-opband) | 2,912 | perovskite composition records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [Foundry semiconductor impurity charge-state transitions](docs/catalog/property_benchmarks.md#mdf-semiconductor-defectlevels) | 2,910 | semiconductor-impurity records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [OQMD-derived oxygen-vacancy formation energies](docs/catalog/property_benchmarks.md#oqmd-oxygen-vacancy-sites-2023) | 2,677 | oxygen-site property rows | open | CC BY 4.0 (Zenodo record metadata) |
| [JARVIS-FF classical force-field calculations](docs/catalog/property_benchmarks.md#jarvis-ff) | 2,538 | force-field calculation records | open | CC BY 4.0 (Figshare deposit) |
| [SuperBand electronic-band / superconductivity dataset](docs/catalog/property_benchmarks.md#superband) | 2,474 | materials | open | Creative Commons Attribution 4.0 (database); MIT (software) |
| [MAST-ML perovskite stability educational slice](docs/catalog/property_benchmarks.md#mastml-perovskite-education) | 1,929 | perovskite composition/feature rows | open | MIT |
| [Materials Project / Petretto DFPT phonons (2018)](docs/catalog/property_benchmarks.md#mp-dfpt-phonons-2018) | 1,521 | materials | open | Not verified |
| [Quantum-Chemical Bonding Database for Solid-State Materials (2023)](docs/catalog/property_benchmarks.md#lobster-bonding-2023) | 1,520 | compounds | open | CC BY 4.0 |
| [JARVIS-WTBH electron Hamiltonians](docs/catalog/property_benchmarks.md#jarvis-wtbh-electron) | 1,440 | electron Hamiltonian entries | open | Not verified for selected 1,440-entry index snapshot; original four-part Figshare Hamiltonian collection declares CC BY 4.0 |
| [CMR A2BCX4 quaternary chalcogenides](docs/catalog/property_benchmarks.md#cmr-a2bcx4) | 1,368 | ASE calculation/structure rows | open | Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification |
| [Foundry double-perovskite oxide band gaps](docs/catalog/property_benchmarks.md#mdf-double-perovskite-bandgaps) | 1,306 | double-perovskite composition records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [Matbench phonons](docs/catalog/property_benchmarks.md#matbench-phonons) | 1,265 | task samples | open | Not verified |
| [Materials Project elastic tensor release (2015)](docs/catalog/property_benchmarks.md#mp-elastic-2015) | 1,181 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Foundry / University of Alabama Heusler magnetization](docs/catalog/property_benchmarks.md#mdf-heusler-magnetization) | 1,153 | Heusler compound records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [JARVIS superconductivity 3D DFT cohort](docs/catalog/property_benchmarks.md#jarvis-supercon-3d) | 1,058 | materials | open | CC BY 4.0 |
| [Materials Project dielectric tensor release (2017)](docs/catalog/property_benchmarks.md#mp-dielectric-2017) | 1,056 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Materials Project piezoelectric tensor release (2015)](docs/catalog/property_benchmarks.md#mp-piezo-2015) | 941 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Kumagai oxygen-vacancy database](docs/catalog/property_benchmarks.md#kumagai-oxygen-vacancies) | 937 | oxide hosts | open | CC BY 4.0 explicitly for all data in the author repository |
| [JARVIS high-pressure hydride superconductivity campaign](docs/catalog/property_benchmarks.md#jarvis-high-pressure-hydride-2024) | ≥900 | structure-pressure calculation cases | open | Creative Commons Attribution 4.0 International |
| [Superhydra binary-hydride database](docs/catalog/property_benchmarks.md#superhydra) | 880 | hypothetical hydride structures | open | Not verified |
| [Ternary fluoride-ion battery electrode reaction pairs](docs/catalog/property_benchmarks.md#ternary-fluoride-electrode-pairs) | 807 | fluorinated/defluorinated reaction pairs | open | CC0 (Figshare data-file metadata) |
| [Hennig BETE-NET released EPC cohort](docs/catalog/property_benchmarks.md#hennig-bete-net) | 806 | released crystal structures | open | Apache-2.0 (repository declaration) |
| [Matbench jdft2d](docs/catalog/property_benchmarks.md#matbench-jdft2d) | 636 | task samples | open | Not verified |
| [Literature-derived battery ionic migration barriers](docs/catalog/property_benchmarks.md#migration-barriers-literature-2025) | 621 | ionic migration pathways | open | CC BY 4.0 |
| [CompSC literature-curated conventional-superconductor structures and EPC parameters](docs/catalog/property_benchmarks.md#compsc-literature-epc) | 586 | crystal structures | open | Not verified; no repository license file or data license statement found. |
| [Trinquet nonlinear-optical SHG tensor dataset](docs/catalog/property_benchmarks.md#trinquet-shg-2024) | 579 | inorganic semiconductor structures | open | CC BY 4.0 |
| [JARVIS vacancy formation-energy release](docs/catalog/property_benchmarks.md#jarvis-vacancydb) | 464 | defect calculation records | open | CC BY 4.0 (Figshare deposit) |
| [Ricci polar-material ferroelectric screening dataset](docs/catalog/property_benchmarks.md#ricci-polar-ferroelectrics-2024) | 447 | polar materials with computed polarization | open | CC BY 4.0 (paper and its supplementary tables) |
| [Predicted high-dielectric ternary oxide structures](docs/catalog/property_benchmarks.md#predicted-high-dielectric-oxides) | 441 | computed ternary-oxide structures | open | CC BY 4.0 |
| [MAST-ML dilute-solute diffusion educational slice](docs/catalog/property_benchmarks.md#mastml-dilute-diffusion-education) | 408 | host–solute feature/property rows | open | MIT |
| [UW CMG dilute-solute diffusion database](docs/catalog/property_benchmarks.md#uw-cmg-dilute-solute-diffusion) | ≥400 | host-solute diffusion systems | open | CC BY 4.0 |
| [Antiperovskite superconductivity DFPT dataset](docs/catalog/property_benchmarks.md#antiperovskite-superconductivity-dfpt) | 384 | material calculation cases | open | Creative Commons Attribution 4.0 International |
| [Smidt first-principles ferroelectric candidate database](docs/catalog/property_benchmarks.md#smidt-ferroelectric-2020) | 255 | completed polar–nonpolar structure pairs | open | CC BY 4.0 |
| [Nanoporous-material heat-capacity DFT and prediction dataset](docs/catalog/property_benchmarks.md#porous-heat-capacity-2022) | 232 | DFT-labelled parent structures | open | CC BY 4.0 (Materials Cloud dataset metadata) |
| [MINT-ATLAS atomistic magnetic interactions](docs/catalog/property_benchmarks.md#mint-atlas) | 209 | OPTIMADE structure records | open | Not verified: client MIT license covers software; no dataset-specific license established |
| [Bond-focused grain-boundary solute interaction spectra](docs/catalog/property_benchmarks.md#gb-solute-interaction-spectra) | ~200 | binary alloy systems | open | CC BY 4.0 |
| [Sufyan altermagnetic spin-splitting screening release](docs/catalog/property_benchmarks.md#altermagnet-spin-splitting-2026) | 171 | ranked material records | open | CC BY 4.0 (Zenodo metadata) |
| [JARVIS superconductivity 2D DFT cohort](docs/catalog/property_benchmarks.md#jarvis-supercon-2d) | 161 | materials | open | CC BY 4.0 |
| [HTSC-2025 ambient-pressure BCS superconductor benchmark](docs/catalog/property_benchmarks.md#htsc-2025) | 140 | material records | open | MIT License (ScienceDB V1 registrant metadata) |
| [HH130 half-Heusler thermal-transport / MLIP release](docs/catalog/property_benchmarks.md#hh130-mathub) | 130 | half-Heusler compounds | open | Not verified for downloadable data/model archive; article is CC BY-NC 3.0 |
| [CMR ABX2 photovoltaic polytypes](docs/catalog/property_benchmarks.md#cmr-abx2) | 123 | ASE calculation/structure rows | open | Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification |
| [Phono3py 103-compound finite-displacement dataset (PBEsol)](docs/catalog/property_benchmarks.md#phonondb-103-pbesol) | 103 | compounds | open | Not verified |
| [CMR perovskite optical-absorption spectra](docs/catalog/property_benchmarks.md#cmr-perovskite-absorption) | 79 | ASE calculation/structure rows | open | Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification |
| [Oxygen migration barriers in perovskites](docs/catalog/property_benchmarks.md#oxygen-migration-perovskites-2016) | ≥40 | perovskite systems | open | CC BY 4.0 |
| [INS-derived magnetic exchange and Monte Carlo dataset](docs/catalog/property_benchmarks.md#ins-exchange-magnetic-2025) | Unranked | magnetic compounds with exchange models | open | CC BY 4.0 |
| [Materials Cloud fast Li-ion conductor screening](docs/catalog/property_benchmarks.md#materialscloud-fast-li-ion-conductors) | Unranked | released crystal systems / trajectories | open | CC BY 4.0 |
| [Materials Project representation-independent charge densities](docs/catalog/property_benchmarks.md#mp-charge-density-pyrho) | Unranked | charge-density records | registration | Not verified separately for the charge-density endpoint; consult Materials Project data terms |
| [TopoHSE-DB](docs/catalog/property_benchmarks.md#topohse-db) | Unranked | classified crystalline-material entries | open | CC BY 2.0 |
| [Wurtzite solid-solution PiezoML data](docs/catalog/property_benchmarks.md#wurtzite-piezoml-dryad) | Unranked | candidate/DFT calculation records | open | CC0 1.0 (Dryad data terms; bundled software licenses need separate checking) |

<a id="generation-benchmarks"></a>
### Crystal generation and discovery benchmarks

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [OpenLAM Crystal Philately challenge collection](docs/catalog/generation_benchmarks.md#openlam-crystal-philately) | ≥19,800,000 | valid structures | registration | Not verified |
| [Alex-MP reference dataset (MatterGen public release)](docs/catalog/generation_benchmarks.md#alex-mp-mattergen-reference) | 845,997 | structures | open | Not verified |
| [Alex-MP-20 (MatterGen)](docs/catalog/generation_benchmarks.md#alex-mp20-mattergen) | 607,684 | structures | open | Creative Commons Attribution 4.0 International (upstream MP-20 and Alexandria data-release READMEs) |
| [MP-20 (CDVAE benchmark)](docs/catalog/generation_benchmarks.md#mp20-cdvae) | 45,231 | structures | open | Not verified |
| [Perov-5 / Matbench perovskites](docs/catalog/generation_benchmarks.md#perov5-cdvae-matbench) | 18,928 | structures | open | Not verified |
| [FerroGen MatterGen generated crystal cohort](docs/catalog/generation_benchmarks.md#ferrogen-mattergen-12800) | 12,800 | generated CIF files | open | CC BY 4.0 (Zenodo metadata) |
| [Carbon-24 (CDVAE benchmark)](docs/catalog/generation_benchmarks.md#carbon24-cdvae) | 10,153 | structures | open | Not verified |

<a id="experimental-properties"></a>
### Experimental properties and literature extraction

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [ChemDataExtractor stress-strain property database](docs/catalog/experimental_properties.md#cde-stress-strain-2024) | 720,308 | extracted property records | open | CC BY 4.0 |
| [ChemDataExtractor battery materials database (2020)](docs/catalog/experimental_properties.md#cde-battery-2020) | 292,313 | property records | open | CC BY 4.0 |
| [JCAP metal-oxide synthesis, imaging and UV–Vis cohort](docs/catalog/experimental_properties.md#jcap-metal-oxide-optical-179k) | 179,072 | synthesized metal-oxide samples | open | CC0 1.0 (Figshare HDF5) |
| [Material Synthesis 2025 (MatSyn25)](docs/catalog/experimental_properties.md#matsyn25) | 163,240 | synthesis processes | open | CC BY-NC 4.0 |
| [Text-mined sol-gel synthesis and phase-purity outcomes](docs/catalog/experimental_properties.md#solgel-phase-purity-2026) | ~148,000 | synthesis protocol records | open | CC BY 4.0 |
| [High Throughput Experimental Materials Database (HTEM)](docs/catalog/experimental_properties.md#htem) | ≥140,000 | entries | mixed | Not verified |
| [ChemDataExtractor refractive-index and dielectric database](docs/catalog/experimental_properties.md#cde-refractive-dielectric-2022) | 109,880 | optical/dielectric literature records | open | CC BY 4.0 |
| [Starrydata2 experimental materials datasets](docs/catalog/experimental_properties.md#starrydata2) | 106,815 | samples | open | CC BY 4.0 |
| [ChemDataExtractor semiconductor band-gap database](docs/catalog/experimental_properties.md#cde-bandgaps-2022) | 100,236 | band-gap literature records | open | MIT (Figshare dataset declaration) |
| [ChemDataExtractor yield-strength and grain-size databases](docs/catalog/experimental_properties.md#cde-yield-grainsize) | 94,554 | extracted property records | open | MIT (Figshare data deposit) |
| [3DSC_ICSD — superconductors linked to ICSD structures](docs/catalog/experimental_properties.md#3dsc-icsd) | 86,490 | matched crystal structures | mixed | CC BY 4.0 (public labels/IDs only; underlying ICSD CIFs separately licensed) |
| [LeMat-Synth synthesis-procedure corpus](docs/catalog/experimental_properties.md#lemat-synth) | ~81,000 | source papers | mixed | Not verified |
| [Solid-state synthesis recipes with impurity phases](docs/catalog/experimental_properties.md#solid-state-synthesis-impurities) | 80,806 | synthesis reactions | open | CC BY 4.0 |
| [Northeast Materials Database (NEMAD) — magnetic materials](docs/catalog/experimental_properties.md#nemad-magnetic) | 67,573 | magnetic-material entries | open | Not verified for full website database; processed ML archive declares CC BY 4.0 |
| [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](docs/catalog/experimental_properties.md#cde-curie-neel-2025) | 56,037 | property records | open | CC BY 4.0 |
| [Starrydata — Thermoelectric Materials](docs/catalog/experimental_properties.md#starrydata-thermoelectric-materials) | 55,676 | samples | open | CC BY 4.0 |
| [Perovskite Database Project (solar cells)](docs/catalog/experimental_properties.md#perovskite-solar-cell-database) | ≥42,400 | device records | open | Creative Commons Attribution 4.0 International (data, unless otherwise noted); MIT (code) |
| [ChemDataExtractor dye-sensitized solar-cell devices](docs/catalog/experimental_properties.md#cde-dye-sensitized-solar-devices) | 41,860 | device-report JSON documents | open | MIT |
| [ChemDataExtractor Curie and Néel database (2018)](docs/catalog/experimental_properties.md#cde-curie-neel-2018) | 39,822 | property records | open | Not verified |
| [NIST/ARPA-E adsorption isotherm database (NIST-ISODB)](docs/catalog/experimental_properties.md#nist-isodb) | 37,703 | adsorption isotherms | open | Not verified: NIST metadata links generic open-data license, but database homepage requests contacting technical staff about data licensing/reproduction |
| [Text-mined solution-based inorganic synthesis procedures](docs/catalog/experimental_properties.md#text-mined-solution-synthesis) | 35,675 | synthesis procedures | open | CC BY 4.0 |
| [Digital Hydrogen Platform (DigHyd)](docs/catalog/experimental_properties.md#dighyd) | ≥30,000 | data entries | open | Not verified |
| [ZeoSyn zeolite synthesis dataset](docs/catalog/experimental_properties.md#zeosyn) | 23,961 | synthesis routes | open | MIT (repository-wide declaration; data-specific licence not separately verified) |
| [ChemDataExtractor thermoelectric materials database](docs/catalog/experimental_properties.md#cde-thermoelectric) | 22,805 | property records | open | MIT |
| [Text-mined inorganic solid-state synthesis recipes](docs/catalog/experimental_properties.md#text-mined-solid-state-synthesis) | 19,488 | synthesis entries | open | CC BY 4.0 |
| [SuperCon² text-extracted superconductivity records](docs/catalog/experimental_properties.md#supercon2-text) | 18,943 | text-extracted material-property records | open | Not verified |
| [Starrydata — Magnetic Materials](docs/catalog/experimental_properties.md#starrydata-magnetic-materials) | 16,607 | samples | open | CC BY 4.0 |
| [Stanev SuperCon subset / JARVIS supercon_chem composition–Tc benchmark](docs/catalog/experimental_properties.md#jarvis-supercon-chem) | 16,414 | composition/Tc records | open | CC BY 4.0 (Figshare deposit) |
| [IPOP inorganic phosphor optical-property dataset](docs/catalog/experimental_properties.md#ipop-v3) | 16,023 | property observations | open | CC BY 4.0 |
| [ChemDataExtractor perovskite solar-cell devices](docs/catalog/experimental_properties.md#cde-perovskite-solar-devices) | 15,818 | device-report JSON documents | open | MIT |
| [ChemDataExtractor water-splitting photocatalysis](docs/catalog/experimental_properties.md#cde-photocatalysis-water-splitting) | 15,755 | extracted photocatalytic activity records | open | CC BY 4.0 |
| [Aluminum alloy composition and mechanical-property literature datasets](docs/catalog/experimental_properties.md#aluminum-alloy-literature-2022) | 14,884 | alloy composition entries | open | CC BY 4.0 |
| [Starrydata — Battery Materials](docs/catalog/experimental_properties.md#starrydata-battery-materials) | 14,087 | samples | open | CC BY 4.0 |
| [ULTERA high-entropy-alloy property database](docs/catalog/experimental_properties.md#ultera-2025) | ≥12,540 | experimental HEA/MEA property observations | restricted | Not verified; access is granted through provider review |
| [LLM high-entropy alloy phase and processing database](docs/catalog/experimental_properties.md#hea-llm-2026) | 12,427 | literature-derived alloy entries | open | CC BY 4.0 |
| [FePTP iron-containing phase-transformation pathways](docs/catalog/experimental_properties.md#feptp-iron-phase-pathways) | 11,241 | phase-transformation pathways | open | CC BY 4.0 (Figshare v2) |
| [Starrydata — Dielectric Materials](docs/catalog/experimental_properties.md#starrydata-dielectric-materials) | 9,904 | samples | open | CC BY 4.0 |
| [sysTEm systematically verified experimental thermoelectrics](docs/catalog/experimental_properties.md#system-thermoelectric) | 8,650 | composition–temperature observations | open | MIT (repository declaration) |
| [NEMAD / GPTArticleExtractor thermoelectric database](docs/catalog/experimental_properties.md#nemad-thermoelectric) | 7,123 | thermoelectric compound entries | open | Not verified; no dataset-specific license verified |
| [CO2 electrocatalysis and catalyst synthesis corpora](docs/catalog/experimental_properties.md#co2-electrocatalyst-llm-corpus) | 6,985 | human-annotated benchmark records | open | Not verified for ScienceDB data deposits |
| [LLM-extracted magnetocaloric materials database (Yuan–Yang–Patra–Liao)](docs/catalog/experimental_properties.md#mce-llm-2024) | 6,614 | literature-extracted material-property rows | open | Not verified; no repository dataset license verified |
| [Welded-joint fatigue property database](docs/catalog/experimental_properties.md#weld-fatigue-2025) | 5,797 | fatigue condition/parameter records | open | CC BY 4.0 |
| [3DSC_MP — superconductors with Materials Project structures](docs/catalog/experimental_properties.md#3dsc-mp) | 5,773 | matched crystal structures | open | CC BY 4.0 |
| [Open Catalyst Experiments 2024 (OCx24) experimental data](docs/catalog/experimental_properties.md#ocx24-experimental) | 5,412 | experimental test records | open | Not verified |
| [Text-mined layered sodium cathode synthesis and performance](docs/catalog/experimental_properties.md#layered-na-cathode-textmine) | 5,265 | extracted experimental records | open | CC0 (Figshare data-item metadata) |
| [ESTM experimentally synthesized thermoelectric materials](docs/catalog/experimental_properties.md#estm-simd) | 5,205 | composition-temperature observations | open | Not verified; no dataset-specific or repository license verified |
| [Text-mined gold nanoparticle synthesis and morphology](docs/catalog/experimental_properties.md#aunp-textmined-synthesis) | 5,154 | publication-level synthesis records | open | CC BY 4.0 |
| [Nuclear structural material Charpy impact tests](docs/catalog/experimental_properties.md#nuclear-charpy-impact) | 4,961 | Charpy impact test records | open | CC BY 4.0 |
| [Shon–Min text-mined ionic conductivity database](docs/catalog/experimental_properties.md#shon-ionic-conductivity-2023) | 4,924 | text-extracted conductivity records | open | Not verified for repository data; publication and supplementary material carry CC BY-NC-ND 4.0 |
| [Starrydata — Condensed Matter](docs/catalog/experimental_properties.md#starrydata-condensed-matter) | 4,409 | samples | open | CC BY 4.0 |
| [DigBat / Dynamic Database of Solid-State Electrolytes](docs/catalog/experimental_properties.md#digbat) | 3,816 | experimental electrolyte materials | open | Not verified |
| [Starrydata — Resistor](docs/catalog/experimental_properties.md#starrydata-resistor) | 3,776 | samples | open | CC BY 4.0 |
| [IUPAC solid–liquid equilibrium reference observations](docs/catalog/experimental_properties.md#iupac-solid-liquid-reference-2023) | 3,446 | released SLE observations | open | Catalog declares NIST data-use terms; separate redistribution rights of compiled third-party measurements not verified |
| [Refractiveindex.info optical constants](docs/catalog/experimental_properties.md#refractiveindex-info) | 3,328 | published optical data records | open | CC0 1.0 |
| [Text-mined perovskite solar-device fabrication attributes](docs/catalog/experimental_properties.md#psc-fabrication-textmine-2025) | 3,164 | article-linked fabrication records | open | CC0 |
| [Cu-Cr-X mechanical and electrical property dataset](docs/catalog/experimental_properties.md#cu-cr-x-figure-extraction) | 3,018 | alloy composition-processing-property records | open | CC BY 4.0 (Figshare v2) |
| [Foundry experimental band-gap structure cohort](docs/catalog/experimental_properties.md#mdf-experimental-band-gaps) | 2,808 | experimental band-gap records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [polyVERSE load-dependent experimental Vickers hardness](docs/catalog/experimental_properties.md#polyverse-load-hardness) | 2,480 | composition-load hardness observations | open | Custom Georgia Tech Research Corporation General Public Use License; commercial-gain sale requires separate agreement |
| [FatigueData-AM2022 additively manufactured alloys](docs/catalog/experimental_properties.md#fatiguedata-am2022) | 2,460 | fatigue test-condition datasets | open | CC BY 4.0 (Figshare v2) |
| [NIST Heat Transmission Properties of Insulating and Building Materials (SRD 81)](docs/catalog/experimental_properties.md#nist-srd81-insulation) | 2,175 | measurement records | open | Database states copyright U.S. Department of Commerce, all rights reserved; no open data redistribution license verified; data redistribution rights not verified |
| [Starrydata — General DB](docs/catalog/experimental_properties.md#starrydata-general-db) | 2,158 | samples | open | CC BY 4.0 |
| [AlloyData-2024LT low-temperature alloy mechanics](docs/catalog/experimental_properties.md#alloydata-lowtemp) | 1,913 | experimental test-condition records | open | CC BY 4.0 |
| [Copper-alloy mechanical properties and electrical conductivity (Gorsse 2023)](docs/catalog/experimental_properties.md#cu-alloys-mechanical-2023) | 1,831 | composition-processing-property-reference records | open | CC0 1.0 (Figshare dataset) |
| [Starrydata — High Thermal Conductivity Materials](docs/catalog/experimental_properties.md#starrydata-high-thermal-conductivity-materials) | 1,737 | samples | open | CC BY 4.0 |
| [Starrydata — Low Thermal Conductivity Materials](docs/catalog/experimental_properties.md#starrydata-low-thermal-conductivity-materials) | 1,654 | samples | open | CC BY 4.0 |
| [Starrydata — Organic Thermoelectric Materials](docs/catalog/experimental_properties.md#starrydata-organic-thermoelectric-materials) | 1,590 | samples | open | CC BY 4.0 |
| [Nuclear structural material creep tests](docs/catalog/experimental_properties.md#nuclear-creep-properties) | 1,583 | creep test/specimen records | open | CC BY 4.0 |
| [L-PBF commercial alloy relative-density dataset](docs/catalog/experimental_properties.md#lpbf-relative-density) | 1,579 | literature processing-condition observations | open | Not verified for dataset; article license is not assigned to repository data |
| [Borg expanded MPEA mechanical properties and phases](docs/catalog/experimental_properties.md#mpea-borg-expanded) | 1,545 | composition–condition–reference records | open | CC BY 4.0 |
| [Starrydata — Hypermaterial](docs/catalog/experimental_properties.md#starrydata-hypermaterial) | 1,525 | samples | open | CC BY 4.0 |
| [HYPOD-X: quasicrystals and approximants](docs/catalog/experimental_properties.md#hypod-x) | 1,448 | composition/sample instances | open | CC BY 4.0 |
| [Experimental interfacial thermal resistance and descriptors](docs/catalog/experimental_properties.md#itr-interface-descriptors) | 1,318 | interface–temperature observations | open | CC BY 4.0 |
| [SuperMat public superconductivity linked-record CSV](docs/catalog/experimental_properties.md#supermat-linked-records) | 1,305 | linked literature records | mixed | CC BY 4.0 (dataset); Apache 2.0 (code) |
| [Calorimetric inorganic formation enthalpies](docs/catalog/experimental_properties.md#experimental-formation-enthalpy-2017) | 1,276 | experimental formation-enthalpy entries | open | CC BY 4.0 |
| [EKHI optical and thermal radiative properties](docs/catalog/experimental_properties.md#ekhi-radiative-2026) | 1,251 | experimental property curves | open | CC BY 4.0 |
| [Sub-sized nuclear structural material tensile tests](docs/catalog/experimental_properties.md#nuclear-subsize-tensile) | 1,050 | tensile test records | open | CC BY 4.0 |
| [SC-CoMIcs superconductivity information-extraction corpus](docs/catalog/experimental_properties.md#sc-comics) | 1,000 | annotated abstracts | open | CC BY-NC 3.0 (deposit and abstract text); separate annotation-specific license Not verified |
| [Starrydata — Solid State Battery Materials](docs/catalog/experimental_properties.md#starrydata-solid-state-battery-materials) | 967 | samples | open | CC BY 4.0 |
| [Liverpool Ionics Dataset](docs/catalog/experimental_properties.md#liverpool-ionics) | 820 | conductivity-at-temperature records | open | Free academic/research use with attribution; commercial extraction or reutilisation requires University of Liverpool licence (provider terms) |
| [ML-HydPARK metal-hydride storage properties](docs/catalog/experimental_properties.md#ml-hydpark) | 772 | composition/property records | open | CC BY 4.0 (versioned data deposit) |
| [Metallic-material combustion property database](docs/catalog/experimental_properties.md#metal-combustion-properties) | 725 | combustion measurement records | open | CC BY 4.0 (versioned data deposit) |
| [Starrydata — Piezoelectric Materials](docs/catalog/experimental_properties.md#starrydata-piezoelectric-materials) | 680 | samples | open | CC BY 4.0 |
| [Experimental 2D Materials Database (X2DB)](docs/catalog/experimental_properties.md#x2db) | 603 | metadata records | open | CC BY-NC 4.0 |
| [OBELiX experimental solid electrolyte conductivity](docs/catalog/experimental_properties.md#obelix) | 599 | experimental electrolyte entries | open | CC BY 4.0 |
| [Caltech experimental Li-ion structure–conductivity database](docs/catalog/experimental_properties.md#caltech-li-conductivity-571) | 571 | experimental structure-conductivity entries | open | CC0 1.0 (CaltechDATA metadata rights) |
| [China Space Station levitation thermophysical dataset](docs/catalog/experimental_properties.md#css-levitation-thermophysical) | 565 | levitation experimental records | open | CC BY 4.0 |
| [Starrydata — Air Battery Materials](docs/catalog/experimental_properties.md#starrydata-air-battery-materials) | 529 | samples | open | CC BY 4.0 |
| [Oxygen-ion conductor Arrhenius property dataset](docs/catalog/experimental_properties.md#oxygen-ion-conductor-2026) | 483 | oxide measurement-condition entries | open | CC BY 4.0 |
| [Foundry steel composition and mechanical properties](docs/catalog/experimental_properties.md#mdf-steel-strength) | 312 | steel composition/property records | registration | CC BY 4.0 (MDF deposit rights declaration) |
| [DAX-Ti experimental Ti-alloy mechanical-property compilation](docs/catalog/experimental_properties.md#dax-ti-experimental) | 282 | alloy entries | open | CC BY 4.0 (Zenodo dataset) |
| [Mechanically deformed ferritic-steel XCT defect database](docs/catalog/experimental_properties.md#ferritic-steel-xct-defects) | 276 | sample-condition XCT datasets | open | CC0 1.0 (Dryad) |
| [Fe/MgO soft magnetic composite processing properties](docs/catalog/experimental_properties.md#softmag-fe-mgo) | 274 | corrected processing-condition samples | open | CC BY 4.0 |
| [FatigueData-CMA2022 complex metallic-alloy fatigue database](docs/catalog/experimental_properties.md#fatiguedata-cma2022) | 272 | fatigue test-condition datasets | open | CC BY 4.0 (Figshare dataset); MIT applies separately to accompanying scripts |
| [teMatDb272 thermoelectric material database](docs/catalog/experimental_properties.md#tematdb272) | 272 | curated thermoelectric sample curve sets | open | CC BY 4.0 (Zenodo v1.1.6 deposit) |
| [HEA fracture and impact toughness dataset](docs/catalog/experimental_properties.md#hea-fracture-impact-2023) | 245 | metallurgical-condition property records | open | CC BY 4.0 |
| [Literature-curated complex-oxide thermal expansion](docs/catalog/experimental_properties.md#complex-oxide-cte-2026) | 204 | composition–temperature-range records | open | MIT (repository declaration) |
| [Multinary alloy HER catalyst performance](docs/catalog/experimental_properties.md#her-multinary-alloys-2026) | 180 | experimental catalyst/performance records | open | CC BY 4.0 |
| [Optical emissivity curves for heterogeneous engineered designs](docs/catalog/experimental_properties.md#optical-emissivity-designs-2022) | 153 | emissivity curve records | open | CC0 |
| [Trace-IN625 source-aware tensile properties](docs/catalog/experimental_properties.md#trace-in625-tensile) | 149 | tensile-property records | open | CC BY 4.0 for structured data; image crops retain per-source licenses |
| [AISI52100 grease-lubricated rolling-contact fatigue benchmark](docs/catalog/experimental_properties.md#aisi52100-rolling-contact-fatigue) | 63 | four-ball tribometer trials | open | CC BY 4.0 (Mendeley Data v3) |
| [Aggregated oxide synthesis parameter distributions](docs/catalog/experimental_properties.md#oxide-synthesis-aggregates-2017) | 30 | oxide material-system summaries | open | MIT |
| [Robinson HTS Wire Critical Current Database](docs/catalog/experimental_properties.md#robinson-hts-critical-current) | 24 | wire/film characterization datasets | open | Creative Commons Attribution 4.0 International (individual datasets) |
| [Correlative chemical, crystallographic and magnetic iron-oxide grains](docs/catalog/experimental_properties.md#hawaii-ironoxide-correlative-grains) | 23 | deposited component datasets | open | CC BY 3.0 Unported (PANGAEA publication series) |
| [NIST hafnia-on-silicon planar film metrology set](docs/catalog/experimental_properties.md#nist-hafnia-planar-reference-2025) | 12 | 200mm hafnia-coated silicon wafers | open | NIST data-use terms explicitly linked by release metadata; not a Creative Commons license |
| [BAM temperature-dependent elastic alloy reference data](docs/catalog/experimental_properties.md#bam-temperature-elastic-alloys) | 3 | alloy systems with paired manufacturing routes | open | CC BY 4.0 |
| [304L stainless-steel full-field DIC and infrared thermography](docs/catalog/experimental_properties.md#steel304l-dic-ir-fullfield) | Unranked | specimen-test measurement records | open | CC0 1.0 (Figshare+ v1) |
| [Corrosion-resistant alloy electrochemical metrics](docs/catalog/experimental_properties.md#corrosion-resistant-alloy-metrics) | Unranked | corrosion metric/condition records | open | CC BY 4.0 |
| [Inconel718 correlative 3D microstructure and deformation fields](docs/catalog/experimental_properties.md#in718-correlative-3d-ebsd-dic) | Unranked | registered multimodal specimen datasets | open | CC0 1.0 (Dryad) |
| [MDR SuperCon Datasheet](docs/catalog/experimental_properties.md#mdr-supercon) | Unranked | records | open | Creative Commons BY Attribution 4.0 International |
| [NIST Cryogenic Materials Property Database](docs/catalog/experimental_properties.md#nist-cryogenic-materials) | Unranked | material/property records | open | No collection-specific open data redistribution license verified |
| [NIST Structural Ceramics Database (SRD 30)](docs/catalog/experimental_properties.md#nist-structural-ceramics-srd30) | Unranked | material/property records | open | Database states copyright U.S. Department of Commerce, all rights reserved; no open data redistribution license verified; data redistribution rights not verified |
| [NIST targeted-chemical-pressure Ruddlesden–Popper dielectric data](docs/catalog/experimental_properties.md#nist-rp-chemical-pressure-dielectrics) | Unranked | material samples | open | NIST dataset-use permission explicitly stated in README; article-content reuse separately refers to publisher terms |
| [NIST WebHTS / High Temperature Superconducting Materials Database (SRD 62)](docs/catalog/experimental_properties.md#nist-webhts-srd62) | Unranked | evaluated material-property records | open | NIST Standard Reference Data copyright; all rights reserved. Specific redistribution license not verified; see provider SRD terms. |
| [Self-cleaning coating material and property corpora](docs/catalog/experimental_properties.md#self-cleaning-coating-literature) | Unranked | material/property/source group records | open | CC BY 4.0 |

<a id="diffraction-spectroscopy"></a>
### Diffraction, spectroscopy and characterization

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [ICDD Powder Diffraction File PDF-5+](docs/catalog/diffraction_spectroscopy.md#icdd-pdf5) | ≥1,126,200 | reference entries | commercial | Limited, nonexclusive, and nontransferable license |
| [Materials Project K-edge XANES release](docs/catalog/diffraction_spectroscopy.md#mp-kedge-xanes-2018) | ≥500,000 | site-resolved K-edge XANES spectra | open | CC0 1.0 (Figshare K-edge archive) |
| [SIMPOD simulated powder X-ray diffraction benchmark](docs/catalog/diffraction_spectroscopy.md#simpod-powder-xrd) | 467,861 | COD structure/diffractogram pairs | open | CC0 1.0 (Science Data Bank depositor metadata) |
| [Materials Project L-edge XANES release](docs/catalog/diffraction_spectroscopy.md#mp-ledge-xanes-2021) | ~140,000 | site-wise L2 or L3 XANES spectra | open | MIT (Figshare L-XAS archive) |
| [opXRD: Open Experimental Powder X-ray Diffraction Database](docs/catalog/diffraction_spectroscopy.md#opxrd) | 92,552 | diffraction patterns | open | CC BY 4.0 |
| [Synthetic inelastic-neutron spectra — inorganic crystal subset](docs/catalog/diffraction_spectroscopy.md#ins-crystals-10023) | 10,023 | inorganic crystal models with simulated INS | open | CC BY 4.0 (Zenodo 1.0.1) |
| [Oulu computational Raman database](docs/catalog/diffraction_spectroscopy.md#raman-oulu-5099) | 5,099 | materials with calculated Raman properties | open | CC BY 4.0 (Materials Cloud deposit) |
| [Quaternary-phosphonium-salt image-to-molecule morphology benchmark](docs/catalog/diffraction_spectroscopy.md#qps-morphology-images) | 4,037 | SEM and optical images | open | CC BY 4.0 (Figshare v2) |
| [Two-dimensional materials ab initio Raman spectra](docs/catalog/diffraction_spectroscopy.md#raman-2d-3504) | 3,504 | two-dimensional materials | open | CC BY 4.0 (Materials Cloud deposit) |
| [Lithium-thiophosphate sulfur K-edge XAS](docs/catalog/diffraction_spectroscopy.md#lps-sulfur-kedge-xas) | 2,681 | site-resolved sulfur K-edge spectra | open | CC BY 4.0 (Materials Cloud deposit) |
| [Aachen-Heerlen annotated steel microstructures](docs/catalog/diffraction_spectroscopy.md#aachen-heerlen-steel-sem) | 2,580 | SEM images | open | CC0 1.0 (verified image and polygon deposits) |
| [MDR XAFS DB](docs/catalog/diffraction_spectroscopy.md#mdr-xafs) | 2,264 | collection items | open | CC BY-NC-SA 4.0 for whole database; individual data CC BY or CC BY-NC-SA |
| [Raman Open Database (ROD)](docs/catalog/diffraction_spectroscopy.md#raman-open-database) | 1,133 | entries | open | CC0 |
| [Pd-on-carbon SEM ordering benchmark](docs/catalog/diffraction_spectroscopy.md#pd-carbon-sem-ordering) | 1,000 | SEM images | open | CC BY 4.0 (both Figshare datasets) |
| [REMI Fe-Co-Ni combinatorial library](docs/catalog/diffraction_spectroscopy.md#remi-fe-co-ni-combinatorial) | 921 | composition-spread sample points | open | Not verified |
| [JARVIS-STM computational scanning-tunneling microscopy](docs/catalog/diffraction_spectroscopy.md#jarvis-stm) | 716 | exfoliable two-dimensional materials | open | CC BY 4.0 (Figshare data items) |
| [REMI Fe-Ga-Pd combinatorial library](docs/catalog/diffraction_spectroscopy.md#remi-fe-ga-pd-combinatorial) | 278 | composition-spread sample points | open | Not verified |
| [AmalgaMatch correlative materials microscopy benchmark](docs/catalog/diffraction_spectroscopy.md#amalgamatch-microscopy) | 187 | annotated image pairs | open | CC BY 4.0 (Fordatis repository license link) |
| [Hybrid-functional inorganic-crystal Raman database](docs/catalog/diffraction_spectroscopy.md#hybrid-raman-crystal-2024) | 161 | inorganic compounds | open | CC BY 4.0 (Zenodo and primary code/data release) |
| [USGS updated geologic-materials XRD reference library](docs/catalog/diffraction_spectroscopy.md#usgs-rockjock-xrd-2021) | 156 | pure-material reference diffractograms | open | CC0 1.0 Universal (USGS release rights) |
| [DL-ADD MoS2/WS2 atomic-defect STM benchmark](docs/catalog/diffraction_spectroscopy.md#dl-add-tmd-stm-defects) | 105 | original STM benchmark images | open | CC BY 4.0 (OSF project license) |
| [MicroLib SliceGAN microstructure library](docs/catalog/diffraction_spectroscopy.md#microlib-slicegan) | 87 | source microstructure entries | open | Not verified; Zenodo declares open access but no dataset license in retrieved metadata |
| [Materials Project Raman tensor and RRUFF matching benchmark](docs/catalog/diffraction_spectroscopy.md#mp-raman-2019) | 55 | computed inorganic compounds | open | CC BY 4.0 (Figshare v2; source rights still apply) |
| [Battery-interphase IR/Raman/XRD reference library](docs/catalog/diffraction_spectroscopy.md#battery-interphase-ir-raman-xrd) | 10 | reference compounds | open | CC0 1.0 (Dryad dataset) |
| [NIST MgO ultraviolet atom-probe mass spectra](docs/catalog/diffraction_spectroscopy.md#nist-mgo-apt-spectra) | 10 | mass-spectrum condition files | open | NIST data-use terms explicitly linked by release metadata; not a Creative Commons license |
| [Nanomaterial STEM tomography reference collection](docs/catalog/diffraction_spectroscopy.md#stem-nanomaterial-tomography-2016) | 5 | tomographic material systems | open | CC0 1.0 verified for sampled collection items; check per item for reuse |
| [Zn-doped zeolite13X multimodal synchrotron benchmark](docs/catalog/diffraction_spectroscopy.md#zeolite13x-multimodal-tomography) | 1 | bespoke two-phase sample | open | CC BY 4.0 verified for XRD-CT deposit; check linked deposits individually |
| [BraggNN high-energy diffraction microscopy training/validation data](docs/catalog/diffraction_spectroscopy.md#braggnn-hedm-datasets) | Unranked | diffraction frame/Bragg-peak records | open | Not verified; no dataset license in retrieved MDF/DataCite metadata |
| [Graphene/black-phosphorus ARPES simulation and HOPG reference data](docs/catalog/diffraction_spectroscopy.md#arpes-graphene-bp-2016) | Unranked | simulation/spectral records | open | CC0 1.0 (Dryad data metadata) |
| [RRUFF mineral spectroscopy and diffraction](docs/catalog/diffraction_spectroscopy.md#rruff) | Unranked | samples | open | Not verified |

## Maintain and cite

Edit [data/datasets.json](data/datasets.json), then run `python3 scripts/build_catalog.py`. Run `python3 scripts/build_catalog.py --check` before opening a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for count and source requirements.

Please cite each original dataset when reusing it. Use [CITATION.cff](CITATION.cff) to cite this catalog. Catalog text and metadata are CC BY 4.0; scripts are MIT. Listed datasets retain their own terms. MatVerse hosts catalog metadata and links; it does not mirror the dataset payloads.
