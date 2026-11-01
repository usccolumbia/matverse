<h1>
  <a href="http://mleg.cse.sc.edu"><img src="assets/mleg-logo-readme.svg" alt="Machine Learning and Evolution Lab (MLEG)" width="154" height="40" align="right"></a>
  <img src="assets/matverse-logo.png" alt="MatVerse logo" width="40" height="40" align="absmiddle">&nbsp;MatVerse
  <a href="https://usccolumbia.github.io/matverse/?q=thermoelectric"><img src="assets/search-box.svg" alt="Search MatVerse datasets" width="230" height="24" align="absmiddle"></a>
</h1>

**A source-verified atlas of crystal materials datasets.**

**[Search the interactive directory](https://usccolumbia.github.io/matverse/)** · [Download the standalone HTML](https://github.com/usccolumbia/matverse/raw/refs/heads/main/index.html) · [All source links](sources.md)

{{DATASETS}} dataset and release records · {{CATEGORIES}} categories · {{SOURCES}} distinct dataset evidence URLs · checked **November 1, 2026**

MatVerse surveys periodic crystal structures and their associated data: experimental crystallography, computed inorganic solids, machine-learning interatomic potential (MLIP) configurations, 2D materials, porous frameworks, molecular crystals, surfaces, and property and discovery benchmarks. It also includes crystal-related experimental property collections that supply compositions or measurements without complete atomic coordinates.

The catalog includes **LeMat, MateriaViva Open, Alexandria, OMat24, Matbench Discovery/WBM, Scientific Data descriptors and Starrydata**, alongside established databases and newer releases. It is a broad, living survey rather than an exhaustive census. A record can be a dataset, a named subset, or a release; records are not necessarily independent corpora.

[Read the survey](docs/SURVEY.md) · [Full JSON](data/datasets.json) · [CSV export](data/datasets.csv) · [Repository and resource directory](docs/resources.md) · [Scientific Data index](docs/scientific-data.md) · [ACS paper crosswalk](docs/review-crosswalk.md) · [Lineage and overlap](docs/overlap.md) · [Methods and schema](docs/METHODOLOGY.md)

## Read the counts correctly

- **Structures/materials:** usually equilibrium or curated structural records. Polymorphs, temperatures, disorder models and functional variants can create several records per composition.
- **Configurations/frames:** snapshots from relaxation, molecular dynamics or perturbation. Millions of frames can originate from far fewer parent crystals.
- **Property records/samples/patterns:** observations, literature samples or characterization data. These may have no atom-resolved structure.
- **Aggregates and derivatives overlap.** LeMat, MateriaViva, parent databases, benchmark subsets and format mirrors cannot be added into one material total.
- **Access and licensing are separate.** A free website, model license or open-access paper does not establish a dataset's redistribution rights. Unverified terms remain explicit.

Each linked dataset card records the release, unit, count evidence, available structure level, provenance, labels, access, license and caveats. There are {{UNRANKED}} records with unverified size; these remain unranked. Counts are mostly provider-reported, with selected metadata sums and small-file recounts identified explicitly. “Checked” means the documentation was inspected; it does not mean every payload was downloaded, every row audited, or each claim independently reproduced.

The [HTML directory](https://usccolumbia.github.io/matverse/) searches names, properties, methods, tags and source evidence. Filter by category, access, structure availability, license status or counted data type; expand a release for its evidence and caveats. Export the current results as CSV or JSON. The standalone `index.html` also works offline.

The separate **[Source entries view](https://usccolumbia.github.io/matverse/?view=sources)** searches all {{SOURCE_ENTRY_COUNT}} imported link entries from {{SOURCE_COLLECTION_COUNT}} inspected collections. This includes every extracted entry from [Blaiszik's list](https://usccolumbia.github.io/matverse/?view=sources&collection=blaiszik) (274 occurrences, 218 URLs) and [Seda Oturak's list](https://usccolumbia.github.io/matverse/?view=sources&collection=sedaoturak) (90 occurrences, 87 URLs). Filter by collection and scope; export labels, URLs and original sections. All are included in [sources.md](sources.md). The [coverage audit](docs/collection-coverage.md) records revisions, extraction boundaries and hashes. Imported links include adjacent domains and discovery resources; individual counts and licenses need their own evidence before entering the ranked dataset table.

**[All 14 Starrydata project datasets](docs/starrydata.md)** are individually searchable, with separate sample/curve/figure/paper counts and download links. The [45-file manifest](data/starrydata_files.json) retains file sizes and SHA-256 values corroborated against release asset metadata. Projects overlap and are subsets of the combined Starrydata entry.

**[Superconductivity datasets and resources](docs/superconductivity.md)** compare experimental critical temperatures, matched crystal structures, electronic bands, computed electron–phonon data and model-training releases, including Hennig-group contributions. Search recognizes “superconductor,” “superconducting,” “superconductivity” and “SuperCon.” When a source-list filter hides a catalog dataset, the search overview exposes matching dataset records and opens them with the query preserved.

The [requested-resource crosswalk](docs/requested-resources.md) maps the November resource list to existing datasets, newly added platforms, polymer/model resources and supporting papers. Original legacy URLs remain in the [source-entry inventory](https://usccolumbia.github.io/matverse/?view=sources&collection=user_resources_20261101).

## Materials dataset search tools

{{SEARCH_TOOLS_TABLE}}

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

**[Search {{API_ROUTE_COUNT}} API, SDK and bulk-file routes](https://usccolumbia.github.io/matverse/?view=apis)** · [Access guide and examples](docs/api-access.md) · [Machine-readable API registry](data/api_sources.json)

Find programmatic access to Materials Project, OQMD, AFLOW, COD, Alexandria, JARVIS, NOMAD, Materials Cloud, MPDS and other sources. Each route records its interface type, authentication, formats, scope, documentation and verification status. “Agent-ready” means a documented software access path; it does not certify data quality, complete labels or unrestricted reuse. Query APIs, metadata APIs, bulk SDKs and static downloads remain distinguishable.

**[OPTIMADE](https://www.optimade.org/)** (Open Databases Integration for Materials Design) standardizes structure queries, response attributes and pagination across participating databases. The [API guide](docs/api-access.md#optimade-one-standard-across-materials-databases) explains provider discovery, version checks, filters, coordinate fields and provider-specific property extensions. Standard access preserves each provider's authentication and licensing requirements.

Try the **[Materials Cloud OPTIMADE Client](https://optimadeclient.materialscloud.io/)** to select a provider and search its structures. The **[official clients directory](https://www.optimade.org/clients)** compares browser and Python clients. The [provider crosswalk](docs/api-access.md#providers-visible-in-the-supplied-screenshot) records all 17 provider options visible in the supplied screenshot, including Materials Cloud Archive, MPDD, Matterverse, NOMAD, ODBX, Open Materials Database, PSDI, TCOD, 2DMatpedia and AtomGPT.

**[Complete JARVIS audit](docs/jarvis-coverage.md):** all 13 rows in the homepage Databases table (numbered 1–7 and 9–14), all 65 named entries in its linked Figshare table, and all 66 current downloader names are included in the [searchable JARVIS source inventory](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_databases). Newly cataloged releases include QETB, FF, interfaces, surfaces, vacancies and electron/phonon Hamiltonians. Alternate portals and mirrors are identified without adding duplicate corpus totals.
