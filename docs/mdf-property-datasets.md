# Property datasets discovered through Materials Data Facility

Checked 2026-11-01. **Eight new structured property cohorts** were selected from **244 distinct public deposit subjects** returned by ten property searches. The full catalog now contains 524 dataset/release records.

[MDF homepage](https://www.materialsdatafacility.org/) · [Search MDF](https://www.materialsdatafacility.org/search) · [Foundry-ML](https://foundry-ml.org/) · [Search these MatVerse additions](https://usccolumbia.github.io/matverse/?q=MDF-property-20261101)

## Selection criteria and evidence limits

Selection required crystal-related property content, a stable deposit DOI/source ID, an explicit Foundry record count, declared input/target fields and units, and an explicit dataset rights statement. All eight selected metadata records declare CC BY 4.0. These are positive documentation and reuse signals; they do not independently certify numerical accuracy, complete labels or unbiased sampling.

The public metadata subject endpoints returned HTTP 200 without credentials. Counts below are the provider’s `projects.foundry.n_items`, not independent payload row counts or unique-crystal counts. Split/file paths and schemas were inspected; full file transfer and Foundry loading were not attempted. The documented data route uses Globus/Foundry and may require account authorization. Public metadata access and full payload access remain separate.

[Selected metadata and schemas](../research/mdf_selected_metadata_20261101.json) · [Subject response receipts](../research/mdf_selected_subject_receipts_20261101.json) · [Query receipts](../research/mdf_property_search_20261101.json)

## Selected releases

| Release | Declared records | Counted unit | Structure availability |
|---|---:|---|---|
| [Foundry assorted computational band-gap cohort](catalog/property_benchmarks.md#mdf-assorted-computed-band-gaps) | 105,594 | computed band-gap records | mixed |
| [Foundry Wolverton oxide perovskite stability and vacancies](catalog/property_benchmarks.md#mdf-wolverton-oxides) | 4,914 | oxide perovskite records | composition_only |
| [Foundry perovskite O p-band centers](catalog/property_benchmarks.md#mdf-perovskite-opband) | 2,912 | perovskite composition records | composition_only |
| [Foundry semiconductor impurity charge-state transitions](catalog/property_benchmarks.md#mdf-semiconductor-defectlevels) | 2,910 | semiconductor-impurity records | composition_only |
| [Foundry experimental band-gap structure cohort](catalog/experimental_properties.md#mdf-experimental-band-gaps) | 2,808 | experimental band-gap records | mixed |
| [Foundry double-perovskite oxide band gaps](catalog/property_benchmarks.md#mdf-double-perovskite-bandgaps) | 1,306 | double-perovskite composition records | composition_only |
| [Foundry / University of Alabama Heusler magnetization](catalog/property_benchmarks.md#mdf-heusler-magnetization) | 1,153 | Heusler compound records | composition_only |
| [Foundry steel composition and mechanical properties](catalog/experimental_properties.md#mdf-steel-strength) | 312 | steel composition/property records | composition_only |

The two band-gap JSON cohorts declare structure fields, but coordinate completeness was not audited. The other tables provide composition, sublattice, site, prototype or lattice descriptors; complete atomic coordinates are not established for those releases.

Band-gap records include experimental measurement conditions or calculated functional labels. Experimental and calculated targets must remain distinguishable. Defect records describe host–impurity/site/charge combinations, not 2,910 different semiconductor host structures. The Heusler table distinguishes magnetic moments in Bohr magnetons from saturation magnetization in emu/cc. O p-band centers are referenced to the Fermi level and separate GGA from GGA+U. Steel composition tables alone do not encode all processing and microstructure factors that affect strength. The linked cards retain these limits and the full source endpoints.

## File/schema evidence

| MDF source ID | Declared split file | Input / target field count |
|---|---|---:|
| `foundry_experimental_band_gaps_v1.1` | `data_exp_no_repeat_new.json` | 10 |
| `foundry_assorted_computational_band_gaps_v1.1` | `All_no_MP_Aflow_OQMD_new.json` | 9 |
| `double_perovskite_bandgap_v1.1` | `Dataset_double_perovskites_gap_v1.csv` | 6 |
| `perovskite_opbandcenter_v1.1` | `Perovskite_Opband_dataset_v1.csv` | 4 |
| `heusler_magnetization_v1.1` | `Dataset_heusler_magnetic_v1.csv` | 10 |
| `semiconductor_defectlevels_v1.1` | `Dataset_semiconductor_defectlevels_v1.csv` | 37 |
| `wolverton_oxides_v1.1` | `Dataset_wolverton_oxides_v1.csv` | 16 |
| `steel_strength_v1.1` | `Dataset_steel_strength.csv` | 18 |

Field counts are schema descriptors, not material counts. Different target columns may have different coverage. The schema snapshots preserve their field names, descriptions and units.

## Search coverage

The supplied MDF search page uses the public Globus Search index `1a57bbe5-5272-477f-9d31-343b8258b7a5`. Its read-only query contract was inspected in the page’s published client code. Each query restricted results to `mdf.resource_type:dataset`, requested at most 100 results, and returned every matching subject because each reported total was below that cap. Queries can overlap. This is a ten-query property search, not an inventory of all MDF deposits.

| Property query | Returned / matching deposit subjects |
|---|---:|
| elastic | 16 / 16 |
| thermal | 37 / 37 |
| band | 30 / 30 |
| dielectric | 17 / 17 |
| mechanical | 56 / 56 |
| diffusion | 88 / 88 |
| thermoelectric | 5 / 5 |
| magnetic | 31 / 31 |
| piezoelectric | 3 / 3 |
| photovoltaic | 2 / 2 |

All 244 distinct returned subjects are retained as discovery entries, including adjacent or uncertain resources. Their presence does not verify the quality, count, licensing or crystal-coordinate content of every deposit. [Candidate ledger](../research/mdf_property_candidates_20261101.json) · [Search inventory](../research/collection_mdf_properties_20261101.json).

## Existing-source mirrors and deferred leads

MDF’s 1,181-entry elastic-tensor, 1,056-entry dielectric and 941-entry piezoelectric cohorts map to existing Materials Project releases. The 408-entry diffusion cohort maps to the existing educational/source lineage. These were not added as independent new corpora. Separate MP, OQMD and AFLOW band-gap mirrors also overlap parent databases; provider metadata rights should be reconciled with upstream terms before reuse, especially where terms differ.

The Systematically Verified Thermoelectric dataset, Robert Freer thermoelectric tables, thermal-expansion cohorts and experimental thermal-conductivity deposits remain useful follow-up leads. They were not all promoted in this pass: complete size, rights or payload checks remain unresolved for some. Their metadata routes are preserved in the candidate/source inventory.

## Programmatic follow-up

The official [Foundry client](https://github.com/MLMI2-CSSI/foundry) supports searching, schema inspection and dataset loading. Start from a deposit DOI, review its schema and access requirements, then load a small sample before scaling. Store the MDF source ID, DOI, file version and property units with the data. SDK licensing does not replace each deposit’s dataset license.

[Materials dataset search tools](../sources.md#materials-dataset-search-tools) · [Back to MatVerse](../README.md)
