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

**Official routes:** [homepage](https://starrydata.github.io/starrydata_datasets/) · [data](https://github.com/starrydata/starrydata_datasets/releases) · [paper](https://doi.org/10.1080/27660400.2025.2590811) · [code](https://github.com/starrydata/starrydata_datasets)

**Evidence:**

- [Starrydata live release manifest](https://starrydata.github.io/starrydata_datasets/manifest.json) (checked 2026-11-01): Snapshot reports 106815 sample rows, 239098 curve rows, 66890 figures and 17560 papers with data; file hashes included.
- [Starrydata 20261101 archival metadata](https://api.figshare.com/v2/articles/34875318) (checked 2026-11-01): November-1 archive identifies its data licence as CC BY 4.0.
- [Starrydata dataset release repository](https://github.com/starrydata/starrydata_datasets) (checked 2026-11-01): Documents daily project splits and sample-ID collision affecting snapshots from 2026-04-01 through 2026-09-08.

**Reuse and interpretation notes:**

- Samples are not deduplicated chemical compositions; curves contain multiple x/y points.
- Avoid affected April–September 2026 snapshots or use composite (SID, sample_id) joins.
- Project splits are membership-based and can overlap; summed project counts overstate the full database.
- Composition and property data do not supply full periodic atomic structures.

**Tags:** priority, literature-digitization, CSV, temperature-dependent, hashes.

<a id="3dsc-icsd"></a>
## 3DSC_ICSD

SuperCon critical temperatures linked to ICSD identifiers and matched structures.

**Size:** 86,490 matched crystal structures (source wording: 9,150 SuperCon entries matched with 86,490 crystal structures).

**Scope:** Published 3DSC_ICSD matches, including repeated measurement conditions

**Release:** 2023 published release. **Year:** 2023.

**Provenance:** mixed. **Structure availability:** `structure_linked`.

**Labels/content:** critical temperature; composition; ICSD structure identifiers.

**Access:** mixed. **Dataset license:** CC BY 4.0 (public labels/IDs only; underlying ICSD CIFs separately licensed).

**Official routes:** [homepage](https://github.com/aimat-lab/3DSC) · [paper](https://www.nature.com/articles/s41597-023-02721-y) · [code](https://github.com/aimat-lab/3DSC) · [data](https://doi.org/10.6084/m9.figshare.24499924)

**Evidence:**

- [3DSC Scientific Data descriptor](https://www.nature.com/articles/s41597-023-02721-y) (checked 2026-11-01): Reports 9150 SuperCon entries matched to 86490 structures; public CSV gives ICSD IDs; full reconstruction requires ICSD licence.
- [3DSC_ICSD (only Tc and ICSD IDs) repository metadata](https://api.figshare.com/v2/articles/24499924) (checked 2026-11-01): Confirms public data deposit and its stated licence; applies to deposited files.

**Reuse and interpretation notes:**

- Public IDs and labels do not confer redistribution rights to ICSD CIFs.
- Many matches share composition but differ in measurement conditions; artificial doping can approximate sample structures.

**Tags:** Scientific-Data, superconductivity, licensed-structures.

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

<a id="3dsc-mp"></a>
## 3DSC_MP

SuperCon critical temperatures linked to Materials Project crystal structures.

**Size:** 5,773 matched crystal structures (source wording: 5,759 SuperCon entries matched with 5,773 crystal structures).

**Scope:** Published 3DSC_MP release; count is one-to-many matched structures

**Release:** 2023 published release. **Year:** 2023.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** critical temperature; composition; structural descriptors.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/aimat-lab/3DSC) · [paper](https://www.nature.com/articles/s41597-023-02721-y) · [code](https://github.com/aimat-lab/3DSC) · [data](https://doi.org/10.6084/m9.figshare.24499930)

**Evidence:**

- [3DSC Scientific Data descriptor](https://www.nature.com/articles/s41597-023-02721-y) (checked 2026-11-01): Reports 5759 SuperCon entries and 5773 MP-derived structures; CIFs available; matching sometimes uses artificial doping.
- [3DSC_MP repository metadata](https://api.figshare.com/v2/articles/24499930) (checked 2026-11-01): Confirms public data deposit and its stated licence; applies to deposited files.

**Reuse and interpretation notes:**

- Structures can be approximate proxies modified by occupancy substitution; they are not all measurements of the labeled superconducting sample.
- Labels and structures have different provenance.

**Tags:** Scientific-Data, superconductivity, matched-structures.

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

**Reuse and interpretation notes:**

- Former GUI service has been replaced by datasheets.
- Use the DOI of the actual version downloaded.
- Full atomic structures are not generally supplied; derivative ML subsets have different cleaning and counts.

**Tags:** NIMS, superconductivity, versioned, composition-properties.
