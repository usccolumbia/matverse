# Scientific Data property and synthesis datasets — 2026-11-01

## Brief and method

RQ1: Which property-specific or synthesis datasets in *Scientific Data* are missing from the current 214-record MatVerse catalog? RQ2: What are the measured/computed/extracted units, structural representation and experimental or computational conditions? RQ3: Is there a verified release route, and what data license applies independently of the journal article?

The deep-research workflow was applied as a bounded journal-specific survey: primary Nature keyword searches for mechanical, thermal, ferroic, magnetic, electronic, ionic and synthesis data were followed by a second pass through the centrally harvested full-journal Crossref title inventory. The complete journal metadata and harvest receipts are maintained by the parent task in `../journal_works.json`, `../journal_candidates.json` and `../journal_harvest_receipts.json`. No OpenAlex bulk queries were made in this task. Primary articles, data repositories and small payloads were inspected; article-in-press PDFs were read with the PDF skill where Nature HTML exposed only an abstract.

Thirty full records are proposed in `additions.json`. `leads.json` preserves 96 scoped journal works with added/existing/deferred dispositions. Title matching is a coverage screen, not proof of dataset suitability. Unverified leads, platform/ontology papers, standalone molecular data and characterization-led resources were not promoted through this perspective. FePTP and the 179,072-metal-oxide synthesis/optical library are assigned to the characterization perspective. Large structural corpora, bilayer sets, MOFs and Ti/Ti64 structural datasets belong to the structure perspective.

## Evidence and safeguards

Every proposed record has a primary Scientific Data DOI, a release route and dated evidence. Data access and redistribution rights are separate: L-PBF relative-density and the CO2 electrocatalysis corpora have explicit unverified data licenses. They are publicly described/accessed resources, without an inferred grant of reuse rights. The layered sodium-cathode Figshare data items declare **CC0**, independently of the article license. SPSE declares CC BY for its deposit, but most bundled parent structures originate in ICSD and their underlying coordinate rights remain separately qualified.

Raw article HTML, PDF, API bodies and inspected payloads are confined to ignored `research/cache/sdata_properties/`. Retained compact receipts identify request URLs, statuses, data metadata, file identities and SHA-256 hashes. `cache_manifest.json` hashes the actual cache files. `validation_receipt.json` records successful current-schema and `url_ok` validation of all 30 additions together with the unchanged 214 canonical records. No canonical, generated UI or Git files were edited.

## Material findings and denominator choices

| Release | Published/released unit used | Key evidence limit |
|---|---:|---|
| Expanded Borg MPEA | 1,545 composition/condition/reference rows | CSV independently counted; 630 alloys is a different denominator. Includes distinct experimental and rule-of-mixtures fields. |
| Aluminum alloys | 14,884 composition entries | Separate 1,278 mechanical-property records, not an additive crystal count. |
| HEA fracture/impact | 245 metallurgical-condition records | Sum of 153 fracture-toughness, 14 impact-toughness and 78 impact-energy records; targets remain distinct. |
| AlloyData-2024LT | 1,913 test-condition records | Figshare v9 JSON independently counted across 239 articles. |
| Nuclear subsize tensile | 1,050 tests | 55-column conditions; no coordinates. |
| CDE yield/grain | 94,554 property records | 64,269 yield plus 30,285 grain records; derived engineering-ready/combined tables excluded from total. |
| Oxygen ion conductors | 483 measurement-condition entries | CSV independently counted; Arrhenius-fit parameters and regimes retained. |
| Soft magnetic Fe/MgO | **274 corrected samples** | Original paper/CSV has 282; deposit v2 removes duplicate data and corrects/re-measures densities. Both CSVs counted. |
| Interfacial thermal resistance | 1,318 observations | 457 interface samples/54 materials differ from the 298-material descriptor table and >80,000 constructible pairs. |
| Aggregated oxide synthesis | 30 material-system summaries | Top-level JSON count; distributions from large literature corpora are not individual synthesis recipes. |
| CDE stress-strain | 720,308 extracted records | Quantities, not unique crystals or full stress-strain curves; overlap with earlier yield/grain extraction is plausible. |
| LLM HEA phase/processing | 12,427 entries | Experimental and theoretical records; phase labels are not coordinates. |
| Weld fatigue | 5,797 parameter records | 1,666 source publications and curve points are different units. |
| Calorimetric enthalpy | 1,276 entries | JSON independently counted; calculated comparison fields separate from calorimetry. |
| Predicted high dielectric oxides | 441 structures | JSON independently counted; all 441 have POSCAR data; 33 preferred candidates are a subset. |
| SPSE | **11,989 BVSE documents** | Archive independently counted: 7,678 geometric, 49 hierarchical calculation, 121 literature and 91,763 parent CIF documents. Rounded paper value 12,000 is not used. |
| BAM elastic reference data | 3 alloy systems | Each has additive/conventional variants and specimen temperature series; 3 is not measurement-point count. Concept DOI routes resolve to 2025 versions. |
| INS exchange/MC | null | Paper says nearly 100 compounds, archive description over 70; exact archive count not reconciled. |
| Sol-gel phase purity | approximately 148,000 protocols | Approximately 28,000 impure outcomes and 53,000 source papers; bulk 707 MB JSONL not downloaded. |
| Trace-IN625 | 149 tensile-property records | 120 IN625 plus 29 composite/graded/joined material records, linked to 482 source-condition records; images have per-source terms. |
| HER multinary alloys | 180 experimental catalyst/performance records | Separate 100-composition acquisition list is a model proposal, not measured data. |
| Nuclear Charpy | 4,961 impact tests | Specimen-size and irradiation context essential. |
| Nuclear creep | 1,583 test/specimen records | Individual rows are tests with 70 condition/property columns. |
| CSS levitation | 565 experiments | 420 on-orbit plus 145 ground-matched; includes liquid-phase properties and is adjacent to crystal data. |
| L-PBF relative density | 1,579 observations | Eleven-column processing/density table; data license not verified. |
| Layered Na cathode extraction | 5,265 records | Combined/subset tables and CSV/JSON formats overlap; CC0 data-item metadata verified. |
| Gold nanoparticle synthesis | 5,154 article-level records | 7,608 synthesis and 12,519 characterization paragraphs are nested counts; not every paragraph supplies a complete recipe. |
| Water-splitting photocatalysis | 15,755 extraction records | Catalyst/illumination/reaction conditions; reported precision 71.2%, recall 36.3%. |
| CO2 electrocatalysis | 6,985 benchmark extraction records | Separate 77,016 NLP and 30,283 LLM records overlap source documents; record is an entity/label/sentence, not necessarily a complete performance tuple. |
| Alloy corrosion | null | Six worksheet target categories; formatting, repeated and unnumbered conditions prevent a defensible simple row total. A numeric-first-column tally is retained only as an audit diagnostic and is not promoted as dataset size. |

## Comparisons and scope limits

Literature mechanical compilations provide composition, processing, phase labels and measurement conditions, while the dielectric prediction release supplies atomic coordinates and computed tensors. They address different reuse questions. Likewise, SPSE empirical BVSE and geometric transport descriptors must remain separate from full first-principles NEB labels; INS-fitted exchange parameters must remain separate from Monte Carlo transition temperatures; calorimetric enthalpies must remain separate from computed comparison values.

The combined mechanical corpus covers overlapping alloy families and source papers. A new release or a different property does not prove disjoint unique materials. Counts should never be added into a global crystal total. Atomic-coordinate availability is conservatively marked: composition-only for property tables and text-mined recipes, structure-linked where only parent IDs/phase references are sufficient, periodic-atomic for verified embedded POSCARs or explicit VESTA structure releases, and mixed for interfaces and high-temperature liquid/solid experiments.

The central title inventory was used to detect older releases and recent accepted manuscripts. Existing MP elastic/piezo/dielectric, Smidt ferroelectrics, CDE band-gap/optical/thermoelectric/battery and Curie–Néel sets, SuperBand, 3DSC, JARVIS, Fang Wannier tensors, EKHI, Ti/Cu mechanics and complex-alloy fatigue records were not duplicated. Standalone spectroscopy, microstructure image libraries and platform/ontology/narrative corpora remain in their assigned perspective or deferred. Additional plausible but unverified leads remain visible rather than being promoted from titles alone.
