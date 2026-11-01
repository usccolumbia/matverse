# Experimental properties and literature extraction

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="cde-battery-2020"></a>
## ChemDataExtractor battery materials database (2020)

Literature-mined battery material-property relationships in SQL, CSV and JSON.

**Size:** 292,313 property records (source wording: 292,313 data records).

**Scope:** 2020 descriptor full dataset; 214617 unique chemical–property relationships and 17354 extracted chemicals

**Release:** Figshare v2, 2020-07-13. **Year:** 2020.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** capacity; voltage; conductivity; Coulombic efficiency; energy.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/ShuHuang/batterydatabase) · [data](https://doi.org/10.6084/m9.figshare.11888115.v2) · [paper](https://www.nature.com/articles/s41597-020-00602-2) · [code](https://github.com/ShuHuang/batterydatabase)

**Evidence:**

- [Battery materials Scientific Data descriptor](https://www.nature.com/articles/s41597-020-00602-2) (checked 2026-11-01): Reports 292313 records, 214617 unique chemical-property relations and 17354 chemicals.
- [Battery database v2 metadata](https://api.figshare.com/v2/articles/11888115/versions/2) (checked 2026-11-01): Confirms 2020 release and CC BY 4.0.

**Reuse and interpretation notes:**

- Includes heterogeneous battery materials, not exclusively crystalline solids.
- No full periodic structures; material names and measurements need context.
- Later BatteryBERT enhancement is a different release with different counts.

**Tags:** Scientific-Data, batteries, text-mining, composition-properties.

<a id="matsyn25"></a>
## Material Synthesis 2025 (MatSyn25)

Automatically extracted two-dimensional-material synthesis procedures with material and process information.

**Size:** 163,240 synthesis processes (source wording: 163,240 pieces of synthesis process information).

**Scope:** Author-described extraction from 85160 articles; not a count of unique materials

**Release:** 2025-10-01 author preprint and public data card. **Year:** 2025.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** synthesis procedures; target material identity; process steps; conditions.

**Access:** open. **Dataset license:** CC BY-NC 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/MatSynAI/MatSyn25) · [data](https://huggingface.co/datasets/MatSynAI/MatSyn25) · [paper](https://arxiv.org/abs/2510.00776) · [code](https://github.com/MatSynAI/MatSyn25)

**Evidence:**

- [MatSyn25 author preprint](https://arxiv.org/abs/2510.00776) (checked 2026-11-01): Abstract reports 163240 synthesis processes extracted from 85160 articles.
- [MatSyn25 provider data card](https://huggingface.co/datasets/MatSynAI/MatSyn25/raw/main/README.md) (checked 2026-11-01): Public card explicitly declares cc-by-nc-4.0.

**Reuse and interpretation notes:**

- LLM/text extraction is not independent experimental reproduction.
- Process entries are not distinct crystal structures.
- Noncommercial licence applies; payload completeness was not audited.

**Tags:** 2D, synthesis, LLM-extraction, collection-blaiszik.

<a id="htem"></a>
## High Throughput Experimental Materials Database (HTEM)

Experimental inorganic thin-film libraries combining synthesis, composition, diffraction and optoelectronic measurements.

**Size:** ≥140,000 entries (source wording: >140,000 entries).

**Scope:** Historical 2018 database including nonpublic measurements; not current public-only size

**Release:** 2018 Scientific Data descriptor. **Year:** 2018.

**Provenance:** experimental. **Structure availability:** `structure_linked`.

**Labels/content:** synthesis conditions; composition; XRD; optical absorption; conductivity; band gap.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://htem.nrel.gov/) · [paper](https://www.nature.com/articles/sdata201853)

**Evidence:**

- [HTEM Scientific Data descriptor](https://www.nature.com/articles/sdata201853) (checked 2026-11-01): Reports over 140000 entries with synthesis/characterization; more than half of property data public at publication.

**Reuse and interpretation notes:**

- Historical total includes data not publicly released; do not advertise 140000 as an open-download subset.
- Thin-film sample measurements and diffraction features do not generally supply periodic coordinates.
- Current host could not be resolved during this audit; current operational status and size unverified.

**Tags:** Scientific-Data, thin-films, high-throughput-experiment, historical-count.

<a id="starrydata2"></a>
## Starrydata2 experimental materials datasets

Digitized experimental property curves with composition, sample and source-paper metadata.

**Size:** 106,815 samples (source wording: 106815 samples; 239098 curves).

**Scope:** Full snapshot; project splits overlap and are not separate additive datasets

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** thermoelectric properties; thermal conductivity; magnetism; dielectric properties; piezoelectric properties; battery properties.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [paper](https://doi.org/10.1080/27660400.2025.2590811) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_curves.csv.gz)

Other denominators (not added to the ranking):

- 239,098 curves: Manifest full-database total
- 66,890 figures: Manifest full-database total
- 17,560 papers: Manifest full-database total

**Evidence:**

- [Starrydata live release manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): Snapshot reports 106815 sample rows, 239098 curve rows, 66890 figures and 17560 papers with data; file hashes included.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata dataset release repository](https://github.com/starrydata/starrydata_datasets) (checked 2026-11-01): Documents daily project splits, CSV structure, and the 2026 sample-ID collision/correction history.

**Reuse and interpretation notes:**

- Samples are not deduplicated chemical compositions; curves contain multiple x/y points.
- Project splits are membership-based and can overlap; summed project counts overstate the full database.
- Composition and property data do not supply full periodic atomic structures.
- Provider warns of sample_id collisions in 2026-04-01 through 2026-09-04 snapshots; inspect the correction history and use composite (SID, sample_id) joins where needed.
- The manifest counts 17,560 papers with data, while all_papers.csv.gz has 56,624 metadata rows; these are different scopes.
- Fourteen project subsets are separately cataloged for searching, with membership overlaps. Download URLs use a mutable latest tag; verify file hashes against data/starrydata_files.json.

**Tags:** priority, literature-digitization, CSV, temperature-dependent, hashes.

<a id="3dsc-icsd"></a>
## 3DSC_ICSD — superconductors linked to ICSD structures

Experimental SuperCon critical temperatures associated with ICSD identifiers and matched crystal structures; public coordinates remain subject to ICSD licensing.

**Size:** 86,490 matched crystal structures (source wording: 9,150 SuperCon entries matched with 86,490 crystal structures).

**Scope:** Published 3DSC_ICSD matches, including repeated measurement conditions

**Release:** 2023 published release. **Year:** 2023.

**Provenance:** mixed. **Structure availability:** `structure_linked`.

**Labels/content:** critical temperature; composition; ICSD structure identifiers.

**Access:** mixed. **Dataset license:** CC BY 4.0 (public labels/IDs only; underlying ICSD CIFs separately licensed).

**Official routes:** [homepage](https://github.com/aimat-lab/3DSC) · [paper](https://www.nature.com/articles/s41597-023-02721-y) · [code](https://github.com/aimat-lab/3DSC) · [data](https://doi.org/10.6084/m9.figshare.24499924)

Other denominators (not added to the ranking):

- 9,150 SuperCon composition/Tc entries: Experimental label cohort associated with 86490 structure matches; not additional materials

**Evidence:**

- [3DSC Scientific Data descriptor](https://www.nature.com/articles/s41597-023-02721-y) (checked 2026-11-01): Reports 9150 SuperCon entries matched to 86490 structures; public CSV gives ICSD IDs; full reconstruction requires ICSD licence.
- [3DSC_ICSD (only Tc and ICSD IDs) repository metadata](https://api.figshare.com/v2/articles/24499924) (checked 2026-11-01): Confirms public data deposit and its stated licence; applies to deposited files.
- [3DSC primary article full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10663493/fullTextXML) (checked 2026-11-01): Confirms 5,759 labels/5,773 MP structures and 9,150 labels/86,490 ICSD structures, artificial doping, ICSD reconstruction limitations and source-cohort overlap.
- [Upstream SuperCon missing-target convention](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/README.md) (checked 2026-11-01): The 3DSC descriptor identifies this Stanev parent. Its author README assigns zero to unreported Tc; inherited zeros must be assessed with measurement provenance.

**Reuse and interpretation notes:**

- Public IDs and labels do not confer redistribution rights to ICSD CIFs.
- Many matches share composition but differ in measurement conditions; artificial doping can approximate sample structures.
- The matched SuperCon composition/Tc-entry count is distinct from the larger matched-structure count; the two 3DSC cohorts overlap and should not be summed as independent materials.
- Public CSV identifies original ICSD structures, not redistributed or necessarily already artificially doped coordinates; reconstructing adapted structures requires licensed ICSD access.
- Repeated crystallographic measurements or measurement temperatures can generate many structures for a single SuperCon entry.
- The 3DSC authors operationally label Tc=0 entries as nonsuperconductors. Their Stanev parent also assigns zero to unreported Tc; zero alone does not verify a tested negative or a lower-temperature detection bound.

**Tags:** Scientific-Data, superconductivity, licensed-structures, superconductor, superconductors.

<a id="lemat-synth"></a>
## LeMat-Synth synthesis-procedure corpus

LLM/VLM-extracted synthesis procedures and linked performance information across materials classes, with extraction-quality scores.

**Size:** ~81,000 source papers (source wording: 81k source open-access papers (paper); official docs say over 80,000).

**Scope:** Source-paper corpus, not unique materials, atomic structures or extracted synthesis records

**Release:** v1.0. **Year:** 2025.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** synthesis procedures; reagents; processing conditions; performance values; extraction quality.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://lematerial.org/lemat-synth/overview/) · [data](https://huggingface.co/datasets/LeMaterial/LeMat-Synth) · [paper](https://arxiv.org/abs/2510.26824) · [code](https://github.com/LeMaterial/lematerial-llm-synthesis)

**Evidence:**

- [LeMat-Synth: a multi-modal toolbox to curate broad synthesis procedure databases from scientific literature](https://arxiv.org/abs/2510.26824) (checked 2026-11-01): Paper reports 81k curated open-access papers, 35 synthesis methods and 16 material classes.
- [LeMat-Synth official overview](https://lematerial.org/lemat-synth/overview/) (checked 2026-11-01): v1.0 built from over 80,000 open-access papers; outputs extracted materials, synthesis recipes, performance data and LLM-based quality scores.

**Reuse and interpretation notes:**

- Adjacent process/property context; does not promise periodic atomic coordinates for every record.
- Source papers, extracted recipes and unique materials are different counted units.
- Hugging Face raw dataset card returned HTTP 401 during this audit; code and documentation are public.
- AI extraction and judge scores are not individual expert verification of every recipe.

**Tags:** synthesis, literature, LLM extraction, LeMaterial, adjacent context.

<a id="solid-state-synthesis-impurities"></a>
## Solid-state synthesis recipes with impurity phases

LLM-extracted target and secondary-phase reactions with synthesis metadata and publication provenance.

**Size:** 80,806 synthesis reactions (source wording: 80,806 syntheses ... including 18,869 ... with impurity phase(s)).

**Scope:** Published dataset; 61937 records have no reported impurity phase

**Release:** 2025 published Figshare release. **Year:** 2025.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** target reactions; impurity phases; precursors; operations; temperature; time.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/slee-lab/solid-state-recipes-with-impurity) · [data](https://doi.org/10.6084/m9.figshare.30423274) · [paper](https://www.nature.com/articles/s41597-025-06222-y) · [code](https://github.com/slee-lab/solid-state-recipes-with-impurity)

**Evidence:**

- [Impurity-aware synthesis Scientific Data descriptor](https://www.nature.com/articles/s41597-025-06222-y) (checked 2026-11-01): Reports 80806 extracted syntheses, 18869 explicitly including impurities; supplies public JSON deposit.
- [Impurity synthesis Figshare metadata](https://api.figshare.com/v2/articles/30423274) (checked 2026-11-01): Confirms JSON archive and CC BY 4.0 release.

**Reuse and interpretation notes:**

- No reported impurity is not proof of experimental phase purity.
- LLM-extracted literature records require source checking for scientific use.

**Tags:** Scientific-Data, synthesis, impurity-phases, LLM-extraction.

<a id="cde-curie-neel-2025"></a>
## ChemDataExtractor/Snowball Curie–Néel dataset (2025)

Magnetic-transition records extracted using ChemDataExtractor 2.2.2 and Snowball v2.

**Size:** 56,037 property records (source wording: 56,037 records).

**Scope:** 2025 dataset extracted from 108181 articles; not a deduplicated structure set

**Release:** Figshare v2; 2025 descriptor. **Year:** 2025.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** Curie temperature; Néel temperature.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/C-R-Kelly/Curie-Neel-temperature-dataset) · [data](https://doi.org/10.6084/m9.figshare.29559686.v2) · [paper](https://www.nature.com/articles/s41597-025-06244-6) · [code](https://github.com/C-R-Kelly/Curie-Neel-temperature-dataset)

**Evidence:**

- [2025 magnetic temperature Scientific Data descriptor](https://www.nature.com/articles/s41597-025-06244-6) (checked 2026-11-01): Reports 56037 records; evaluation precision 72%, recall 61%; data CC BY 4.0.
- [Curie–Néel v2 repository metadata](https://api.figshare.com/v2/articles/29559686/versions/2) (checked 2026-11-01): Confirms version and CC BY 4.0 data files.

**Reuse and interpretation notes:**

- NLP errors and ambiguous chemical names remain.
- Count is extracted relationships, not unique magnetic crystals.
- Overlaps earlier magnetic literature datasets; additive union size not established.

**Tags:** Scientific-Data, magnetism, text-mining.

<a id="starrydata-thermoelectric-materials"></a>
## Starrydata — Thermoelectric Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata ThermoelectricMaterials project.

**Size:** 55,676 samples (source wording: 55,676 sample rows; 158,020 curve rows).

**Scope:** Project ThermoelectricMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Thermoelectric Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 158,020 curves: ThermoelectricMaterials project manifest count
- 40,328 figures: ThermoelectricMaterials project manifest count
- 9,547 papers: ThermoelectricMaterials project manifest count

**Evidence:**

- [Starrydata ThermoelectricMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The ThermoelectricMaterials project reports 55676 samples, 158020 curves, 40328 figures and 9547 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, ThermoelectricMaterials, literature-digitization, overlap, CSV.

<a id="perovskite-solar-cell-database"></a>
## Perovskite Database Project (solar cells)

Literature-curated metal-halide perovskite solar-cell devices, linking compositions, device stacks, synthesis, performance and bibliographic provenance.

**Size:** ≥42,400 device records (source wording: over 42,400 devices in the publication corpus).

**Scope:** Historical Nature Energy release extracted from literature published through February 2020; not a current device-total assertion

**Release:** 2021 publication historical corpus; current hosting migrated to NOMAD by 2026. **Year:** 2021.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** perovskite composition; device stack; processing conditions; power conversion efficiency; current-voltage metrics; quantum efficiency; stability; publication DOI.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International (data, unless otherwise noted); MIT (code).

**Official routes:** [homepage](https://www.perovskitedatabase.com/) · [data](https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database) · [paper](https://doi.org/10.1038/s41560-021-00941-3) · [code](https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database)

**Evidence:**

- [An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles](https://www.nature.com/articles/s41560-021-00941-3) (checked 2026-11-01): Methods reports manual extraction of over 42,400 devices through February 2020; records describe device/process/performance attributes and DOI links.
- [Perovskite Database official project page](https://www.perovskitedatabase.com/) (checked 2026-11-01): Official page states hosting migrated from MaterialsZone to NOMAD after the 2020–2026 period and links the current database and code.
- [Perovskite Database license](https://www.perovskitedatabase.com/how-to-cite/) (checked 2026-11-01): Unless otherwise noted, database data are CC BY 4.0 and code MIT.

**Reuse and interpretation notes:**

- Device records are not independent crystal structures or unique perovskite compositions.
- Atomic coordinates are not a required input; the catalogue row is composition/process/property context.
- If only averaged device measurements were available, the original curation could represent those as one entry and record the number averaged.
- The paper appeared online in 2021 and in Nature Energy volume 7 (2022); the count is historical.
- The collection’s old MaterialsZone access route has been superseded by the official NOMAD migration.

**Tags:** perovskite, photovoltaic, solar cell, experimental, literature, NOMAD, collection:sedaoturak.

<a id="cde-curie-neel-2018"></a>
## ChemDataExtractor Curie and Néel database (2018)

Automatically extracted magnetic-transition temperatures linked to compounds and source documents.

**Size:** 39,822 property records (source wording: 39,822 records).

**Scope:** 2018 full extraction: 11340 Néel and 28482 Curie records

**Release:** 2018 published release. **Year:** 2018.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** Curie temperature; Néel temperature.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/cjcourt/magdb) · [data](https://doi.org/10.6084/m9.figshare.c.3954418) · [paper](https://www.nature.com/articles/sdata2018111) · [code](https://github.com/cjcourt/magdb)

**Evidence:**

- [Magnetic transition Scientific Data descriptor](https://www.nature.com/articles/sdata2018111) (checked 2026-11-01): Reports 39822 extracted records and estimated overall precision 73%; data deposited on Figshare.

**Reuse and interpretation notes:**

- Automated literature extraction is not equivalent to expert-validated measurements.
- Property records are not unique compounds.
- Related 2025 dataset uses a different corpus/parser; do not merge counts blindly.

**Tags:** Scientific-Data, magnetism, text-mining, historical-release.

<a id="text-mined-solution-synthesis"></a>
## Text-mined solution-based inorganic synthesis procedures

Hydrothermal and precipitation procedures with targets, precursors, quantities, operations and reactions.

**Size:** 35,675 synthesis procedures (source wording: 20,037 hydrothermal ... and 15,638 precipitation ... reactions).

**Scope:** Published v4 JSON release: 20037 + 15638 procedures

**Release:** Figshare v4, 2022-02-04. **Year:** 2022.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** precursors; targets; quantities; solvents; operations; synthesis conditions.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/CederGroupHub/text-mined-solution-synthesis_public) · [data](https://doi.org/10.6084/m9.figshare.16583387.v4) · [paper](https://www.nature.com/articles/s41597-022-01317-2) · [code](https://github.com/CederGroupHub/text-mined-solution-synthesis_public)

**Evidence:**

- [Solution-synthesis Scientific Data descriptor](https://www.nature.com/articles/s41597-022-01317-2) (checked 2026-11-01): Data Records gives 20037 hydrothermal and 15638 precipitation procedures, each represented as JSON.
- [Solution-synthesis v4 metadata](https://api.figshare.com/v2/articles/16583387/versions/4) (checked 2026-11-01): Confirms v4 data release and CC BY 4.0.

**Reuse and interpretation notes:**

- Procedures are not unique compounds or measured property points.
- Literature extraction is subject to missing fields and publication-selection bias.

**Tags:** Scientific-Data, synthesis, text-mining, JSON.

<a id="dighyd"></a>
## Digital Hydrogen Platform (DigHyd)

Human-checked literature-mined hydrogen-storage data including capacities and thermodynamic parameters.

**Size:** ≥30,000 data entries (source wording: >30,000 data entries).

**Scope:** Published September-2026 database description; not a unique-material count

**Release:** September 2026 author descriptor. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** gravimetric hydrogen capacity; hydrogenation enthalpy; hydrogenation entropy; PCT behavior.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.dighyd.org) · [data](https://www.dighyd.org) · [paper](https://link.springer.com/article/10.1007/s00339-026-09903-6)

**Evidence:**

- [DigHyd author descriptor](https://link.springer.com/article/10.1007/s00339-026-09903-6) (checked 2026-11-01): Reports over 30000 entries from over 4000 experimental sources; human-reviewed capacity and PCT-derived thermodynamic parameters.

**Reuse and interpretation notes:**

- Entries are measurements/relationships, not unique structures or materials.
- Full periodic atomic structures and a bulk data licence were not verified.
- Article licence must not be automatically assigned to the live database.

**Tags:** hydrides, hydrogen-storage, literature-digitization.

<a id="zeosyn"></a>
## ZeoSyn zeolite synthesis dataset

Literature-curated zeolite hydrothermal routes linking gel composition, crystallization conditions, organic templates and framework products.

**Size:** 23,961 synthesis routes (source wording: 23,961 zeolite synthesis routes).

**Scope:** Author repository cohort covering 233 zeolite topologies and 921 organic structure-directing agents

**Release:** 2024 author release. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `structure_linked`.

**Labels/content:** gel composition; crystallization temperature; crystallization time; aging conditions; OSDA identity; IZA framework code.

**Access:** open. **Dataset license:** MIT (repository-wide declaration; data-specific licence not separately verified).

**Official routes:** [homepage](https://github.com/eltonpan/zeosyn_dataset) · [data](https://github.com/eltonpan/zeosyn_dataset/blob/master/dataset/ZEOSYN.xlsx) · [paper](https://doi.org/10.1021/acscentsci.3c01615) · [code](https://github.com/eltonpan/zeosyn_dataset)

**Evidence:**

- [ZeoSyn author README](https://raw.githubusercontent.com/eltonpan/zeosyn_dataset/master/README.md) (checked 2026-11-01): Reports 23961 routes, 233 topologies and 921 OSDAs; identifies source workbook and synthesis fields.
- [ZeoSyn repository licence](https://raw.githubusercontent.com/eltonpan/zeosyn_dataset/master/LICENSE) (checked 2026-11-01): Repository declares MIT; no separate dataset-specific licence was located in this bounded audit.

**Reuse and interpretation notes:**

- Synthesis routes are not distinct atomic structures or materials.
- Framework codes link products to structural classes; routes do not guarantee unique refined coordinates.
- The collection labels data CC BY; this audit preserves the directly observed repository declaration and the licence uncertainty.

**Tags:** zeolites, synthesis, literature, collection-blaiszik.

<a id="cde-thermoelectric"></a>
## ChemDataExtractor thermoelectric materials database

Text-mined thermoelectric properties linked to chemical names and measurement temperatures.

**Size:** 22,805 property records (source wording: 22,805 data records).

**Scope:** Full extracted database described in 2022 paper, before optional aggregated/inferred variant

**Release:** 2022 published release. **Year:** 2022.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** ZT; thermal conductivity; Seebeck coefficient; electrical conductivity; power factor; temperature.

**Access:** open. **Dataset license:** MIT.

**Official routes:** [homepage](https://github.com/odysie/thermoelectricsdb) · [data](https://doi.org/10.6084/m9.figshare.19658787) · [paper](https://www.nature.com/articles/s41597-022-01752-1) · [code](https://github.com/odysie/thermoelectricsdb)

**Evidence:**

- [Thermoelectric Scientific Data descriptor](https://www.nature.com/articles/s41597-022-01752-1.pdf) (checked 2026-11-01): Reports 22805 records across 10641 extracted chemical names; estimated extraction precision 82.25%.
- [Thermoelectric database Figshare metadata](https://api.figshare.com/v2/articles/19658787) (checked 2026-11-01): Repository metadata explicitly specifies MIT for data/source archives.

**Reuse and interpretation notes:**

- Extracted names are not deduplicated crystal structures.
- Separate aggregated-with-inferences data includes derived values; preserve inference flags.
- Repository MIT licence is recorded separately from article licensing.

**Tags:** Scientific-Data, thermoelectrics, text-mining.

<a id="text-mined-solid-state-synthesis"></a>
## Text-mined inorganic solid-state synthesis recipes

Machine-extracted precursor, target, operation and condition records with balanced reactions.

**Size:** 19,488 synthesis entries (source wording: 19,488 synthesis entries).

**Scope:** 2019 published v3 dataset, not later repository updates

**Release:** Figshare v3, 2019-09-27. **Year:** 2019.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** precursors; target compositions; operations; temperature; time; balanced reaction.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/CederGroupHub/text-mined-synthesis_public) · [data](https://doi.org/10.6084/m9.figshare.9722159.v3) · [paper](https://www.nature.com/articles/s41597-019-0224-1) · [code](https://github.com/CederGroupHub/text-mined-synthesis_public)

**Evidence:**

- [Solid-state synthesis Scientific Data descriptor](https://www.nature.com/articles/s41597-019-0224-1) (checked 2026-11-01): Data Records and abstract identify 19488 synthesis entries in the deposited dataset.
- [Solid-state synthesis v3 metadata](https://api.figshare.com/v2/articles/9722159/versions/3) (checked 2026-11-01): Confirms release v3, dated 2019-09-27, under CC BY 4.0.

**Reuse and interpretation notes:**

- Paper also mentions 19744 reactions elsewhere; 19488 is the release-specific Data Records count retained here.
- Reported successful literature procedures do not establish phase purity or experimental reproducibility.
- Later updates have different counts.

**Tags:** Scientific-Data, synthesis, text-mining, JSON.

<a id="supercon2-text"></a>
## SuperCon² text-extracted superconductivity records

Automatically extracted literature records linking material mentions to critical-temperature statements, pressure and bibliographic context.

**Size:** 18,943 text-extracted material-property records (source wording: 18,943 nonheader rows in the named cleaned CSV; original v22.12.03 has 40,324 rows).

**Scope:** Named v23.04.28 cleaned CSV, independently recounted; rows are not necessarily unique materials

**Release:** supercon2_v23.04.28_cleanup.csv; snapshot 2026-11-01. **Year:** 2023.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** material mention; composition mention; critical-temperature statement; pressure mention; measurement method; bibliographic provenance.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/lfoppiano/supercon) · [data](https://github.com/lfoppiano/supercon/blob/main/data/supercon2_v23.04.28_cleanup.csv) · [paper](https://doi.org/10.1080/27660400.2022.2153633) · [code](https://github.com/lfoppiano/supercon)

Other denominators (not added to the ranking):

- 40,324 text-extracted records: Original supercon2_v22.12.03.csv, independently counted; not additive to cleaned release

**Evidence:**

- [SuperCon² author repository](https://github.com/lfoppiano/supercon) (checked 2026-11-01): Repository describes automatic superconductivity information extraction from an arXiv-paper corpus and exposes versioned CSV outputs.
- [SuperCon² cleaned CSV v23.04.28](https://raw.githubusercontent.com/lfoppiano/supercon/main/data/supercon2_v23.04.28_cleanup.csv) (checked 2026-11-01): CSV parser counted 18,943 nonheader rows; SHA-256 f7598571a59a35ae1ba281643f41f80248863f9e73e13b39e45659ea6170eb2d.
- [SuperCon² original CSV v22.12.03](https://raw.githubusercontent.com/lfoppiano/supercon/main/data/supercon2_v22.12.03.csv) (checked 2026-11-01): Original version independently contains 40,324 nonheader rows; it is not interchangeable with the later cleaned release.

**Reuse and interpretation notes:**

- Rows are extracted assertions and can include repeated mentions, incomplete formulas, and statements about experimental or theoretical work.
- These counts do not establish unique superconducting materials or independently validated experimental Tc labels.
- Data-specific reuse license was not verified; software or article licensing is not substituted for dataset rights.
- Shares literature and extraction methodology with SuperMat; no union deduplication was performed.

**Tags:** superconductivity, text mining, SuperCon, literature extraction, Tc, superconductor, superconductors.

<a id="starrydata-magnetic-materials"></a>
## Starrydata — Magnetic Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata MagneticMaterials project.

**Size:** 16,607 samples (source wording: 16,607 sample rows; 16,982 curve rows).

**Scope:** Project MagneticMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Magnetic Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 16,982 curves: MagneticMaterials project manifest count
- 4,942 figures: MagneticMaterials project manifest count
- 2,246 papers: MagneticMaterials project manifest count

**Evidence:**

- [Starrydata MagneticMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The MagneticMaterials project reports 16607 samples, 16982 curves, 4942 figures and 2246 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, MagneticMaterials, literature-digitization, overlap, CSV.

<a id="jarvis-supercon-chem"></a>
## Stanev SuperCon subset / JARVIS supercon_chem composition–Tc benchmark

SuperCon-derived author composition/Tc table mirrored in JARVIS JSON format. Unreported critical temperatures are encoded as zero; no atomic coordinates are included.

**Size:** 16,414 composition/Tc records (source wording: 16,414 composition/Tc records).

**Scope:** Same 16,414 formula/Tc pair multiset in the Stanev author CSV and JARVIS JSON; row order and identifiers differ

**Release:** JARVIS Figshare v1 (2023-05-20); upstream 2018 author table, Git revision 6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5. **Year:** 2023.

**Provenance:** literature measurements and zero-coded missing targets. **Structure availability:** `composition_only`.

**Labels/content:** reported superconducting critical temperature; chemical formula; zero-coded unreported Tc targets.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare deposit).

**Official routes:** [homepage](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/supercon_chem_Tc/) · [data](https://doi.org/10.6084/m9.figshare.22975787.v1) · [paper](https://doi.org/10.1038/s41524-018-0085-8) · [code](https://github.com/usnistgov/jarvis) · [upstream](https://github.com/vstanev1/Supercon/tree/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5) · [upstream_csv](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/Supercon_data.csv)

Other denominators (not added to the ranking):

- 3,966 zero-coded Tc rows: Both public formats; includes unreported targets and does not establish confirmed negative experiments

**Evidence:**

- [JARVIS-Tools official dataset inventory](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): Lists supercon_chem as a downloadable 16,414-entry superconductor chemical-formula dataset.
- [JARVIS supercon_chem Tc benchmark](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/supercon_chem_Tc/) (checked 2026-11-01): Defines formula-only experimental-Tc prediction and consistently identifies dataset size 16,414.
- [JARVIS supercon_chem Figshare version 1 metadata](https://api.figshare.com/v2/articles/22975787) (checked 2026-11-01): Confirms 2023-05-20 deposit, CC BY 4.0 rights, the downloadable JSON ZIP, and provenance links to vstanev1/Supercon and the Stanev paper.
- [Official supercon_chem JSON ZIP](https://ndownloader.figshare.com/files/40719260) (checked 2026-11-01): Independently parsed 16,414 records with id, Tc and formula fields. ZIP SHA-256 14b7489822a1c25407cd6c83989dfca7f14263dfe6b5dc9f859969430c09e5b7.
- [Stanev author missing-target convention](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/README.md) (checked 2026-11-01): Author states unreported critical temperatures are encoded as Tc=0. These values do not automatically establish tested negative experiments.
- [Stanev author CSV and JARVIS mirror audit](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/Supercon_data.csv) (checked 2026-11-01): CSV has 16,414 rows and 3,966 zeros; the exact (formula, numerical Tc) multiset matches official JARVIS JSON with zero extra/missing pairs. CSV SHA-256: b34a955cc59f7a1556bc92c4b9db559bfd634c03227b7e95337a2e5d69227dd6.

**Reuse and interpretation notes:**

- Contains no atomic coordinates; source identifiers and formulas do not establish an unambiguous crystal structure.
- A derivative of SuperCon/Stanev data; overlap with MDR SuperCon, UCI and other cleaned SuperCon benchmarks must not be counted as independent new measurements.
- Includes Tc = 0 records; 16,414 is not a count of positive superconductors.
- Official JARVIS DFT supercon_3d and supercon_2d cohorts have different structures, labels and counts.
- Tc=0 includes targets assigned when critical temperature was unreported. The 3,966 zero-coded rows are not automatically confirmed negative experiments or distinct compounds.
- The two public formats represent the same cohort and are counted once. The author repository has no explicit data license; CC BY 4.0 is recorded for the JARVIS Figshare deposit.

**Tags:** superconductivity, JARVIS, SuperCon, experimental Tc, composition benchmark, derivative, superconductor, superconductors, Stanev, Supercon_data.csv, missing labels.

<a id="starrydata-battery-materials"></a>
## Starrydata — Battery Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata BatteryMaterials project.

**Size:** 14,087 samples (source wording: 14,087 sample rows; 32,586 curve rows).

**Scope:** Project BatteryMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Battery Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 32,586 curves: BatteryMaterials project manifest count
- 13,004 figures: BatteryMaterials project manifest count
- 1,689 papers: BatteryMaterials project manifest count

**Evidence:**

- [Starrydata BatteryMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The BatteryMaterials project reports 14087 samples, 32586 curves, 13004 figures and 1689 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, BatteryMaterials, literature-digitization, overlap, CSV.

<a id="starrydata-dielectric-materials"></a>
## Starrydata — Dielectric Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata DielectricMaterials project.

**Size:** 9,904 samples (source wording: 9,904 sample rows; 16,555 curve rows).

**Scope:** Project DielectricMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Dielectric Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 16,555 curves: DielectricMaterials project manifest count
- 4,643 figures: DielectricMaterials project manifest count
- 2,208 papers: DielectricMaterials project manifest count

**Evidence:**

- [Starrydata DielectricMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The DielectricMaterials project reports 9904 samples, 16555 curves, 4643 figures and 2208 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, DielectricMaterials, literature-digitization, overlap, CSV.

<a id="3dsc-mp"></a>
## 3DSC_MP — superconductors with Materials Project structures

Experimental SuperCon critical temperatures associated with matched Materials Project crystal structures, including approximate doping proxies.

**Size:** 5,773 matched crystal structures (source wording: 5,759 SuperCon entries matched with 5,773 crystal structures).

**Scope:** Published 3DSC_MP release; count is one-to-many matched structures

**Release:** 2023 published release. **Year:** 2023.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** critical temperature; composition; structural descriptors.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/aimat-lab/3DSC) · [paper](https://www.nature.com/articles/s41597-023-02721-y) · [code](https://github.com/aimat-lab/3DSC) · [data](https://doi.org/10.6084/m9.figshare.24499930)

Other denominators (not added to the ranking):

- 5,759 SuperCon composition/Tc entries: Experimental label cohort associated with 5773 matched structures; not additional materials

**Evidence:**

- [3DSC Scientific Data descriptor](https://www.nature.com/articles/s41597-023-02721-y) (checked 2026-11-01): Reports 5759 SuperCon entries and 5773 MP-derived structures; CIFs available; matching sometimes uses artificial doping.
- [3DSC_MP repository metadata](https://api.figshare.com/v2/articles/24499930) (checked 2026-11-01): Confirms public data deposit and its stated licence; applies to deposited files.
- [3DSC primary article full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10663493/fullTextXML) (checked 2026-11-01): Confirms 5,759 labels/5,773 MP structures and 9,150 labels/86,490 ICSD structures, artificial doping, ICSD reconstruction limitations and source-cohort overlap.
- [Upstream SuperCon missing-target convention](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/README.md) (checked 2026-11-01): The 3DSC descriptor identifies this Stanev parent. Its author README assigns zero to unreported Tc; inherited zeros must be assessed with measurement provenance.

**Reuse and interpretation notes:**

- Structures can be approximate proxies modified by occupancy substitution; they are not all measurements of the labeled superconducting sample.
- Labels and structures have different provenance.
- The matched SuperCon composition/Tc-entry count is distinct from the larger matched-structure count; the two 3DSC cohorts overlap and should not be summed as independent materials.
- Fourteen matched SuperCon entries have two MP structures, explaining 5,773 structures versus 5,759 matched labels.
- The 3DSC authors operationally label Tc=0 entries as nonsuperconductors. Their Stanev parent also assigns zero to unreported Tc; zero alone does not verify a tested negative or a lower-temperature detection bound.

**Tags:** Scientific-Data, superconductivity, matched-structures, superconductor, superconductors.

<a id="ocx24-experimental"></a>
## Open Catalyst Experiments 2024 (OCx24) experimental data

Electrocatalyst tests with composition, XRF and XRD phase-matching metadata, linked to a separate computational screening cohort.

**Size:** 5,412 experimental test records (source wording: 5,412 raw test rows; 672 distinct sample IDs).

**Scope:** Directly counted in pinned raw CSV; repeated conditions/reactions/replicates per sample

**Release:** ExpDataDump_241113.csv at fairchem 61266df4188e. **Year:** 2024.

**Provenance:** experimental. **Structure availability:** `structure_linked`.

**Labels/content:** cell voltage; current density; Faradaic efficiency; composition; XRF; XRD phase matches.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/applications/ocx/data) · [data](https://raw.githubusercontent.com/facebookresearch/fairchem/61266df4188eeca70fc56baebfba8abd74a0c695/src/fairchem/applications/ocx/data/experimental_data/ExpDataDump_241113.csv) · [code](https://github.com/facebookresearch/fairchem)

Other denominators (not added to the ranking):

- 672 distinct sample IDs: Pinned raw experimental CSV, including all unfiltered samples

**Evidence:**

- [OCx24 pinned raw experimental CSV](https://raw.githubusercontent.com/facebookresearch/fairchem/61266df4188eeca70fc56baebfba8abd74a0c695/src/fairchem/applications/ocx/data/experimental_data/ExpDataDump_241113.csv) (checked 2026-11-01): Direct CSV enumeration gives 5412 rows and 672 unique sample id values; SHA-256 saved in receipt.
- [OCx24 author data documentation](https://raw.githubusercontent.com/facebookresearch/fairchem/main/src/fairchem/applications/ocx/data/README.md) (checked 2026-11-01): Defines experimental/XRD/XRF data and separate clean/processed cohorts; computational screening is a separate table.

**Reuse and interpretation notes:**

- Raw sample-ID count differs from the collection's 572-sample summary; retain exact cohort and filtering definitions.
- Replicates and test conditions expand row count; rows are not unique compositions.
- XRD phase matches do not establish unique atomic structures for every sample.
- MIT software licence was observed; separate experimental-data reuse licence was not verified.

**Tags:** electrocatalysis, XRD-linked, experiment, collection-blaiszik.

<a id="starrydata-condensed-matter"></a>
## Starrydata — Condensed Matter

Digitized experimental property curves and sample/publication metadata in the Starrydata CondensedMatter project.

**Size:** 4,409 samples (source wording: 4,409 sample rows; 6,848 curve rows).

**Scope:** Project CondensedMatter within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Condensed Matter project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_curves.csv.gz)

Other denominators (not added to the ranking):

- 6,848 curves: CondensedMatter project manifest count
- 1,943 figures: CondensedMatter project manifest count
- 808 papers: CondensedMatter project manifest count

**Evidence:**

- [Starrydata CondensedMatter project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The CondensedMatter project reports 4409 samples, 6848 curves, 1943 figures and 808 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, CondensedMatter, literature-digitization, overlap, CSV.

<a id="digbat"></a>
## DigBat / Dynamic Database of Solid-State Electrolytes

Curated solid-electrolyte compositions and transport measurements linked to a separate computational collection.

**Size:** 3,816 experimental electrolyte materials (source wording: 3,816 experimental solid-state electrolytes).

**Scope:** June-2026 experimental subset across inorganic, solid-polymer and gel-polymer modules

**Release:** June 2026 experimental subset. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `mixed`.

**Labels/content:** ionic conductivity; activation energy; temperature; processing metadata.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.digbat.org) · [data](https://www.digbat.org) · [paper](https://doi.org/10.1016/j.nanoms.2026.07.001)

**Evidence:**

- [Tohoku University DigBat provider announcement](https://www.tohoku.ac.jp/en/press/digbat_an_ai_ready_digital_platform_for_solid_state_battery_research.html) (checked 2026-11-01): June-2026 statistics distinguish 3816 experimental materials, 27645 conductivity entries and 852 computational materials.
- [DigBat author paper](https://www.sciencedirect.com/science/article/pii/S2589965126001236) (checked 2026-11-01): Describes DDSE extension to inorganic/polymer electrolytes and integrated transport simulations.

**Reuse and interpretation notes:**

- Experimental material count excludes the separate 852 computational entries.
- Polymer/gel modules are adjacent to crystalline materials; filter for inorganic SSEs when required.
- Portal connection failed in this audit; release data verified through provider announcement and author paper.
- Open web access does not establish a bulk-redistribution licence.

**Tags:** solid-electrolytes, ionic-transport, DDSE, mixed-material-classes.

<a id="starrydata-resistor"></a>
## Starrydata — Resistor

Digitized experimental property curves and sample/publication metadata in the Starrydata Resistor project.

**Size:** 3,776 samples (source wording: 3,776 sample rows; 4,627 curve rows).

**Scope:** Project Resistor within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Resistor project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_curves.csv.gz)

Other denominators (not added to the ranking):

- 4,627 curves: Resistor project manifest count
- 1,339 figures: Resistor project manifest count
- 785 papers: Resistor project manifest count

**Evidence:**

- [Starrydata Resistor project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The Resistor project reports 3776 samples, 4627 curves, 1339 figures and 785 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, Resistor, literature-digitization, overlap, CSV.

<a id="starrydata-general-db"></a>
## Starrydata — General DB

Digitized experimental property curves and sample/publication metadata in the Starrydata GeneralDB project.

**Size:** 2,158 samples (source wording: 2,158 sample rows; 7,589 curve rows).

**Scope:** Project GeneralDB within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; General DB project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_curves.csv.gz)

Other denominators (not added to the ranking):

- 7,589 curves: GeneralDB project manifest count
- 1,670 figures: GeneralDB project manifest count
- 297 papers: GeneralDB project manifest count

**Evidence:**

- [Starrydata GeneralDB project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The GeneralDB project reports 2158 samples, 7589 curves, 1670 figures and 297 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, GeneralDB, literature-digitization, overlap, CSV.

<a id="starrydata-high-thermal-conductivity-materials"></a>
## Starrydata — High Thermal Conductivity Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata HighThermalConductivityMaterials project.

**Size:** 1,737 samples (source wording: 1,737 sample rows; 2,638 curve rows).

**Scope:** Project HighThermalConductivityMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; High Thermal Conductivity Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 2,638 curves: HighThermalConductivityMaterials project manifest count
- 718 figures: HighThermalConductivityMaterials project manifest count
- 351 papers: HighThermalConductivityMaterials project manifest count

**Evidence:**

- [Starrydata HighThermalConductivityMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The HighThermalConductivityMaterials project reports 1737 samples, 2638 curves, 718 figures and 351 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, HighThermalConductivityMaterials, literature-digitization, overlap, CSV.

<a id="starrydata-low-thermal-conductivity-materials"></a>
## Starrydata — Low Thermal Conductivity Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata LowThermalConductivityMaterials project.

**Size:** 1,654 samples (source wording: 1,654 sample rows; 3,553 curve rows).

**Scope:** Project LowThermalConductivityMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Low Thermal Conductivity Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 3,553 curves: LowThermalConductivityMaterials project manifest count
- 846 figures: LowThermalConductivityMaterials project manifest count
- 274 papers: LowThermalConductivityMaterials project manifest count

**Evidence:**

- [Starrydata LowThermalConductivityMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The LowThermalConductivityMaterials project reports 1654 samples, 3553 curves, 846 figures and 274 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, LowThermalConductivityMaterials, literature-digitization, overlap, CSV.

<a id="starrydata-organic-thermoelectric-materials"></a>
## Starrydata — Organic Thermoelectric Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata OrganicThermoelectricMaterials project.

**Size:** 1,590 samples (source wording: 1,590 sample rows; 4,263 curve rows).

**Scope:** Project OrganicThermoelectricMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Organic Thermoelectric Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 4,263 curves: OrganicThermoelectricMaterials project manifest count
- 797 figures: OrganicThermoelectricMaterials project manifest count
- 181 papers: OrganicThermoelectricMaterials project manifest count

**Evidence:**

- [Starrydata OrganicThermoelectricMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The OrganicThermoelectricMaterials project reports 1590 samples, 4263 curves, 797 figures and 181 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, OrganicThermoelectricMaterials, literature-digitization, overlap, CSV.

<a id="starrydata-hypermaterial"></a>
## Starrydata — Hypermaterial

Digitized experimental property curves and sample/publication metadata in the Starrydata Hypermaterial project.

**Size:** 1,525 samples (source wording: 1,525 sample rows; 2,509 curve rows).

**Scope:** Project Hypermaterial within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Hypermaterial project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_curves.csv.gz)

Other denominators (not added to the ranking):

- 2,509 curves: Hypermaterial project manifest count
- 820 figures: Hypermaterial project manifest count
- 272 papers: Hypermaterial project manifest count

**Evidence:**

- [Starrydata Hypermaterial project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The Hypermaterial project reports 1525 samples, 2509 curves, 820 figures and 272 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, Hypermaterial, literature-digitization, overlap, CSV.

<a id="hypod-x"></a>
## HYPOD-X: quasicrystals and approximants

Literature-curated compositions, structural types, synthesis, phase regions and temperature-dependent properties.

**Size:** 1,448 composition/sample instances (source wording: 915 QCs, 525 ACs, and 8 QCs or ACs).

**Scope:** Composition dataset only; sum of three explicitly reported classes

**Release:** Figshare v3, 2024 release. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `structure_linked`.

**Labels/content:** composition; structure type; sample fabrication; phase diagrams; thermal conductivity; electrical resistivity; magnetic susceptibility.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://www.nature.com/articles/s41597-024-04043-z) · [paper](https://www.nature.com/articles/s41597-024-04043-z) · [data](https://doi.org/10.6084/m9.figshare.25650705.v3)

**Evidence:**

- [HYPOD-X Scientific Data descriptor](https://www.nature.com/articles/s41597-024-04043-z) (checked 2026-11-01): Composition dataset has 915 QC, 525 AC and 8 ambiguous instances; separate property dataset has 1449 curves and 52311 points.
- [HYPOD-X v3 Figshare metadata](https://api.figshare.com/v2/articles/25650705/versions/3) (checked 2026-11-01): Confirms published v3 data deposit and CC BY 4.0.

**Reuse and interpretation notes:**

- Counted sample/composition instances are not atomic coordinate structures.
- Includes aperiodic quasicrystals; approximants are periodic.
- Property dataset overlaps Starrydata infrastructure and should not be summed with it.

**Tags:** Scientific-Data, quasicrystals, approximants, Starrydata-linked.

<a id="supermat-linked-records"></a>
## SuperMat public superconductivity linked-record CSV

Public linked material, critical-temperature, pressure and measurement-method records exported from the SuperMat annotated literature corpus.

**Size:** 1,305 linked literature records (source wording: 1,305 nonheader linked-record rows in SuperMat-2.0.csv).

**Scope:** Public CSV 2.0 export, independently counted; not the entire article-annotation corpus

**Release:** SuperMat-2.0.csv; snapshot 2026-11-01. **Year:** 2021.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** material mention; critical-temperature statement; pressure mention; measurement method; article identifier.

**Access:** mixed. **Dataset license:** CC BY 4.0 (dataset); Apache 2.0 (code).

**Official routes:** [homepage](https://github.com/lfoppiano/SuperMat) · [data](https://github.com/lfoppiano/SuperMat/blob/master/data/csv/SuperMat-2.0.csv) · [paper](https://doi.org/10.1080/27660400.2021.1918396) · [code](https://github.com/lfoppiano/SuperMat)

**Evidence:**

- [SuperMat author repository README](https://raw.githubusercontent.com/lfoppiano/SuperMat/master/README.md) (checked 2026-11-01): Specifies dataset CC BY 4.0 and code Apache 2.0; notes copyrighted full-text corpus cannot be publicly distributed and is held in a private submodule.
- [SuperMat public CSV 2.0](https://raw.githubusercontent.com/lfoppiano/SuperMat/master/data/csv/SuperMat-2.0.csv) (checked 2026-11-01): Independently parsed 1,305 nonheader rows with material, tcValue, pressure, me_method and source-filename fields. SHA-256 80e84ab67649a562a838c5a58fa8bb8025fe1e3225ad2eb664d9bcf3be8ed3ce.

**Reuse and interpretation notes:**

- Public linked CSV is accessible; full copyrighted article text and full annotations are not generally public.
- Rows describe literature relations and may include partial material mentions; they are not 1,305 unique compositions or independently measured Tc values.
- Original paper corpus statistics describe another unit/version and are not substituted for this CSV row count.

**Tags:** superconductivity, text mining, named entities, relation extraction, SuperCon, superconductor, superconductors.

<a id="sc-comics"></a>
## SC-CoMIcs superconductivity information-extraction corpus

Superconductivity abstract corpus with stand-off named-entity and relation annotations for materials information extraction.

**Size:** 1,000 annotated abstracts (source wording: 1,000 superconductivity-related abstracts).

**Scope:** SC-CoMIcs version 3 corpus; abstracts are not unique material records

**Release:** Mendeley Data version 3 (2021-06-29). **Year:** 2021.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** material entity annotations; critical-temperature text annotations; relation annotations.

**Access:** open. **Dataset license:** CC BY-NC 3.0 (deposit and abstract text); separate annotation-specific license Not verified.

**Official routes:** [homepage](https://data.mendeley.com/datasets/xc9fjz2p3h/3) · [data](https://doi.org/10.17632/xc9fjz2p3h.3) · [paper](https://aclanthology.org/2020.lrec-1.834/) · [code](https://github.com/tti-coin/sc-comics)

**Evidence:**

- [SC-CoMIcs Mendeley Data version 3](https://data.mendeley.com/datasets/xc9fjz2p3h/3) (checked 2026-11-01): Author deposit describes 1,000 abstracts and stand-off annotations; abstract sharing is specifically permitted under CC BY-NC 3.0 and version 3 does not change the corpus content.
- [SC-CoMIcs author repository](https://github.com/tti-coin/sc-comics) (checked 2026-11-01): Provides corpus tools and annotated files; links abstract text to the Mendeley deposit under CC BY-NC 3.0.

**Reuse and interpretation notes:**

- Abstract text has a noncommercial license; a separate annotation-specific license was not independently verified.
- The ranked count denotes documents, not superconducting compounds or measured Tc observations.
- Useful for information-extraction benchmarks, not a ready-made atomic-structure/Tc dataset.

**Tags:** superconductivity, text mining, corpus, named entities, relation extraction, superconductor, superconductors.

<a id="starrydata-solid-state-battery-materials"></a>
## Starrydata — Solid State Battery Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata SolidStateBatteryMaterials project.

**Size:** 967 samples (source wording: 967 sample rows; 2,002 curve rows).

**Scope:** Project SolidStateBatteryMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Solid State Battery Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 2,002 curves: SolidStateBatteryMaterials project manifest count
- 644 figures: SolidStateBatteryMaterials project manifest count
- 109 papers: SolidStateBatteryMaterials project manifest count

**Evidence:**

- [Starrydata SolidStateBatteryMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The SolidStateBatteryMaterials project reports 967 samples, 2002 curves, 644 figures and 109 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, SolidStateBatteryMaterials, literature-digitization, overlap, CSV.

<a id="starrydata-piezoelectric-materials"></a>
## Starrydata — Piezoelectric Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata PiezoelectricMaterials project.

**Size:** 680 samples (source wording: 680 sample rows; 1,036 curve rows).

**Scope:** Project PiezoelectricMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Piezoelectric Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 1,036 curves: PiezoelectricMaterials project manifest count
- 320 figures: PiezoelectricMaterials project manifest count
- 102 papers: PiezoelectricMaterials project manifest count

**Evidence:**

- [Starrydata PiezoelectricMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The PiezoelectricMaterials project reports 680 samples, 1036 curves, 320 figures and 102 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, PiezoelectricMaterials, literature-digitization, overlap, CSV.

<a id="x2db"></a>
## Experimental 2D Materials Database (X2DB)

Structured literature metadata for experimentally realized monolayer and few-layer materials, linked where possible to computational structures.

**Size:** 603 metadata records (source wording: Found 603 rows out of 603).

**Scope:** Live unfiltered X2DB rows; multiple publications or samples may share composition

**Release:** Provider live table, checked 2026-11-01. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `structure_linked`.

**Labels/content:** synthesis methods; crystal phase; layer count; morphology; substrates; characterization metadata.

**Access:** open. **Dataset license:** CC BY-NC 4.0.

**Official routes:** [homepage](https://x2db.fysik.dtu.dk/) · [data](https://x2db.fysik.dtu.dk/) · [paper](https://doi.org/10.1021/acsnano.6c01514)

**Evidence:**

- [X2DB live provider table](https://x2db.fysik.dtu.dk/) (checked 2026-11-01): Unfiltered table displays 603 rows and CC BY-NC 4.0 licensing.
- [2DHub: X2DB documentation](https://2dhub.org/x2db/x2db.html) (checked 2026-11-01): Provider describes experimental literature metadata and computational structure links; explicitly excludes measurement datasets.

**Reuse and interpretation notes:**

- Contains metadata, not raw experimental measurement datasets.
- 603 rows are not necessarily 603 unique compositions or atomic structures.
- Noncommercial licence conditions apply.

**Tags:** 2D, experimental-metadata, structure-linked, collection-blaiszik.

<a id="starrydata-air-battery-materials"></a>
## Starrydata — Air Battery Materials

Digitized experimental property curves and sample/publication metadata in the Starrydata AirBatteryMaterials project.

**Size:** 529 samples (source wording: 529 sample rows; 1,176 curve rows).

**Scope:** Project AirBatteryMaterials within full Starrydata snapshot; a membership subset that can overlap other projects

**Release:** DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** digitized property curves; sample composition; publication metadata; Air Battery Materials project.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases/tag/latest) · [code](https://github.com/starrydata/starrydata_datasets) · [papers](https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_papers.csv.gz) · [samples](https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_samples.csv.gz) · [curves](https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_curves.csv.gz)

Other denominators (not added to the ranking):

- 1,176 curves: AirBatteryMaterials project manifest count
- 292 figures: AirBatteryMaterials project manifest count
- 45 papers: AirBatteryMaterials project manifest count

**Evidence:**

- [Starrydata AirBatteryMaterials project manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): The AirBatteryMaterials project reports 529 samples, 1176 curves, 292 figures and 45 papers in DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST). File byte lengths and SHA-256 hashes match GitHub release metadata.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata latest release asset metadata](https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest) (checked 2026-11-01): Project papers, samples and curves archives are listed. All 45 full/project file sizes and digest hashes match the inspected manifest; payloads were not independently recounted.

**Reuse and interpretation notes:**

- A subset of starrydata2, not an independent additional material collection; project membership overlaps.
- Sample count is not unique composition or refined crystal-structure count; curves can contain multiple x/y values.
- Atomic coordinates and complete phase information are not guaranteed.
- Latest download URLs are mutable; compare SHA-256 and size with the saved file manifest.
- The provider documents 2026 sample-ID collisions and corrected releases; preserve source-paper IDs when joining.

**Tags:** Starrydata, project-subset, AirBatteryMaterials, literature-digitization, overlap, CSV.

<a id="robinson-hts-critical-current"></a>
## Robinson HTS Wire Critical Current Database

Experimental critical-current characterizations of commercial HTS wire and film samples across temperature, field magnitude and field angle, with n-values and downloadable data.

**Size:** 24 wire/film characterization datasets (source wording: 24 public wire/film-characterization datasets in Figshare collection v23).

**Scope:** Collection articles_count=24, independently matched by the 24-item public articles list; not the number of measurement points or unique superconducting compounds

**Release:** Figshare collection v23, published 2025-10-14; checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** critical current; n-value; temperature dependence; magnetic-field dependence; field-angle dependence; wire/sample metadata.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International (individual datasets).

**Official routes:** [homepage](https://htsdb.wimbush.eu/about) · [data](https://doi.org/10.6084/m9.figshare.c.2861821) · [paper](https://doi.org/10.1109/TASC.2016.2628700)

**Evidence:**

- [Robinson HTS collection metadata](https://api.figshare.com/v2/collections/2861821) (checked 2026-11-01): Public collection v23 declares 24 articles and a 2025-10-14 publication snapshot.
- [Robinson HTS public collection articles](https://api.figshare.com/v2/collections/2861821/articles?page_size=100) (checked 2026-11-01): Public list contains 24 characterization datasets, including commercial wires and a YBCO film.
- [Robinson HTS database official documentation](https://htsdb2.wimbush.eu/about) (checked 2026-11-01): Describes complete Figshare datasets for particular samples, critical-current/n-value curves and CC BY 4.0 licensing.

**Reuse and interpretation notes:**

- Twenty-four counts characterized wire/film datasets; each contains many operating-condition measurements and is not a new bulk crystal.
- Commercial product/sample variation matters; multiple products can share the same superconducting composition.
- No atomic-coordinate structures are promised by the wire-performance dataset.
- The web visualizer is JavaScript-dependent; the Figshare collection provides the archival data route.

**Tags:** superconductivity, HTS, critical current, wire, REBCO, BSCCO, experimental curves, superconductor, superconductors.

<a id="mdr-supercon"></a>
## MDR SuperCon Datasheet

Versioned successor to the former MatNavi SuperCon superconducting-materials database.

**Size:** Unranked records (source wording: No primary release row count verified).

**Scope:** Ver.240322 metadata; historical SuperCon totals are not substituted

**Release:** Ver.240322. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** critical temperature; superconducting material composition; related measured properties.

**Access:** open. **Dataset license:** Creative Commons BY Attribution 4.0 International.

**Official routes:** [homepage](https://doi.org/10.48505/nims.3739) · [data](https://doi.org/10.48505/nims.4487)

**Evidence:**

- [MDR SuperCon Datasheet Ver.240322](https://mdr.nims.go.jp/datasets/650c4826-f0ca-42e8-8dd9-94025a5307ce?locale=ja) (checked 2026-11-01): NIMS describes re-edited SuperCon, DOI-versioned updates, oxide/metal and organic tables, and CC BY 4.0.
- [NIMS-registered metadata for MDR SuperCon Datasheet Ver.240322](https://api.datacite.org/dois/10.48505/nims.4487) (checked 2026-11-01): Confirms version-specific title, re-edited SuperCon description, related README DOI and CC BY 4.0 rights; supplies no release row count.
- [NIMS-registered metadata for MDR SuperCon series DOI](https://api.datacite.org/dois/10.48505/nims.3739) (checked 2026-11-01): Confirms series landing page and CC BY 4.0; series DOI should not be treated as a fixed version or fixed row count.

**Reuse and interpretation notes:**

- Former GUI service has been replaced by datasheets.
- Use the DOI of the actual version downloaded.
- Full atomic structures are not generally supplied; derivative ML subsets have different cleaning and counts.
- Ver.240322 is a specifically verified version, not a claim to the latest release.
- Direct NIMS dataset access timed out during this audit; version, DOI relationships and CC BY 4.0 were corroborated using NIMS-registered DataCite metadata. A release row count remains unverified.

**Tags:** NIMS, superconductivity, versioned, composition-properties, superconductor, superconductors.

<a id="nist-webhts-srd62"></a>
## NIST WebHTS / High Temperature Superconducting Materials Database (SRD 62)

Evaluated literature data for oxide superconductors, linking thermal, mechanical and superconducting properties with composition, processing and numeric structural descriptors.

**Size:** Unranked evaluated material-property records (source wording: Current material/measurement count not verified).

**Scope:** Historical SRD 62 corpus; no numeric total inferred from portal or search choices

**Release:** Data content last updated 1996; provider metadata version 1.0.0 (2015). **Year:** 2015.

**Provenance:** literature. **Structure availability:** `structure_linked`.

**Labels/content:** critical temperature; superconducting properties; thermal properties; mechanical properties; density; crystal structure descriptors; processing conditions.

**Access:** open. **Dataset license:** NIST Standard Reference Data copyright; all rights reserved. Specific redistribution license not verified; see provider SRD terms..

**Official routes:** [homepage](https://data.nist.gov/pdr/lps/ECBCC1C130112ED9E04306570681B10723) · [data](https://doi.org/10.18434/T4KP8J) · [paper](https://www.nist.gov/publications/nist-www-high-temperature-superconducting-materials-database-webhts-version-20)

**Evidence:**

- [NIST SRD 62 official resource metadata](https://data.nist.gov/od/id/ECBCC1C130112ED9E04306570681B10723) (checked 2026-11-01): Identifies WebHTS, DOI 10.18434/T4KP8J, public access, oxide-superconductor scope, evaluated properties and structural tables.
- [NIST WebHTS search portal](https://srdata.nist.gov/CeramicDataPortal/hit) (checked 2026-11-01): Portal explicitly states last data-content update 1996; query fields include structure type and chemical family.
- [NIST SRD copyright and licensing statements](https://www.nist.gov/open/license) (checked 2026-11-01): Distinguishes copyrighted Standard Reference Data from other NIST employee works; no blanket public-domain assumption is warranted.
- [NIST 62: NIST/NRIM High Temperature Superconductors Database Version 2.0](https://www.nist.gov/publications/nist-62-nistnrim-high-temperature-superconductors-database-version-20) (checked 2026-11-01): R. G. Munro’s 2008 publication documents the same WebHTS/SRD 62 family and 1987–1996 literature; no distinct downloadable corpus/count established.

**Reuse and interpretation notes:**

- Provider page remains reachable; no end-of-service declaration was found, but the scientific data are historical (last content update 1996).
- Public browsing is distinct from permission to redistribute the copyrighted SRD compilation.
- Numeric structural tables do not establish a downloadable CIF/atomic-coordinate dataset.
- IEEE lists the metadata route and legacy search portal separately; both point to the same SRD 62 corpus.

**Tags:** superconductivity, oxide, cuprate, reference data, NIST, historical, superconductor, superconductors.
