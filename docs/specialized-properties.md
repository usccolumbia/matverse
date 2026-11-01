# Specialized materials property datasets: an OpenAlex search

Checked 2026-11-01. **35 new dataset/release records**, plus an expanded DDSE/DigBat lineage record. The catalog now contains 524 records. This is a local research expansion, not an exhaustive census of published data.

[Search the additions](https://usccolumbia.github.io/matverse/?q=property-focused) · [Search receipt](../research/openalex_property_20261101/search_manifest.json) · [Retrieved-work ledger](../research/openalex_property_20261101/retrieved_works.json) · [Selected-paper OpenAlex checks](../research/openalex_property_20261101/selected_paper_openalex_checks.json)

## Abstract

Starting from the DDSE paper, this search examines specialized property datasets across electrochemical transport, ferroic and optical response, thermal and magnetic properties, alloy mechanics, hydrogen storage and combustion. The useful distinction is between measured properties with experimental conditions, calculated responses attached to structures, and literature records attached mainly to compositions. These populations support different tasks. Their headline counts cannot be combined into a number of independent crystals.

## Questions and scope

Which paper-backed releases complement the existing catalog? What are their counted units, property provenance and structural representations? Which access, reuse and source-lineage limits affect reuse? Isolated molecular or liquid-electrolyte collections are adjacent leads; they are not automatically promoted into the ranked crystal-materials catalog. Some retained optical and electrolyte resources contain mixed crystalline, amorphous or polymer populations, which their cards label explicitly.

## OpenAlex search and verification

The search ran **41 keyword queries and one DDSE reference/citation traversal**, yielding **1,946 returned occurrences and 1,761 distinct query-retrieved works**. Exact DOI metadata checks supplement that corpus. Queries had no year restriction; keyword runs requested up to 50 results, and DDSE traversal used a 100-result per-direction cap. No final result-list limit was applied. These caps, indexing differences and keyword selection limit recall. A retrieved work is not necessarily a dataset paper, and most retrieved works remain unreviewed leads.

OpenAlex was searched automatically with the paper-search script. Primary publisher pages, author repositories and data deposits verified promoted releases. Crossref and Semantic Scholar were not additional systematic search corpora. CNKI and Wanfang were not searched: 英文库没检索到 ≠ 没人研究过. Some supplementary OpenAlex DOI requests returned HTTP 429; those failures are preserved, with independent query and primary-source evidence retained rather than inferred IDs.

| Search run | Returned works | Recorded response |
|---|---:|---|
| experimental catalytic activity materials dataset database (search) | 50 | `research/openalex_property_20261101/core/catalytic_activity.json`; SHA-256 in receipt |
| alloy corrosion dataset database (search) | 50 | `research/openalex_property_20261101/core/corrosion.json`; SHA-256 in receipt |
| A dynamic database of solid-state electrolyte DDSE picturing all-solid-state batteries (search) | 17 | `research/openalex_property_20261101/core/ddse_search.json`; SHA-256 in receipt |
| 10.1016/j.nanoms.2023.08.002 (snowball) | 124 | `research/openalex_property_20261101/core/ddse_snowball.json`; SHA-256 in receipt |
| hydrogen storage materials database dataset (search) | 50 | `research/openalex_property_20261101/core/hydrogen_storage.json`; SHA-256 in receipt |
| materials experimental property dataset database (search) | 50 | `research/openalex_property_20261101/core/property_databases.json`; SHA-256 in receipt |
| solid electrolyte ionic conductivity database (search) | 50 | `research/openalex_property_20261101/electrochem/01_solid_electrolyte.json`; SHA-256 in receipt |
| battery electrode materials property dataset (search) | 50 | `research/openalex_property_20261101/electrochem/02_battery_electrode.json`; SHA-256 in receipt |
| experimental ionic conductivity database lithium (search) | 50 | `research/openalex_property_20261101/electrochem/03_experimental_conductivity.json`; SHA-256 in receipt |
| diffusion coefficient materials dataset (search) | 50 | `research/openalex_property_20261101/electrochem/04_diffusion.json`; SHA-256 in receipt |
| diffusion database dilute solute materials (search) | 50 | `research/openalex_property_20261101/electrochem/05_solute_diffusion.json`; SHA-256 in receipt |
| battery electrolyte conductivity dataset CALiSol (search) | 10 | `research/openalex_property_20261101/electrochem/06_liquid_electrolytes.json`; SHA-256 in receipt |
| ionic migration barriers dataset (search) | 49 | `research/openalex_property_20261101/electrochem/07_migration_barriers.json`; SHA-256 in receipt |
| conductivity electrolyte formulations experiments (search) | 50 | `research/openalex_property_20261101/electrochem/08_electrolyte_experiments.json`; SHA-256 in receipt |
| solid electrolyte conductivity dataset Laskowski (search) | 50 | `research/openalex_property_20261101/electrochem/09_laskowski.json`; SHA-256 in receipt |
| experimental band gap database inorganic semiconductors (search) | 50 | `research/openalex_property_20261101/ferroic/raw/bandgap.json`; SHA-256 in receipt |
| Auto generated database semiconductor band gaps ChemDataExtractor (search) | 50 | `research/openalex_property_20261101/ferroic/raw/cde-gap-target.json`; SHA-256 in receipt |
| database refractive indices dielectric constants ChemDataExtractor (search) | 45 | `research/openalex_property_20261101/ferroic/raw/cde-optical-target.json`; SHA-256 in receipt |
| dielectric refractive index data driven dataset crystals (search) | 50 | `research/openalex_property_20261101/ferroic/raw/dielectric.json`; SHA-256 in receipt |
| automatically curated first principles database ferroelectrics (search) | 50 | `research/openalex_property_20261101/ferroic/raw/ferroelectric-target.json`; SHA-256 in receipt |
| ferroelectric database data descriptor (search) | 50 | `research/openalex_property_20261101/ferroic/raw/ferroelectric.json`; SHA-256 in receipt |
| ferroelectric piezoelectric dielectric materials dataset database (search) | 50 | `research/openalex_property_20261101/ferroic/raw/ferroic.json`; SHA-256 in receipt |
| nonlinear optical materials dataset database (search) | 50 | `research/openalex_property_20261101/ferroic/raw/nlo.json`; SHA-256 in receipt |
| database optical absorption spectra crystalline materials (search) | 50 | `research/openalex_property_20261101/ferroic/raw/optical-spectra.json`; SHA-256 in receipt |
| optical electronic crystal materials dataset refractive index (search) | 50 | `research/openalex_property_20261101/ferroic/raw/optical.json`; SHA-256 in receipt |
| Discovery wurtzite solid solutions enhanced piezoelectric response machine learning (search) | 50 | `research/openalex_property_20261101/ferroic/raw/piezo-wurtzite.json`; SHA-256 in receipt |
| Second harmonic generation tensors high throughput density functional perturbation (search) | 50 | `research/openalex_property_20261101/ferroic/raw/shg-target.json`; SHA-256 in receipt |
| Dataset tensorial optical transport properties Wannier function method (search) | 29 | `research/openalex_property_20261101/ferroic/raw/tensor-target.json`; SHA-256 in receipt |
| TopoHSE database (search) | 12 | `research/openalex_property_20261101/ferroic/raw/topohse.json`; SHA-256 in receipt |
| topological materials database dataset (search) | 49 | `research/openalex_property_20261101/ferroic/raw/topological.json`; SHA-256 in receipt |
| mechanical electrical properties dataset Cu Cr alloys (search) | 50 | `research/openalex_property_20261101/transport/query_cucr.json`; SHA-256 in receipt |
| thermoelectric material database self consistent (search) | 50 | `research/openalex_property_20261101/transport/query_curation.json`; SHA-256 in receipt |
| fatigue database complex metallic alloys (search) | 50 | `research/openalex_property_20261101/transport/query_fatigue.json`; SHA-256 in receipt |
| load dependent hardness dataset (search) | 49 | `research/openalex_property_20261101/transport/query_hardness.json`; SHA-256 in receipt |
| magnetic materials database dataset magnetocaloric (search) | 50 | `research/openalex_property_20261101/transport/query_magnetic.json`; SHA-256 in receipt |
| magnetocaloric autogenerated database language models (search) | 13 | `research/openalex_property_20261101/transport/query_magnetocaloric.json`; SHA-256 in receipt |
| elastic hardness database materials dataset (search) | 50 | `research/openalex_property_20261101/transport/query_mechanical.json`; SHA-256 in receipt |
| lattice thermal conductivity high throughput database (search) | 50 | `research/openalex_property_20261101/transport/query_phonon.json`; SHA-256 in receipt |
| NEMAD teMatDb ESTM Wenzhou thermoelectric (search) | 0 | `research/openalex_property_20261101/transport/query_refined.json`; SHA-256 in receipt |
| thermal conductivity database materials (search) | 50 | `research/openalex_property_20261101/transport/query_thermal.json`; SHA-256 in receipt |
| thermoelectric transport dataset database (search) | 50 | `research/openalex_property_20261101/transport/query_thermoelectric.json`; SHA-256 in receipt |
| compilation experimental mechanical microstructural titanium alloys (search) | 49 | `research/openalex_property_20261101/transport/query_ti.json`; SHA-256 in receipt |

Raw publisher bodies, dataset payloads and caches remain local and ignored by Git. The normalized work ledger, source hashes, query outcomes and perspective decisions remain available. Counts are documentation-reported unless a card explicitly identifies an independent small-file recount.

## DDSE is the earlier name of the DigBat lineage

The requested paper is now explicitly linked in [DigBat / Dynamic Database of Solid-State Electrolytes](catalog/experimental_properties.md#digbat). The original DDSE, DDSE 2.0 and DigBat are stages of one growing platform. The current catalog rank retains the June 2026 experimental-material count; earlier snapshots and measurement counts are additional denominators, not separate additive corpora.

| Snapshot | Experimental materials | Experimental observations | Separate computational module | Evidence |
|---|---:|---:|---|---|
| Original DDSE, online 2023 / 2024 issue | 678 | Not substituted for material count | Not asserted from this source | [Original paper](https://doi.org/10.1016/j.nanoms.2023.08.002) |
| DDSE 2.0, 23 November 2024 | 2,349 | 18,309 performance records | 601 materials / 802 performance records | [Technical report](https://www.techscience.com/cmc/v81n3/59074/html) |
| DigBat, June 2026 | 3,816 | 27,645 conductivity entries | 852 materials | [Provider announcement](https://www.tohoku.ac.jp/en/press/digbat_an_ai_ready_digital_platform_for_solid_state_battery_research.html) |

The computational module supports structural visualization and VASP-format downloads, whereas experimental conductivity records carry temperature and sample context. Full experimental structure coverage and a bulk data redistribution license were not established for the platform.

## Verified additions, grouped by catalog category

Sizes descend within each existing category. Null sizes remain unranked. Each linked card provides count evidence, source release, access, rights, label conditions and overlap notes.

| Dataset / release | Reported volume | Counted unit | Structure availability | Property provenance |
|---|---:|---|---|---|
| [ChemDataExtractor refractive-index and dielectric database](catalog/experimental_properties.md#cde-refractive-dielectric-2022) | 109,880 | optical/dielectric literature records | composition_only | experimental |
| [ChemDataExtractor semiconductor band-gap database](catalog/experimental_properties.md#cde-bandgaps-2022) | 100,236 | band-gap literature records | composition_only | experimental |
| [Northeast Materials Database (NEMAD) — magnetic materials](catalog/experimental_properties.md#nemad-magnetic) | 67,573 | magnetic-material entries | composition_only | experimental |
| [IPOP inorganic phosphor optical-property dataset](catalog/experimental_properties.md#ipop-v3) | 16,023 | property observations | composition_only | experimental |
| [NEMAD / GPTArticleExtractor thermoelectric database](catalog/experimental_properties.md#nemad-thermoelectric) | 7,123 | thermoelectric compound entries | composition_only | mixed |
| [LLM-extracted magnetocaloric materials database (Yuan–Yang–Patra–Liao)](catalog/experimental_properties.md#mce-llm-2024) | 6,614 | literature-extracted material-property rows | composition_only | literature_extracted_mixed |
| [ESTM experimentally synthesized thermoelectric materials](catalog/experimental_properties.md#estm-simd) | 5,205 | composition-temperature observations | composition_only | experimental |
| [Shon–Min text-mined ionic conductivity database](catalog/experimental_properties.md#shon-ionic-conductivity-2023) | 4,924 extracted records from 1,457 papers | text-extracted conductivity records | composition_only | literature |
| [Refractiveindex.info optical constants](catalog/experimental_properties.md#refractiveindex-info) | 3,328 | published optical data records | mixed | mixed |
| [Cu-Cr-X mechanical and electrical property dataset](catalog/experimental_properties.md#cu-cr-x-figure-extraction) | 3,018 | alloy composition-processing-property records | composition_only | experimental |
| [polyVERSE load-dependent experimental Vickers hardness](catalog/experimental_properties.md#polyverse-load-hardness) | 2,480 | composition-load hardness observations | composition_only | experimental |
| [Copper-alloy mechanical properties and electrical conductivity (Gorsse 2023)](catalog/experimental_properties.md#cu-alloys-mechanical-2023) | 1,831 | composition-processing-property-reference records | composition_only | experimental |
| [EKHI optical and thermal radiative properties](catalog/experimental_properties.md#ekhi-radiative-2026) | 1,251 | experimental property curves | composition_only | experimental |
| [Liverpool Ionics Dataset](catalog/experimental_properties.md#liverpool-ionics) | 820 measurements; 403 unique near-room-temperature compositions | conductivity-at-temperature records | composition_only | literature |
| [ML-HydPARK metal-hydride storage properties](catalog/experimental_properties.md#ml-hydpark) | 772 | composition/property records | composition_only | literature |
| [Metallic-material combustion property database](catalog/experimental_properties.md#metal-combustion-properties) | 725 | combustion measurement records | composition_only | literature |
| [OBELiX experimental solid electrolyte conductivity](catalog/experimental_properties.md#obelix) | 599 experimental entries; 321 with CIF files | experimental electrolyte entries | mixed | literature |
| [Caltech experimental Li-ion structure–conductivity database](catalog/experimental_properties.md#caltech-li-conductivity-571) | 571 experimental Li-containing compounds | experimental structure-conductivity entries | structure_linked | literature |
| [DAX-Ti experimental Ti-alloy mechanical-property compilation](catalog/experimental_properties.md#dax-ti-experimental) | 282 | alloy entries | composition_only | experimental |
| [FatigueData-CMA2022 complex metallic-alloy fatigue database](catalog/experimental_properties.md#fatiguedata-cma2022) | 272 | fatigue test-condition datasets | composition_only | experimental |
| [teMatDb272 thermoelectric material database](catalog/experimental_properties.md#tematdb272) | 272 | curated thermoelectric sample curve sets | composition_only | experimental |
| [Polyanion sodium cathode atomic structure and dynamics](catalog/mlip_configurations.md#polyanion-sodium-cathode-2025) | 298,144 configurations; 113,532 with atomic charges | periodic atomic configurations | periodic_atomic | computed |
| [Fang Wannier optical and transport tensors](catalog/property_benchmarks.md#fang-wannier-optical-transport-2025) | 7,301 | material entries | periodic_atomic | computed |
| [WenzhouTE computed thermoelectric database](catalog/property_benchmarks.md#wenzhou-te) | 3,607 | calculated materials | structure_linked | computed |
| [Ternary fluoride-ion battery electrode reaction pairs](catalog/property_benchmarks.md#ternary-fluoride-electrode-pairs) | 807 reaction pairs; overlapping 168 direct-reaction subset | fluorinated/defluorinated reaction pairs | structure_linked | computed |
| [Literature-derived battery ionic migration barriers](catalog/property_benchmarks.md#migration-barriers-literature-2025) | 621 archived migration-barrier entries | ionic migration pathways | periodic_atomic | computed |
| [Trinquet nonlinear-optical SHG tensor dataset](catalog/property_benchmarks.md#trinquet-shg-2024) | 579 | inorganic semiconductor structures | periodic_atomic | computed |
| [Ricci polar-material ferroelectric screening dataset](catalog/property_benchmarks.md#ricci-polar-ferroelectrics-2024) | 447 | polar materials with computed polarization | structure_linked | computed |
| [UW CMG dilute-solute diffusion database](catalog/property_benchmarks.md#uw-cmg-dilute-solute-diffusion) | more than 400 host–solute systems | host-solute diffusion systems | structure_linked | computed |
| [Smidt first-principles ferroelectric candidate database](catalog/property_benchmarks.md#smidt-ferroelectric-2020) | 255 | completed polar–nonpolar structure pairs | periodic_atomic | computed |
| [HH130 half-Heusler thermal-transport / MLIP release](catalog/property_benchmarks.md#hh130-mathub) | 130 | half-Heusler compounds | periodic_atomic | computed |
| [Oxygen migration barriers in perovskites](catalog/property_benchmarks.md#oxygen-migration-perovskites-2016) | over 40 perovskites | perovskite systems | structure_linked | computed |
| [Materials Cloud fast Li-ion conductor screening](catalog/property_benchmarks.md#materialscloud-fast-li-ion-conductors) | ~60 shortlisted FPMD candidates described; exact released structure/trajectory count not recounted | released crystal systems / trajectories | periodic_atomic | computed |
| [TopoHSE-DB](catalog/property_benchmarks.md#topohse-db) | Not verified | classified crystalline-material entries | structure_linked | computed |
| [Wurtzite solid-solution PiezoML data](catalog/property_benchmarks.md#wurtzite-piezoml-dryad) | Not verified | candidate/DFT calculation records | periodic_atomic | computed |

## What changes across property families

**Electrochemical transport.** [OBELiX experimental solid electrolyte conductivity](catalog/experimental_properties.md#obelix) links 321 CIFs to a larger 599-material experimental cohort; [Liverpool Ionics Dataset](catalog/experimental_properties.md#liverpool-ionics) counts 820 conductivity-at-temperature measurements rather than 820 unique compositions. DDSE/DigBat spans several ion and material classes, while these releases support narrower lithium-conductor studies. Measurement temperature, sample processing and label provenance must remain available when joining them.

The [Literature-derived battery ionic migration barriers](catalog/property_benchmarks.md#migration-barriers-literature-2025) archive counts pathways, whereas [Polyanion sodium cathode atomic structure and dynamics](catalog/mlip_configurations.md#polyanion-sodium-cathode-2025) counts atomistic configurations. Their 621 pathways and 298,144 frames do not represent the same sampling unit. The 619-record live migration repository and 621-record archived release are explicitly distinguished. The larger sodium cohort has charge labels for only a subset of its frames.

**Ferroic and optical response.** [Smidt first-principles ferroelectric candidate database](catalog/property_benchmarks.md#smidt-ferroelectric-2020) contains completed polar/nonpolar structure workflows; [Ricci polar-material ferroelectric screening dataset](catalog/property_benchmarks.md#ricci-polar-ferroelectrics-2024) reports a polarization-calculated cohort and smaller screening subsets. These are computed candidates, not experimentally demonstrated switching events. [Trinquet nonlinear-optical SHG tensor dataset](catalog/property_benchmarks.md#trinquet-shg-2024) provides static nonlinear-response tensors, whereas [Fang Wannier optical and transport tensors](catalog/property_benchmarks.md#fang-wannier-optical-transport-2025) includes frequency/temperature-dependent electronic responses with model assumptions stated in its card.

Large literature tables such as [ChemDataExtractor semiconductor band-gap database](catalog/experimental_properties.md#cde-bandgaps-2022) and [ChemDataExtractor refractive-index and dielectric database](catalog/experimental_properties.md#cde-refractive-dielectric-2022) count records, not unique structure determinations. [IPOP inorganic phosphor optical-property dataset](catalog/experimental_properties.md#ipop-v3) preserves host/dopant and luminescence observations; [EKHI optical and thermal radiative properties](catalog/experimental_properties.md#ekhi-radiative-2026) counts experimental curves. These collections need material-state and measurement-condition filtering before comparison with crystal-specific computed labels.

**Thermal and magnetic properties.** [teMatDb272 thermoelectric material database](catalog/experimental_properties.md#tematdb272) preserves sample curve sets, while [ESTM experimentally synthesized thermoelectric materials](catalog/experimental_properties.md#estm-simd) counts composition-temperature observations. [WenzhouTE computed thermoelectric database](catalog/property_benchmarks.md#wenzhou-te) is a computed database, and [NEMAD / GPTArticleExtractor thermoelectric database](catalog/experimental_properties.md#nemad-thermoelectric) mixes experimental and theoretical source records. Electronic-only thermal conductivity or fixed-relaxation-time transport must not be interpreted as total measured thermal conductivity.

[Northeast Materials Database (NEMAD) — magnetic materials](catalog/experimental_properties.md#nemad-magnetic) and [LLM-extracted magnetocaloric materials database (Yuan–Yang–Patra–Liao)](catalog/experimental_properties.md#mce-llm-2024) address different magnetic observables and extraction pipelines. Their records can overlap older literature collections. The magnetocaloric release documents a paper-versus-current-file count discrepancy; extracted rows, corrected subsets and unique materials remain separate denominators.

**Mechanical, storage and reactivity measurements.** [FatigueData-CMA2022 complex metallic-alloy fatigue database](catalog/experimental_properties.md#fatiguedata-cma2022) counts test-condition datasets, whereas [Copper-alloy mechanical properties and electrical conductivity (Gorsse 2023)](catalog/experimental_properties.md#cu-alloys-mechanical-2023) counts processing/property/reference records. [polyVERSE load-dependent experimental Vickers hardness](catalog/experimental_properties.md#polyverse-load-hardness) requires load-aware interpretation and carries custom reuse terms. Composition alone does not encode microstructure, specimen preparation or loading conditions.

[ML-HydPARK metal-hydride storage properties](catalog/experimental_properties.md#ml-hydpark) provides hydride storage and thermodynamic rows; [Metallic-material combustion property database](catalog/experimental_properties.md#metal-combustion-properties) records alloy combustion measurements. Both are composition-level collections with experimental conditions and some derived quantities; neither supplies a new collection of atom-resolved crystal structures.

## Coverage limits and unresolved checks

Three newly included releases retain unknown sizes: TopoHSE-DB classifications, the PiezoML wurtzite archive and the Materials Cloud fast-lithium-conductor trajectory release. Their existence and data routes were verified without turning screened-candidate totals or archive byte sizes into labeled-record counts. Other deferred leads, including pure liquid-electrolyte datasets and releases with unresolved bulk access, remain in the perspective ledgers.

A public page is distinct from a successfully downloaded payload, and article licensing is distinct from an external dataset license. Unknown rights remain explicit. HH130 download availability was not established after an HTTP 502 response. The NEMAD processed archive and full website have separately assessed rights. Source snapshots remain essential because repositories and papers can have different counts.

## Evidence and candidate decisions

- [Electrochemical search and primary-source notes](../research/openalex_property_20261101/electrochem/notes.md)
- [Ferroic/optical search and primary-source notes](../research/openalex_property_20261101/ferroic/notes.md)
- [Thermal/magnetic/mechanical search and primary-source notes](../research/openalex_property_20261101/transport/notes.md)
- [Electrochemical candidate ledger](../research/openalex_property_20261101/electrochem/leads.json)
- [Ferroic candidate ledger](../research/openalex_property_20261101/ferroic/leads.json)
- [Thermal/mechanical candidate ledger](../research/openalex_property_20261101/transport/leads.json)
- [Selected evidence and query entrypoints in source search](https://usccolumbia.github.io/matverse/?view=sources&collection=openalex_properties_20261101)

The search identifies concrete complementary releases, but not a complete registry of every specialized property. Material/measurement distinction, method provenance and versioned rights determine which records can be joined; headline volume alone does not establish suitability for a scientific task.

[Back to MatVerse](../README.md)
