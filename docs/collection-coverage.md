# Source collection coverage

Checked 2026-11-01. The source-entry directory preserves every labeled public HTTP(S) link occurrence in the inspected inventories. Entries include datasets, papers, portals, software, handbooks and adjacent domains; they are not counts of independent crystal datasets.

| Collection | Imported / inventoried entries | Distinct entry URLs | Missing from sources.md | Search |
|---|---:|---:|---:|---|
| [blaiszik/awesome-matchem-datasets](<https://github.com/blaiszik/awesome-matchem-datasets>) | 274 / 274 | 218 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=blaiszik) |
| [JARVIS-Tools Notebooks](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks>) | 229 / 229 | 104 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_notebooks) |
| [Machine Learning Materials Datasets / MAST-ML education](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>) | 9 / 9 | 9 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=mastml) |
| [nanoHUB Machine Learning Lab Module](<https://nanohub.org/tools/intromllab>) | 41 / 41 | 27 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=nanohub_mllab) |
| [REMI: REsource for Materials Informatics](<https://pages.nist.gov/remi/>) | 146 / 146 | 145 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=remi) |
| [sedaoturak/data-resources-for-materials-science](<https://github.com/sedaoturak/data-resources-for-materials-science>) | 90 / 90 | 87 | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection=sedaoturak) |

**789 occurrences; 576 distinct entry URLs across all six collections.** Repeated entries and links shared between lists are retained with their original context. Blaiszik and Seda Oturak together contribute 364 occurrences and 296 distinct URLs at the inspected revisions.

## What complete coverage means

Every entry in each checked inventory is included in sources.md, the downloadable JSON, and the searchable Source entries view. The inventory preserves the source label, URL, original section, scope classification and source collection. Internal page anchors and non-URL placeholders are outside the extraction boundary. Linked external websites are not recursively crawled.

The collection revisions, extraction boundaries and inventory hashes below make this claim reproducible. Live GitHub HEAD matched both requested list revisions when rechecked on 2026-11-01. This is an inventory-completeness check, not independent validation of each destination, dataset size or license. A crystal-related scope label is a triage aid; it does not certify atomic-coordinate availability. The ranked catalog maintains its separate evidence requirements.

## Revisions and extraction boundaries

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

[All source links](../sources.md) · [Complete entry JSON](../data/collection_entries.json) · [Back to catalog](../README.md)
