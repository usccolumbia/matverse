# MatVerse [![Search MatVerse datasets](assets/search-box.svg)](https://usccolumbia.github.io/matverse/?q=thermoelectric)

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
