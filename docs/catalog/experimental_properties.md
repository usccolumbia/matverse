# Experimental properties and literature extraction

[Back to MatVerse](../../README.md)

Checked 2026-11-02. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="cde-stress-strain-2024"></a>
## ChemDataExtractor stress-strain property database

720,308 literature records covering five stress-strain property models, including text- and table-extraction provenance.

**Size:** 720,308 extracted property records (source wording: 720,308).

**Scope:** 720,308 literature records covering five stress-strain property models, including text- and table-extraction provenance.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** yield strength (Pa); ultimate tensile strength (Pa); fracture strength (Pa); Young modulus (Pa); ductility (%); source DOI and extraction metadata.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-03979-6) · [data](https://doi.org/10.6084/m9.figshare.25881025.v1) · [repository](https://github.com/gh-PankajKumar/chemdataextractorv2.3-stresseng)

**Evidence:**

- [A Database of Stress-Strain Properties Auto-generated from the Scientific Literature using ChemDataExtractor](https://www.nature.com/articles/s41597-024-03979-6) (checked 2026-11-01): Data Records states 720,308 records; raw values/units are preserved beside normalized values, and stress units normalize to Pa.
- [Stress-strain dataset deposit](https://api.figshare.com/v2/articles/25881025) (checked 2026-11-01): CC BY 4.0; AllRecords.csv and AllRecords.json plus separate code archive available.

**Reuse and interpretation notes:**

- Records are literature quantities, not unique crystals, specimens or full stress-strain curves.
- May contain noncrystalline/soft materials and multiple reports per material.
- Yield-strength scope overlaps the earlier CDE yield/grain database; extraction errors and alias ambiguity remain.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** Scientific-Data, batteries, text-mining, composition-properties, Scientific-Data-descriptor.

<a id="jcap-metal-oxide-optical-179k"></a>
## JCAP metal-oxide synthesis, imaging and UV–Vis cohort

Composition and processing history linked to RGB images and UV–Vis absorbance spectra.

**Size:** 179,072 synthesized metal-oxide samples (source wording: 179,072).

**Scope:** Material samples only; excludes1,830 substrate references in 180,902 rows

**Release:** 2019 paper cohort; deposit checked 2026-11-01. **Year:** 2019.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** RGB sample images; fractional optical absorbance αL; intended metal composition and loading; annealing and synthesis parameters.

**Access:** open. **Dataset license:** CC0 1.0 (Figshare HDF5).

**Official routes:** [publication](https://doi.org/10.1038/s41597-019-0019-4) · [data](https://doi.org/10.6084/m9.figshare.7502207.v1)

Other denominators (not added to the ranking):

- 99,965 unique intended compositions: Paper-reported material composition count
- 1,830 substrate reference rows: Excluded from main material sample count

**Evidence:**

- [JCAP metal-oxide synthesis, imaging and UV–Vis cohort — Scientific Data descriptor](https://doi.org/10.1038/s41597-019-0019-4) (checked 2026-11-01): Paper identifies179,072 material samples and 99,965 compositions;1,830 blank reference rows are separate. HDF5 has aligned image, composition, spectrum and process fields.
- [JCAP metal-oxide synthesis, imaging and UV–Vis cohort — primary deposit](https://doi.org/10.6084/m9.figshare.7502207.v1) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Intended metal composition is supplied; oxygen stoichiometry is unknown.
- Repeated compositions under different processing conditions are expected.
- Spectra interpolated to 220 energies over 1.31–3.1eV and images resized to 64×64 pixels.
- Not a resolved crystal-structure cohort and distinct from HTEM despite similar high-throughput experimental scope.

**Tags:** Scientific Data, processing, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="solgel-phase-purity-2026"></a>
## Text-mined sol-gel synthesis and phase-purity outcomes

Approximately 148,000 protocols from approximately 53,000 papers, including approximately 28,000 phase-impure records.

**Size:** ~148,000 synthesis protocol records (source wording: ~148,000).

**Scope:** Approximately 148,000 protocols from approximately 53,000 papers, including approximately 28,000 phase-impure records.

**Release:** 2026 article-in-press; Figshare 33040070 v2. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** target/precursor/reagent composition; synthesis operations and conditions; phase-purity classification; impurity phases; characterization methods; source DOI.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-08492-6) · [data](https://doi.org/10.6084/m9.figshare.33040070.v2) · [repository](https://github.com/hackingmaterials/sol-gel-data)

**Evidence:**

- [Text-mined dataset of sol-gel synthesis protocols with phase purity outcomes using large language models](https://www.nature.com/articles/s41597-026-08492-6) (checked 2026-11-01): Article-in-press PDF Data Records gives ~148,000 protocol records and protocol/operations/phase_purity schema; record-level all-field agreement reported as 68%.
- [Sol-gel v2 deposit](https://api.figshare.com/v2/articles/33040070) (checked 2026-11-01): CC BY 4.0; sol_gel_dataset.jsonl available as a 707 MB file.

**Reuse and interpretation notes:**

- Approximate paper count, not an independently recounted archive size; no bulk JSONL download.
- Synthesis records are not independent materials or atomic crystal structures.
- Overlap with earlier solution/solid-state mining corpora is possible; phase-purity labels rely on extracted literature context.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** Scientific-Data, thin-films, high-throughput-experiment, historical-count, Scientific-Data-descriptor.

<a id="cde-refractive-dielectric-2022"></a>
## ChemDataExtractor refractive-index and dielectric database

Literature-mined refractive index and dielectric constant records with conditions and source provenance.

**Size:** 109,880 optical/dielectric literature records (source wording: 109,880).

**Scope:** 49,076 refractive-index records plus 60,804 dielectric-constant records on 11,054 unique chemicals; not a crystal count.

**Release:** 2022 published release. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** refractive index; dielectric constant; wavelength; frequency and dielectric loss when reported; source DOI.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://doi.org/10.6084/m9.figshare.12781142.v2) · [paper](https://doi.org/10.1038/s41597-022-01295-5) · [download](https://ndownloader.figshare.com/files/33982973)

**Count derivation:** separate refractive-index and dielectric records, not unique chemicals; 49,076 + 60,804 = 109,880.

**Evidence:**

- [Zhao and Cole, Scientific Data 9, 192](https://www.nature.com/articles/s41597-022-01295-5) (checked 2026-11-01): Reports separate 49,076/60,804 property denominators and 11,054 chemicals; records preserve wavelength, dielectric loss, units and source metadata.
- [CDE optical database deposit metadata](https://api.figshare.com/v2/articles/12781142) (checked 2026-11-01): Version 2 supplies JSON, SQL, CSV and code under CC BY 4.0.

**Reuse and interpretation notes:**

- Contains organic and inorganic chemicals and is not restricted to crystals; no atomic structures.
- Never treat the total as 109,880 independent materials or assume each record has both properties.
- Frequency, wavelength, specimen and extraction warning flags matter for comparing numerical values.
- Composition-linked literature data require source review to distinguish phases and resolve extraction errors.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="cde-bandgaps-2022"></a>
## ChemDataExtractor semiconductor band-gap database

Literature-extracted semiconductor band gaps with chemical identifiers, temperature and source provenance.

**Size:** 100,236 band-gap literature records (source wording: 100,236).

**Scope:** 100,236 property records extracted from 128,776 papers; 21,053 unique chemical names. Includes 7,656 manually curated BandgapDB records.

**Release:** 2022 published release. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** band gap (eV); measurement temperature (K); chemical composition when parsed; source DOI and sentence.

**Access:** open. **Dataset license:** MIT (Figshare dataset declaration).

**Official routes:** [homepage](https://doi.org/10.6084/m9.figshare.14079863.v1) · [paper](https://doi.org/10.1038/s41597-022-01294-6) · [repository](https://github.com/QingyangDong-qd220/BandgapDatabase1)

**Evidence:**

- [Dong and Cole, Scientific Data 9, 193](https://pmc.ncbi.nlm.nih.gov/articles/PMC9065101/) (checked 2026-11-01): Reports 100,236 non-computational band-gap records; CSV, JSON and MongoDB include temperatures, source DOIs and sentences. Reported weighted precision is 84% and recall 65%.
- [CDE band-gap deposit metadata](https://api.figshare.com/v2/articles/14079863) (checked 2026-11-01): Figshare v1 supplies Bandpgap_database_v2.zip and code_v2.zip under MIT.

**Reuse and interpretation notes:**

- Composition/chemical-name labels are not periodic structures or phase-resolved crystal identifiers.
- Not all semiconductor records are inorganic crystalline solids; filter source context before crystal-only use.
- Repeated conditions, aliases and literature reports are multiple records, not unique materials.
- Overlaps BandgapDB by construction; automatic extraction can introduce assignment errors.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="cde-yield-grainsize"></a>
## ChemDataExtractor yield-strength and grain-size databases

64,269 yield-strength plus 30,285 grain-size records.

**Size:** 94,554 extracted property records (source wording: 94,554).

**Scope:** 64,269 yield-strength plus 30,285 grain-size records. Engineering-ready yield-strength and combined-property tables are derived overlapping subsets.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2022.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** yield strength (Pa); grain size; raw/normalized units and ranges; compound names; source DOI; parser/blacklist flags.

**Access:** open. **Dataset license:** MIT (Figshare data deposit).

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01301-w) · [data](https://doi.org/10.6084/m9.figshare.14946186.v1) · [repository](https://github.com/gh-PankajKumar/ChemDataExtractorStressEng)

**Count derivation:** primary yield-strength + grain-size extraction tables; derived subsets excluded; 64,269 + 30,285 = 94,554.

**Evidence:**

- [Auto-generating databases of Yield Strength and Grain Size using ChemDataExtractor](https://www.nature.com/articles/s41597-022-01301-w) (checked 2026-11-01): Data Records specifies the 64,269 and 30,285 primary extraction counts, plus derived engineering-ready and combined tables.
- [Yield/grain data deposit](https://api.figshare.com/v2/articles/14946186) (checked 2026-11-01): MIT-licensed Databases.zip and separate Code.zip are available.

**Reuse and interpretation notes:**

- Covers materials beyond crystalline metals, including soft materials; filter specimen class before crystal-only use.
- Chemical-name records provide no atomistic structure and can contain extraction/assignment errors.
- Later CDE stress-strain release has overlapping yield-strength scope; do not add as unique materials.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** Scientific-Data, superconductivity, licensed-structures, superconductor, superconductors, Scientific-Data-descriptor.

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

**Tags:** Scientific-Data, synthesis, impurity-phases, LLM-extraction, Scientific-Data-descriptor.

<a id="nemad-magnetic"></a>
## Northeast Materials Database (NEMAD) — magnetic materials

LLM-extracted magnetic literature records with transition temperatures, magnetization and crystallographic descriptors.

**Size:** 67,573 magnetic-material entries (source wording: 67,573).

**Scope:** Paper release; composition, structural descriptors and magnetic properties define entries

**Release:** 2025 paper release, checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Curie / Néel / Curie-Weiss temperature (K); coercivity (Oe); magnetization and remanence (A/m); magnetic moment (μB); susceptibility; crystallographic descriptors and source DOI.

**Access:** open. **Dataset license:** Not verified for full website database; processed ML archive declares CC BY 4.0.

**Official routes:** [homepage](https://www.nemad.org) · [publication](https://doi.org/10.1038/s41467-025-64458-z) · [processed_data](https://github.com/sumanitani/NEMAD-MagneticML) · [archive](https://doi.org/10.5281/zenodo.17042814)

**Evidence:**

- [The northeast materials database for magnetic materials](https://www.nature.com/articles/s41467-025-64458-z) (checked 2026-11-01): Publisher/full text reports 67,573 entries and Table 1 units; full database at nemad.org and processed training data on GitHub/Zenodo.
- [NEMAD-MagneticML v1.0 deposit](https://zenodo.org/records/17042814) (checked 2026-11-01): Open processed ML release; deposit metadata declares CC BY 4.0. This does not establish the license of the full website corpus.

**Reuse and interpretation notes:**

- Independent extraction release; source literature may overlap CDE Curie–Néel and Starrydata magnetic records, so counts cannot be added as unique materials.
- NEMAD is a separate author/provider extraction lineage from Court/Cole ChemDataExtractor/Snowball Curie–Néel releases; literature overlap is plausible and no row-level deduplication or inherited-source equivalence is established.
- Crystal structure/lattice/space-group descriptors do not establish complete atomic-coordinate coverage.
- Retain experimental-status flag and source DOI; property completeness varies. Website requires JavaScript; full live corpus not exported in this audit.

**Tags:** magnetism, literature-mining, conditions-required, property-focused, OpenAlex-survey-20261101.

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

**Tags:** Scientific-Data, magnetism, text-mining, Scientific-Data-descriptor.

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

<a id="cde-dye-sensitized-solar-devices"></a>
## ChemDataExtractor dye-sensitized solar-cell devices

Literature-extracted dye-sensitized solar-cell records with device performance and component-material information.

**Size:** 41,860 device-report JSON documents (source wording: 41,860).

**Scope:** Downloaded Figshare v1 JSON archive has 26,930 Elsevier + 14,930 RSC documents, with 41,860 distinct internal IDs. Paper instead states 41,680 devices and 475,045 attribute sub-entries.

**Release:** Figshare 13516220 v1; independently counted JSONL release. **Year:** 2022.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** power conversion efficiency; open-circuit voltage; short-circuit current/current density; fill factor; device/material names; irradiance and area when available; source DOI; measured/derived value flags.

**Access:** open. **Dataset license:** MIT.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01355-w) · [data](https://doi.org/10.6084/m9.figshare.13516220.v1) · [repository](https://github.com/edbeard/dsc_db)

**Evidence:**

- [Perovskite- and Dye-Sensitized Solar-Cell Device Databases Auto-generated Using ChemDataExtractor](https://www.nature.com/articles/s41597-022-01355-w) (checked 2026-11-01): Describes a DSC device corpus with 475,045 property/material sub-entries; article device count is 41,680. Data contain cognate photovoltaic properties and component materials.
- [Dye-sensitized Solar Cell Database v1](https://api.figshare.com/v2/articles/13516220) (checked 2026-11-01): Deposit declares MIT. Downloaded dsc_json.zip independently contains 41,860 JSONL documents with distinct internal IDs across Elsevier/RSC files.

**Reuse and interpretation notes:**

- Records represent reported photovoltaic devices, not unique chemical compositions or periodic crystal structures.
- Raw, standardized and algebraically derived device quantities coexist; retain calculated-value flags and irradiance/area assumptions.
- Multiple reports of the same material/device can occur; no global physical-device deduplication established.
- JSON and MongoDB releases are alternate formats of the same population.
- Published 41,680 device count disagrees with the 41,860-document archive recount; this record uses the archive and does not silently equate them.
- DSCs include molecular dyes, electrolytes and engineered layers; this is adjacent to crystal-structure data.

**Tags:** Scientific-Data, device-or-engineered-material-scope, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** Scientific-Data, magnetism, text-mining, historical-release, Scientific-Data-descriptor.

<a id="nist-isodb"></a>
## NIST/ARPA-E adsorption isotherm database (NIST-ISODB)

Literature-traceable single- and multicomponent adsorption measurements for solid adsorbents, including MOFs and zeolites.

**Size:** 37,703 adsorption isotherms (source wording: 37,703).

**Scope:** Historical provider count as of 2023-12-01; not the current live total or number of crystals

**Release:** Provider documented 2023-12-01 snapshot; access rechecked 2026-11-01. **Year:** 2016.

**Provenance:** experimental. **Structure availability:** `structure_linked`.

**Labels/content:** adsorption isotherms; temperature; pressure; adsorbent and adsorbate identity; measurement metadata; source DOI.

**Access:** open. **Dataset license:** Not verified: NIST metadata links generic open-data license, but database homepage requests contacting technical staff about data licensing/reproduction.

**Official routes:** [homepage](https://adsorption.nist.gov/isodb/index.php) · [api](https://adsorption.nist.gov/isodb/index.php#apis) · [metadata](https://data.nist.gov/od/id/FF429BC1787D8B3EE0431A570681E858236) · [doi](https://doi.org/10.18434/T43882)

Other denominators (not added to the ranking):

- 8,265 adsorbent material identities: Same provider historical snapshot, 2023-12-01
- 4,367 source articles: Same provider historical snapshot, 2023-12-01

**Evidence:**

- [NIST Data Resources for Adsorption](https://www.nist.gov/programs-projects/nist-data-resources-adsorption) (checked 2026-11-01): Provider gives 37,703 isotherms, 8,265 adsorbents, 449 adsorbates and 4,367 articles as of December 1, 2023. Isotherms derive from interlaboratory studies, contributed data or tabulation/digitization of published articles; API formats include JSON/XML/CSV.
- [NIST dataset metadata](https://data.nist.gov/od/id/FF429BC1787D8B3EE0431A570681E858236) (checked 2026-11-01): Dataset DOI, public access and API distribution are explicitly listed, with a link to generic NIST open-license terms.
- [NIST-ISODB homepage](https://adsorption.nist.gov/isodb/index.php#home) (checked 2026-11-01): Live homepage content states data are measured adsorption properties and asks users to consult technical contacts for licensing or reproduction of the data contents. API documentation lists isotherm and material endpoints.

**Reuse and interpretation notes:**

- Isotherms are measurements/curves, not independent crystal structures.
- Includes noncrystalline sorbents; the 37,703 total is not a porous-crystal-only count.
- Registry may link external crystallographic records; periodic coordinates are not guaranteed in each isotherm.
- Direct API JSON attempts returned HTTP 403 during this check; browser homepage and API documentation were retrievable.
- Historical 2023 count is explicitly retained because a new live inventory could not be fetched.

**Tags:** adsorption, experimental, isotherm, NIST, MOF, zeolite, additional-materials-20261101, Data.gov-selection-20261101.

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

**Tags:** Scientific-Data, synthesis, text-mining, JSON, Scientific-Data-descriptor.

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

**Tags:** Scientific-Data, thermoelectrics, text-mining, Scientific-Data-descriptor.

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

**Tags:** Scientific-Data, synthesis, text-mining, JSON, Scientific-Data-descriptor.

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

<a id="ipop-v3"></a>
## IPOP inorganic phosphor optical-property dataset

Literature-curated doped inorganic phosphor observations with experimental optical properties and measurement conditions.

**Size:** 16,023 property observations (source wording: 16,023).

**Scope:** 16,023 observations spanning 3,952 host–dopant combinations, 2,238 host materials, 21 dopant elements and 553 articles in v3.

**Release:** 2024 published release. **Year:** 2024.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** photoluminescence maximum wavelength; photoluminescence excitation maxima; CIE chromaticity coordinates; luminescence lifetime; quantum efficiency; thermal quenching T50; measurement temperature and excitation wavelength.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://doi.org/10.6084/m9.figshare.24771186) · [paper](https://doi.org/10.1038/s41598-024-58351-w) · [repository](https://github.com/KRICT-DATA/IPOP-dataset-ver-3.0)

**Evidence:**

- [Jang et al., Optical property dataset of inorganic phosphor](https://www.nature.com/articles/s41598-024-58351-w) (checked 2026-11-01): Describes v3 composition/host/dopant data, property observations and experimental conditions, with downloadable dataset and feature files.
- [IPOP v3 deposit metadata](https://api.figshare.com/v2/articles/24771186) (checked 2026-11-01): Data deposit licensing and files verified through Figshare metadata.

**Reuse and interpretation notes:**

- Observation counts are not unique crystals and do not imply every observation reports all eight optical targets.
- Doped host formulas and measurement conditions do not constitute atomic coordinate structures.
- Overlaps earlier IPOP versions; retain v3 as the release record rather than additive versions.

**Tags:** property-focused, OpenAlex-survey-20261101.

<a id="cde-perovskite-solar-devices"></a>
## ChemDataExtractor perovskite solar-cell devices

Literature-extracted perovskite solar-device performance and component-material records.

**Size:** 15,818 device-report JSON documents (source wording: 15,818).

**Scope:** Downloaded Figshare v1 archive has 8,259 Elsevier + 7,559 RSC documents with distinct internal IDs; paper reports 185,836 property/material sub-entries for these 15,818 devices.

**Release:** Figshare 13516238 v1; independently counted JSONL release. **Year:** 2022.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** power conversion efficiency; open-circuit voltage; short-circuit current/current density; fill factor; device/material names; irradiance and area when available; source DOI; measured/derived value flags.

**Access:** open. **Dataset license:** MIT.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01355-w) · [data](https://doi.org/10.6084/m9.figshare.13516238.v1) · [repository](https://github.com/edbeard/pv_database)

**Evidence:**

- [Perovskite- and Dye-Sensitized Solar-Cell Device Databases Auto-generated Using ChemDataExtractor](https://www.nature.com/articles/s41597-022-01355-w) (checked 2026-11-01): Separately describes PSC and DSC corpora; the PSC corpus contains 185,836 attribute sub-entries organized into 15,818 photovoltaic records.
- [Perovskite Solar Cell Database v1](https://api.figshare.com/v2/articles/13516238) (checked 2026-11-01): Deposit declares MIT. Independently parsed PSC JSONL files contain 15,818 documents and distinct internal IDs.

**Reuse and interpretation notes:**

- Records represent reported photovoltaic devices, not unique chemical compositions or periodic crystal structures.
- Raw, standardized and algebraically derived device quantities coexist; retain calculated-value flags and irradiance/area assumptions.
- Multiple reports of the same material/device can occur; no global physical-device deduplication established.
- JSON and MongoDB releases are alternate formats of the same population.
- Distinct extraction lineage from the manually compiled Perovskite Database Project, with potentially overlapping source papers/devices. Do not add as independent unique materials.

**Tags:** Scientific-Data, device-or-engineered-material-scope, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="cde-photocatalysis-water-splitting"></a>
## ChemDataExtractor water-splitting photocatalysis

15,755 extracted activity records from a 47,357-paper corpus, with catalyst and reaction/illumination context.

**Size:** 15,755 extracted photocatalytic activity records (source wording: 15,755).

**Scope:** 15,755 extracted activity records from a 47,357-paper corpus, with catalyst and reaction/illumination context.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2023.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** water-splitting activity; photocatalyst/co-catalyst composition; additives; illumination wavelength/source; experiment duration; source DOI.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-023-02511-6) · [data](https://doi.org/10.6084/m9.figshare.21932211.v1) · [repository](https://github.com/ti250/cdedatabase)

**Evidence:**

- [Automated Construction of a Photocatalysis Dataset for Water-Splitting Applications](https://www.nature.com/articles/s41597-023-02511-6) (checked 2026-11-01): Paper reports 15,755 records with catalyst, co-catalyst, additive, reaction time and light conditions; evaluated precision 71.2%, recall 36.3%.
- [Photocatalysis data deposit](https://api.figshare.com/v2/articles/21932211) (checked 2026-11-01): CC BY 4.0; databasefiles.zip is public.

**Reuse and interpretation notes:**

- Activity records are not unique crystals and may involve composite/noncrystalline catalysts.
- Units and normalization bases differ by source; preserve extracted reaction context.
- Extraction performance limits and source assignment should be retained; no atomic structures.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="aluminum-alloy-literature-2022"></a>
## Aluminum alloy composition and mechanical-property literature datasets

14,884 composition records and a separate 1,278-record mechanical-property table.

**Size:** 14,884 alloy composition entries (source wording: 14,884).

**Scope:** 14,884 composition records and a separate 1,278-record mechanical-property table. Sources are journal full text, tables, registered Aluminum Association designations and patents.

**Release:** Materials Cloud 2021.80 v1; 2022 descriptor. **Year:** 2022.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** element weight fractions; alloy designation; yield/tensile strength; elongation; processing state; source DOI/patent.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01215-7) · [data](https://doi.org/10.24435/MATERIALSCLOUD:VX-FY)

**Evidence:**

- [Aluminum alloy compositions and properties extracted from a corpus of scientific manuscripts and US patents](https://www.nature.com/articles/s41597-022-01215-7) (checked 2026-11-01): Paper describes composition.csv with 14,884 rows (4,958 full text, 5,227 table, 550 named, 4,149 patent) and properties.csv with 1,278 observations.
- [Materials Cloud aluminum alloy archive](https://archive.materialscloud.org/records/8djnx-brx78) (checked 2026-11-01): Version v1 record openly supplies composition/property files and declares CC BY 4.0.

**Reuse and interpretation notes:**

- The two table counts are different data types; 14,884 is not the count of measured property labels.
- Multiple reports/designations can describe the same alloy; compositions are not unique crystals.
- Tables do not supply periodic atomic structures.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="ultera-2025"></a>
## ULTERA high-entropy-alloy property database

Literature-curated compositionally complex alloy properties with processing/phase context, including refractory alloys.

**Size:** ≥12,540 experimental HEA/MEA property observations (source wording: 12,540).

**Scope:** Literature-curated compositionally complex alloy properties with processing/phase context, including refractory alloys.

**Release:** Zenodo May 2025 alpha snapshot. **Year:** 2025.

**Provenance:** experimental; literature-curated. **Structure availability:** `composition_only`.

**Labels/content:** mechanical properties; phase/processing metadata; thermal and magnetic property fields; source DOI and composition.

**Access:** restricted. **Dataset license:** Not verified; access is granted through provider review.

**Official routes:** [homepage](https://phaseslab.com/ultera/) · [data](https://doi.org/10.5281/zenodo.15716432)

Other denominators (not added to the ranking):

- 15,462 property datapoints including support data: Provider count including lower-entropy alloys
- 4,270 experimentally observed HEA/MEA materials (lower bound): Provider 4,270+ composition/processing/material identities
- 813 source publications: May 2025 snapshot

**Evidence:**

- [ULTERA May 2025 alpha snapshot](https://zenodo.org/records/15716432) (checked 2026-11-01): Reports 12,540+ experimental HEA/MEA property points, 4,270+ materials and 813 publications; files are restricted and access requests require collaborator review.
- [ULTERA public deposit metadata](https://zenodo.org/api/records/15716432) (checked 2026-11-01): Access_right is restricted, no public file list or data license was returned; public metadata differs from file access.

**Reuse and interpretation notes:**

- Provider-gated release; no access request was submitted and no private data were retrieved.
- The larger 15,462 total includes lower-entropy support data; it is not the ranked HEA/MEA denominator.
- May overlap other published alloy datasets; source records must be reconciled before merging.

**Tags:** additional-materials-20261101.

<a id="hea-llm-2026"></a>
## LLM high-entropy alloy phase and processing database

12,427 extracted HEA entries from 4,625 publisher-accessible papers, with experimental/theoretical origin and phase/synthesis context.

**Size:** 12,427 literature-derived alloy entries (source wording: 12,427).

**Scope:** 12,427 extracted HEA entries from 4,625 publisher-accessible papers, with experimental/theoretical origin and phase/synthesis context.

**Release:** Mendeley Data j75v9bbbjz v1; 2026 descriptor. **Year:** 2026.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** alloy composition; phase identities and count; processing conditions; experimental/theoretical study type.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-06930-z) · [data](https://doi.org/10.17632/j75v9bbbjz.1) · [repository](https://github.com/Vladimirchizh/hea_database)

**Evidence:**

- [High Entropy Alloys Database generated with Large Language Model](https://www.nature.com/articles/s41597-026-06930-z) (checked 2026-11-01): Paper reports 12,427 HEAs characterized from 4,625 papers, distinguishing experimental and theoretical studies and phase parsing limitations.
- [HEA_database Mendeley v1](https://data.mendeley.com/datasets/j75v9bbbjz/1) (checked 2026-11-01): Deposit published 2025-12-25; lists parsed and raw-response CSV datasets and declares CC BY 4.0.

**Reuse and interpretation notes:**

- Not 12,427 verified unique crystal structures; phase labels do not provide coordinates.
- LLM extraction and CSV parsing have separate error modes; variable composition series can be collapsed incorrectly.
- Publisher-accessible subset covers only about 20% of the corpus described in the paper; overlaps earlier alloy compilations.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="feptp-iron-phase-pathways"></a>
## FePTP iron-containing phase-transformation pathways

Iron-phase precursor/product identities, operation conditions and transformation outcomes extracted from literature.

**Size:** 11,241 phase-transformation pathways (source wording: 11,241).

**Scope:** Published text-mined cohort from 4,245 papers

**Release:** 2026 paper cohort; deposit checked 2026-11-01. **Year:** 2026.

**Provenance:** literature_extracted. **Structure availability:** `composition_only`.

**Labels/content:** precursor/product phase; reaction category and operation sequence; temperature/time and other reaction conditions; extent of transformation; reaction equations.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare v2).

**Official routes:** [publication](https://doi.org/10.1038/s41597-026-07067-9) · [data](https://doi.org/10.6084/m9.figshare.30759095.v2)

Other denominators (not added to the ranking):

- 4,245 source papers: Literature supporting pathway cohort

**Evidence:**

- [FePTP iron-containing phase-transformation pathways — Scientific Data descriptor](https://doi.org/10.1038/s41597-026-07067-9) (checked 2026-11-01): Data Records describe 11,241 pathways from 4,245 papers, including unchanged outcomes; release supplies pathways.jsonl and mineral glossary.
- [FePTP iron-containing phase-transformation pathways — primary deposit](https://doi.org/10.6084/m9.figshare.30759095.v2) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Includes environmental/mineral and biotransformation pathways; select solid-state/materials transformations for MatVerse-specific reuse.
- Phase names/compositions are provided, not resolved atomic structures.
- Changed and unchanged pathways must remain distinct; automated extraction is not proof of phase-pure synthesis.

**Tags:** Scientific Data, processing, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="system-thermoelectric"></a>
## sysTEm systematically verified experimental thermoelectrics

Curated experimental thermoelectric transport values with publication and source-dataset provenance.

**Size:** 8,650 composition–temperature observations (source wording: 8,650).

**Scope:** Curated experimental thermoelectric transport values with publication and source-dataset provenance.

**Release:** GitHub main workbook snapshot 2026-11-01. **Year:** 2026.

**Provenance:** experimental; literature-curated. **Structure availability:** `composition_only`.

**Labels/content:** temperature (K); Seebeck coefficient (µV/K); electrical conductivity (S/cm); power factor; zT; total/electronic/lattice thermal conductivity.

**Access:** open. **Dataset license:** MIT (repository declaration).

**Official routes:** [homepage](https://github.com/tankylz/sysTEm_dataset) · [data](https://github.com/tankylz/sysTEm_dataset/blob/main/sysTEm_dataset.xlsx) · [paper](https://doi.org/10.1007/s40192-026-00446-5)

Other denominators (not added to the ranking):

- 1,437 standardized composition strings: Distinct current Pymatgen Composition strings; not independently deduplicated experimental specimens

**Evidence:**

- [sysTEm author repository](https://github.com/tankylz/sysTEm_dataset) (checked 2026-11-01): Describes MRL/ESTM merger and systematic zT consistency checks with a 10% tolerance; lists columns and units.
- [Current final workbook](https://raw.githubusercontent.com/tankylz/sysTEm_dataset/main/sysTEm_dataset.xlsx) (checked 2026-11-01): Independently counted 8,650 nonempty data rows/unique row IDs and 1,437 standardized composition strings; temperature range 10–1275 K.
- [sysTEm repository license](https://raw.githubusercontent.com/tankylz/sysTEm_dataset/main/LICENSE) (checked 2026-11-01): Repository declares MIT; parent-source lineage remains explicit.

**Reuse and interpretation notes:**

- Overlaps existing ESTM and extended MRL data; do not sum parent and merged counts.
- Rows are temperature observations, not 8,650 distinct materials.
- Formula consistency checks do not independently reproduce measurements; not every row has every target.
- No atomic coordinates are supplied by this workbook.

**Tags:** additional-materials-20261101.

<a id="nemad-thermoelectric"></a>
## NEMAD / GPTArticleExtractor thermoelectric database

Literature-extracted experimental and computational thermoelectric properties with separate measurement temperatures and structural metadata.

**Size:** 7,123 thermoelectric compound entries (source wording: 7,123).

**Scope:** Published 2025 database cohort; not independently deduplicated compositions

**Release:** 2025 paper release, checked 2026-11-01. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** Seebeck coefficient (μV/K); electrical conductivity (S/m); thermal conductivity (W/m/K); power factor (μW/m/K²); dimensionless ZT; property-specific temperature (K); lattice parameters (Å).

**Access:** open. **Dataset license:** Not verified; no dataset-specific license verified.

**Official routes:** [homepage](https://nemad.org) · [publication](https://doi.org/10.1016/j.commatsci.2025.113855) · [preprint](https://arxiv.org/abs/2501.00564)

**Evidence:**

- [Large Language Model-Driven Database for Thermoelectric Materials](https://arxiv.org/html/2501.00564v1) (checked 2026-11-01): Authors report 7,123 entries from Elsevier literature, approximately 66% from experimental papers. Table 1 provides an experimental/theoretical flag, property-specific temperatures and units; conclusion identifies nemad.org as the open database.
- [Published thermoelectric database paper](https://doi.org/10.1016/j.commatsci.2025.113855) (checked 2026-11-01): OpenAlex identifies the 2025 Computational Materials Science version of the same named work; not counted separately from preprint.

**Reuse and interpretation notes:**

- Approximately66% of records are experimental; retain the origin flag. Bulk, thin-film and nanostructured material forms are mixed and must remain distinguished.
- Same hosting platform as magnetic NEMAD but a separate property corpus; no addition to a global unique-material count.
- May overlap Starrydata and ChemDataExtractor thermoelectric source literature.
- Experimental-status field must be retained; missing or mixed measurement temperatures cannot be collapsed into one row-level condition.
- Descriptive crystal metadata does not guarantee complete atomic coordinates.
- Full JavaScript website export and dataset license were not verified.
- The primary paper describes approximately 66% experimental-source papers; theoretical values are also included. Do not interpret the whole dataset as experimental measurements.

**Tags:** thermoelectric, literature-mining, temperature-dependent, property-focused, OpenAlex-survey-20261101.

<a id="co2-electrocatalyst-llm-corpus"></a>
## CO2 electrocatalysis and catalyst synthesis corpora

6,985 benchmark records from 1,081 publications; separate NLP and LLM extended corpora contain 77,016 and 30,283 records from 5,941 documents.

**Size:** 6,985 human-annotated benchmark records (source wording: 6,985).

**Scope:** 6,985 benchmark records from 1,081 publications; separate NLP and LLM extended corpora contain 77,016 and 30,283 records from 5,941 documents.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** catalyst entities; electrocatalysis conditions/results; entity labels and source sentences; catalyst synthesis operations/conditions; source DOI.

**Access:** open. **Dataset license:** Not verified for ScienceDB data deposits.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-03180-9) · [data](https://doi.org/10.57760/sciencedb.13290) · [extended_1](https://doi.org/10.57760/sciencedb.13292) · [extended_2](https://doi.org/10.57760/sciencedb.13293) · [repository](https://github.com/cxqwindy/CO2_reduction_electrocatalysts_db)

**Evidence:**

- [Large language model enhanced corpus of CO2 reduction electrocatalysts and synthesis procedures](https://www.nature.com/articles/s41597-024-03180-9) (checked 2026-11-01): Paper distinguishes manually constructed benchmark records, two machine-extracted corpora, and synthesis procedures; records include entities, labels and source sentences.
- [CO2 corpus data release statement](https://www.nature.com/articles/s41597-024-03180-9) (checked 2026-11-01): Data Records identifies ScienceDB benchmark/extended corpora and separate synthesis-procedure JSON; external data license was not independently confirmed.

**Reuse and interpretation notes:**

- Benchmark/extended corpora overlap sources and represent information-extraction records, not independent measured crystals.
- External deposit rights not verified; article CC BY is not assigned to these datasets.
- No atomic structures, and label/entity records do not imply complete quantitative catalyst-performance tuples.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mce-llm-2024"></a>
## LLM-extracted magnetocaloric materials database (Yuan–Yang–Patra–Liao)

Magnetocaloric literature records retaining entropy change, magnetic field and transition temperature, with separately curated MP-linked subsets.

**Size:** 6,614 literature-extracted material-property rows (source wording: 6,614).

**Scope:** Current modified6125.csv parsed with Python csv: 6,614 rows excluding header; paper describes 6,615 entries

**Release:** 2024 paper release, checked 2026-11-01. **Year:** 2024.

**Provenance:** literature_extracted_mixed. **Structure availability:** `composition_only`.

**Labels/content:** magnetic entropy change ΔSM (source units; typically J/kg/K); magnetic field (T or kOe, source field); Curie temperature (source field); material name; source literature metadata for linked subset.

**Access:** open. **Dataset license:** Not verified; no repository dataset license verified.

**Official routes:** [publication](https://doi.org/10.1063/5.0206855) · [preprint](https://arxiv.org/abs/2403.02553) · [repository](https://github.com/RunqingYang1996/MCEdatabase) · [download](https://github.com/RunqingYang1996/MCEdatabase/blob/main/databasecsv/modified6125.csv)

**Evidence:**

- [Enhancing Magnetocaloric Material Discovery: A Machine Learning Approach Using an Autogenerated Database by Large Language Models](https://arxiv.org/html/2403.02553v1) (checked 2026-11-01): Paper reports 6,615 raw entries, 1,426 inorganic-filtered entries and 752 MP matches. ML training normalizes fields to 5 T and uses 229 unique materials.
- [Primary MCE database repository](https://github.com/RunqingYang1996/MCEdatabase) (checked 2026-11-01): README distinguishes raw, inorganic and human-corrected MP-linked releases. Downloaded modified6125.csv parses to 6,614 data rows; updated linked CSV parses to 714 rows.

**Reuse and interpretation notes:**

- Published and current CSV counts disagree (6,615 vs 6,614; 752 MP matches vs 714 rows in current human-corrected linked CSV); filename labels are not trusted counts.
- The raw database includes organic and alloyed materials; it is not wholly a periodic inorganic crystal dataset.
- Raw field units and string/range values need normalization; field strength strongly affects entropy change.
- The paper's linearly scaled 5 T maximum-per-material training values are derived targets, not direct measurements all made at 5 T.
- Source abstracts may describe experimental and computed results; retain origin and do not label the entire corpus uniformly experimental.

**Tags:** magnetocaloric, literature-mining, field-dependent, mixed-origin, property-focused, OpenAlex-survey-20261101.

<a id="weld-fatigue-2025"></a>
## Welded-joint fatigue property database

5,797 parameter records extracted from 1,666 publications with linked stress–life, strain–life and load–life data.

**Size:** 5,797 fatigue condition/parameter records (source wording: 5,797).

**Scope:** 5,797 parameter records extracted from 1,666 publications with linked stress–life, strain–life and load–life data.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** fatigue life; S–N and ε–N curves; welding process; specimen/loading conditions; alloy processing and geometry.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-06067-5) · [data](https://doi.org/10.6084/m9.figshare.29254265.v2) · [repository](https://github.com/WeldingTJU/DataScience)

**Evidence:**

- [A Dataset of Fatigue Properties for Welded Joints](https://www.nature.com/articles/s41597-025-06067-5) (checked 2026-11-01): Paper discusses all 5,797 parameter records and maps separate fatigue curves to experimental contexts from 1,666 publications.
- [Weld fatigue v2 deposit](https://api.figshare.com/v2/articles/29254265) (checked 2026-11-01): CC BY 4.0; parameter and curve JSONs, Excel database and terminology map listed.

**Reuse and interpretation notes:**

- Parameter records, curve points and source publications are distinct units.
- Dataset is about joints and processing states, not unique chemical compositions/crystals.
- Likely overlaps other literature fatigue compilations; no cross-release source deduplication.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** Scientific-Data, superconductivity, matched-structures, superconductor, superconductors, Scientific-Data-descriptor.

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

<a id="layered-na-cathode-textmine"></a>
## Text-mined layered sodium cathode synthesis and performance

5,265 records from 1,747 documents, combining chemical composition, synthesis parameters and electrochemical cycling/rate relations.

**Size:** 5,265 extracted experimental records (source wording: 5,265).

**Scope:** 5,265 records from 1,747 documents, combining chemical composition, synthesis parameters and electrochemical cycling/rate relations.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** specific capacity; cycling stability; rate performance; test conditions; composition; synthesis parameters; source DOI.

**Access:** open. **Dataset license:** CC0 (Figshare data-item metadata).

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-03196-1) · [data](https://doi.org/10.6084/m9.figshare.c.6828414.v1) · [repository](https://github.com/GGNoWayBack/cathodedataextractor)

**Evidence:**

- [A document-level information extraction pipeline for layered cathode materials for sodium-ion batteries](https://www.nature.com/articles/s41597-024-03196-1) (checked 2026-11-01): Paper abstract and Data Availability identify 5,265 records and public CSV/JSON deposit, preserving experimental and performance relations.
- [Layered cathode extraction collection](https://api.figshare.com/v2/collections/6828414/articles) (checked 2026-11-01): Collection exposes six JSON/CSV data items for cycling, rate and combined data; mirrors/formats and subsets are overlapping.
- [Combined layered cathode data release](https://api.figshare.com/v2/articles/24116592) (checked 2026-11-01): Primary all-cycling/rate data item declares CC0; the paired CSV/JSON all-data items share the same release population.

**Reuse and interpretation notes:**

- Text-mined values are not atomistic structures and relation extraction can misassign materials/conditions.
- Cycling and rate subsets, combined files and CSV/JSON formats should not be summed.
- Distinct from the DFT polyanion sodium cathode configuration dataset already cataloged.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="estm-simd"></a>
## ESTM experimentally synthesized thermoelectric materials

Manually compiled thermoelectric observations released with the SIMD materials representation study.

**Size:** 5,205 composition-temperature observations (source wording: 5,205).

**Scope:** Published ESTM cohort, verified as 5,205 rows × 8 columns in dataset/estm.xlsx

**Release:** 2022 paper release, checked 2026-11-01. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** measurement temperature (K); Seebeck coefficient (μV/K); electrical conductivity (S/m); thermal conductivity (W/m/K); power factor (W/m/K²); dimensionless ZT; source DOI.

**Access:** open. **Dataset license:** Not verified; no dataset-specific or repository license verified.

**Official routes:** [publication](https://doi.org/10.1038/s41524-022-00897-2) · [repository](https://github.com/KRICT-DATA/SIMD) · [download](https://github.com/KRICT-DATA/SIMD/blob/main/dataset/estm.xlsx)

Other denominators (not added to the ranking):

- 880 unique thermoelectric materials: Paper-reported compositions represented by the observations

**Evidence:**

- [A public database of thermoelectric materials and system-identified material representation for data-driven discovery](https://www.nature.com/articles/s41524-022-00897-2) (checked 2026-11-01): Paper reports 5,205 observations for 880 materials, identified by composition and measuring temperature.
- [SIMD primary repository](https://github.com/KRICT-DATA/SIMD) (checked 2026-11-01): README distinguishes full ESTM from a separately distributed Starrydata subset. Downloaded ESTM worksheet has 5,205 rows and explicit units in all property column names.

**Reuse and interpretation notes:**

- ESTM is distinct from the repository's separately included Starrydata slice; do not catalog that slice as another independent source.
- 880 material count is provider-reported; 5,205 is the observation count.
- Power factor and ZT can be derived from measured quantities; preserve this distinction.
- No periodic atomic structures are provided in the released worksheet.

**Tags:** thermoelectric, experimental, temperature-dependent, property-focused, OpenAlex-survey-20261101.

<a id="aunp-textmined-synthesis"></a>
## Text-mined gold nanoparticle synthesis and morphology

5,154 article records containing 7,608 synthesis and 12,519 characterization paragraphs, with codified recipes and morphological entities.

**Size:** 5,154 publication-level synthesis records (source wording: 5,154).

**Scope:** 5,154 article records containing 7,608 synthesis and 12,519 characterization paragraphs, with codified recipes and morphological entities.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2022.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** precursor/reagent quantities; operations and conditions; particle size; particle morphology; seed-mediated growth flag; source DOI.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01321-6) · [data](https://doi.org/10.6084/m9.figshare.16614262.v3) · [repository](https://github.com/CederGroupHub/text-mined-aunp-synthesis_public)

**Evidence:**

- [Text-mined dataset of gold nanoparticle synthesis procedures, morphologies, and size entities](https://www.nature.com/articles/s41597-022-01321-6) (checked 2026-11-01): Data Records defines each top-level JSON record as one publication with nested paragraphs; some have recipe, morphology, both or neither.
- [AuNP synthesis v3 deposit](https://api.figshare.com/v2/articles/16614262/versions/3) (checked 2026-11-01): CC BY 4.0; article-level JSON release available.

**Reuse and interpretation notes:**

- Do not present 5,154 as unique nanoparticles, full recipes or crystalline structures.
- Morphology and diameter depend on method/context; article/paragraph counts are separate units.
- Nanoparticle synthesis is adjacent to bulk crystal data; no atomistic coordinate archive.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="nuclear-charpy-impact"></a>
## Nuclear structural material Charpy impact tests

4,961 Charpy records from 109 publications with 55-column composition, treatment, irradiation, specimen and test metadata.

**Size:** 4,961 Charpy impact test records (source wording: 4,961).

**Scope:** 4,961 Charpy records from 109 publications with 55-column composition, treatment, irradiation, specimen and test metadata.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Charpy impact energy; specimen dimensions; test temperature; irradiation conditions; composition and processing.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-04823-1) · [data](https://doi.org/10.24435/materialscloud:p6-5y) · [repository](https://github.com/avakanski/Charpy-Impact-Test-Dataset)

**Evidence:**

- [Comprehensive Toughness Dataset of Nuclear Reactor Structural Materials using Charpy V-Notch Impact Testing](https://www.nature.com/articles/s41597-025-04823-1) (checked 2026-11-01): Paper states 4,961 records; each spreadsheet row is an individual Charpy test with specimen dimensions and conditions.
- [Materials Cloud Charpy archive](https://archive.materialscloud.org/records/q4x6v-dyt25) (checked 2026-11-01): Open spreadsheet archive declares CC BY 4.0.

**Reuse and interpretation notes:**

- Specimen-size effects prevent treating subsize and standard-size energy as one interchangeable target.
- Records are tests, not independent compositions/crystals.
- No atomic coordinate data and possible source overlap with nuclear tensile/creep datasets.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="shon-ionic-conductivity-2023"></a>
## Shon–Min text-mined ionic conductivity database

ChemDataExtractor-derived ionic-conductivity records with chemical names, provenance and selected solid-electrolyte family labels.

**Size:** 4,924 text-extracted conductivity records (source wording: 4,924 extracted records from 1,457 papers).

**Scope:** Published extraction output; not a count of distinct materials or fully validated experimental measurements.

**Release:** 2023 publication JSON/XLSX release. **Year:** 2023.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** ionic conductivity; chemical formula/name; source DOI; selected structural-family labels.

**Access:** open. **Dataset license:** Not verified for repository data; publication and supplementary material carry CC BY-NC-ND 4.0.

**Official routes:** [homepage](https://github.com/shonyeajin/Ionical_conductivity_database) · [data](https://github.com/shonyeajin/Ionical_conductivity_database/blob/main/database/IonicalConductivityDatabase.json) · [paper](https://doi.org/10.1021/acsomega.3c01424)

**Evidence:**

- [Shon and Min 2023 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10210167/) (checked 2026-11-01): Reports 4,924 ionic-conductivity records extracted from 1,457 of 3,258 papers; describes eight electrolyte structural-type annotations and extraction validation limits.
- [Author data release](https://github.com/shonyeajin/Ionical_conductivity_database) (checked 2026-11-01): README links IonicalConductivityDatabase.json and reconstructed battery data; GitHub API confirms a 7,063,926-byte JSON file.

**Reuse and interpretation notes:**

- An extraction dataset derived from the existing battery-database corpus, not an independent set of newly measured materials.
- Temperature attribution and numerical extraction errors require original-paper checks; evaluation extracted 10 of 38 reference materials.
- Eight structural families are labels, not atomic coordinates; the complete extracted set is not proved all crystalline or solid.
- A public repository does not establish an unrestricted data licence.

**Tags:** solid-electrolytes, text-mining, ChemDataExtractor, overlap:cde-battery-2020, property-focused, OpenAlex-survey-20261101.

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

Curated solid-electrolyte compositions and transport measurements linked to a separate computational collection. Original DDSE paper: A dynamic database of solid-state electrolyte (DDSE) picturing all-solid-state batteries.

**Size:** 3,816 experimental electrolyte materials (source wording: 3,816 experimental solid-state electrolytes).

**Scope:** June-2026 experimental subset across inorganic, solid-polymer and gel-polymer modules

**Release:** June 2026 experimental subset. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `mixed`.

**Labels/content:** ionic conductivity; activation energy; temperature; processing metadata.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.digbat.org) · [data](https://www.digbat.org) · [paper](https://doi.org/10.1016/j.nanoms.2026.07.001) · [original_paper](https://doi.org/10.1016/j.nanoms.2023.08.002) · [original_data](https://doi.org/10.50974/00137195) · [ddse2_paper](https://doi.org/10.32604/cmc.2024.060288)

Other denominators (not added to the ranking):

- 678 experimental electrolyte materials: Original DDSE paper, online 2023 / journal issue 2024; historical snapshot, not additive to DigBat
- 2,349 experimental electrolyte materials: DDSE 2.0 snapshot 2024-11-23; historical subset
- 18,309 experimental performance records: DDSE 2.0 snapshot 2024-11-23; repeated temperatures/properties per material
- 601 computational materials: DDSE 2.0 snapshot 2024-11-23; separate computational module
- 802 computational performance records: DDSE 2.0 snapshot 2024-11-23
- 27,645 conductivity data entries: DigBat June 2026 provider snapshot; distinct from 3,816 experimental materials
- 852 computational materials: DigBat June 2026 provider snapshot; separate from experimental-material ranking count

**Evidence:**

- [Tohoku University DigBat provider announcement](https://www.tohoku.ac.jp/en/press/digbat_an_ai_ready_digital_platform_for_solid_state_battery_research.html) (checked 2026-11-01): June-2026 statistics distinguish 3816 experimental materials, 27645 conductivity entries and 852 computational materials.
- [DigBat author paper](https://www.sciencedirect.com/science/article/pii/S2589965126001236) (checked 2026-11-01): Describes DDSE extension to inorganic/polymer electrolytes and integrated transport simulations.
- [Original DDSE paper (online 2023; volume 6 issue 2, 2024)](https://doi.org/10.1016/j.nanoms.2023.08.002) (checked 2026-11-01): The original database reports 678 electrolyte materials from 291 literature sources, distinct from later DDSE/DigBat snapshots.
- [DDSE 2.0 primary technical report](https://www.techscience.com/cmc/v81n3/59074/html) (checked 2026-11-01): 2024-11-23 snapshot: 2,349 experimental materials with 18,309 performance records and 601 computational materials with 802 performance records. The computational module supports VASP structure download.

**Reuse and interpretation notes:**

- Experimental material count excludes the separate 852 computational entries.
- Polymer/gel modules are adjacent to crystalline materials; filter for inorganic SSEs when required.
- Portal connection failed in this audit; release data verified through provider announcement and author paper.
- Open web access does not establish a bulk-redistribution licence.
- DDSE 2023, DDSE 2.0 (November 2024) and DigBat (June 2026) are overlapping historical snapshots of one evolving platform; their counts must not be added.

**Tags:** solid-electrolytes, ionic-transport, DDSE, mixed-material-classes, property-focused, OpenAlex-survey-20261101.

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

<a id="iupac-solid-liquid-reference-2023"></a>
## IUPAC solid–liquid equilibrium reference observations

Literature-compiled reference solubility/liquidus observations for ten binary solid–liquid equilibrium systems, with source identifiers and accepted/rejected flags.

**Size:** 3,446 released SLE observations (source wording: 3,446).

**Scope:** Numeric source-tagged rows in ten *_SLE*.xlsx tables only; includes 21 explicitly rejected R rows, which must remain distinguishable from 3,425 accepted rows. Other property workbooks not added.

**Release:** NIST mds2-2807 data release issued 2023-03-17; files checked 2026-11-01. **Year:** 2023.

**Provenance:** experimental; critically compiled literature. **Structure availability:** `composition_only`.

**Labels/content:** solute/solvent identity and InChI; liquid mole fraction; absolute temperature K (ITS-90); pressure kPa where tabulated; source reference; accepted/rejected status.

**Access:** open. **Dataset license:** Catalog declares NIST data-use terms; separate redistribution rights of compiled third-party measurements not verified.

**Official routes:** [paper](https://doi.org/10.1515/pac-2021-1002) · [data](https://data.nist.gov/od/ds/mds2-2807/DataFiles.zip) · [readme](https://data.nist.gov/od/ds/mds2-2807/Readme.txt) · [catalog](https://catalog.data.gov/dataset/literature-experimental-data-for-reference-materials-for-phase-equilibrium-studies-2-solid-aae7b)

Other denominators (not added to the ranking):

- 10 binary SLE systems: Ten separately named SLE workbooks
- 3,425 accepted SLE observations: Blank status flag according to workbook definitions
- 21 rejected observations: Explicit R status; excluded from accepted observations

**Count derivation:** Header-mapped count of numeric source-tagged x1/T data rows in ten SLE tables; 145 + 302 + 1,110 + 1,086 + 157 + 16 + 79 + 132 + 106 + 313 = 3,446.

**Evidence:**

- [Data.gov agency release metadata](https://catalog.data.gov/dataset/literature-experimental-data-for-reference-materials-for-phase-equilibrium-studies-2-solid-aae7b) (checked 2026-11-01): Attached ranks 88/91. Identifies NIST ark:/88434/mds2-2807, publication DOI, ZIP/README routes and a NIST license-policy link.
- [IUPAC data README](https://data.nist.gov/od/ds/mds2-2807/Readme.txt) (checked 2026-11-01): Maps twenty workbooks to the technical-report figures and distinguishes solid-liquid, vapor-liquid, liquid-liquid, excess enthalpy and activity-coefficient data.
- [Inspected IUPAC reference archive](https://data.nist.gov/od/ds/mds2-2807/DataFiles.zip) (checked 2026-11-01): Independently counted 3,446 source-tagged observations in ten SLE tables: 3,425 accepted and 21 R-rejected; headers define mole fraction, temperature scale, source codes and pressure context.

**Reuse and interpretation notes:**

- A specialized solid/solution thermodynamic reference set, not a crystal-coordinate database.
- Do not train on R-rejected observations as accepted targets; preserve those curation flags.
- Ten binary systems and twenty workbooks are not 3,446 independent materials. Repeated digitized/literature observations may share experiments.
- Pressure and mole fraction occupy different columns in two workbooks; parse by explicit header instead of fixed column offsets.
- Uncertainty completeness and underlying source-paper rights were not independently established for every measurement.

**Tags:** Data.gov-selection-20261101, solid-liquid equilibrium, solubility, quality flags, reference materials.

<a id="refractiveindex-info"></a>
## Refractiveindex.info optical constants

Condition-resolved optical-constant data from publications and materials datasheets in YAML format.

**Size:** 3,328 published optical data records (source wording: 3,328).

**Scope:** December 2023 descriptor snapshot: 3,135 linear-optical records for 605 materials plus 193 nonlinear-optical records for 89 materials; material populations may overlap.

**Release:** December 2023 descriptor snapshot; live repository separately maintained. **Year:** 2024.

**Provenance:** mixed. **Structure availability:** `mixed`.

**Labels/content:** refractive index n; extinction coefficient k; nonlinear refractive index n2; wavelength-dependent dispersion.

**Access:** open. **Dataset license:** CC0 1.0.

**Official routes:** [homepage](https://refractiveindex.info/) · [paper](https://doi.org/10.1038/s41597-023-02898-2) · [repository](https://github.com/polyanskiy/refractiveindex.info-database) · [download](https://doi.org/10.6084/m9.figshare.c.6868000.v1)

**Count derivation:** December 2023 linear + nonlinear optical data records, not disjoint material counts; 3,135 + 193 = 3,328.

**Evidence:**

- [Polyanskiy, Scientific Data 11, 94](https://www.nature.com/articles/s41597-023-02898-2) (checked 2026-11-01): December 2023 snapshot distinguishes linear and nonlinear data records and material counts; YAML records carry publication and conditions.
- [Optical constants database repository](https://github.com/polyanskiy/refractiveindex.info-database) (checked 2026-11-01): Maintainer declares database CC0 1.0; YAML data include original references and material details.

**Reuse and interpretation notes:**

- Broad materials scope includes crystals, amorphous solids, liquids and gases; a crystal-only denominator is unverified.
- No general atomic structure archive; mixed here indicates phase/specimen-resolved optical records across physical states.
- Snapshot count does not claim the live repository size as of 2026.
- Experimental and theoretical optical constants may coexist; inspect each original reference and preserve wavelength, temperature and orientation.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="psc-fabrication-textmine-2025"></a>
## Text-mined perovskite solar-device fabrication attributes

Article-level extraction of perovskite-device layer materials, architecture and fabrication details.

**Size:** 3,164 article-linked fabrication records (source wording: 3,164).

**Scope:** Figshare v2 JSON RECORDS list contains 3,164 entries with 3,164 unique source DOIs and 30 fields. Paper Phase I subset contains 1,505 records; the final population includes Phase II expansion.

**Release:** Figshare 25868737 v2; 3,164-record JSON recount. **Year:** 2025.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** perovskite composition and ion fractions; substrate/transport-layer/contact materials; cell architecture/flexibility; layer deposition method; spin-coating rate and duration; annealing conditions; top-contact thickness.

**Access:** open. **Dataset license:** CC0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-04566-z) · [data](https://doi.org/10.6084/m9.figshare.25868737.v2) · [repository](https://github.com/vvatpvv/psc-database)

**Evidence:**

- [Auto-generating a database on the fabrication details of perovskite solar devices](https://www.nature.com/articles/s41597-025-04566-z) (checked 2026-11-01): Data Records identifies 30 attributes; after filtering, 1,505 Phase I records and 3,164 combined final records were retained.
- [device_attributes_combined.json v2](https://api.figshare.com/v2/articles/25868737) (checked 2026-11-01): Data deposit declares CC0; downloaded JSON independently contains 3,164 records and unique DOIs.

**Reuse and interpretation notes:**

- One record is linked to a paper and is not a count of every separately fabricated/tested device in that paper.
- Phase I intentionally reuses source papers represented in the existing Perovskite Database Project; Phase II adds an independent source-paper expansion. Counts are not disjoint.
- Current extraction can return one HTL and one ETL; double-layer transport materials may be incompletely represented.
- Composition/layer labels and deposition parameters do not provide periodic atomic coordinates or guarantee a unique phase.
- This fabrication corpus is distinct from the CDE photovoltaic-performance corpus; source overlap remains possible.

**Tags:** Scientific-Data, device-or-engineered-material-scope, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="cu-cr-x-figure-extraction"></a>
## Cu-Cr-X mechanical and electrical property dataset

Automated figure extraction linked to manually curated composition, processing and literature metadata for Cu-Cr-X alloys.

**Size:** 3,018 alloy composition-processing-property records (source wording: 3,018).

**Scope:** Paper cohort extracted from 251 figures in 146 papers

**Release:** 2025 paper release, checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** hardness (source-specific units); yield / tensile strength (MPa); electrical conductivity (%IACS); thermal / thermomechanical processing metadata.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare v2).

**Official routes:** [publication](https://doi.org/10.1038/s41597-025-06295-9) · [download](https://doi.org/10.6084/m9.figshare.29369987.v2) · [repository](https://github.com/PPW6/Auto_fig_extractor)

**Evidence:**

- [Mechanical and Electrical Properties dataset of Cu-Cr-X alloys generated with automated figure data extraction](https://www.nature.com/articles/s41597-025-06295-9) (checked 2026-11-01): Paper reports 3,018 records from 251 figures across 146 papers; Figshare JSON/XLSX release and source DOI are documented.
- [Cu-Cr-X Figshare v2 metadata](https://api.figshare.com/v2/articles/29369987) (checked 2026-11-01): Public JSON archive and XLSX available; metadata declares CC BY 4.0 and version DOI 10.6084/m9.figshare.29369987.v2.

**Reuse and interpretation notes:**

- A figure-derived record is not an independent composition or unique crystal.
- Keep property-unit and treatment metadata per record; extraction and outlier labels remain useful quality evidence.
- Shares an application domain and potentially experiments with Gorsse 2023; distinct extraction/release does not imply disjoint data.
- Full spreadsheet units and per-property completeness were not independently audited.

**Tags:** mechanical, alloys, figure-extraction, processing-aware, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="mdf-experimental-band-gaps"></a>
## Foundry experimental band-gap structure cohort

Graph Network Based Deep Learning of Band Gaps - Experimental Band Gaps

**Size:** 2,808 experimental band-gap records (source wording: 2,808).

**Scope:** Foundry projects.foundry.n_items for foundry_experimental_band_gaps_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** foundry_experimental_band_gaps_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2021.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** band gap; measurement temperature; measurement method; band-gap type; declared crystal structure.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/foundry_experimental_band_gaps_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/foundry_experimental_band_gaps_v1.1/) · [release](https://doi.org/10.18126/wg3u-g8vu) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=foundry_experimental_band_gaps_v1.1) (checked 2026-11-01): Public subject response identifies foundry_experimental_band_gaps_v1.1, DOI 10.18126/wg3u-g8vu, n_items=2,808, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The JSON schema declares a structure field; atomic-coordinate completeness across the cohort was not audited.

**Tags:** MDF, Foundry, MDF-property-20261101.

<a id="polyverse-load-hardness"></a>
## polyVERSE load-dependent experimental Vickers hardness

Experimental indentation hardness with applied load, released separately from DFT-derived hardness proxy rows.

**Size:** 2,480 composition-load hardness observations (source wording: 2,480).

**Scope:** Published curated experimental subset; verified as 2,480 data rows in only_exp_data.csv

**Release:** 2026 paper release, checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Vickers hardness (GPa in paper abstract; verify stored-unit convention); indentation load (N); chemical composition.

**Access:** open. **Dataset license:** Custom Georgia Tech Research Corporation General Public Use License; commercial-gain sale requires separate agreement.

**Official routes:** [publication](https://doi.org/10.1007/s00339-026-09913-4) · [repository](https://github.com/Ramprasad-Group/polyVERSE/tree/main/Other/AM_hardness) · [download](https://github.com/Ramprasad-Group/polyVERSE/blob/main/Other/AM_hardness/only_exp_data.csv) · [license](https://github.com/Ramprasad-Group/polyVERSE/blob/main/LICENSE)

**Evidence:**

- [Load-dependent hardness prediction for materials using machine learning](https://link.springer.com/article/10.1007/s00339-026-09913-4) (checked 2026-11-01): Methods report 2,480 unique composition-load records, 69 elements and 514 chemical systems; applied loads span below 2 to above 50 N.
- [polyVERSE primary experimental data CSV](https://raw.githubusercontent.com/Ramprasad-Group/polyVERSE/main/Other/AM_hardness/only_exp_data.csv) (checked 2026-11-01): Downloaded CSV contains 2,480 data rows with composition, load, hardness, category and type fields.
- [polyVERSE GTRC license](https://raw.githubusercontent.com/Ramprasad-Group/polyVERSE/main/LICENSE) (checked 2026-11-01): License explicitly includes code, data and documentation; grants redistribution/modification under conditions and requires a separate agreement for commercial-gain sales.

**Reuse and interpretation notes:**

- Repository also provides computed proxy hardness; retain experimental category and do not combine them as measured values.
- The article abstract reports GPa but its conclusion reports MPa; CSV column lacks unit metadata. Stored hardness-unit convention needs checking before quantitative harmonization.
- Processing/microstructure metadata are largely absent.
- Dataset can contain noncrystalline alloy compositions; a crystalline-only subset has not been isolated.
- Custom license is not an OSI/Creative-Commons open-data license.

**Tags:** hardness, experimental, load-dependent, license-restricted, property-focused, OpenAlex-survey-20261101.

<a id="fatiguedata-am2022"></a>
## FatigueData-AM2022 additively manufactured alloys

Fatigue curves linked to alloy identity, additive-manufacturing parameters, processing and testing conditions.

**Size:** 2,460 fatigue test-condition datasets (source wording: 2,460).

**Scope:** 1,610 S–N +236 ε–N +614 crack-growth datasets

**Release:** 2023 paper cohort; deposit checked 2026-11-01. **Year:** 2023.

**Provenance:** literature_extracted. **Structure availability:** `composition_only`.

**Labels/content:** stress-life curves (MPa, cycles); strain-life curves; fatigue crack-growth data; AM and post-processing parameters; static mechanical properties.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare v2).

**Official routes:** [publication](https://doi.org/10.1038/s41597-023-02150-x) · [data](https://doi.org/10.6084/m9.figshare.22337629.v2)

Other denominators (not added to the ranking):

- 116 AM alloy types: Paper-reported composition/type coverage

**Count derivation:** Sum of three disjoint fatigue-curve families reported in descriptor; 1,610 + 236 + 614 = 2,460.

**Evidence:**

- [FatigueData-AM2022 additively manufactured alloys — Scientific Data descriptor](https://doi.org/10.1038/s41597-023-02150-x) (checked 2026-11-01): Paper reports 116 alloy types and 1,610+236+614 curve datasets. MAT/JSON/XLSX deposit is separate from FatigueData-CMA2022.
- [FatigueData-AM2022 additively manufactured alloys — primary deposit](https://doi.org/10.6084/m9.figshare.22337629.v2) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Distinct AM-focused release, but source papers/curves can overlap other fatigue compilations; no cross-release deduplication.
- Curve datasets, data points and alloy identities are different units.
- EXCEL curves are sampled where necessary; raw JSON/MAT can preserve richer point sets.
- Preserve AM process, treatment, surface, temperature, stress ratio and run-out flags.

**Tags:** Scientific Data, processing, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="nist-srd81-insulation"></a>
## NIST Heat Transmission Properties of Insulating and Building Materials (SRD 81)

Historical guarded-hot-plate measurements of building and insulating materials with specimen, apparatus and conditioning metadata; public JSON API.

**Size:** 2,175 measurement records (source wording: 2,175).

**Scope:** Complete response from documented TableAllData endpoint retrieved 2026-11-01; one distinct database id per object

**Release:** Web version 2.0 (December 2015); data content last updated 1983. **Year:** 2015.

**Provenance:** experimental literature compilation. **Structure availability:** `composition_only`.

**Labels/content:** thermal conductivity; thermal conductance; thermal resistance; thermal resistivity; density; test conditions.

**Access:** open. **Dataset license:** Database states copyright U.S. Department of Commerce, all rights reserved; no open data redistribution license verified; data redistribution rights not verified.

**Official routes:** [homepage](https://srdata.nist.gov/insulation/) · [download](https://srdata.nist.gov/insulation/api/TableAllData) · [documentation](https://srdata.nist.gov/insulation/Home/DataFieldDef) · [doi](https://doi.org/10.18434/T4RC7M)

**Evidence:**

- [SRD 81 live public JSON API](https://srdata.nist.gov/insulation/api/TableAllData) (checked 2026-11-01): Downloaded 2,175 objects with 2,175 distinct id values. Fields include material/manufacturer, specimen, density, thickness, mean temperature, temperature difference, conductivity, uncertainty, apparatus, method and conditioning; 1,667 rows have null unc.
- [SRD 81 scope and measurement method](https://srdata.nist.gov/insulation/Home/Intro) (checked 2026-11-01): Describes historical 200-mm guarded-hot-plate measurements, over 2,000 observations, most near 24 °C, with broad specimen-density coverage.
- [SRD 81 definitions and uncertainty](https://srdata.nist.gov/insulation/Home/DataFieldDef) (checked 2026-11-01): Defines SI/IP property units, specimen and pre-test conditions, apparatus and test mode; describes relative expanded uncertainty conventions. API numeric fields do not embed units.
- [SRD 81 release history](https://srdata.nist.gov/insulation/Home/VersionHistory) (checked 2026-11-01): Web version 2.0 released December 2015, superseding version 1.0 released January 2000.
- [SRD 81 landing page and rights](https://srdata.nist.gov/insulation/) (checked 2026-11-01): Current public page identifies data content last updated 1983 and copyright U.S. Department of Commerce with all rights reserved.

**Reuse and interpretation notes:**

- 2,175 counts measurement rows, not distinct materials or specimens; API snapshot was checked 2026-11-01.
- API fields do not encode units. Values appear to use inch-pound conventions; confirm each unit/conversion against the UI before quantitative reuse, and do not label API values SI by default.
- 1,667 of 2,175 API rows have null uncertainty. Provider default uncertainty guidance does not supply measured row-specific uncertainty.
- Apparent thermal transmission properties can combine conduction, radiation and convection; they are not intrinsic lattice thermal conductivity.
- Historical data content ends in 1983; current site accessibility and the 2015 software release are separate from measurement freshness.
- Public access does not establish an open redistribution license.

**Tags:** Data.gov attachment ranks 27, 28, guarded hot plate, measurement conditions, public JSON API, Data.gov-selection-20261101.

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

<a id="alloydata-lowtemp"></a>
## AlloyData-2024LT low-temperature alloy mechanics

Figshare v9 JSON independently contains 239 articles and 1,913 test-condition records.

**Size:** 1,913 experimental test-condition records (source wording: 1,913).

**Scope:** Figshare v9 JSON independently contains 239 articles and 1,913 test-condition records. Tables describe low-temperature alloy properties and detailed processing/testing metadata.

**Release:** Figshare 25912267 v9; independently counted JSON. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** yield strength (MPa); ultimate tensile strength (MPa); elongation (%); Charpy impact energy; temperature (K); alloy composition and treatment.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-05512-9) · [data](https://doi.org/10.6084/m9.figshare.25912267.v9) · [repository](https://github.com/xuzpgroup/HaoxuanTang/tree/main/LowTData)

**Evidence:**

- [Mechanical performance dataset for alloy with applications at low temperatures](https://www.nature.com/articles/s41597-025-05512-9) (checked 2026-11-01): Data Records defines one scientific record per experimental test condition and a hierarchical JSON schema with default unit system and missing values.
- [AlloyData deposit metadata](https://api.figshare.com/v2/articles/25912267) (checked 2026-11-01): CC BY 4.0; downloaded AlloyData-2024LT.json has 239 articles and 1,913 entries under article.scidata.datasets.

**Reuse and interpretation notes:**

- Low-temperature series can include room-temperature reference measurements; retain individual temperatures.
- Mechanical targets are sparse, and alloy counts differ from test records.
- May share experiments with other literature alloy compilations; no cross-release deduplication.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="cu-alloys-mechanical-2023"></a>
## Copper-alloy mechanical properties and electrical conductivity (Gorsse 2023)

Literature-derived Cu-alloy treatment conditions and mechanical/electrical measurements for precipitation-strengthened alloy design.

**Size:** 1,831 composition-processing-property-reference records (source wording: 1,831).

**Scope:** Published 2023 Cu-alloy CSV release; approximately 150 alloy compositions

**Release:** 2023 paper release, checked 2026-11-01. **Year:** 2023.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Vickers hardness (HV); yield strength (MPa); ultimate tensile strength (MPa); electrical conductivity (%IACS); solution / ageing temperature (K); treatment time (h); cold reduction (%).

**Access:** open. **Dataset license:** CC0 1.0 (Figshare dataset).

**Official routes:** [publication](https://doi.org/10.1038/s41597-023-02411-9) · [download](https://doi.org/10.6084/m9.figshare.23735373.v1) · [collection](https://doi.org/10.6084/m9.figshare.c.6475600.v1)

**Evidence:**

- [Dataset of mechanical properties and electrical conductivity of copper-based alloys](https://www.nature.com/articles/s41597-023-02411-9) (checked 2026-11-01): Data Records specify 1,831 records; conditions, target units and source DOI fields are documented. Approximately 150 compositions are represented.
- [Figshare primary dataset metadata](https://api.figshare.com/v2/articles/23735373) (checked 2026-11-01): Public CSV Cu_alloys_database_2023_06_06.csv; metadata declares CC0 and DOI 10.6084/m9.figshare.23735373.v1.

**Reuse and interpretation notes:**

- Observation count is not distinct-alloy count.
- Microstructure is often insufficiently reported; thermal and thermomechanical processing are retained instead.
- Mechanical properties are sparse: paper reports 1,614 hardness, 163 yield-strength, 276 ultimate-strength and 1,826 conductivity records.
- May share source experiments with the separate Cu-Cr-X release; no cross-release deduplication performed.
- Composition/property tables do not contain full atomic structures.

**Tags:** mechanical, hardness, electrical-conductivity, alloys, processing-aware, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="nuclear-creep-properties"></a>
## Nuclear structural material creep tests

1,583 creep specimens/records from 54 peer-reviewed sources plus additional NDMAS data as described by the paper.

**Size:** 1,583 creep test/specimen records (source wording: 1,583).

**Scope:** 1,583 creep specimens/records from 54 peer-reviewed sources plus additional NDMAS data as described by the paper.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** creep rupture life; creep strain/rate; stress and temperature; specimen geometry; irradiation conditions; alloy composition and treatment.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-07563-y) · [data](https://doi.org/10.24435/materialscloud:99-xr) · [repository](https://github.com/avakanski/Dataset-of-Creep-Properties-for-Nuclear-Structural-Materials)

**Evidence:**

- [Compilation of Creep Property Data for Nuclear Structural Materials](https://www.nature.com/articles/s41597-026-07563-y) (checked 2026-11-01): Data Records defines one creep test per row and 70 columns; paper reports 1,583 specimens and source identifiers.
- [Materials Cloud nuclear creep archive](https://archive.materialscloud.org/records/s60kq-qg914) (checked 2026-11-01): Open Excel and CSV table release declares CC BY 4.0.

**Reuse and interpretation notes:**

- Tests include different alloys, specimen sizes, stresses and irradiation histories; preserve these conditions.
- Creep test count does not imply a unique compound or phase count.
- No periodic atomic coordinate coverage.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="lpbf-relative-density"></a>
## L-PBF commercial alloy relative-density dataset

1,579 observations with ten input columns and relative-density percentage, covering printing/material, atmosphere, powder and geometry context.

**Size:** 1,579 literature processing-condition observations (source wording: 1,579).

**Scope:** 1,579 observations with ten input columns and relative-density percentage, covering printing/material, atmosphere, powder and geometry context.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** relative density (%); laser power/speed; hatch/layer parameters; shielding gas; powder size; part geometry.

**Access:** open. **Dataset license:** Not verified for dataset; article license is not assigned to repository data.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-04576-x) · [data](https://doi.org/10.7910/DVN/VPBQK8) · [repository](https://github.com/GermanOmar/data_LPBF)

**Evidence:**

- [Laser powder bed fusion dataset for relative density prediction of commercial metallic alloys](https://www.nature.com/articles/s41597-025-04576-x) (checked 2026-11-01): Data Records says rows are observations, first ten columns input variables and eleventh relative density in percent.
- [L-PBF release statement](https://www.nature.com/articles/s41597-025-04576-x) (checked 2026-11-01): Data Records gives 1,579 observations and identifies the Harvard Dataverse Excel deposit; repository license endpoint returned no license.

**Reuse and interpretation notes:**

- Dataset-specific license not verified; public article/repository does not establish reuse rights.
- Printing samples are not unique alloys or atomic structures.
- Protective atmosphere, powder size, geometry and processing must accompany density comparisons.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mpea-borg-expanded"></a>
## Borg expanded MPEA mechanical properties and phases

Static Figshare v9 CSV contains 1,545 records; paper reports 630 alloys from 265 publications.

**Size:** 1,545 composition–condition–reference records (source wording: 1,545).

**Scope:** Static Figshare v9 CSV contains 1,545 records; paper reports 630 alloys from 265 publications. Rows preserve processing, temperature, test mode and phases.

**Release:** Figshare 12642953 v9, static 1,545-row release. **Year:** 2020.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** yield strength (MPa); ultimate tensile/compression strength (MPa); elongation (%); Vickers hardness; Young modulus (GPa); density (g/cm³); phase labels; grain size (µm).

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-020-00768-9) · [data](https://doi.org/10.6084/m9.figshare.12642953.v9) · [repository](https://github.com/CitrineInformatics/MPEA_dataset)

**Evidence:**

- [Expanded dataset of mechanical properties and observed phases of multi-principal element alloys](https://www.nature.com/articles/s41597-020-00768-9) (checked 2026-11-01): Data Records defines records by unique composition, property, temperature and reference combination; composition and processing metadata accompany sparse mechanical measurements.
- [MPEA deposit metadata](https://api.figshare.com/v2/articles/12642953) (checked 2026-11-01): CC BY 4.0; MPEA_dataset.csv independently parsed as 1,545 data rows.

**Reuse and interpretation notes:**

- Includes rule-of-mixtures density and modulus estimates alongside experimental fields; distinguish their origin.
- Alloy phases and microstructure descriptors are not atomic coordinates.
- Contains earlier MPEA review data plus updates; later alloy/fatigue compilations can share source experiments.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

**Tags:** Scientific-Data, quasicrystals, approximants, Starrydata-linked, Scientific-Data-descriptor.

<a id="itr-interface-descriptors"></a>
## Experimental interfacial thermal resistance and descriptors

1,318 ITR observations for 457 interface samples involving 54 materials, with a separate 298-material descriptor table.

**Size:** 1,318 interface–temperature observations (source wording: 1,318).

**Scope:** 1,318 ITR observations for 457 interface samples involving 54 materials, with a separate 298-material descriptor table.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2020.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** interfacial thermal resistance; measurement temperature; interface chemistry/interlayers; synthesis and pretreatment; measurement method; physical/chemical descriptors.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-020-0373-2) · [data](https://doi.org/10.5281/zenodo.3564173)

**Evidence:**

- [Physical and chemical descriptors for predicting interfacial thermal resistance](https://www.nature.com/articles/s41597-020-0373-2) (checked 2026-11-01): Data Records states 1,318 observations, 457 samples and 54 materials; descriptors cover 298 materials, not 80,000 measured interfaces.
- [ITR descriptor and observation archive](https://zenodo.org/api/records/3564173) (checked 2026-11-01): CC BY 4.0; separate descriptor, ITR and training workbooks are listed.

**Reuse and interpretation notes:**

- Interfaces can involve amorphous materials, graphite/graphene and crystalline substrates; not a pure bulk-crystal dataset.
- The >80,000 constructible descriptor pairs are predictions/input combinations, not measured ITR labels.
- Do not count reused training-table rows as additional observations.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="experimental-formation-enthalpy-2017"></a>
## Calorimetric inorganic formation enthalpies

1,276 entries from over 50 years of high-temperature calorimetry, with phase/structure metadata and optional first-principles comparison fields.

**Size:** 1,276 experimental formation-enthalpy entries (source wording: 1,276).

**Scope:** 1,276 entries from over 50 years of high-temperature calorimetry, with phase/structure metadata and optional first-principles comparison fields.

**Release:** 2017 article and cited data release, checked 2026-11-01. **Year:** 2017.

**Provenance:** experimental. **Structure availability:** `structure_linked`.

**Labels/content:** standard formation enthalpy; chemical composition; phase/structure identifiers; calorimetric method; DFT comparison when available.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/sdata.2017.162) · [data](https://doi.org/10.6084/m9.figshare.c.3822835)

**Evidence:**

- [Experimental formation enthalpies for intermetallic phases and other inorganic compounds](https://www.nature.com/articles/sdata2017162) (checked 2026-11-01): Paper reports 1,276 measured formation-enthalpy entries for intermetallics, borides, carbides and silicides, with structural information and calculated comparisons.
- [Calorimetric formation enthalpy dataset](https://api.figshare.com/v2/articles/5193229) (checked 2026-11-01): Figshare data item in collection 3822835 declares CC BY 4.0 and provides enthalpy_formation.json.

**Reuse and interpretation notes:**

- Experimental and DFT enthalpy fields have different provenance.
- Repeated measurements/phases can share composition; preserve uncertainty, reference state and method.
- Structural descriptors/identifiers do not establish full atomic-coordinate coverage.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="ekhi-radiative-2026"></a>
## EKHI optical and thermal radiative properties

Digitized experimental optical and radiative curves for solid specimens with original-publication provenance.

**Size:** 1,251 experimental property curves (source wording: 1,251).

**Scope:** 1,251 curves containing 18,999 numerical values for 171 solid materials from 167 primary sources; 16 subproperties within four main properties.

**Release:** 2026 published release. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** emittance; reflectance; transmittance; absorptance; temperature; spectral wavelength; specimen and geometry metadata.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://thermomat.ehu.eus/ekhi) · [paper](https://doi.org/10.1038/s41597-026-07083-9) · [download](https://doi.org/10.6084/m9.figshare.30581240)

**Evidence:**

- [Gabirondo-López et al., Scientific Data 13, 740](https://www.nature.com/articles/s41597-026-07083-9) (checked 2026-11-01): Data Records gives 1,251 curves, 18,999 values, 171 solids and 167 accessible original sources; data deposit is CC BY 4.0.

**Reuse and interpretation notes:**

- Scope includes metallic elements/alloys, nonmetallic solids and coatings; crystalline fraction unverified and no atomic coordinates.
- Curves have differing temperature, wavelength, measurement geometry and specimen conditions.
- Digitizes historical TPRC values; digitization validation does not guarantee original experimental accuracy.
- Curve count is not a material count and property coverage is uneven.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="nuclear-subsize-tensile"></a>
## Sub-sized nuclear structural material tensile tests

1,050 literature tensile-test records with 55 columns covering nuclear structural materials, specimen dimensions and irradiation/testing conditions.

**Size:** 1,050 tensile test records (source wording: 1,050).

**Scope:** 1,050 literature tensile-test records with 55 columns covering nuclear structural materials, specimen dimensions and irradiation/testing conditions.

**Release:** 2025 article and cited data release, checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** yield strength; ultimate tensile strength; elongation; specimen geometry; irradiation dose/temperature; composition and treatment.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-04329-2) · [data](https://doi.org/10.24435/materialscloud:ws-8j) · [code](https://github.com/avakanski/Subsized-Specimens-Tensile-Properties)

**Evidence:**

- [Dataset of tensile properties for sub-sized specimens of nuclear structural materials](https://www.nature.com/articles/s41597-024-04329-2) (checked 2026-11-01): Paper states 1,050 records and defines each spreadsheet row as a single tensile test with 55 columns.
- [Materials Cloud tensile archive](https://archive.materialscloud.org/records/vywsz-wxn79) (checked 2026-11-01): Version v3 record supplies spreadsheet data and declares CC BY 4.0.

**Reuse and interpretation notes:**

- Specimen-size effects and irradiation/treatment conditions must accompany tensile values.
- Full atomic structures absent; test specimens and phase descriptions are not atomistic representations.
- Distinct from the Charpy and creep property tables despite shared material families.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="liverpool-ionics"></a>
## Liverpool Ionics Dataset

Expert-validated AC impedance lithium-ion conductivity measurements with composition, temperature and structural-family labels.

**Size:** 820 conductivity-at-temperature records (source wording: 820 measurements; 403 unique near-room-temperature compositions).

**Scope:** Original paper corpus from 214 sources, including 434 directly measured and 31 extrapolated room-temperature records.

**Release:** Original 820-entry publication; provider correction dated 2024-10-18. **Year:** 2023.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** ionic conductivity; measurement temperature; composition; structural family; chemical family.

**Access:** open. **Dataset license:** Free academic/research use with attribution; commercial extraction or reutilisation requires University of Liverpool licence (provider terms).

**Official routes:** [homepage](https://pcwww.liv.ac.uk/~msd30/lmds/LiIonDatabase.html) · [paper](https://doi.org/10.1038/s41524-022-00951-z)

Other denominators (not added to the ranking):

- 403 unique compositions: Near-room-temperature subset of original paper, not the full temperature-resolved table
- 465 near-room-temperature records: 434 direct plus 31 extrapolated, covering 403 unique compositions

**Evidence:**

- [Liverpool Ionics primary paper](https://www.nature.com/articles/s41524-022-00951-z?error=cookies_not_supported) (checked 2026-11-01): Reports 820 entries from 214 sources, 434 measured plus 31 extrapolated near-room-temperature records covering 403 unique compositions; published 16 January 2023.
- [University of Liverpool dataset and terms](https://pcwww.liv.ac.uk/~msd30/lmds/LiIonDatabase.html) (checked 2026-11-01): Provider page supplies table/CSV, commercial reuse conditions and an October 2024 correction for entry 703.

**Reuse and interpretation notes:**

- Structural labels are not atomic-coordinate crystal structures.
- Room-temperature definition is 15–35 degrees C; 31 room-temperature records are extrapolated.
- Mixture of total and bulk conductivities reflects reporting differences.
- The 372-row Foundry export is a separate derivative snapshot and does not replace the full 820-entry count.
- Provider endpoint failed local certificate verification; count verified from publisher and terms from indexed provider content.

**Tags:** solid-electrolytes, ionic-conductivity, curated, noncommercial-terms, property-focused, OpenAlex-survey-20261101.

<a id="ml-hydpark"></a>
## ML-HydPARK metal-hydride storage properties

Curated HydPARK-derived metal-hydride compositions, hydrogen capacities and thermodynamic descriptors.

**Size:** 772 composition/property records (source wording: 772).

**Scope:** ML-HYDPARK_v0.0.5.csv contains 772 data rows; not independently deduplicated crystal structures

**Release:** Zenodo version 0.0.5 (2024-02-19). **Year:** 2024.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** hydrogen storage capacity; hydride formation enthalpy; entropy; temperature; equilibrium pressure; hydrogen-to-metal ratio.

**Access:** open. **Dataset license:** CC BY 4.0 (versioned data deposit).

**Official routes:** [homepage](https://zenodo.org/records/10680097) · [data](https://doi.org/10.5281/zenodo.10680097) · [paper](https://doi.org/10.1021/acs.jpclett.9b02971)

**Evidence:**

- [ML-HydPARK version 0.0.5 deposit](https://zenodo.org/api/records/10680097) (checked 2026-11-01): Deposit identifies a curated HydPARK-derived CSV, version 0.0.5 (2024-02-19), and CC BY 4.0.
- [Independent CSV row count](https://zenodo.org/api/records/10680097/files/ML-HYDPARK_v0.0.5.csv/content) (checked 2026-11-01): Parsed the complete 100,494-byte CSV: 772 data rows after the header. The receipt records its SHA-256 and column names.

**Reuse and interpretation notes:**

- A composition table; crystal coordinates are not included.
- Experimental source measurements and derived equilibrium-pressure descriptors coexist; label coverage is incomplete.
- HydPARK parent data and newer hydrogen databases may overlap. The concept-record URL 7293044 resolved to this version; counts are pinned to v0.0.5.

**Tags:** property-focused, OpenAlex-survey-20261101.

<a id="metal-combustion-properties"></a>
## Metallic-material combustion property database

Literature-curated combustion and ignition data for pure metals and alloys with composition, specimen and atmosphere metadata.

**Size:** 725 combustion measurement records (source wording: 725).

**Scope:** Literature descriptor reports 725 composition/property/experimental-condition/reference records across six worksheets; not 725 distinct alloys

**Release:** Figshare v3 / 2026 descriptor. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** combustion enthalpy; ignition temperature; ignition delay; combustion rate; threshold pressure; oxygen pressure.

**Access:** open. **Dataset license:** CC BY 4.0 (versioned data deposit).

**Official routes:** [homepage](https://github.com/wpl2000/CombustionData) · [data](https://doi.org/10.6084/m9.figshare.29966602.v3) · [paper](https://doi.org/10.1038/s41597-026-06862-8)

**Evidence:**

- [Metal combustion Scientific Data descriptor](https://www.nature.com/articles/s41597-026-06862-8) (checked 2026-11-01): Reports 725 curated data points from 45 publications and defines a record by composition, property, test condition and reference.
- [Combustion data deposit metadata](https://api.figshare.com/v2/articles/29966602) (checked 2026-11-01): Version 3 contains Combustion_Data.xlsx and explicitly reports CC BY 4.0.

**Reuse and interpretation notes:**

- No atomic crystal coordinates are asserted; the materials are composition-level metal/alloy samples.
- Metric units and conditions differ; specimen geometry, test method and oxygen pressure must remain associated with each measurement.
- 725 is descriptor-reported; workbook rows were not independently recounted.

**Tags:** property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="obelix"></a>
## OBELiX experimental solid electrolyte conductivity

Expert-curated experimental room-temperature lithium ionic conductivity with crystallographic metadata and a partial CIF collection.

**Size:** 599 experimental electrolyte entries (source wording: 599 experimental entries; 321 with CIF files).

**Scope:** Provider README and publication benchmark; entries may share compositions.

**Release:** v1.0.0 publication benchmark / provider snapshot. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `mixed`.

**Labels/content:** room-temperature ionic conductivity; bulk/total conductivity distinction; composition; space group; lattice parameters; partial CIF coverage.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/NRC-Mila/OBELiX) · [data](https://github.com/NRC-Mila/OBELiX/tree/main/data) · [paper](https://doi.org/10.1039/d5dd00441a)

Other denominators (not added to the ranking):

- 321 CIF files: Subset of the 599 experimental entries

**Evidence:**

- [OBELiX author repository](https://github.com/NRC-Mila/OBELiX) (checked 2026-11-01): README reports 599 entries and 321 CIFs, with columns for original source DOI, close-match structure provenance and Liverpool/Laskowski crosswalks.
- [OBELiX data licence](https://raw.githubusercontent.com/NRC-Mila/OBELiX/main/LICENSE.txt) (checked 2026-11-01): Repository licence is Creative Commons Attribution 4.0.
- [OBELiX data availability](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00441a) (checked 2026-11-01): Publication identifies v1.0.0 benchmark; 291 of 321 CIFs have added random noise.

**Reuse and interpretation notes:**

- Overlaps Liverpool and Laskowski source datasets; do not sum their material counts.
- Only 321 entries have CIF files; some are close matches rather than exact structures of the measured samples.
- Noise-modified CIFs and partial occupancies require care in structure-based modeling.
- 599 entries are not established as 599 unique chemical compositions.

**Tags:** solid-electrolytes, ionic-conductivity, experimental, CIF-subset, property-focused, OpenAlex-survey-20261101.

<a id="caltech-li-conductivity-571"></a>
## Caltech experimental Li-ion structure–conductivity database

Experimental Li-ion conductivities joined to ICSD structure identifiers, with a separate ensemble-model prediction file.

**Size:** 571 experimental structure-conductivity entries (source wording: 571 experimental Li-containing compounds).

**Scope:** Experimental database in ionic_conductivity_database.csv; excludes the separate model prediction file.

**Release:** CaltechDATA v1, 25 April 2025. **Year:** 2025.

**Provenance:** literature. **Structure availability:** `structure_linked`.

**Labels/content:** room-temperature ionic conductivity; ICSD collection code; source DOI; lowest measured temperature.

**Access:** open. **Dataset license:** CC0 1.0 (CaltechDATA metadata rights).

**Official routes:** [homepage](https://data.caltech.edu/records/23mvv-6gk43) · [data](https://doi.org/10.22002/23mvv-6gk43) · [paper](https://doi.org/10.1039/d5dd00052a)

**Evidence:**

- [CaltechDATA provider record](https://data.caltech.edu/records/23mvv-6gk43) (checked 2026-11-01): Describes 571 Li-containing compounds with conductivity and ICSD collection codes, and separates a predicted superionic-likelihood CSV.
- [CaltechDATA machine-readable metadata](https://data.caltech.edu/api/records/23mvv-6gk43) (checked 2026-11-01): Lists two CSV files and CC0 1.0 rights.

**Reuse and interpretation notes:**

- Structure identifiers do not convey redistribution rights to full ICSD coordinates.
- Separate predicted superionic likelihoods must not be presented as measured conductivity.
- Shares Laskowski literature lineage with other electrolyte collections; material overlap not quantified here.

**Tags:** solid-electrolytes, ionic-conductivity, ICSD-linked, experimental, property-focused, OpenAlex-survey-20261101.

<a id="css-levitation-thermophysical"></a>
## China Space Station levitation thermophysical dataset

565 records: 420 on-orbit and 145 ground-matched containerless electrostatic levitation experiments on metallic alloys, ceramics and other materials.

**Size:** 565 levitation experimental records (source wording: 565).

**Scope:** 565 records: 420 on-orbit and 145 ground-matched containerless electrostatic levitation experiments on metallic alloys, ceramics and other materials.

**Release:** 2026 article and cited data release, checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** liquid-phase density; thermal response indicators; temperature history; composition; gravity environment; experimental configuration.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-06428-0) · [data](https://doi.org/10.5281/zenodo.17156569) · [repository](https://github.com/CSU-SPACE/CMPR_Levitation)

**Count derivation:** on-orbit + ground-matched experiment records; 420 + 145 = 565.

**Evidence:**

- [Materials dataset from microgravity levitation experiments on the China Space Station](https://www.nature.com/articles/s41597-025-06428-0) (checked 2026-11-01): Corrected primary article reports 565 experiment records and separates 420 on-orbit from 145 matched ground experiments.
- [CSS levitation dataset archive](https://zenodo.org/api/records/17156569) (checked 2026-11-01): CC BY 4.0; CMPR_Levitation_Dataset.xlsx released.

**Reuse and interpretation notes:**

- High-temperature/liquid-phase properties are not periodic crystal structures; include here as material thermophysical context.
- Containerless experiments and material identities are different counts.
- Use correction-linked/current article definitions and preserve gravity and thermal conditions.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="oxygen-ion-conductor-2026"></a>
## Oxygen-ion conductor Arrhenius property dataset

483 oxide entries from 84 experimental reports spanning 60 years, including separate low/high-temperature Arrhenius regimes when present.

**Size:** 483 oxide measurement-condition entries (source wording: 483).

**Scope:** 483 oxide entries from 84 experimental reports spanning 60 years, including separate low/high-temperature Arrhenius regimes when present.

**Release:** 2002 article and cited data release, checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** activation energy; Arrhenius prefactor; temperature break point; oxygen non-stoichiometry; bulk/total conductivity flag; composition.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-07100-x) · [data](https://doi.org/10.5281/zenodo.18947543) · [repository](https://github.com/JerryGarcia1995/OxygenIonConductor)

**Evidence:**

- [Charting the Landscape of Oxygen Ion Conductors: A 60-Year Dataset with Interpretable Regression Models](https://www.nature.com/articles/s41597-026-07100-x) (checked 2026-11-01): Data Records states 483 oxides and defines each entry by one oxide under a given measurement condition, preserving two-regime Arrhenius fits and bulk/total conductivity metadata.
- [Oxygen-ion data release metadata](https://zenodo.org/api/records/18947543) (checked 2026-11-01): CC BY 4.0; releases oxygen_ion_conductor_dataset.csv.

**Reuse and interpretation notes:**

- 483 is not established as 483 unique compositions.
- Activation energies are fits to conductivity data, not atomistic migration-barrier calculations.
- Bulk and total conductivities must remain distinguishable; no periodic coordinates.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mdf-steel-strength"></a>
## Foundry steel composition and mechanical properties

Dataset containing compositions and mechanical properties (yield strength, tensile strength, elongation) of 312 steel alloys

**Size:** 312 steel composition/property records (source wording: 312).

**Scope:** Foundry projects.foundry.n_items for steel_strength_v1.1; metadata-defined cohort, not a unique-structure recount

**Release:** steel_strength_v1.1 / public MDF metadata snapshot 2026-11-01. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** yield strength; tensile strength; elongation at fracture; composition weight percent.

**Access:** registration. **Dataset license:** CC BY 4.0 (MDF deposit rights declaration).

**Official routes:** [homepage](https://www.materialsdatafacility.org/detail/steel_strength_v1.1) · [data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=/foundry/steel_strength_v1.1/) · [release](https://doi.org/10.18126/524z-vd6m) · [code](https://github.com/MLMI2-CSSI/foundry)

**Evidence:**

- [MDF public deposit metadata and Foundry schema](https://search.api.globus.org/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5/subject?subject=steel_strength_v1.1) (checked 2026-11-01): Public subject response identifies steel_strength_v1.1, DOI 10.18126/524z-vd6m, n_items=312, the data file/split, input/target fields and units, and a CC-BY 4.0 rights declaration.

**Reuse and interpretation notes:**

- Count is the provider-reported Foundry n_items field, not an independent full-payload recount or a guarantee that every target is populated.
- Public deposit metadata was retrieved successfully without credentials. Bulk file transfer/loading was not attempted; the documented Globus/Foundry route may require account authorization.
- This is a named, versioned property cohort. Its rows must not be added to upstream databases as independent new crystals.
- The tabular schema provides composition/site/prototype or lattice descriptors; a complete set of atomic coordinates is not established for this release.
- Microstructure, heat treatment and processing history are not captured by the listed composition-only inputs; these factors can affect strength.

**Tags:** MDF, Foundry, MDF-property-20261101.

<a id="dax-ti-experimental"></a>
## DAX-Ti experimental Ti-alloy mechanical-property compilation

Composition, phases and processing conditions linked to experimental Ti-alloy stiffness, hardness and strength.

**Size:** 282 alloy entries (source wording: 282).

**Scope:** Static-0.1.0 cohort from 105 experimental studies

**Release:** 2022 paper release, checked 2026-11-01. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Young modulus (GPa); Vickers hardness (HV); yield / ultimate strength (MPa); elongation (%); grain size (μm); oxygen content (wppm); phase constituents and processing conditions.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo dataset).

**Official routes:** [publication](https://doi.org/10.1038/s41597-022-01283-9) · [download](https://doi.org/10.5281/zenodo.6089749) · [repository](https://gitlab.com/comari/dax-ti)

**Evidence:**

- [A compilation of experimental data on the mechanical properties and microstructural features of Ti-alloys](https://www.nature.com/articles/s41597-022-01283-9) (checked 2026-11-01): Paper reports 282 entries from 105 studies; Table 1 supplies units, reference DOI, phases and treatment conditions; experiments are at room temperature.
- [DAX-Ti static-0.1.0 deposit](https://zenodo.org/records/6089749) (checked 2026-11-01): Open CC BY 4.0 deposit exposes static CSV, field definitions and helper script; description identifies 282 distinct alloys.

**Reuse and interpretation notes:**

- Room-temperature alloy properties depend on processing, phases and test method, not composition alone.
- Tensile strain is positive and compression strain negative; some nonfracturing specimens have deformation capped at ±50%.
- Not every entry contains all properties; oxygen/grain-size coverage is incomplete.
- Phase labels are not full periodic atomic structures.

**Tags:** mechanical, elastic, hardness, alloys, processing-aware, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="ferritic-steel-xct-defects"></a>
## Mechanically deformed ferritic-steel XCT defect database

Ferritic-steel volumetric defect images and quantified descriptors linked to deformation state.

**Size:** 276 sample-condition XCT datasets (source wording: 276).

**Scope:** 134 tensile-tested plus142 fatigue-tested sample datasets

**Release:** 2025 paper cohort; deposit checked 2026-11-01. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** XCT volumes; defect volume, shape, size and topology; strain/fracture progression; loading conditions.

**Access:** open. **Dataset license:** CC0 1.0 (Dryad).

**Official routes:** [publication](https://doi.org/10.1038/s41597-025-06141-y) · [data](https://doi.org/10.5061/dryad.9cnp5hqpf)

Other denominators (not added to the ranking):

- 938 tensile defect-feature entries: 134 tensile datasets
- 2,305 fatigue defect-feature entries: 142 fatigue datasets

**Evidence:**

- [Mechanically deformed ferritic-steel XCT defect database — Scientific Data descriptor](https://doi.org/10.1038/s41597-025-06141-y) (checked 2026-11-01): Abstract/methods report 276 datasets, including134 tensile and 142 fatigue samples with 938 and 2,305 defect-feature entries respectively.
- [Mechanically deformed ferritic-steel XCT defect database — primary deposit](https://doi.org/10.5061/dryad.9cnp5hqpf) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- One ferritic alloy;276 image/condition datasets are not276 materials.
- Raw voxel size 3 µm; fatigue quantification uses downscaled 12 µm data, affecting small-defect detection.
- Sub-voxel defects can be overestimated and sizes are reported as ranges.
- Fatigue subgroup counts elsewhere in text do not reconcile directly with 142; preserve descriptor totals rather than silently recomputing.
- Latest public API metadata reports submitted version status; published paper cohort defines this record.

**Tags:** Scientific Data, processing, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="softmag-fe-mgo"></a>
## Fe/MgO soft magnetic composite processing properties

Corrected Dataset v.2.csv contains 274 rows; original paper and first CSV describe 282 samples.

**Size:** 274 corrected processing-condition samples (source wording: 274).

**Scope:** Corrected Dataset v.2.csv contains 274 rows; original paper and first CSV describe 282 samples. Duplicate removal and density remeasurements are documented.

**Release:** Figshare 25975198 v2, corrected 274-row CSV. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** density (g/cm³); coercivity (A/m); resonant frequency (kHz); DC/3 kHz permeability; MgO particle size; pressing/annealing conditions.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-04286-w) · [data](https://doi.org/10.6084/m9.figshare.25975198.v2)

**Evidence:**

- [The first experimentally obtained dataset on processing parameters and properties of soft magnetic composites](https://www.nature.com/articles/s41597-024-04286-w) (checked 2026-11-01): Paper reports 282 independently prepared processing combinations for Fe/MgO and five measured properties; newer release includes a corrected data table.
- [Soft-magnetic deposit v2](https://api.figshare.com/v2/articles/25975198) (checked 2026-11-01): Deposit CC BY 4.0; describes removed duplicate data and remeasured/corrected densities; original CSV 282 rows, corrected CSV 274.

**Reuse and interpretation notes:**

- Use corrected file for v2; do not sum original and corrected tables.
- Composite sample count is not unique crystal compositions; no atomic structures.
- Preserve categorical annealing atmosphere coding when using corrected file.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="fatiguedata-cma2022"></a>
## FatigueData-CMA2022 complex metallic-alloy fatigue database

Literature-derived stress-life, strain-life and fatigue-crack-growth curves with processing, load and testing conditions.

**Size:** 272 fatigue test-condition datasets (source wording: 272).

**Scope:** Paper release covering metallic glasses and multi-principal element alloys; not a count of compositions or scalar data points

**Release:** 2023 paper release, checked 2026-11-01. **Year:** 2023.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** stress-life S–N curves (MPa and cycles); strain-life ε–N curves; fatigue crack growth da/dN–ΔK curves; strength and fracture toughness; processing sequence; test temperature, load ratio and environment.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare dataset); MIT applies separately to accompanying scripts.

**Official routes:** [publication](https://doi.org/10.1038/s41597-023-02354-1) · [download](https://doi.org/10.6084/m9.figshare.23007362.v2) · [repository](https://github.com/xuzpgroup/ZianZhang/tree/main/FatigueData-CMA2022)

**Evidence:**

- [Fatigue database of complex metallic alloys](https://www.nature.com/articles/s41597-023-02354-1) (checked 2026-11-01): Paper documents 272 test-condition datasets with three fatigue-curve families, material/processing/testing metadata and default MPa stress units.
- [FatigueData-CMA2022 deposit metadata](https://api.figshare.com/v2/articles/23007362) (checked 2026-11-01): Open v2 deposit includes MAT, JSON and XLSX with CC BY 4.0 license.

**Reuse and interpretation notes:**

- Includes amorphous metallic glasses as well as crystalline MPEAs; filter material class for crystal-specific use.
- Dataset count differs from number of compositions and curve points; EXCEL curves are sampled to 500 points per dataset while MAT/JSON preserve richer curves.
- When unspecified, authors assume uniaxial testing at 25 °C in air and stress concentration Kt=1; these are imputed defaults, not reported measurements.
- Use stress ratio, surface/processing state and run-out flags; do not aggregate fatigue values by composition alone.

**Tags:** mechanical, fatigue, curves, mixed-structure, processing-aware, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

<a id="tematdb272"></a>
## teMatDb272 thermoelectric material database

Digitized temperature-dependent transport curves filtered for agreement between reported and recalculated ZT.

**Size:** 272 curated thermoelectric sample curve sets (source wording: 272).

**Scope:** High-fidelity subset in teMatDb v1.1.6, selected from 355 raw digitized curve sets

**Release:** teMatDb v1.1.6 / teMatDb272 (2025-05-26). **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Seebeck coefficient versus temperature; electrical resistivity versus temperature; thermal conductivity versus temperature; dimensionless ZT versus temperature.

**Access:** open. **Dataset license:** CC BY 4.0 (Zenodo v1.1.6 deposit).

**Official routes:** [homepage](https://tematdb.streamlit.app) · [publication](https://arxiv.org/abs/2505.19150) · [download](https://doi.org/10.5281/zenodo.15518036) · [repository](https://github.com/byungkiryu/teMatDb)

Other denominators (not added to the ranking):

- 355 raw sample curve sets: Parent digitized cohort before self-consistent ZT filtering
- 14,717 temperature-property pairs: teMatDb272 as reported by accompanying preprint
- 262 publications: Sources for teMatDb272

**Evidence:**

- [teMatDb v1.1.6: Thermoelectric Material Database](https://zenodo.org/records/15518036) (checked 2026-11-01): Deposit reports 355 raw curve sets and 272 high-fidelity samples; metadata declares CC BY 4.0 and exposes versioned ZIP.
- [A High-Quality Thermoelectric Material Database with Self-Consistent ZT Filtering](https://arxiv.org/abs/2505.19150) (checked 2026-11-01): Preprint describes 14,717 temperature-property pairs in 272 sample sets across 262 publications and self-consistent ZT filtering.

**Reuse and interpretation notes:**

- Curve sets and temperature-property pairs are different counting units; neither is a unique-crystal count.
- Keep digitized curves, units and individual temperature grids; do not replace them with peak-ZT scalars.
- Property units should be read from the released per-property data; the deposit summary does not establish one global stored-unit convention.
- Independent digitization may overlap UCSB, ESTM and Starrydata source experiments.

**Tags:** thermoelectric, digitized-curves, temperature-dependent, property-focused, OpenAlex-survey-20261101.

<a id="hea-fracture-impact-2023"></a>
## HEA fracture and impact toughness dataset

153 fracture-toughness, 14 impact-toughness and 78 impact-energy records, each describing a distinct metallurgical condition.

**Size:** 245 metallurgical-condition property records (source wording: 245).

**Scope:** 153 fracture-toughness, 14 impact-toughness and 78 impact-energy records, each describing a distinct metallurgical condition.

**Release:** 2023 article and cited data release, checked 2026-11-01. **Year:** 2023.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** fracture toughness (MPa√m); impact toughness; impact energy (J); tensile properties; grain size; processing/test conditions.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01911-4) · [data](https://doi.org/10.24435/materialscloud:d6-pf)

**Count derivation:** three property category records; 153 + 14 + 78 = 245.

**Evidence:**

- [Dataset for Fracture and Impact Toughness of High-Entropy Alloys](https://www.nature.com/articles/s41597-022-01911-4) (checked 2026-11-01): Paper distinguishes the 153/14/78 category counts and describes Excel worksheets with chemistry, processing, phase, specimen and test details.
- [Materials Cloud HEA fracture archive](https://archive.materialscloud.org/records/pvpcb-mpc63) (checked 2026-11-01): Version v3 release declares CC BY 4.0 and contains Excel worksheets for the three property categories.

**Reuse and interpretation notes:**

- A composition can occur under multiple conditions; record count is not unique-alloy count.
- Do not combine fracture toughness, impact toughness and impact energy as one target.
- Companion HEA fatigue and complex metallic alloy releases may overlap alloys and sources; this adds different properties.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="complex-oxide-cte-2026"></a>
## Literature-curated complex-oxide thermal expansion

Measured thermal-expansion coefficients and measurement ranges used for probabilistic complex-oxide modeling.

**Size:** 204 composition–temperature-range records (source wording: 204).

**Scope:** Measured thermal-expansion coefficients and measurement ranges used for probabilistic complex-oxide modeling.

**Release:** Actual CTE Value 10.xlsx in repository tree checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental; literature-curated. **Structure availability:** `composition_only`.

**Labels/content:** composition; thermal-expansion coefficient; start/end measurement temperature (°C); source-paper reference.

**Access:** open. **Dataset license:** MIT (repository declaration).

**Official routes:** [paper](https://doi.org/10.1063/5.0333166) · [homepage](https://github.com/Jordanmarshall-utk/cte-probabilistic-ml) · [data](https://github.com/Jordanmarshall-utk/cte-probabilistic-ml/blob/main/CTE%20Value%2010.xlsx)

**Evidence:**

- [Thermal-expansion dataset paper](https://doi.org/10.1063/5.0333166) (checked 2026-11-01): Matching title/author data-availability statement points to the author repository and processed experimental CTE data.
- [CTE Value 10 workbook](https://raw.githubusercontent.com/Jordanmarshall-utk/cte-probabilistic-ml/main/CTE%20Value%2010.xlsx) (checked 2026-11-01): Independently counted 204 nonempty rows, five columns: Composition, CTE Value, Start Temp (°C), End Temp (°C), paper.
- [CTE repository license](https://raw.githubusercontent.com/Jordanmarshall-utk/cte-probabilistic-ml/main/LICENSE) (checked 2026-11-01): MIT declaration in the repository.

**Reuse and interpretation notes:**

- CTE values are associated with specific temperature intervals and measurement conventions; retain the source reference.
- The README uses a generic dataset filename; the count uses the actual CTE Value 10.xlsx file listed in the repository.
- The second broader composition workbook and engineered feature rows are not added to the main count.
- No atomic coordinates in the selected table.

**Tags:** additional-materials-20261101.

<a id="her-multinary-alloys-2026"></a>
## Multinary alloy HER catalyst performance

180 curated catalyst entries with composition descriptors, onset potential and Tafel slope, linked to source-level measurement conditions.

**Size:** 180 experimental catalyst/performance records (source wording: 180).

**Scope:** 180 curated catalyst entries with composition descriptors, onset potential and Tafel slope, linked to source-level measurement conditions.

**Release:** Zenodo 20406173 v1.0.0; 2026 article-in-press. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** HER onset potential; Tafel slope (mV/dec); normalized atomic-percent composition; source electrochemical metadata; Magpie descriptors.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-07856-2) · [data](https://doi.org/10.5281/zenodo.20406173) · [repository](https://github.com/sgorsse/HER-alloy-catalysts-dataset-GPR)

**Evidence:**

- [Curated dataset of multinary alloy HER catalysts for composition-only modelling with Magpie descriptors and GP baselines](https://www.nature.com/articles/s41597-026-07856-2) (checked 2026-11-01): PDF Data Records gives 180 experimental rows and distinguishes source-context/harmonized tables from a model-guided 100-composition candidate list.
- [HER alloy dataset v1.0.0](https://zenodo.org/api/records/20406173) (checked 2026-11-01): CC BY 4.0 deposit provides dataset/framework archive.

**Reuse and interpretation notes:**

- The 100 proposed candidate alloys are predictions, not measured additions.
- Onset and Tafel values depend on reference electrode, electrolyte, fitting window and iR treatment.
- Composition descriptors do not establish exact crystal phase, atomic structures or intrinsic surface activity.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="optical-emissivity-designs-2022"></a>
## Optical emissivity curves for heterogeneous engineered designs

Figure-extracted emissivity curves with materials, geometry and experimental/computational method metadata.

**Size:** 153 emissivity curve records (source wording: 153).

**Scope:** 153 one-curve JSON records extracted from 176 figures in 64 papers; source figures contain 550 curves, so this is a successfully extracted subset.

**Release:** Figshare 20773552 v1; 153-JSON archive recount. **Year:** 2022.

**Provenance:** mixed. **Structure availability:** `composition_only`.

**Labels/content:** spectral emissivity (dimensionless); wavelength/frequency axis units; material list; engineered geometry/layer keywords; measurement or calculation method; curve extraction quality score; source DOI/figure.

**Access:** open. **Dataset license:** CC0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01699-3) · [data](https://doi.org/10.6084/m9.figshare.20773552.v1) · [collection](https://doi.org/10.6084/m9.figshare.c.6037004.v1) · [repository](https://github.com/ViktoriiaBaib/curvedataextraction)

**Evidence:**

- [Optical emissivity dataset of multi-material heterogeneous designs generated with automated figure extraction](https://www.nature.com/articles/s41597-022-01699-3) (checked 2026-11-01): Data Records defines one JSON per curve, containing material, geometry, method, axes units, legend and quality score; 153 curves retrieved from 550 total source curves.
- [Emissivity data release v1](https://api.figshare.com/v2/articles/20773552) (checked 2026-11-01): Figshare declares CC0; downloaded emissivity_dataset.zip independently contains 153 curve JSON files. Payload explicitly identifies calculated as well as experimental curves.

**Reuse and interpretation notes:**

- Curves describe engineered films, multilayers, composites and other geometries, not unique bulk crystals.
- Experimental and simulated curves coexist; preserve data_type and modeling/measurement method.
- The extraction retains only colored curves that the pipeline recovered; reported recall is 27% over all source curves and 55% over colored curves.
- Quality scores flag curve gaps/conflicting points; digitized points are not original instrument output.
- Geometry keywords are not full atomistic structures; do not merge this release with EKHI as disjoint materials.

**Tags:** Scientific-Data, device-or-engineered-material-scope, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="trace-in625-tensile"></a>
## Trace-IN625 source-aware tensile properties

149 tensile records from 72 of 305 indexed papers; 120 IN625 and 29 IN625-containing composite/graded/joined records, linked to 482 source-condition records.

**Size:** 149 tensile-property records (source wording: 149).

**Scope:** 149 tensile records from 72 of 305 indexed papers; 120 IN625 and 29 IN625-containing composite/graded/joined records, linked to 482 source-condition records.

**Release:** Zenodo 22760894 v3; 2026 article-in-press. **Year:** 2026.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** yield strength; ultimate tensile strength; elongation definition; test temperature/orientation; processing and treatment; source page/table/figure locators.

**Access:** open. **Dataset license:** CC BY 4.0 for structured data; image crops retain per-source licenses.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-08585-2) · [data](https://doi.org/10.5281/zenodo.22760894) · [repository](https://github.com/molindaozi/materials-multimodal-db)

**Evidence:**

- [Trace-IN625 a source aware literature derived dataset of tensile properties and microstructure for additively manufactured IN625](https://www.nature.com/articles/s41597-026-08585-2) (checked 2026-11-01): Article-in-press PDF distinguishes 149 tensile-property records from 482 conditions, 2,206 microstructure/evidence records and 280 released figure crops.
- [Trace-IN625 v3 archive](https://zenodo.org/api/records/22760894) (checked 2026-11-01): CC BY 4.0 structured metadata; six CSVs include tensile_properties.csv, specimen/source-condition and provenance tables. Images carry source-specific licenses.

**Reuse and interpretation notes:**

- The 482 source-condition rows are not independent experimental replicates.
- Tensile layer has 391 populated values, not all three properties for every row; missing values are not zero.
- CC BY 4.0 applies to metadata; third-party figure crops have individual terms and are not atomistic structures.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="aisi52100-rolling-contact-fatigue"></a>
## AISI52100 grease-lubricated rolling-contact fatigue benchmark

Per-trial bearing-steel fatigue lifetime, post-test damage microscopy and derived Weibull statistics under controlled lubrication.

**Size:** 63 four-ball tribometer trials (source wording: 63).

**Scope:** 21 independent trials for each of three calcium-grease grades

**Release:** 2026 descriptor cohort; deposit checked 2026-11-01. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** time to failure (s); post-test pitting/crack/deformation microscopy; Weibull lifetime quantiles; survival, hazard and probability-density functions; grease and mechanical-test conditions.

**Access:** open. **Dataset license:** CC BY 4.0 (Mendeley Data v3).

**Official routes:** [publication](https://doi.org/10.1038/s41597-026-08057-7) · [data](https://doi.org/10.17632/d5n3zgvs7p.3)

Other denominators (not added to the ranking):

- 1,140 post-test optical microscopy images: Damage images across63 trials and their lower balls
- 3 calcium grease grades: NLGI0,00,000 with extreme-pressure additives

**Count derivation:** 21 trials in each of three grease-grade groups; 21 + 21 + 21 = 63.

**Evidence:**

- [Rolling contact fatigue dataset for AISI52100 bearing steel balls under calcium grease lubrication](https://www.nature.com/articles/s41597-026-08057-7) (checked 2026-11-01): Descriptor reports 63 trials,21 per NLGI 0/00/000 grade, at 1470 rpm,5739 N peak axial load and35±3°C;1,140 optical images accompany per-trial metadata.
- [Mendeley Data rolling-contact-fatigue v3](https://data.mendeley.com/datasets/d5n3zgvs7p/3) (checked 2026-11-01): Primary deposit is public, dated 25June2026, version 3, under CC BY 4.0; description identifies IP300 four-ball tests on AISI52100.

**Reuse and interpretation notes:**

- A material-response/tribology benchmark rather than a resolved-crystal structure cohort; one bearing-steel grade is investigated.
- Each trial has one time-to-failure value; three lower balls in a trial share that elapsed time and are not independent fatigue tests.
- Microscopy images show damage at50×magnification(5×objective)and2160×1620 px; image count differs from trial count.
- Weibull curves and lifetime quantiles are derived statistical outputs, not additional measured trials.

**Tags:** Scientific Data, final-title-audit, characterization, condition-dependent, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="oxide-synthesis-aggregates-2017"></a>
## Aggregated oxide synthesis parameter distributions

30 oxide systems summarized from approximately 76,000 relevant articles within a 640,000-article training corpus.

**Size:** 30 oxide material-system summaries (source wording: 30).

**Scope:** 30 oxide systems summarized from approximately 76,000 relevant articles within a 640,000-article training corpus.

**Release:** 2017 article and cited data release, checked 2026-11-01. **Year:** 2017.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** calcination/sintering temperature and time distributions; associated materials; synthesis topic distributions; precursor/material co-occurrences; synthesis-temperature distributions; topic distributions; frequent synthesis parameters.

**Access:** open. **Dataset license:** MIT.

**Official routes:** [paper](https://doi.org/10.1038/sdata.2017.127) · [data](https://doi.org/10.6084/m9.figshare.5221351.v1)

**Evidence:**

- [Machine-learned and codified synthesis parameters of oxide materials](https://www.nature.com/articles/sdata2017127) (checked 2026-11-01): Data Records provides per-material-system JSON and kernel-density estimates for synthesis parameters, not individually reconstructable synthesis recipes.
- [Aggregated oxide synthesis deposit](https://api.figshare.com/v2/articles/5221351) (checked 2026-11-01): MIT-licensed material_synthesis_data.json independently contains 30 embedded JSON system summaries.

**Reuse and interpretation notes:**

- Corpus paper counts are not the released data-record count.
- Aggregated distributions should not be presented as individual successful recipes or measured physical properties.
- No atomic structures; distinct aggregation from later Ceder solid-state/solution recipe releases.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

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

<a id="hawaii-ironoxide-correlative-grains"></a>
## Correlative chemical, crystallographic and magnetic iron-oxide grains

Individual natural iron-oxide grain chemistry, EBSD phase/orientation and magnetic-domain images registered across techniques.

**Size:** 23 deposited component datasets (source wording: 23).

**Scope:** PANGAEA publication-series component count; not grain or crystal count

**Release:** 2018 descriptor cohort; deposit checked 2026-11-01. **Year:** 2018.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** microprobe elemental composition (atomic %); SEM/BSE and phase observations; EBSD orientations and Euler angles; AFM/MFM magnetic-domain images; before/after-heating grain comparisons.

**Access:** open. **Dataset license:** CC BY 3.0 Unported (PANGAEA publication series).

**Official routes:** [publication](https://doi.org/10.1038/sdata.2018.162) · [data](https://doi.org/10.1594/PANGAEA.886180)

Other denominators (not added to the ranking):

- 11 sampled lava-flow/site groups: Published study provenance groups

**Evidence:**

- [Chemical,crystallographic and magnetic characterisation of individual iron-oxide grains in Hawaiian lavas](https://www.nature.com/articles/sdata2018162) (checked 2026-11-01): Descriptor investigates 3–6 individual~3–10 µm grains from each of 11 lava flows with MFM, microprobe and SEM/EBSD; per-grain binders align techniques.
- [PANGAEA primary publication series](https://doi.pangaea.de/10.1594/PANGAEA.886180) (checked 2026-11-01): Landing page identifies23 component datasets, CC BY 3.0 Unported licensing and download routes for constituent data.

**Reuse and interpretation notes:**

- Natural-lava provenance is geological, but included evidence is grain-level material chemistry, crystallography and magnetism rather than a geospatial survey.
- 23 denotes component deposits; the exact count of fully characterized grains was not independently established.
- EBSD orientations and microscopy are not a periodic atomic-coordinate database.
- Per-site deposits and per-grain binders are complementary representations and must not be summed as independent samples.
- Retain grain/site identifier, heating history and chemistry-quality flags; microprobe analyses with>2%Si can include surrounding material.

**Tags:** Scientific Data, final-title-audit, characterization, condition-dependent, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="nist-hafnia-planar-reference-2025"></a>
## NIST hafnia-on-silicon planar film metrology set

Spatially resolved X-ray reflectometry and spectroscopic ellipsometry for ALD hafnia films, with wafer/deposition provenance and preliminary thickness-model fits.

**Size:** 12 200mm hafnia-coated silicon wafers (source wording: 12).

**Scope:** Twelve sister wafers across four deposition runs; full SE maps target four selected wafers and XRR coverage varies across wafers.

**Release:** NIST mds2-3930 v1.0.1; README v1.0.0; CHIPS-6-02-25-00-set. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** X-ray reflectometry; ellipsometric Psi/Delta spectra; preliminary film thickness(nm); refractive-index model parameters; fit errors; wafer position(cm); deposition batch and chamber position.

**Access:** open. **Dataset license:** NIST data-use terms explicitly linked by release metadata; not a Creative Commons license.

**Official routes:** [homepage](https://data.nist.gov/od/id/mds2-3930) · [data](https://doi.org/10.18434/mds2-3930)

**Evidence:**

- [NIST current primary release metadata](https://data.nist.gov/od/id/mds2-3930) (checked 2026-11-01): Current version1.0.1 identifies12 wafers, downloadable raw RAS/RASX and SE formats, text model exports and instrument-alignment files; release history says v1.0.1 added the CHIPS collection.
- [Hafnia release README and inspected text exports](https://data.nist.gov/od/ds/mds2-3930/CHIPS-6-02-25-00-set%2FREADME.txt) (checked 2026-11-01): Documents65 ALD cycles on200mm Si, four runs/chamber positions, instrument models/serials and wafer mapping. Downloaded fit table labels X/Y(cm), thickness(nm), Cauchy parameters and individual Error columns. Fits assume one Cauchy layer over300–1000nm.

**Reuse and interpretation notes:**

- Small process-correlated wafer cohort;12 wafers are not12 chemistries or independent deposition batches.
- Reported thickness parameters are preliminary single-layer Cauchy fits; fit errors are not a complete certified uncertainty budget.
- XRR is intended to reduce SE uncertainty, while fuller maps and diced reference-material distribution are described as future work.
- Some full instrument formats are proprietary; text exports and raw ASCII RAS provide reusable subsets.
- README has a likely wafer typo24-04 while the deposition list says25-04; preserve original identifiers when reconciling.

**Tags:** Data.gov-selection-20261101, verified-2026-11-01, specialist-experimental-data.

<a id="bam-temperature-elastic-alloys"></a>
## BAM temperature-dependent elastic alloy reference data

Ti-6Al-4V, IN718 and AISI316L each have additive and conventional manufacturing variants, with specimen-level temperature series and uncertainty.

**Size:** 3 alloy systems with paired manufacturing routes (source wording: 3).

**Scope:** Ti-6Al-4V, IN718 and AISI316L each have additive and conventional manufacturing variants, with specimen-level temperature series and uncertainty.

**Release:** 2023 paper; Zenodo concept DOI routes currently resolve to 2025 versions. **Year:** 2023.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** Young modulus; shear modulus; resonance frequencies; thermal expansion; density; temperature; measurement uncertainty.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-023-02387-6) · [ti_data](https://doi.org/10.5281/zenodo.7813732) · [in718_data](https://doi.org/10.5281/zenodo.7813824) · [316l_data](https://doi.org/10.5281/zenodo.7813835)

**Evidence:**

- [Elastic modulus data for additively and conventionally manufactured variants of Ti-6Al-4V, IN718 and AISI 316 L](https://www.nature.com/articles/s41597-023-02387-6) (checked 2026-11-01): Paper describes dynamic-resonance elastic measurements on three alloys with two manufacturing routes and specimen/temperature/uncertainty metadata.
- [BAM Ti64 current version](https://zenodo.org/api/records/14617243) (checked 2026-11-01): CC BY 4.0; workbook plus coversheet, room temperature–400 °C.
- [BAM IN718 current version](https://zenodo.org/api/records/14617176) (checked 2026-11-01): CC BY 4.0; room temperature–800 °C.
- [BAM AISI316L current version](https://zenodo.org/api/records/14616480) (checked 2026-11-01): CC BY 4.0; room temperature–900 °C.

**Reuse and interpretation notes:**

- Three is the alloy-system count, not total specimens or temperature observations.
- Moduli derive from measured resonance and specimen dimensions; preserve uncertainty and processing state.
- No periodic atomic structures; latest referenced concept DOI routes resolve to 2025 BAM versions.

**Tags:** Scientific-Data, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="steel304l-dic-ir-fullfield"></a>
## 304L stainless-steel full-field DIC and infrared thermography

Synchronized displacement, strain, temperature and mechanical-loading data for calibrating metal-plasticity models.

**Size:** Unranked specimen-test measurement records (source wording: Not reported).

**Scope:** Independent test-record count not established; seven geometry designs are reported

**Release:** 2024 descriptor cohort; deposit checked 2026-11-01. **Year:** 2024.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** full-field displacement and strain; infrared temperature fields; force-extension-time histories; specimen geometry coordinates (mm); rolling orientation and loading-rate metadata.

**Access:** open. **Dataset license:** CC0 1.0 (Figshare+ v1).

**Official routes:** [publication](https://doi.org/10.1038/s41597-024-03949-y) · [data](https://doi.org/10.25452/figshare.plus.25483534.v1)

Other denominators (not added to the ranking):

- 7 unique nonstandard specimen geometries: Descriptor reports seven unique geometries,with conventional tensile dog-bone comparisons

**Evidence:**

- [Digital image correlation and infrared thermography data for seven unique geometries of304L stainless steel](https://www.nature.com/articles/s41597-024-03949-y) (checked 2026-11-01): Descriptor supplies raw/postprocessed DIC/IR and force data, specimen drawings, test matrix and metallurgy report; tests vary orientation, rate and thermal loading.
- [304L Figshare+ primary metadata](https://api.figshare.com/v2/articles/25483534) (checked 2026-11-01): Open deposit is version 1, DOI 10.25452/figshare.plus.25483534.v1, under CC0; metadata confirms repeated conditions and raw plus synchronized/registered outputs.

**Reuse and interpretation notes:**

- One rolled304L sheet lot; geometries, orientations and repeated tests are not independent material compositions.
- No periodic atomic-coordinate release is established; geometric coordinates describe specimen boundaries and measurement grids.
- Preserve specimen ID, rolling direction, rate, thermal loading and synchronization metadata.
- Some tests have two DIC systems instead of IR; not every modality exists for every test.
- Processed arrays can contain NaN for missing spatial/temporal data; MATLAB7.3 files require HDF5-compatible readers.

**Tags:** Scientific Data, final-title-audit, characterization, condition-dependent, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="corrosion-resistant-alloy-metrics"></a>
## Corrosion-resistant alloy electrochemical metrics

Literature-curated alloy corrosion metrics with solution, microstructure and testing context.

**Size:** Unranked corrosion metric/condition records (source wording: Not verified).

**Scope:** Six property sections from 85 publications; exact row count has not been reconciled across worksheets, repeated conditions and metric types.

**Release:** Figshare 13038257 v2; 2021 descriptor. **Year:** 2021.

**Provenance:** experimental. **Structure availability:** `composition_only`.

**Labels/content:** pitting/repassivation/crevice potential (mV versus SCE); pitting/crevice temperature (°C); corrosion/passivation current density (A/cm²); corrosion rate (mm/year); composition and treatment; chloride concentration and pH.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-021-00840-y) · [data](https://doi.org/10.6084/m9.figshare.13038257.v2)

**Evidence:**

- [Electrochemical metrics for corrosion resistant alloys](https://www.nature.com/articles/s41597-021-00840-y) (checked 2026-11-01): Describes six corrosion property sections from 85 publications with composition, chloride/pH, treatment, microstructure and test methods.
- [CRA workbook deposit v2](https://api.figshare.com/v2/articles/13038257) (checked 2026-11-01): CC BY 4.0 workbook release; downloaded worksheet headers verify stored potential, temperature, current-density and corrosion-rate units.

**Reuse and interpretation notes:**

- Individual corrosion metrics are different targets and not universally complete for each sample.
- Potential reference electrode, solution composition, pH, scan rate, temperature and microstructure affect comparisons.
- No atomic crystal coordinates. Worksheet formatting and repeated/unnumbered rows prevent a verified total from simple row-number counting.

**Tags:** Scientific-Data, corrosion, conditions-required, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="in718-correlative-3d-ebsd-dic"></a>
## Inconel718 correlative 3D microstructure and deformation fields

Co-registered SEM, HR-DIC and 3D EBSD fields for microstructure–plasticity analysis of Inconel718.

**Size:** Unranked registered multimodal specimen datasets (source wording: Not reported).

**Scope:** No unambiguous independent-specimen count established

**Release:** 2022 paper cohort; deposit checked 2026-11-01. **Year:** 2022.

**Provenance:** experimental. **Structure availability:** `mixed`.

**Labels/content:** 3D grain orientations and grain IDs; HR-DIC strain and slip fields; 2D/3D EBSD patterns; microstructural meshes.

**Access:** open. **Dataset license:** CC0 1.0 (Dryad).

**Official routes:** [publication](https://doi.org/10.1038/s41597-022-01525-w) · [data](https://doi.org/10.5061/dryad.83bk3j9sj)

**Evidence:**

- [Inconel718 correlative3D microstructure and deformation fields — Scientific Data descriptor](https://doi.org/10.1038/s41597-022-01525-w) (checked 2026-11-01): Primary descriptor and Dryad release 3D EBSD, strain/slip fields and meshes. Paper describes 526 serial sections; orientation conventions and coordinate transformations are documented.
- [Inconel718 correlative3D microstructure and deformation fields — primary deposit](https://doi.org/10.5061/dryad.83bk3j9sj) (checked 2026-11-01): Named release route, access and rights verified against repository or depositor metadata; details in local receipts.

**Reuse and interpretation notes:**

- Voxel/mesh coordinates describe microstructure, not periodic atom positions.
- 2D and 3D Euler conventions differ; apply supplied coordinate transformations.
- HR-DIC map spacing 100.34 nm and slip-amplitude pixel 33.45 nm; do not interchange.
- Repository API latest version status is submitted; count/version claims here refer to published descriptor cohort, not draft updates.

**Tags:** Scientific Data, processing, verified-2026-11-01, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mpod"></a>
## Material Properties Open Database (MPOD)

Quantitative physical-property data for crystalline materials. The advertised OPTIMADE structure endpoint timed out; data availability and licensing require provider confirmation.

**Size:** Unranked material-property records (source wording: Unranked).

**Scope:** Full collection size not verified; no estimate assigned.

**Release:** Provider/API snapshot, checked 2026-11-01. **Year:** Not verified.

**Provenance:** source-dependent; corpus not audited. **Structure availability:** `structure_linked`.

**Labels/content:** physical properties of crystalline materials.

**Access:** mixed. **Dataset license:** Not verified; inspect collection and original-source terms before redistribution.

**Official routes:** [homepage](http://mpod.cimav.edu.mx) · [documentation](https://providers.optimade.org/v1/links) · [api_index](https://providers.optimade.org/index-metadbs/mpod)

**Evidence:**

- [Material Properties Open Database (MPOD) provider documentation](https://providers.optimade.org/v1/links) (checked 2026-11-01): Quantitative physical-property data for crystalline materials. The advertised OPTIMADE structure endpoint timed out; data availability and licensing require provider confirmation.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.

**Reuse and interpretation notes:**

- Database/provider snapshot checked 2026-11-01; overlapping records and releases must not be summed as unique materials.
- Public availability is distinct from reuse permissions; per-record provenance and rights may differ.
- No defensible full-collection size verified; deliberately unranked.  API: OPTIMADE; Advertised route could not be verified: <urlopen error timed out>

**Tags:** Repository-coverage-20261101, mpod, Material Properties Open Database (MPOD).

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

<a id="nist-cryogenic-materials"></a>
## NIST Cryogenic Materials Property Database

Temperature-dependent engineering-material property correlations, explicit fit coefficients and usable ranges, with a regenerator heat-capacity table.

**Size:** Unranked material/property records (source wording: Not verified).

**Scope:** Public collection; total record count not verified

**Release:** Current TRC-hosted collection, checked 2026-11-01; individual revisions vary. **Year:** Not verified.

**Provenance:** experimental literature compilation. **Structure availability:** `composition_only`.

**Labels/content:** thermal conductivity; specific heat; Young modulus; thermal expansion; volumetric heat capacity.

**Access:** open. **Dataset license:** No collection-specific open data redistribution license verified.

**Official routes:** [homepage](https://trc.nist.gov/cryogenics/materials/materialproperties.htm) · [documentation](https://trc.nist.gov/cryogenics/materials/references.htm)

**Evidence:**

- [NIST authoritative relocation notice](https://www.nist.gov/mml/acmd/nist-cryogenic-materials-property-database-index) (checked 2026-11-01): Official NIST page explicitly moves the collection to the TRC materials-property index, preserving identity of the attached legacy database.
- [6061-T6 aluminum correlation tables](https://trc.nist.gov/cryogenics/materials/6061%20Aluminum/6061_T6Aluminum_rev.htm) (checked 2026-11-01): Retrievable HTML tables provide coefficients, equations, property units, kelvin temperature ranges and fit errors for four properties; conductivity and specific heat have stated data ranges 4–300 K.
- [Cryogenic property source bibliography](https://trc.nist.gov/cryogenics/materials/references.htm) (checked 2026-11-01): Material-specific references supply literature provenance, including an Al6061 section.
- [Regenerator material numerical table](https://trc.nist.gov/cryogenics/materials/RegeneratorMaterials/Regenerator%20Materials%20rev%2009-22-06.htm) (checked 2026-11-01): Retrievable spreadsheet-style HTML contains temperature-dependent volumetric heat capacities, with K and J/cm3-K labels.

**Reuse and interpretation notes:**

- Correlations fitted to compiled data are not independent raw measurements; fit error relative to data is not measurement uncertainty.
- No verified complete bulk export or homogeneous release version; retrievable numerical tables are HTML, and individual material/property coverage varies.
- The regenerator link returns spreadsheet-style HTML, not a verified standalone XLS/CSV file.
- Index links and sampled data tables were verified; an exhaustive material, coefficient or measurement count was not established.
- Respect each material, temper, orientation and equation-validity range; do not extrapolate fits beyond their stated ranges.
- Public access does not establish an open redistribution license.

**Tags:** Data.gov attachment ranks 40, 41, 44, cryogenic, property correlations, fit ranges, Data.gov-selection-20261101.

<a id="nist-structural-ceramics-srd30"></a>
## NIST Structural Ceramics Database (SRD 30)

Literature-derived ceramic property tables linked to processing, composition, measurement methods, evaluation status and bibliography.

**Size:** Unranked material/property records (source wording: Not verified).

**Scope:** Public collection; total record count not verified

**Release:** Live Ceramics Data Portal; data content last updated 2002. **Year:** 2002.

**Provenance:** experimental literature compilation. **Structure availability:** `composition_only`.

**Labels/content:** thermal properties; mechanical properties; density; grain size; processing; measurement uncertainty.

**Access:** open. **Dataset license:** Database states copyright U.S. Department of Commerce, all rights reserved; no open data redistribution license verified; data redistribution rights not verified.

**Official routes:** [homepage](https://srdata.nist.gov/CeramicDataPortal/scd) · [doi](https://doi.org/10.18434/T4F30D) · [example](https://srdata.nist.gov/CeramicDataPortal/Scd/Y00001)

**Evidence:**

- [WebSCD database and evaluation criteria](https://srdata.nist.gov/CeramicDataPortal/scd) (checked 2026-11-01): Public search page identifies last data update 2002, ceramic families and evaluation criteria; it documents processing/composition and bibliography support.
- [SCD citation Y00001 numerical record](https://srdata.nist.gov/CeramicDataPortal/Scd/Y00001) (checked 2026-11-01): Live HTML record contains corundum heat-capacity values with K and J kg−1 K−1 units, value uncertainties, calorimetry methods, processing notes, source citation and property-specific evaluation labels.
- [Current structural-ceramics search results](https://srdata.nist.gov/CeramicDataPortal/Scd/DoSearch) (checked 2026-11-01): Unfiltered search returns a linked citation index. Repeated citations can represent different materials; row or citation totals are not a unique-material count.

**Reuse and interpretation notes:**

- No verified complete structured bulk export or dataset cardinality; numerical per-citation HTML tables are publicly retrievable.
- Evaluation labels are property-specific: the sampled record marks heat capacity evaluated and grain size unevaluated. Do not label all values validated.
- Legacy data content last updated 2002; catalog/site timestamps do not indicate new measurements.
- Contains literature data and may overlap NIST Property Data Summaries and other compilations.
- Public access does not establish an open redistribution license.

**Tags:** Data.gov attachment ranks 195, 197, ceramics, evaluated literature, processing conditions, Data.gov-selection-20261101.

<a id="nist-rp-chemical-pressure-dielectrics"></a>
## NIST targeted-chemical-pressure Ruddlesden–Popper dielectric data

Experimental XRD and frequency-, temperature- and field-dependent dielectric curves for Ba-containing titanate superlattices, accompanied by computed crystal models.

**Size:** Unranked material samples (source wording: Not verified).

**Scope:** Distinct sample count was not established; verified release contains nine CSV tables and nine CIF models. Do not convert curve rows into independent materials.

**Release:** NIST M31968 / mds10xz9qd v1.0.2;2019 study. **Year:** 2019.

**Provenance:** mixed. **Structure availability:** `mixed`.

**Labels/content:** XRD intensity versus2theta; dielectric constant versus temperature; complex permittivity versus frequency; dielectric tunability versus DC field; loss tangent; figure of merit; DFT energy versus ionic distortion; DFT CIF models.

**Access:** open. **Dataset license:** NIST dataset-use permission explicitly stated in README; article-content reuse separately refers to publisher terms.

**Official routes:** [homepage](https://data.nist.gov/od/id/7619E70B50E70FE5E05324570681A1921968) · [data](https://doi.org/10.18434/M31968) · [paper](https://doi.org/10.1038/s41563-019-0564-4)

Other denominators (not added to the ranking):

- 9 computed CIF models: Downloaded TGZ inventory; not experimental sample count
- 9 CSV figure-data tables: Release payload inventory

**Evidence:**

- [NIST primary release metadata](https://data.nist.gov/od/id/7619E70B50E70FE5E05324570681A1921968) (checked 2026-11-01): Current version1.0.2 links nine CSV tables and CIF TGZ plus README; inspected archive contains9 CIFs(PE/FE variants for n2–6; n2_FE absent).
- [Dataset README, schema and rights](https://data.nist.gov/od/ds/7619E70B50E70FE5E05324570681A1921968/README.txt) (checked 2026-11-01): Provides variable-by-variable units/conditions: XRD degrees/counts; temperature K; frequency Hz; field kV/cm; film thickness and n. Dataset permission includes modification/distribution with acknowledgement and change notice; calibration details are delegated to the article methods.

**Reuse and interpretation notes:**

- Narrow engineered thin-film series; preserve layer number, film thickness, substrate/strain, temperature, frequency and applied field when comparing values.
- CIFs and DFT distortion-energy curves are computed models; measured dielectric curves are a separate provenance layer.
- Nine files or nine computed structures do not establish nine independently measured materials.
- README delegates calibration to article methods; a complete measurement uncertainty budget was not independently reconstructed.
- CSV tables include multi-curve columns and blanks; preserve column-specific units and avoid treating every cell as an independent sample.

**Tags:** Data.gov-selection-20261101, verified-2026-11-01, specialist-experimental-data.

<a id="nist-trc-alloy"></a>
## NIST TRC Alloy Data

Experimental thermophysical properties of unary, binary and ternary metallic systems with original-publication provenance and uncertainty.

**Size:** Unranked experimental property records (source wording: Unranked).

**Scope:** Full collection size not verified; no estimate assigned.

**Release:** Provider/API snapshot, checked 2026-11-01. **Year:** Not verified.

**Provenance:** experimental literature. **Structure availability:** `composition_only`.

**Labels/content:** thermophysical properties; thermochemical properties; composition and measurement conditions; uncertainty.

**Access:** mixed. **Dataset license:** Not verified; inspect collection and original-source terms before redistribution.

**Official routes:** [homepage](https://trc.nist.gov/MetalsAlloyUI/) · [documentation](https://www.nist.gov/mgi/materials-data-resources)

**Evidence:**

- [NIST TRC Alloy Data provider documentation](https://www.nist.gov/mgi/materials-data-resources) (checked 2026-11-01): Experimental thermophysical properties of unary, binary and ternary metallic systems with original-publication provenance and uncertainty.
- [NIST TRC Alloy Data · API access by request documentation](https://www.nist.gov/mgi/materials-data-resources) (checked 2026-11-01): Provider explicitly states API access is available upon request. This is the access-information page, not a callable API endpoint; no data API tested.

**Reuse and interpretation notes:**

- Database/provider snapshot checked 2026-11-01; overlapping records and releases must not be summed as unique materials.
- Public availability is distinct from reuse permissions; per-record provenance and rights may differ.
- No defensible full-collection size verified; deliberately unranked.

**Tags:** Repository-coverage-20261101, nist-trc-alloy, NIST TRC Alloy Data.

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

<a id="self-cleaning-coating-literature"></a>
## Self-cleaning coating material and property corpora

Text-mined coating-material dictionaries, property-value groups and stability/durability sentiment statistics.

**Size:** Unranked material/property/source group records (source wording: Not verified).

**Scope:** Release includes 38 JSON tables from a 39,011-paper corpus. Tables cover six overlapping function/property corpora, material dictionaries/frequencies, grouped numerical values and sentiment summaries; no reconciled unique observation/material total is asserted.

**Release:** Figshare 23896434 v2; 38-table archive inventory. **Year:** 2024.

**Provenance:** literature. **Structure availability:** `composition_only`.

**Labels/content:** contact angle; sliding angle; refractive index; transmittance; material frequency/co-occurrence; stability/durability sentiment; source DOI.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-02983-0) · [data](https://doi.org/10.6084/m9.figshare.23896434.v2) · [repository](https://github.com/MasterAI-EAM/self-cleaning)

**Evidence:**

- [Automatically Generated Datasets: Present and Potential Self-Cleaning Coating Materials](https://www.nature.com/articles/s41597-024-02983-0) (checked 2026-11-01): Data Records describes four output formats: material statistics, dictionary, numerical self-cleaning/optical values, and stability/durability sentiment. The 39,011 figure is source-paper count.
- [Self-cleaning coating data release v2](https://api.figshare.com/v2/articles/23896434/versions/2) (checked 2026-11-01): Figshare declares CC BY 4.0. Downloaded RAR contains 38 JSON tables; inspected value tables group each numeric value with lists of DOI/material pairs.

**Reuse and interpretation notes:**

- 39,011 papers, 38 JSON files, unique numeric-value groups and individual DOI/material pairs are different units; none is promoted as a unique crystal count.
- Hydrophilic, hydrophobic, oleophobic, omniphobic, photocatalytic and self-cleaning corpora can overlap; do not sum them as independent materials.
- Material names may refer to polymers, composites, coatings or substrates; no atomic crystal structures.
- Automated value/material pairing and sentiment labels require source-context checks; sentiment is not a measured durability property.
- Article states data release omits original-text excerpts; source DOI provenance remains available.

**Tags:** Scientific-Data, device-or-engineered-material-scope, Scientific-Data-descriptor, Scientific-Data-survey-20261101.
