# Four-descriptor final title audit

Completed 2026-11-01. Four distinct records are staged in `final_audit_additions.json`; dispositions and retrieval receipts are separate. The earlier 25-record `additions.json` was preserved unchanged, verified against its prior SHA-256 receipt. No canonical catalog, UI, source script or Git changes were made.

| Descriptor | Staged counting unit | Access / data rights | Scope and principal limit |
|---|---|---|---|
| DL-ADD atomic defects, 2023 | 105 original benchmark STM images: 70 MoS2 training +20 MoS2 test +15 WS2 transfer-test | Public OSF project and data folders; associated project license independently resolved to CC BY 4.0 | Experimental image benchmark, not105 crystals or resolved atomic-coordinate records. Augmented crops/transforms excluded from count. |
| 304L full-field DIC +IR, 2024 | Independent test-record count unknown (`null`); seven geometry designs recorded separately | Figshare+v1, CC0 | Repeated tests, orientations, rates and thermal conditions in one rolled-steel lot. Spatial/temporal measurements and specimen geometry are not atomic positions. |
| Hawaiian iron-oxide grains, 2018 | 23 component datasets in the PANGAEA publication series | Public PANGAEA series, CC BY 3.0 | Inclusion is justified by directly correlated grain chemistry, EBSD orientations/phases and MFM domains; geographical provenance does not make this a generic geospatial survey. Exact fully characterized grain count remains unverified. |
| AISI52100 rolling-contact fatigue, 2026 | 63 four-ball trials;1,140 microscopy images counted separately | Mendeley v3, CC BY 4.0 | Material-response/tribology benchmark with one steel grade and three greases; one lifetime per trial, not independent times for each of three lower balls. |

All four paper DOIs matched the parent's full journal metadata and all four records passed the dataset JSON schema. Dataset licenses came from the external deposits, not from the Scientific Data article license. Raw publisher HTML and deposit/API payloads remain only under ignored `research/cache/sdata_characterization/`; compact metadata/hash receipts are in this task folder.

DL-ADD uses room-temperature constant-current STM at−1V sample bias and1nA. MoS2 and WS2 image fields are50×50nm and60×60nm, represented at256×256px. The publication evaluates90 original MoS2 images and15 WS2 images; this105-image paper cohort is the staged scope. The number of repository files, masks and augmented variants was not used as the size. Appearance-based impurity/void labels do not establish a complete chemical or atomic defect structure.

The304L resource provides raw and processed DIC/IR, force/extension/time, nominal specimen drawings, a test matrix and a supplier metallurgy report. Some specimens have back-to-back DIC systems instead of IR, and processed arrays can contain NaN. The total number of independent test records was not inferred from the200 exposed repository file entries. Retrieving the test-matrix PDF for independent recounting was unnecessary once the schema allowed an explicitly unknown count.

The iron-oxide paper studies3–6 large(~3–10µm) grains from each of11 flow/site groups. The PANGAEA series explicitly reports23 component datasets and separate grain-analysis binders. These depositor components must not be summed as grain identities; microprobe-only and fully correlative grains differ. Chemistry, orientation conventions, heating steps and analytical-quality flags must remain attached to individual grains.

Rolling-contact tests use IP300,1470rpm,5739N peak axial load and35±3°C, with21 trials per NLGI0/00/000 calcium-grease grade. Lifetimes are in seconds. Weibull quantiles/functions are derived from those trials. Optical damage images were acquired at50×total magnification(5×objective),2160×1620px. Material/lubricant/loading history controls interpretation; these results should not be treated as intrinsic crystal stability or generic bulk strength.
