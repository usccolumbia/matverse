# MatVerse

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

The [HTML directory](https://usccolumbia.github.io/matverse/) searches names, properties, methods, tags and source evidence. Filter by category, access, structure availability, license status or counted data type; expand a release for its evidence and caveats. Export the current results as CSV or JSON. The standalone `index.html` also works offline. Both requested collection repositories and the additional teaching/tool/resource links are cross-referenced in [sources.md](sources.md), including their adjacent resources.

**[All 14 Starrydata project datasets](docs/starrydata.md)** are individually searchable, with separate sample/curve/figure/paper counts and download links. The [45-file manifest](data/starrydata_files.json) retains file sizes and SHA-256 values corroborated against release asset metadata. Projects overlap and are subsets of the combined Starrydata entry.
