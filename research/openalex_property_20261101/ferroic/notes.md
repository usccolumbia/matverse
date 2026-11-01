# Ferroic, optical and electronic property search — 2026-11-01

## Research brief and decision rule

RQ1: Which released crystal-relevant ferroic, dielectric, optical and topological datasets are missing from the existing 171-record MatVerse catalog? RQ2: What exactly is counted and what structural representation and conditions accompany each release? RQ3: Are the data themselves available and what license governs them?

This is a local integration proposal: no canonical catalog, generated UI, scripts, Git state, or external service was edited. `additions.json` contains 11 complete proposed catalog records, validated together with the existing catalog by its current validation function. `leads.json` preserves the queried works and dispositions. Raw scholarly responses, publisher/deposit HTML and extracted text, Figshare API metadata and direct OpenAlex DOI metadata are retained in `raw/`; `raw_manifest.json` records SHA-256 and byte counts.

## Coverage

The required actual paper-search script was run with `--sources openalex --per-source 50 --query ...` and no final `--limit`. The default cache path failed due to sandbox restrictions; subsequent successful queries set `PAPER_CACHE_DIR=/private/tmp/matverse-ferroic-cache`. All search responses report network_status=ok. Script results are sorted newest-first, so a 50-result query is a bounded sample, not an exhaustive census. Broad searches were supplemented with named-release searches and primary DOI/deposit verification. Search perspectives covered ferroic screening, optical spectra/constants, nonlinear response, semiconductor gaps, and topological classifications.

| Query | Returned | Raw response |
|---|---:|---|
| experimental band gap database inorganic semiconductors | 50 | raw/bandgap.json |
| Auto generated database semiconductor band gaps ChemDataExtractor | 50 | raw/cde-gap-target.json |
| database refractive indices dielectric constants ChemDataExtractor | 45 | raw/cde-optical-target.json |
| dielectric refractive index data driven dataset crystals | 50 | raw/dielectric.json |
| automatically curated first principles database ferroelectrics | 50 | raw/ferroelectric-target.json |
| ferroelectric database data descriptor | 50 | raw/ferroelectric.json |
| ferroelectric piezoelectric dielectric materials dataset database | 50 | raw/ferroic.json |
| nonlinear optical materials dataset database | 50 | raw/nlo.json |
| database optical absorption spectra crystalline materials | 50 | raw/optical-spectra.json |
| optical electronic crystal materials dataset refractive index | 50 | raw/optical.json |
| Discovery wurtzite solid solutions enhanced piezoelectric response machine learning | 50 | raw/piezo-wurtzite.json |
| Second harmonic generation tensors high throughput density functional perturbation | 50 | raw/shg-target.json |
| Dataset tensorial optical transport properties Wannier function method | 29 | raw/tensor-target.json |
| TopoHSE database | 12 | raw/topohse.json |
| topological materials database dataset | 49 | raw/topological.json |

## Included release comparisons and exact denominator safeguards

| Release | Counted unit | Structural evidence and distinction |
|---|---:|---|
| Smidt ferroelectrics | 255 completed polar/nonpolar workflow pairs | Atomic structures and VASP archives; 200 higher-quality and 126 newly proposed are subsets. Not a count of experimentally switched ferroelectrics. |
| Ricci polar ferroelectrics | 447 computed polarization materials | Supplementary tables linked to MP; 1,978 is initial screening and 182 is the ranked potential-ferroelectric subset. API availability was promised by the paper and was not verified here. |
| Trinquet SHG | 579 semiconductors | Full static SHG and electronic dielectric tensors, JSON and Structure API route; multiple mirrors represent one release. |
| Fang Wannier | 7,301 materials | Per-material structures and optical/transport tensors; constant 10 fs relaxation time, undoped Fermi level, 100–1000 K transport, optical energies 0–2.5 eV. Thermal conductivity and zT omit lattice contribution. |
| CDE band gaps | 100,236 records | Composition/chemical-name literature corpus, not atomic structures; 21,053 unique chemical names and 7,656 imported BandgapDB records. |
| CDE optical | 109,880 records | 49,076 refractive-index and 60,804 dielectric records; 11,054 chemicals is a different denominator. |
| refractiveindex.info | 3,328 records in Dec. 2023 snapshot | 3,135 linear and 193 nonlinear records; 605/89 material counts may overlap. Contains crystalline, amorphous and fluid systems; no crystal-only count verified. |
| TopoHSE-DB | null | Published HSE06 classification study and RODARE trace_files.zip verified. Exact classification count and atomic coordinate archive not audited. |
| Wurtzite PiezoML | null | Dryad README describes relaxed structures and explicit finite-strain e33 data; >3,000 generated, ~500 proxy-screened, 30 selected and 11 enhanced predictions are distinct stages, not a single verified label count. |
| IPOP v3 | 16,023 observations | 3,952 host/dopant combinations and 2,238 hosts, 553 papers; composition and measurement conditions, no atomistic coordinates. |
| EKHI | 1,251 curves | 18,999 values, 171 solids, 167 original sources; not necessarily all crystalline and includes coatings. |

Smidt searches existing polar/nonpolar structural relationships whereas Ricci generates nonpolar references with pseudosymmetry; their counts cannot be added as independent crystals. SHG is static electronic second-order response whereas Fang provides frequency-dependent conductivity/shift-current and electronic transport. CDE records and optical-constant curves preserve experimental context but cannot identify arbitrary crystal polymorphs from composition alone. TopoHSE uses hybrid-functional classifications and differs methodologically from the existing semilocal/TQC catalog, while crystal populations can still overlap.

The five broad experimental/optical resources (CDE gap, CDE refractive/dielectric, refractiveindex.info, IPOP and EKHI) are explicitly composition-only or mixed. They are useful property navigation resources but must be filtered when downstream work requires crystalline specimens or atomic structures. `mixed` for refractiveindex.info does not claim that coordinate structures are bundled.

## License and access verification

Figshare metadata, rather than journal article licenses, supports the data licenses: Smidt CC BY 4.0; Fang CC BY 4.0 despite its separate article CC BY-NC-ND license; CDE gaps MIT; CDE optical CC BY 4.0; IPOP CC BY 4.0. Materials Cloud declares SHG CC BY 4.0. RODARE declares TopoHSE CC BY 2.0. Dryad terms specify CC0 for data; licenses for bundled code still need separate checking. The refractiveindex.info database repository explicitly declares CC0. Ricci is available in article/supplementary tables under the article’s CC BY 4.0 terms. EKHI’s primary data-description section explicitly identifies the deposited data as CC BY 4.0.

No statement of web accessibility is a claim that every bulk archive was downloaded. Deposit metadata and file listings were verified; the 143.7 MB TopoHSE archive, 548 MB PiezoML archive and Fang data archive were not bulk-downloaded. Unknown counts remain null.

## Existing records and remaining leads

Existing MP piezoelectric, MP dielectric, Matbench dielectric, C2DB, SNUMAT, OMDB, TQC, JARVIS and MP transport records were not re-added. The exact-DOI matching in `leads.json` marks known catalog releases as existing when a DOI route is present in canonical source URLs. Unverified search hits remain `lead`; this is not a recommendation to promote them. In particular, the Xie 2,354-structure NLO database, high-throughput absorption-spectrum workflow, AI4NLO, PTST and topological phonon catalog merit further deposit and scope checks. OpenAlex peer-review response/decision-letter records are retained as leads for provenance but are not dataset candidates.

A useful follow-up is direct table/archive inspection of Ricci and TopoHSE, followed by a crystal-only subset audit for broad optical resources. OpenAlex search itself does not prove a release exists or supply a data license. Exact DOI lookups supplement the search responses with OpenAlex IDs for promoted works; other works can retain null OpenAlex IDs because the required search wrapper omits them.
