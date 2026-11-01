# Dataset repositories, discovery tools and adjacent resources

[Back to MatVerse](../README.md)

These resources are navigation layers, collections, APIs, format mirrors or adjacent data. They are not additional independent crystal datasets and are not included in size rankings.

| Resource | Role | Description |
|---|---|---|
| [Battery Archive](https://batteryarchive.org/) | adjacent_experimental_data_portal | Cross-institution battery cycling and disruptive-test data; cell-performance resource adjacent to crystal datasets. Full CSV files requested by email. |
| [Archived Wikipedia List of Superconductors (IEEE-linked PDF)](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/11/List_of_superconductors_wikipedia.pdf) | archived reference list | IEEE-linked historical list hosted on an academic website. It is retained as a source-navigation route; currency, row count and independent validation were not established, so it is not ranked as a new dataset. |
| [Matbench v0.1 suite](https://matbench.materialsproject.org/) | benchmark suite | Thirteen property-prediction tasks from ten underlying sources; includes both composition-only and structure inputs. The catalogue groups shared structure cohorts and does not sum tasks as unique crystals. |
| [SpringerMaterials](https://materials.springer.com/) | commercial_database_portal | Commercial curated materials-property platform covering several source collections. |
| [IEEE CSC Superconductor Properties Wiki](https://wiki.ieeecsc.org/) | community property-reference wiki | Community-maintained superconducting parameters with literature citations, including Tc, Jc, critical fields, specific heat, gap and structure parameters. IEEE advertises thousands of materials; an independently verified record count, data export and dataset-wide license were not established. IEEE states that it verifies publication provenance rather than entry accuracy. |
| [LeMat-GenBench](https://github.com/LeMaterial/lemat-genbench) | crystal-generation evaluation framework | Evaluates generated crystals using validity, distribution, diversity, novelty, and stability metrics with multi-MLIP/hull configurations; its reference datasets overlap LeMat-Bulk. Framework code is Apache licensed; not an additional crystal count. |
| [Materials Data Facility / Foundry](https://www.materialsdatafacility.org/) | data_repository | Materials-data publication, discovery and access services; Foundry provides programmatic loading of ML-ready deposits. |
| [NIST Materials Data Repository](https://materialsdata.nist.gov/) | data_repository | Materials research deposits from NIST and the wider community; terms are defined per provider and collection. |
| [Catalysis-Hub / CatHub](https://www.catalysis-hub.org/) | database_portal | Open surface-reaction collection with geometries, reaction energies and linked calculations; primary 2019 descriptor reported >100,000 adsorption/reaction energies, which is a historical property count rather than a current count of unique materials. |
| [Digital Catalysis Platform (DigCat)](https://www.digcat.org/) | database_portal | Experimental-performance and computational-structure platform. Provider page currently reports >0.4M experimental and >0.4M computational records; a 2024 author preprint reports >400k performance records and >300k structures. Counts are version-dependent and not a unique-material ranking; bulk data license not verified. |
| [MOFX-DB](https://mof.tech.northwestern.edu/) | database_portal | Adsorption-data portal aggregating experimental and hypothetical MOFs, COFs and zeolites. Source datasets overlap CoRE, hMOF, ToBaCCo and IZA; portal totals are not additional unique structures. |
| [NIMS MatNavi](https://mits.nims.go.jp/en/) | database_portal | Registered browsing across inorganic, metallic, thermophysical and other materials databases; mass downloading and scraping prohibited. |
| [Data Resources for Materials Science](https://github.com/sedaoturak/data-resources-for-materials-science) | dataset collection | User-supplied dataset/resource collection. All inspected document links, scope labels and revision provenance are preserved in sources.md; linked dataset counts require their own primary evidence. |
| [ColabFit Exchange](https://materials.colabfit.org/) | dataset exchange | Searchable atomistic datasets and standardized configurations; tracks separate property and configuration identifiers, including mixed molecular and periodic domains. |
| [Matbench Discovery data sets](https://matbench-discovery.materialsproject.org/data/sets) | dataset registry and benchmark | Registry of model training/reference/test datasets and a discovery-style stability benchmark. User-nominated page returned HTTP 403; its first-party GitHub registry and WBM documentation were used. |
| [NIMS MatDaCs](https://mat-dacs.dxmt.nims.go.jp/en/) | dataset_discovery_catalog | Discovery catalogue for materials databases and computational tools, including provider links and openness notes. |
| [Digital Hydrogen-S](https://digital-hydrogen.com/storage) | dataset_portal_pending_primary_verification | Solid-state hydrogen-storage data portal identified in the supplied review. Primary paper exists; primary content and current portal totals could not be independently inspected. |
| [SevenNet-Omni domain bridging set](https://doi.org/10.6084/m9.figshare.30399814) | domain bridging data | Primary paper makes the bridging DFT data available through this deposit. Distinguish recomputed bridging structures from the 15 overlapping source datasets and their mixed-domain frame total. |
| [Machine Learning Materials Datasets / MAST-ML education](https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254) | educational dataset collection | Three MIT-licensed educational tables for MAST-ML: dilute-solute diffusion, perovskite stability and adjacent metallic-glass properties. Feature rows have no atomic coordinates; source families and packaging must remain distinct. |
| [LeMaterial Atompack](https://huggingface.co/datasets/LeMaterial/Atompack) | format mirror | Public atomistic datasets repackaged for streaming in Atompack format. The card identifies upstream MatPES, MP-ALOE, MPtrj, OMat24 and OC20; do not count format mirrors as new datasets. |
| [Awesome Materials & Chemistry Datasets](https://github.com/blaiszik/awesome-matchem-datasets) | github_collection | Broad discovery list of materials and chemistry datasets; verify each numerical claim at the originating repository. |
| [matminer dataset collection](https://github.com/hackingmaterials/matminer) | github_collection | Python loaders and dataset metadata for community materials datasets; retain original dataset citations and licences. |
| [Roberts superconductive-materials survey (1976; literature through March 1975)](https://doi.org/10.1063/1.555540) | historical evaluated data tables | B. W. Roberts reference compilation of critical temperatures, critical fields, composition and crystal-structure types, including negative experiments. IEEE labels it by the 1975 literature cutoff; the publication is Journal of Physical and Chemical Reference Data 5, 581 (1976). Retained as a reference source rather than a separately counted modern dataset. |
| [Roberts Properties of Selected Superconductive Materials, 1978 Supplement](https://doi.org/10.6028/NBS.TN.983) | historical reference supplement | NBS Technical Note 983 supplements the earlier survey with literature through fall 1977, including Tc, critical fields, crystal structure and negative experiments. No independent structure or sample total is inferred from this publication. |
| [REMI: REsource for Materials Informatics](https://pages.nist.gov/remi/) | instructional resource and dataset directory | NIST pre-alpha notebook/resource index with tagged tutorials, learning resources and directly linked experimental combinatorial libraries. Owning GitHub repository is archived; directory entries are not additive datasets. |
| [nanoHUB Machine Learning Lab Module](https://nanohub.org/tools/intromllab) | interactive educational module | Version1.7 introductory materials-ML notebook and teaching module. Public descriptions/supporting-document list are readable; running the tool requires login. Program license is GPL3-or-later; example-data rights require separate checking. |
| [OPTIMADE](https://www.optimade.org/) | interoperability API | Common API specification for querying structure providers; a federation/interface, not an additional independent dataset. |
| [Scientific Data materials Data Descriptors](https://www.nature.com/sdata/collections?page=3&type=collection) | journal_collection | Journal descriptors are discovery/provenance documents; linked external repositories hold the actual data. |
| [CatApp](https://cmr.fysik.dtu.dk/catapp/catapp.html) | legacy_property_database | Legacy reaction/activation-energy table for elementary surface reactions. The ~3,000-reaction scale is historical; CatApp does not supply detailed atomic geometries, so it is a navigation/property resource. |
| [CERN STEAM Materials Library (SMaLi)](https://steam.docs.cern.ch/libraries/materials/) | material-property model library | Collection of coded material-property functions for superconducting-magnet engineering, with C implementations and wrappers for Python, MATLAB, GetDP and COMSOL. Documentation includes HTS/LTS critical-current-density models. This is a model/software library, not a counted experimental crystal database. |
| [MatterSim training data availability](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md) | model and availability reference | Public model cards describe training data sizes and released checkpoints. This survey did not verify a complete public training-data download, so checkpoint sizes are not ranked as datasets. |
| [SCLib / JZIS superconducting-transition records](https://jzis.org/materials) | model-curated literature-data portal | Additional primary-source lead outside the IEEE list. Public snapshot reports 13,282 transition results from 6,122 papers, with sample/criterion/condition provenance and CSV downloads. Model checks and sampled-batch checks are not individual expert validation. Project-created data use CC BY 4.0, while upstream-source terms remain applicable; no independent crystal count is claimed here. |
| [AFLOW AEL/AGL thermomechanical property libraries](https://aflow.org/documentation/) | property-library access resource | Distinct AFLOW workflows exposing elastic tensors/moduli and Debye/thermal estimates through AFLUX. Current property-bearing cohort sizes were not verified; no independent current materials count is claimed. |
| [Materials Cloud Archive](https://archive.materialscloud.org/) | repository platform | Versioned dataset deposits with DOI records, files and, for selected datasets, AiiDA provenance graphs. Each deposit needs its own count and license. |
| [Materials Data Facility](https://materialsdatafacility.org/) | repository platform | Materials-data publication and discovery infrastructure. Collection-level counts must not be summed as unique crystals. |
| [NOMAD Repository and Archive](https://nomad-lab.eu/) | repository platform | Code-agnostic raw and normalized computational and experimental archives. Provider snapshot reports 19,425,275 entries and 4,346,100 represented materials; these heterogeneous counters are not a count of unique bulk crystals. |
| [IEEE CSC Superconductor Databases & Resources](https://ieeecsc.org/learning-hub/superconductor-databases-resources) | subject-resource directory | Navigation directory linking the CSC wiki, UCI, NIST reference sources, OSD, existing MP/NIMS resources, Robinson wire data and CERN materials models. Its thirteen scientific routes are not thirteen independent datasets. |
| [JARVIS-Tools Notebooks](https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks) | tools and notebook collection | Archived tutorial repository for electronic structure, force fields, AI and experiments; directs continued development to atomgptlab/jarvis-tools-notebooks. Inventoried README links are navigation resources, not extra dataset counts. |
| [MatterGen MP-20 reprocessed release](https://github.com/microsoft/mattergen/tree/main/data-release/mp-20) | versioned benchmark derivative | PBE-recomputed and element-filtered MP-20 derivative with its own distributed files; keep separate provenance from CDVAE MP-20. Exact file-row count was not verified, so not added as an independently sized dataset. |

## Evidence

### AFLOW AEL/AGL thermomechanical property libraries

- [Official AFLOW REST/AFLUX documentation](https://aflow.org/documentation/) (2026-11-01): Documents AEL elastic and AGL thermal keys; states data free for scientific, academic and non-commercial purposes.

### Archived Wikipedia List of Superconductors (IEEE-linked PDF)

- [IEEE CSC linked reference list](https://ieeecsc.org/learning-hub/superconductor-databases-resources) (2026-11-01): Directory explicitly links the archived Wikipedia superconductors list PDF.

### Awesome Materials & Chemistry Datasets

- [Awesome Materials & Chemistry Datasets](https://github.com/blaiszik/awesome-matchem-datasets) (2026-11-01): README groups structural, property, synthesis and other chemistry/materials datasets with links.

### Battery Archive

- [Battery Archive provider home](https://batteryarchive.org/) (2026-11-01): Offers cycling/disruptive-test visualization; complete cell CSVs available by contacting the provider.

### Catalysis-Hub / CatHub

- [Catalysis-Hub primary data descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/) (2026-11-01): 2019 descriptor documents linked geometries, calculation settings, reaction and activation energies; contributing studies have different scopes.

### CatApp

- [CatApp official CMR page](https://cmr.fysik.dtu.dk/catapp/catapp.html) (2026-11-01): Provides calculated reaction and activation energies on metal surfaces with the 2012 publication reference.
- [Catalysis-Hub primary descriptor discussion of CatApp](https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/) (2026-11-01): Explains that CatApp covers more than 3,000 reactions but lacks atomic structures and detailed calculation output.

### CERN STEAM Materials Library (SMaLi)

- [CERN STEAM Materials documentation](https://steam.docs.cern.ch/libraries/materials/) (2026-11-01): Identifies material-property C code, wrappers, documentation and the CERN GitLab source repository.
- [SMaLi reference documentation](https://steam-material-library.docs.cern.ch/) (2026-11-01): Documents superconducting critical current and HTS/LTS critical-current-density function families.

### ColabFit Exchange

- [ColabFit Exchange](https://materials.colabfit.org/) (2026-11-01): Searchable atomistic datasets and standardized configurations; tracks separate property and configuration identifiers, including mixed molecular and periodic domains.

### Data Resources for Materials Science

- [Data Resources for Materials Science](https://github.com/sedaoturak/data-resources-for-materials-science) (2026-11-01): Inspected the complete README source and extracted public links by section; adjacent and uncertain links remain labeled in the inventory.

### Digital Catalysis Platform (DigCat)

- [DigCat provider laboratory page](https://www.li-lab-cat-design.com/code--database.html) (2026-11-01): Provider reports >0.4 million experimental data and >0.4 million computational data and identifies the current platform/publication.
- [DigCat 2024 author preprint](https://www.cambridge.org/engage/chemrxiv/article-details/6760cd4381d2151a02fb5356) (2026-11-01): Reports >400,000 experimental performance records and >300,000 structures; denominator and release differ from later claims.

### Digital Hydrogen-S

- [Crossref publisher-deposited Digital Hydrogen-S metadata](https://api.crossref.org/works/10.1016/j.ijhydene.2026.153434) (2026-11-01): Confirms author paper title, DOI and Elsevier PII S0360319926000716; does not verify database counts.

### IEEE CSC Superconductor Databases & Resources

- [IEEE CSC resource directory](https://ieeecsc.org/learning-hub/superconductor-databases-resources) (2026-11-01): Lists thirteen scientific resource routes, including two routes to WebHTS/SRD 62 and historical reference books/tables.
- [IEEE-listed route: CSC Wiki](https://wiki.ieeecsc.org/) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Archived Wikipedia list](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/11/List_of_superconductors_wikipedia.pdf) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: UCI Superconductivty Data](https://archive.ics.uci.edu/dataset/464/superconductivty+data) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: NIST SRD 62 metadata](https://data.nist.gov/od/id/ECBCC1C130112ED9E04306570681B10723) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: NIST legacy WebHTS portal](https://srdata.nist.gov/CeramicDataPortal/hit) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Roberts survey](https://srd.nist.gov/jpcrdreprint/1.555540.pdf) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Roberts 1978 supplement](https://books.google.com/books?id=bbHgTVWyFlkC) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Clark OSD](http://osd.clarku.edu/public/about) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Materials Project](https://next-gen.materialsproject.org) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: NIMS MatNavi](https://mits.nims.go.jp) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: MDR SuperCon Datasheet](https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Robinson critical-current data](https://htsdb.wimbush.eu/about) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: CERN materials](https://steam.docs.cern.ch/libraries/materials/) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.

### IEEE CSC Superconductor Properties Wiki

- [IEEE CSC wiki description](https://ieeecsc.org/learning-hub/superconductor-databases-resources) (2026-11-01): Describes community property entries and explicitly limits its assurance to publication in peer-reviewed sources.

### JARVIS-Tools Notebooks

- [Requested notebook README](https://raw.githubusercontent.com/JARVIS-Materials-Design/jarvis-tools-notebooks/master/README.md) (2026-11-01): Lists subject-grouped materials design tutorials and its explicitly linked successor.

### LeMat-GenBench

- [LeMat-GenBench official README](https://raw.githubusercontent.com/LeMaterial/lemat-genbench/main/README.md) (2026-11-01): Defines benchmark families, LeMat-Bulk novelty reference, input formats and comprehensive_multi_mlip_hull configuration.

### LeMaterial Atompack

- [LeMaterial Atompack](https://huggingface.co/datasets/LeMaterial/Atompack) (2026-11-01): Public atomistic datasets repackaged for streaming in Atompack format. The card identifies upstream MatPES, MP-ALOE, MPtrj, OMat24 and OC20; do not count format mirrors as new datasets.

### Machine Learning Materials Datasets / MAST-ML education

- [Machine Learning Materials Datasets Figshare v5](https://api.figshare.com/v2/articles/7017254) (2026-11-01): Three educational datasets with property labels and descriptors; release is MIT licensed.
- [Attached dataset README](https://ndownloader.figshare.com/files/13008500) (2026-11-01): Explains normalized/raw diffusion energies, perovskite site/composition features and metallic-glass reduced transition temperature.

### Matbench Discovery data sets

- [Matbench Discovery dataset registry](https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/datasets.yml) (2026-11-01): Registry describes WBM and numerous parent/training datasets; it is navigation/provenance context, not an additive dataset.

### Matbench v0.1 suite

- [Benchmarking Materials Property Prediction Methods](https://arxiv.org/abs/2005.00707) (2026-11-01): Thirteen tasks from ten experimental/DFT sources, 312 to 132k samples.

### Materials Cloud Archive

- [Materials Cloud Archive](https://archive.materialscloud.org/) (2026-11-01): Versioned dataset deposits with DOI records, files and, for selected datasets, AiiDA provenance graphs. Each deposit needs its own count and license.

### Materials Data Facility

- [Materials Data Facility](https://materialsdatafacility.org/) (2026-11-01): Materials-data publication and discovery infrastructure. Collection-level counts must not be summed as unique crystals.

### Materials Data Facility / Foundry

- [Materials Data Facility](https://www.materialsdatafacility.org/) (2026-11-01): Describes discovery services and Foundry dataset loading.
- [MDF publishing/discovering guides](https://connect.materialsdatafacility.org/how-to) (2026-11-01): Explains data publishing and supported source locations.

### matminer dataset collection

- [matminer dataset summary](https://hackingmaterials.lbl.gov/matminer/dataset_summary.html) (2026-11-01): Lists experimental and calculated datasets with descriptions and provenance.
- [matminer repository](https://github.com/hackingmaterials/matminer) (2026-11-01): Requests citation of original sources when using loaded datasets.

### MatterGen MP-20 reprocessed release

- [MatterGen MP-20 data-release README](https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/mp-20/README.md) (2026-11-01): Describes CC BY 4.0 parent, excluded elements, PBE recomputation and hull filtering.

### MatterSim training data availability

- [MatterSim training data availability](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md) (2026-11-01): Public model cards describe training data sizes and released checkpoints. This survey did not verify a complete public training-data download, so checkpoint sizes are not ranked as datasets.

### MOFX-DB

- [MOFX-DB primary descriptor](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=931567) (2026-11-01): Describes computational adsorption datasets across multiple source families and thermodynamic conditions.

### nanoHUB Machine Learning Lab Module

- [Public module page](https://nanohub.org/tools/intromllab) (2026-11-01): Public activity description identifies version1.7 and states login is required to run.
- [Tool license page](https://nanohub.org/resources/license?tool=intromllab_r36&tmpl=component) (2026-11-01): Program is GPL version3-or-later.

### NIMS MatDaCs

- [NIMS MatDaCs: COD](https://mat-dacs.dxmt.nims.go.jp/en/list/350) (2026-11-01): Provider catalogue entry gives COD description and official link.
- [NIMS MatDaCs: AtomWork-Adv](https://mat-dacs.dxmt.nims.go.jp/en/list/316) (2026-11-01): Provider catalogue entry supplies database scope and access notes.

### NIMS MatNavi

- [NIMS MatNavi](https://mits.nims.go.jp/en/) (2026-11-01): Describes component databases, registration and prohibition of mass data acquisition.

### NIST Materials Data Repository

- [NIST Materials Data Repository](https://materialsdata.nist.gov/) (2026-11-01): Public searchable materials repository; individual providers define data-use terms and review status varies.

### NOMAD Repository and Archive

- [NOMAD Repository and Archive](https://cloud.nomad-lab.eu/nomad-lab/) (2026-11-01): Code-agnostic raw and normalized computational and experimental archives. Provider snapshot reports 19,425,275 entries and 4,346,100 represented materials; these heterogeneous counters are not a count of unique bulk crystals.

### OPTIMADE

- [OPTIMADE](https://www.optimade.org/) (2026-11-01): Common API specification for querying structure providers; a federation/interface, not an additional independent dataset.

### REMI: REsource for Materials Informatics

- [Primary resource CSV](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/_data/resources.csv) (2026-11-01): Homepage table lists instructional notebook resources and tags.
- [Open Access Data list](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md) (2026-11-01): Links experimental Fe–Co–Ni/Fe–Ga–Pd composition-spread data and major material databases.

### Roberts Properties of Selected Superconductive Materials, 1978 Supplement

- [NIST Technical Note 983 publication record](https://www.nist.gov/publications/properties-selected-superconductive-materials-1978-supplement) (2026-11-01): Official record confirms Roberts, 1978, title and DOI 10.6028/NBS.TN.983.

### Roberts superconductive-materials survey (1976; literature through March 1975)

- [Survey of superconductive materials and critical evaluation of selected properties](https://srd.nist.gov/jpcrdreprint/1.555540.pdf) (2026-11-01): Title/abstract identifies the 1976 publication, March 1975 literature cutoff and property tables.

### Scientific Data materials Data Descriptors

- [Scientific Data collections](https://www.nature.com/sdata/collections?page=3&type=collection) (2026-11-01): Lists a collection on characterisation/performance data of energy materials.
- [Scientific Data data policies](https://www.nature.com/sdata/policies/data-policies) (2026-11-01): Requires repository deposits; journal does not itself host datasets.

### SCLib / JZIS superconducting-transition records

- [SCLib public materials snapshot](https://jzis.org/materials) (2026-11-01): 2026-10-31 version 98b37554e5a6 reports 13,282 results, 7,556 material entries counted separately per paper and 6,122 papers; model-review limitations are explicit.
- [SCLib data license](https://raw.githubusercontent.com/JackZH26/SCLib_JZIS/main/LICENSE-DATA) (2026-11-01): Project-created data CC BY 4.0; original upstream terms remain in force.
- [SCLib provenance and upstream-license notes](https://raw.githubusercontent.com/JackZH26/SCLib_JZIS/main/DATA_SOURCES.md) (2026-11-01): Documents arXiv/NIMS/MP provenance routes and per-record upstream-license handling; provider statements require source-specific assessment.

### SevenNet-Omni domain bridging set

- [SevenNet-Omni domain bridging set](https://doi.org/10.6084/m9.figshare.30399814) (2026-11-01): Primary paper makes the bridging DFT data available through this deposit. Distinguish recomputed bridging structures from the 15 overlapping source datasets and their mixed-domain frame total.
- [Optimizing cross-domain transfer for universal machine learning interatomic potentials](https://www.nature.com/articles/s41467-026-70195-8) (2026-11-01): Data availability links the DBS database, in-house DFT results and selected benchmarks to Figshare 30399814.

### SpringerMaterials

- [SpringerMaterials publisher overview](https://www.springernature.com/gp/librarians/products/databases-solutions/springermaterials) (2026-11-01): Curated properties, figures and graphs platform.
