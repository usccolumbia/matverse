# MateriaViva original-source mapping

Checked 2026-11-01. Mapping release: `6010a086ade47c2c99d1b2dca3a944c3996959a4` of [MateriaViva Open](https://huggingface.co/datasets/AI4QC/MateriaViva-Open).

All **56 source IDs** used by the148-property manifest exist in the pinned `licences.json`. `upstream_sources.json` preserves the exact IDs, provider names, provider-declared licenses/classes, and licensing-evidence URLs. Its `url` field points to the original provider or exact upstream release where identified. The direct download for a MatVerse property entry remains MateriaViva, not one of these upstream URLs.

The registry and pre-existing MatVerse evidence establish these source identities. This pass does **not** independently re-verify every upstream dataset version, original record match, or legal interpretation. Registry classifications must not replace the `licence` and `licence_class` stored on individual property rows. An upstream license marked open does not independently establish the rights of every contribution in a grouped dataset.

Specific checks and limits:

- [3DSC license](https://github.com/aimat-lab/3DSC/blob/main/LICENSE.md): its data grant names **3DSC_MP**. The mapping does not grant access to ICSD coordinates or identify property rows as 3DSC_ICSD.
- [OBELiX](https://github.com/NRC-Mila/OBELiX/tree/main/data): access route is the original data folder. The manifest's five ionic-conductivity values are an extracted subset, not the full OBELiX population.
- [Anyterial Altermagnets](https://altermagnets.anyterial.se/about#legal): inspected provider text limits its data license to individual or non-substantial extracts, with separate provisions for identifier lists. Preserve the registry's restricted classification.
- [SPSE](https://doi.org/10.6084/m9.figshare.12011412.v1): exact upstream release route was taken from the already-verified SPSE catalog entry. An attempted Nature HTML request returned a short non-article page despite HTTP200; HTTP status alone was not treated as verification of article contents.
- [SNUMAT repack](https://figshare.com/articles/dataset/21713885): Figshare API confirms the cited artifact is `snumat.json.zip`, a JARVIS-format repack. Do not substitute the original SNUMAT artifact12839240 and claim identical versions.
- [hMOF repack](https://figshare.com/articles/dataset/15127758): Figshare API confirms hMOF in JARVIS-Atoms format. Preserve this exact route, distinct from the original hypothetical-MOF website.
- [JARVIS specialized structures registry citation](https://doi.org/10.6084/m9.figshare.6815705): Figshare API identifies this as **JARVIS-DFT2D**. It does not enumerate all specialized datasets represented by the grouped alias. Use the [JARVIS database index](https://jarvis-tools.readthedocs.io/en/master/databases.html) as the group access route, retaining the registry URL as evidence. Native source IDs and methods are needed to trace specific subreleases.
- The `materials-cloud-archive-static` alias groups **four** records. DataCite API metadata resolves all four, retained individually in the mapping's `records` array. The manifest does not divide its source counts among these records: [A₂BC₂ electrides](https://doi.org/10.24435/materialscloud:zt-z4), [nonlinear optical materials](https://doi.org/10.24435/materialscloud:1z-pd), [optical materials](https://doi.org/10.24435/materialscloud:ed-g2), and [topological materials](https://doi.org/10.24435/materialscloud:m0-zg).
- HADB retains its source-article route and on-request caveat: a public bulk download was not established.
- Registry legacy/archived terms routes remain in `evidence_url`; replacing one with a modern access route does not silently update the original rights claim or release date.

`source_mapping_receipts.json` records stable requested URLs, response sizes, statuses, and SHA256 hashes. Bounded raw responses are under ignored `research/cache/materiaviva_properties_20261101/source_mapping/`. No signed redirect URL values or credentials are stored in the receipts. No canonical data, generated files, or Git history were modified by this source-mapping subtask.
