# Source collection coverage

Checked 2026-11-01. The source-entry directory preserves every labeled public HTTP(S) link occurrence in the inspected inventories. Entries include datasets, papers, portals, software, handbooks and adjacent domains; they are not counts of independent crystal datasets.

| Collection | Imported / inventoried entries | Distinct entry URLs | Missing from sources.md | Search |
|---|---:|---:|---:|---|
| [Additional materials dataset discoveries](<https://github.com/usccolumbia/matverse>) | 243 / 243 | 184 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=additional_20261101) |
| [blaiszik/awesome-matchem-datasets](<https://github.com/blaiszik/awesome-matchem-datasets>) | 274 / 274 | 218 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=blaiszik) |
| [Data.gov materials search — supplied 320-result attachment](<https://catalog.data.gov/?q=materials&sort=relevance&results=320>) | 320 / 320 | 314 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=datagov_20261101) |
| [JARVIS databases and Figshare download registry](<https://jarvis.nist.gov/#Databases>) | 82 / 82 | 80 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_databases) |
| [JARVIS-Tools Notebooks](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks>) | 229 / 229 | 104 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_notebooks) |
| [Machine Learning Materials Datasets / MAST-ML education](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>) | 9 / 9 | 9 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=mastml) |
| [Matbench Discovery dataset directory — all 46 rows](<https://matbench-discovery.materialsproject.org/data/sets>) | 46 / 46 | 46 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=matbench_discovery_20261101) |
| [MDF property dataset search](<https://www.materialsdatafacility.org/search>) | 244 / 244 | 244 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=mdf_properties_20261101) |
| [nanoHUB Machine Learning Lab Module](<https://nanohub.org/tools/intromllab>) | 41 / 41 | 27 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=nanohub_mllab) |
| [OpenAlex specialized materials property survey](<https://openalex.org/>) | 138 / 138 | 138 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=openalex_properties_20261101) |
| [OPTIMADE clients and screenshot provider options](<https://www.optimade.org/clients>) | 19 / 19 | 19 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=optimade_clients) |
| [REMI: REsource for Materials Informatics](<https://pages.nist.gov/remi/>) | 146 / 146 | 145 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=remi) |
| [Scientific Data materials journal search](<https://www.nature.com/sdata/>) | 1520 / 1520 | 1520 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=sdata_20261101) |
| [sedaoturak/data-resources-for-materials-science](<https://github.com/sedaoturak/data-resources-for-materials-science>) | 90 / 90 | 87 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=sedaoturak) |
| [User-supplied materials resources (2026-11-01)](<https://github.com/usccolumbia/matverse/blob/main/docs/requested-resources.md>) | 32 / 32 | 32 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=user_resources_20261101) |

**3433 entries; 3128 distinct entry URLs across all 15 collections.** Repeated entries and links shared between lists are retained with their original context unless the collection boundary explicitly documents exact-URL deduplication. Blaiszik and Seda Oturak together contribute 364 occurrences and 296 distinct URLs at the inspected revisions.

## What complete coverage means

Every entry in each checked inventory is included in sources.md, the downloadable JSON, and the searchable Source entries view. The inventory preserves the source label, URL, original section, scope classification and source collection. Internal page anchors and non-URL placeholders are outside the extraction boundary. Linked external websites are not recursively crawled.

The collection revisions, extraction boundaries and inventory hashes below make this claim reproducible. Live GitHub HEAD matched both requested list revisions when rechecked on 2026-11-01. This is an inventory-completeness check, not independent validation of each destination, dataset size or license. A crystal-related scope label is a triage aid; it does not certify atomic-coordinate availability. The ranked catalog maintains its separate evidence requirements.

## Revisions and extraction boundaries

### Additional materials dataset discoveries

- Inventory: [research/collection_additional_20261101.json](../research/collection_additional_20261101.json)
- Revision: `Local targeted survey 2026-11-01`
- Inventory SHA-256: `e642ea1ff447e80bd129583115f926251734b02c979c15dbc5c3c60fe402a240`
- Scope counts: {"adjacent": 0, "crystal_related": 198, "navigation": 0, "uncertain": 45}

- 50 new source-backed records were selected beyond the 304-record baseline. Searches cover defects/disorder, porous/adsorption, specialized functional/low-dimensional materials, and atomistic/experimental property collections.
- Every official route from the new records and every public URL from the four topical lead ledgers is preserved. This is a bounded search inventory, not a census of the internet.
- Parent datasets, variants, measured observations, calculated frames, generated structures and predicted properties remain distinguishable. Unverified counts/licenses and restricted access remain explicit.
- All work stays local until the user authorizes publishing.

### blaiszik/awesome-matchem-datasets

- Inventory: [research/collection_blaiszik.json](../research/collection_blaiszik.json)
- Revision: `d3b1d551eb6abcfd2ea62bcd75ac18c9471900c8`
- Inventory SHA-256: `a31eea035404648c58874f5f95c1c16fdecbbb2c5dde9533911ca123d3bc98eb`
- Scope counts: {"adjacent": 135, "crystal_related": 83, "navigation": 0, "uncertain": 56}

- Complete pinned raw README audited, including dataset tables, TODO, resources, other links and full changelog.
- All external HTTP(S) Markdown and bare URLs extracted; repeated links retained when label or section differs. Pure internal anchors and non-URL placeholders omitted.
- Tracking parameters dropped; only public content selector query keys retained. No credentials or access-bearing query parameters exported.
- Scope tags are triage, not primary scientific validation. Collection counts and licences are not treated as authoritative dataset evidence.
- Molecular, polymer, protein, reaction, CFD and engineering links remain in extraction as adjacent resources rather than becoming crystal datasets.
- Existing canonical catalog has 115 datasets and 27 resources at comparison time. Exact-URL mismatches can be aliases or derivatives, so missing candidates require identity review.
- Important missing names for verification: 2D Alloy Database, Experimental 2D Materials Database (X2DB), Quantum-Chemical Bonding Database (LOBSTER), ARROWS³ Synthesis Dataset, ZeoSyn, MatSyn25, Carbon Data, AQCat25, OCx24, A-Lab, CAMEO, Perovskite Database Project, MatText, TextEdge, LLM4Mat
- Raw table exact-URL unmatched candidates: OMat24 (Meta), OMC25, Vector-QM24, C2DB, CoRE MOF 2019, QMOF Database, ODAC23, MOFX-DB, Carbon Data, Quantum‑Chemical Bonding DB (LOBSTER), Matbench Discovery, AQCat25, van der Waals Bilayer Database (BiDB), Van der Waals 2D Heterostructure Database (HetDB), Quantum Point Defects Database (QPOD), 2D Alloy Database, MAD (Massive Atomic Diversity), NIST ICSD (subset), CSD (Cambridge), opXRD, MDR SuperCon, OCx24, CoRE MOF 2024, Experimental 2D Materials Database (X2DB), ARROWS³ Synthesis Dataset, A-Lab (Autonomous Inorganic Synthesis), CAMEO (Closed-Loop Autonomous Exploration), MatText, TextEdge, LAMBench-TrainingSet-v1, LLM4Mat, Mat-Instructions, Open Materials Guide (OMG), MatSyn25, L2M3 - Large Language Model MOF Miner, ZeoSyn
- Eight proposed primary-verified additions are in research/collection_blaiszik_additions.json; canonical data was not modified.
- ARROWS Zenodo 8331001 resolves to software njszym/ARROWS v0.0.1 (other-open licence), not by itself a verified 241-experiment dataset; the 241 count was not copied.
- LOBSTER original 2023 Zenodo release has 1520 compounds. Newer NOMAD DOI10.17172/nomad.mc38-9gm1 resolves via DataCite, but collection claim 13800 was not independently verified.
- Carbon-data headline counts 22.9 million atomic environments; provider arithmetic yields 114660 MD snapshots. Labels are from C-GAP-17, not new DFT.
- OCx24 pinned raw CSV has 5412 tests and 672 sample IDs, while clean/processed subsets differ. Collection 572-sample summary was not reused.
- AQCat25 has gated file access and CC BY-NC-SA 4.0 terms; public card access is not unrestricted file access.
- X2DB contains metadata records and explicitly no measurement datasets.
- Existing canonical matches with alternate URLs (for example C2DB, OMat24, CoRE MOF, MAD and OpenLAM) are not new datasets merely because an exact-URL comparison misses them.
- Validated exported URL queries for access-bearing keys and rejected private Figshare /s/ paths; no such URLs remain.

### Data.gov materials search — supplied 320-result attachment

- Inventory: [research/collection_datagov_20261101.json](../research/collection_datagov_20261101.json)
- Revision: `2026-11-01 attachment and live title crosswalk`
- Inventory SHA-256: `fd2be3960e5b387d104fb3e5227ad29500d457f3dcf4e0af4b01b3f44cfd6b72`
- Scope counts: {"adjacent": 0, "crystal_related": 14, "navigation": 0, "uncertain": 306}

- All 320 attached search-result occurrences are retained; the search reports 2,469 results overall, which were not all reviewed.
- Only the documented shortlist received primary-source/payload auditing. Other imported links remain discovery leads, not quality-approved datasets.
- Eight new datasets and an existing adsorption collection form the crystal-related shortlist. Adjacent polymer/composite data, software and handbooks remain resources.

### JARVIS databases and Figshare download registry

- Inventory: [research/collection_jarvis_databases.json](../research/collection_jarvis_databases.json)
- Revision: `3b0c9d0f0c15759135de857dbc93e010db01eb29`
- Inventory SHA-256: `58dd81bdca414d7ff9764dfbe5d9a40791088280dfd7d0016d6c12860b82e152`
- Scope counts: {"adjacent": 10, "crystal_related": 65, "navigation": 7, "uncertain": 0}

- All 13 rows of the homepage Databases table; source numbering skips 8 and ends at 14. WebApps, Tools, Tutorials and Outreach tables are outside this requested extraction boundary.
- All 65 named entries of the linked Figshare documentation table, plus 4 additional names present only in the pinned 66-key get_db_info() downloader registry.
- The stm, wtbh_electron and wtbh_phonon documentation entries require dedicated helpers; they are not current data(name) keys. Original spellings, including halide_peroskites, are preserved.
- Documentation counts refer to named snapshots; upstream databases, derivative mirrors, parameterizations and portal totals overlap. Imported discovery entries are searchable, but entries without individual primary evidence are not all promoted to ranked crystal datasets.

### JARVIS-Tools Notebooks

- Inventory: [research/collection_jarvis_notebooks.json](../research/collection_jarvis_notebooks.json)
- Revision: `e9a794b94e1aadfe86460fd9b884fa345dc3b001`
- Inventory SHA-256: `fdf8858af8517d8fdb5b05f1d18df8135e83fc1975becd831c5f91b31f4f7d46`
- Scope counts: {"adjacent": 24, "crystal_related": 194, "navigation": 11, "uncertain": 0}

- Extraction boundary: requested repository metadata and README at commit e9a794b94e1aadfe86460fd9b884fa345dc3b001, plus the README of the explicitly linked atomgptlab successor at 9d9496e2ad53795b6dcdd8cd55827647bceb1e5b.
- The requested repository is archived/read-only and says it is no longer maintained. Links in both README documents are inventoried; notebook contents and repository trees were not recursively scraped.
- Notebook/tutorial links are teaching and navigation resources, not additive datasets; linked upstream material families already exist in the canonical catalog.
- Section-based relevance labels are conservative navigational classifications; uncertain notebook links require inspection before dataset promotion.

### Machine Learning Materials Datasets / MAST-ML education

- Inventory: [research/collection_mastml.json](../research/collection_mastml.json)
- Revision: `Figshare version5; metadata SHA-256 a89916385075278bdd94780ad0b3eef244e5fdaf184a324001403aa1cf2485b3`
- Inventory SHA-256: `99babb75920f3f47c91ae183296e4cec8a1161a52adfc9c7745ce3e1d6e971a6`
- Scope counts: {"adjacent": 1, "crystal_related": 2, "navigation": 6, "uncertain": 0}

- Extraction boundary: Figshare article metadata v5, its attached README.txt, and metadata-listed file download URLs. CSVs were read only to verify row counts; their cell text was not used to expand links.
- All links means the HTTP/S references in those inspected documents, not all MAST-ML repositories or papers.
- Counts independently parsed after one header row: diffusion408; perovskite1929; metallic glass585. These are educational packaging counts, not new unique crystal structures.
- Metallic-glass data are adjacent, not crystalline structure data. Dataset README bibliography fields are preserved as source links, not treated as independently verified citation metadata.

### Matbench Discovery dataset directory — all 46 rows

- Inventory: [research/collection_matbench_discovery_20261101.json](../research/collection_matbench_discovery_20261101.json)
- Revision: `8869a883a5067015b815886d878bd7aaa3862d2d`
- Inventory SHA-256: `b526049a93c6fd8078d187a58e59e66c5bb9198f1f036fa2fff387ce0a77ce36`
- Scope counts: {"adjacent": 7, "crystal_related": 36, "navigation": 3, "uncertain": 0}

- All46dataset rows in the rendered data/sets table match all46keys in pinneddata/datasets.yml. Each original row has one searchable source entry.
- Existing families, exact new releases, unreleased corpora and adjacent molecular datasets remain distinguishable. The directory reports both structures/configurations and source-defined materials.
- Historical snapshots and unreleased full-corpus sizes do not overwrite current public catalog counts. Allwork remains local until explicit push authorization.

### MDF property dataset search

- Inventory: [research/collection_mdf_properties_20261101.json](../research/collection_mdf_properties_20261101.json)
- Revision: `Public MDF search snapshot 2026-11-01`
- Inventory SHA-256: `18f4d0791b787e945d23d66d9075edf4be7cf894e6f2b50e9f1f507b1cdb0fd3`
- Scope counts: {"adjacent": 16, "crystal_related": 8, "navigation": 0, "uncertain": 220}

- All 244 distinct deposit subjects returned by ten complete property queries (each limit=100; every query total was below that cap) are inventoried as source entries. This is not a complete inventory of all MDF deposits.
- Eight structured property cohorts were selected for explicit counts, target/unit schemas, stable DOI/source IDs and stated dataset rights. This checks documentation quality, not end-to-end scientific correctness or payload completeness.
- MP elastic/dielectric/piezoelectric and diffusion mirrors were identified as existing source lineages; parent and derivative counts are not added.
- Most returned deposits remain discovery leads. Public metadata retrieval is distinct from authorized bulk transfer. No credentials were used.

### nanoHUB Machine Learning Lab Module

- Inventory: [research/collection_nanohub_mllab.json](../research/collection_nanohub_mllab.json)
- Revision: `Version1.7 / revision36 / published2022-09-13 / DOI10.21981/CPNK-XE48`
- Inventory SHA-256: `239e3802d47dd3d4db1b722bd01ed53038bfe8740da6f4e0d4a7ae90cf407b36`
- Scope counts: {"adjacent": 9, "crystal_related": 0, "navigation": 32, "uncertain": 0}

- Extraction boundary: public About page, directly linked Supporting Docs list, and public license page. No launch/login or authenticated tool environment was entered.
- Public description and supporting-document filenames are accessible. Running the tool explicitly requires login; launch access is unverified. No login,403 or other access control was bypassed.
- Supporting documents comprise five teaching slide decks and four teacher/reading/quiz documents; their contents were not opened or mined for further links.
- Public tool license is GNU GPL version3-or-later; this software license is not automatically a license for every example dataset.
- No unique materials count is asserted; visible usage/user counters are not dataset sizes.

### OpenAlex specialized materials property survey

- Inventory: [research/collection_openalex_properties_20261101.json](../research/collection_openalex_properties_20261101.json)
- Revision: `Search snapshot 2026-11-01`
- Inventory SHA-256: `26283a58fb06bee74e56bf33216c7c8f70e7d76a42cc6b4f5e481131abc46cdf`
- Scope counts: {"adjacent": 0, "crystal_related": 97, "navigation": 41, "uncertain": 0}

- 42 bounded query/traversal outputs; 1761 deduplicated query-retrieved works retained in a separate discovery ledger. Only selected release evidence and query entrypoints are imported here; unreviewed general search hits are not all promoted into source cards.
- 35 new catalog releases plus the updated existing DDSE/DigBat family. All counts are release-specific and units remain distinct.
- Primary-source bodies, downloaded payloads and caches remain ignored; normalized work metadata, query outcomes, hashes, candidate decisions and counts are retained.

### OPTIMADE clients and screenshot provider options

- Inventory: [research/collection_optimade_clients.json](../research/collection_optimade_clients.json)
- Revision: `Provider registry response SHA-256 60afab5ecfde397c17e61856f934b74e62d17b5de24b658ee10d8ecc43d0244e`
- Inventory SHA-256: `19c8cd0886b36e775d772b201e64c2a53db84132e8d4f3ba27733da64f311120`
- Scope counts: {"adjacent": 0, "crystal_related": 0, "navigation": 19, "uncertain": 0}

- Both requested client links plus the 17 provider options visibly readable in the supplied screenshot. This is a bounded screenshot crosswalk, not a claim to inventory every currently registered provider.
- Provider IDs, names and index URLs corroborated against the official provider registry on 2026-11-01. Follow index links to child databases; registration is not proof of current endpoint availability or full client compatibility.
- The provider named Matterverse is separate from the MatVerse catalog. Open Materials Database (omdb) is also distinct from the Organic Materials Database at omdb.mathub.io.

### REMI: REsource for Materials Informatics

- Inventory: [research/collection_remi.json](../research/collection_remi.json)
- Revision: `596b04435fb577175264a70c4434f5539b809510`
- Inventory SHA-256: `6d778f961f8e3177053361e1e9a3a764fa4f2dad6503b030b2c292fe9571d923`
- Scope counts: {"adjacent": 25, "crystal_related": 71, "navigation": 46, "uncertain": 4}

- Extraction boundary: REMI repository README, homepage index.html and its _data/resources.csv instructional-resource list, directly linked data/index.md and learn/index.md lists, and the two data-library directories/descriptions linked by data/index.md.
- All links means links in those inspected documents and the direct file lists; linked notebooks, papers, external database sites and other REMI directories were not recursively crawled.
- Direct urllib request to the site returned403; public web-tool reading and the owning public GitHub source remained accessible. Source repository is archived; no protection was bypassed.
- The homepage table has 106 listed rows, which are educational resources, not a materials total.
- Directly linked experimental libraries contain921 Fe–Co–Ni and278 Fe–Ga–Pd aligned composition/diffraction/property rows, independently verified from the released files. No atomic-coordinate structures or release-specific data license were found.

### Scientific Data materials journal search

- Inventory: [research/collection_sdata_20261101.json](../research/collection_sdata_20261101.json)
- Revision: `Crossref ISSN 2052-4463 journal snapshot through 2026-11-01`
- Inventory SHA-256: `0f4ee5680cdc903516a005bbc7d40e7d10e6bac8bc448c0dd85f564e7b253c50`
- Scope counts: {"adjacent": 0, "crystal_related": 127, "navigation": 44, "uncertain": 1349}

- Complete cursor retrieval returned 9,304 distinct indexed journal works; indexing itself and full-text review are not claimed complete.
- All 1,514 broad title-keyword candidates are retained, plus 6 verified descriptor matches missed by title screening. Unreviewed candidates include irrelevant false positives.
- 90 verified new records were integrated with existing descriptor-linked releases. A shared oxide-synthesis aggregate was merged once. Counts, conditions, source lineages and rights remain release-specific.
- Most source entries remain uncertain discovery leads; only mapped primary-source-verified releases appear in the ranked catalog. Corrections are not new datasets. Raw bodies and payloads stay in ignored local caches.

### sedaoturak/data-resources-for-materials-science

- Inventory: [research/collection_sedaoturak.json](../research/collection_sedaoturak.json)
- Revision: `0df2e06e7caa6a49f807c20a068ce98050a14d13`
- Inventory SHA-256: `99eb77eba43715f14d8cb47708e3c88190b1a893028539742d12f0bb858b30c5`
- Scope counts: {"adjacent": 27, "crystal_related": 31, "navigation": 27, "uncertain": 5}

- GitHub recursive tree for the default branch contains exactly one tracked file, README.md; no additional in-repository source lists exist.
- Extracted 90 link occurrences and 87 distinct public URLs across Markdown sections; repeated links retain separate section provenance.
- All raw HTTP(S) URL tokens in the README were accounted for by Markdown-link extraction.
- README SHA-256: ce849ca3f98268ab0529c7081e10060c89757a673f2e2185babf388d489e2065. GitHub blob SHA: 63e7676bdd45169a66e8cba38d6acf9008ccf67d.
- Collection descriptions and historic counts are discovery leads, not independently verified dataset metadata.
- Scope labels preserve isolated-molecule, polymer, amorphous, microscopy, processing and navigation links without automatically ranking them as crystal datasets.
- Canonical comparison performed against data/datasets.json (115 rows) and data/resources.json (27 resources), snapshot during this audit.
- Verified additions are provided in research/collection_sedaoturak_additions.json. Work-function data have a CC BY-NC restriction; perovskite devices carry CC BY 4.0; TQC underlying ICSD-coordinate rights are not assumed.

### User-supplied materials resources (2026-11-01)

- Inventory: [research/collection_user_resources_20261101.json](../research/collection_user_resources_20261101.json)
- Revision: `User request received 2026-11-01; distinct original URLs preserved`
- Inventory SHA-256: `9d093bc1208406c1857b15c6e734ebb9507e712ab3e2901d642a033c71453d47`
- Scope counts: {"adjacent": 4, "crystal_related": 17, "navigation": 11, "uncertain": 0}

- The supplied list contains 26 resource bullets, including CDCS twice, plus 8 additional link mentions, including UCSD SRD twice. The inventory collapses exact URL duplicates to 32 entries; one canonical resource is used for CDCS.
- Original HTTP/HTTPS schemes, historical hostnames and requested article routes are retained as source links. Their inclusion does not assert that each legacy endpoint remains functional.
- The OQDM and NMIS labels are preserved with the correct OQMD and NIMS/AtomWork identities; historical user-supplied numerical descriptions are not substituted for verified release counts.
- Polymers, force-field/model libraries, registries, curation software, review papers and dataset portals receive scope labels and do not increase the count of independent crystal datasets.
- The supplied ADS bibcode resolves to the Clark University Organic Superconductor Database conference presentation; it is kept distinct from UCSD SRD.

[All source links](../sources.md) · [Complete entry JSON](../data/collection_entries.json) · [Back to catalog](../README.md)
