# Materials properties

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="materiaviva-property-band-gap"></a>
## MateriaViva — Electronic band gap

Source-reported electronic band gap values in eV, retained separately for each source and method. The table combines source and method specific gaps; experimental optical gaps and calculated electronic gaps are not interchangeable. Direct access through MateriaViva; 7,824,894 linked structures and 22 original sources.

**Size:** 13,943,575 property values (source wording: 13,943,575).

**Scope:** band_gap.parquet: numeric; 7,824,894 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Electronic band gap; eV; Electronic and optical properties; band_gap; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,273 values; provider-declared class `open`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 4,140,337 values; provider-declared class `open`.
- [Open Quantum Materials Database](https://oqmd.org/download/) (`oqmd`): 1,241,903 values; provider-declared class `open`.
- [NIST JARVIS-QETB tight-binding dataset](https://doi.org/10.6084/m9.figshare.15127788) (`jarvis-qetb`): 841,442 values; provider-declared class `open`.
- [Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (`matbench-discovery`): 247,741 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,205 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 144,438 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 120,161 values; provider-declared class `unclear`.
- [Materiae](https://cmpdc.iphy.ac.cn/materiae/) (`materiae`): 79,266 values; provider-declared class `unclear`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 74,324 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 69,474 values; provider-declared class `open`.
- [SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (`snumat`): 51,652 values; provider-declared class `open`. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.
- [GNoME](https://github.com/google-deepmind/materials_discovery) (`gnome`): 13,483 values; provider-declared class `noncommercial`.
- [Organic Materials Database](https://omdb.mathub.io/) (`omdb-organic`): 10,567 values; provider-declared class `unclear`.
- [2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (`2dmatpedia`): 6,521 values; provider-declared class `open`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 4,863 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 3,749 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (`c2db`): 3,530 values; provider-declared class `open`.
- [Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (`mc2d`): 2,385 values; provider-declared class `open`.
- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 2,080 values; provider-declared class `open`.
- [Theoretical Crystallography Open Database](https://www.crystallography.net/tcod/) (`tcod`): 159 values; provider-declared class `open`.
- [Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (`amdb`): 22 values; provider-declared class `restricted`. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

Other denominators (not added to the ranking):

- 7,824,894 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): band_gap: 13,943,575 value rows; 7,824,894 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 4,140,337 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open Quantum Materials Database](https://oqmd.org/download/) (checked 2026-11-01): MateriaViva source ID oqmd: 1,241,903 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-QETB tight-binding dataset](https://doi.org/10.6084/m9.figshare.15127788) (checked 2026-11-01): MateriaViva source ID jarvis-qetb: 841,442 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (checked 2026-11-01): MateriaViva source ID matbench-discovery: 247,741 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,205 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 144,438 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 120,161 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materiae](https://cmpdc.iphy.ac.cn/materiae/) (checked 2026-11-01): MateriaViva source ID materiae: 79,266 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 74,324 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 69,474 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (checked 2026-11-01): MateriaViva source ID snumat: 51,652 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.
- [Original source: GNoME](https://github.com/google-deepmind/materials_discovery) (checked 2026-11-01): MateriaViva source ID gnome: 13,483 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Organic Materials Database](https://omdb.mathub.io/) (checked 2026-11-01): MateriaViva source ID omdb-organic: 10,567 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: 2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (checked 2026-11-01): MateriaViva source ID 2dmatpedia: 6,521 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 4,863 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 3,749 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Original source: Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (checked 2026-11-01): MateriaViva source ID c2db: 3,530 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (checked 2026-11-01): MateriaViva source ID mc2d: 2,385 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 2,080 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Theoretical Crystallography Open Database](https://www.crystallography.net/tcod/) (checked 2026-11-01): MateriaViva source ID tcod: 159 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (checked 2026-11-01): MateriaViva source ID amdb: 22 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, band_gap, bandgap, energy gap, electronic gap, semiconductor.

<a id="materiaviva-property-formation-energy-per-atom"></a>
## MateriaViva — Formation energy per atom

Source-reported formation energy per atom values in eV/atom, retained separately for each source and method. Direct access through MateriaViva; 8,777,728 linked structures and 15 original sources.

**Size:** 12,377,989 property values (source wording: 12,377,989).

**Scope:** formation_energy_per_atom.parquet: numeric; 8,777,728 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Formation energy per atom; eV/atom; Thermodynamic properties and stability; formation_energy_per_atom; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/formation_energy_per_atom.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/formation_energy_per_atom.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/formation_energy_per_atom.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/formation_energy_per_atom.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,271 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 2,391,772 values; provider-declared class `unclear`.
- [Open Quantum Materials Database](https://oqmd.org/download/) (`oqmd`): 1,244,891 values; provider-declared class `open`.
- [NIST JARVIS-QETB tight-binding dataset](https://doi.org/10.6084/m9.figshare.15127788) (`jarvis-qetb`): 841,368 values; provider-declared class `open`.
- [Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (`matbench-discovery`): 495,482 values; provider-declared class `open`.
- [Carolina Materials Database](http://www.carolinamatdb.org/) (`carolina`): 214,131 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,205 values; provider-declared class `open`.
- [CAMD 2022 coarse-grained discovery set (Ye, Lei, Aykol, Montoya), via ODBX](https://doi.org/10.6084/m9.figshare.19601956.v1) (`camd`): 137,167 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 116,582 values; provider-declared class `open`.
- [GNoME](https://github.com/google-deepmind/materials_discovery) (`gnome`): 27,075 values; provider-declared class `noncommercial`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 17,217 values; provider-declared class `open`.
- [Wren coordinate-free coarse-graining set (Goodall et al.), via ODBX](https://doi.org/10.5281/zenodo.6345276) (`wren`): 4,705 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,715 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Open Databases Integration for Materials Design](https://odbx.science/) (`odbx`): 263 values; provider-declared class `unclear`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 145 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 8,777,728 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): formation_energy_per_atom: 12,377,989 value rows; 8,777,728 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,271 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 2,391,772 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open Quantum Materials Database](https://oqmd.org/download/) (checked 2026-11-01): MateriaViva source ID oqmd: 1,244,891 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-QETB tight-binding dataset](https://doi.org/10.6084/m9.figshare.15127788) (checked 2026-11-01): MateriaViva source ID jarvis-qetb: 841,368 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (checked 2026-11-01): MateriaViva source ID matbench-discovery: 495,482 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Carolina Materials Database](http://www.carolinamatdb.org/) (checked 2026-11-01): MateriaViva source ID carolina: 214,131 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,205 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CAMD 2022 coarse-grained discovery set (Ye, Lei, Aykol, Montoya), via ODBX](https://doi.org/10.6084/m9.figshare.19601956.v1) (checked 2026-11-01): MateriaViva source ID camd: 137,167 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 116,582 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: GNoME](https://github.com/google-deepmind/materials_discovery) (checked 2026-11-01): MateriaViva source ID gnome: 27,075 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 17,217 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Wren coordinate-free coarse-graining set (Goodall et al.), via ODBX](https://doi.org/10.5281/zenodo.6345276) (checked 2026-11-01): MateriaViva source ID wren: 4,705 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,715 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Original source: Open Databases Integration for Materials Design](https://odbx.science/) (checked 2026-11-01): MateriaViva source ID odbx: 263 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 145 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, formation_energy_per_atom, formation enthalpy, formation energy, thermodynamic stability.

<a id="materiaviva-property-total-energy-per-atom"></a>
## MateriaViva — Total energy per atom

Source-reported total energy per atom values in eV/atom, retained separately for each source and method. Absolute energies from different methods and pseudopotentials do not share a universal zero and should not be pooled without reference alignment. Direct access through MateriaViva; 8,505,529 linked structures and 14 original sources.

**Size:** 12,091,066 property values (source wording: 12,091,066).

**Scope:** total_energy_per_atom.parquet: numeric; 8,505,529 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Total energy per atom; eV/atom; Thermodynamic properties and stability; total_energy_per_atom; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_energy_per_atom.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_energy_per_atom.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_energy_per_atom.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_energy_per_atom.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,273 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 2,446,625 values; provider-declared class `unclear`.
- [Open Quantum Materials Database](https://oqmd.org/download/) (`oqmd`): 1,244,891 values; provider-declared class `open`.
- [NIST JARVIS-QETB tight-binding dataset](https://doi.org/10.6084/m9.figshare.15127788) (`jarvis-qetb`): 841,440 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 340,410 values; provider-declared class `open`.
- [Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (`matbench-discovery`): 247,741 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 116,582 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 54,879 values; provider-declared class `open`.
- [ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (`elementa`): 30,230 values; provider-declared class `noncommercial`. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.
- [GNoME](https://github.com/google-deepmind/materials_discovery) (`gnome`): 27,075 values; provider-declared class `noncommercial`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 12,904 values; provider-declared class `open`.
- [2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (`2dmatpedia`): 6,327 values; provider-declared class `open`.
- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 5,434 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,255 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 8,505,529 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): total_energy_per_atom: 12,091,066 value rows; 8,505,529 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 2,446,625 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open Quantum Materials Database](https://oqmd.org/download/) (checked 2026-11-01): MateriaViva source ID oqmd: 1,244,891 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-QETB tight-binding dataset](https://doi.org/10.6084/m9.figshare.15127788) (checked 2026-11-01): MateriaViva source ID jarvis-qetb: 841,440 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 340,410 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (checked 2026-11-01): MateriaViva source ID matbench-discovery: 247,741 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 116,582 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 54,879 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (checked 2026-11-01): MateriaViva source ID elementa: 30,230 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.
- [Original source: GNoME](https://github.com/google-deepmind/materials_discovery) (checked 2026-11-01): MateriaViva source ID gnome: 27,075 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 12,904 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: 2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (checked 2026-11-01): MateriaViva source ID 2dmatpedia: 6,327 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 5,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, total_energy_per_atom, DFT total energy, electronic energy, energy per atom.

<a id="materiaviva-property-spacegroup-number"></a>
## MateriaViva — Space group number

Source-reported space group number values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 7,463,710 linked structures and 21 original sources.

**Size:** 9,658,652 property values (source wording: 9,658,652).

**Scope:** spacegroup_number.parquet: numeric; 7,463,710 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Space group number; unit not specified / unitless; Chemical and structural descriptors; spacegroup_number; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spacegroup_number.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spacegroup_number.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spacegroup_number.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spacegroup_number.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,273 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 2,446,625 values; provider-declared class `unclear`.
- [Carolina Materials Database](http://www.carolinamatdb.org/) (`carolina`): 214,141 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 116,582 values; provider-declared class `open`.
- [Materials Cloud MC3D](https://archive.materialscloud.org/records/szjaf-cfv74) (`mc3d`): 46,818 values; provider-declared class `open`.
- [Materiae](https://cmpdc.iphy.ac.cn/materiae/) (`materiae`): 42,724 values; provider-declared class `unclear`.
- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 30,418 values; provider-declared class `open`.
- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 15,596 values; provider-declared class `open`.
- [SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (`snumat`): 12,913 values; provider-declared class `open`. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.
- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 5,434 values; provider-declared class `open`.
- [SuperBand](https://github.com/ljcj007/SuperBand) (`superband`): 3,170 values; provider-declared class `open`.
- [Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (`mc2d`): 2,913 values; provider-declared class `open`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 2,629 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 1,049 values; provider-declared class `open`.
- [AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (`aflow-prototypes`): 934 values; provider-declared class `open`.
- [HEX high-pressure elemental crystal structures](https://doi.org/10.6084/m9.figshare.25403968.v1) (`hex-high-pressure`): 725 values; provider-declared class `open`.
- [OpenMX AB2 2D structure map](https://www.openmx-square.org/2d-ab2/) (`openmx-2d-ab2`): 323 values; provider-declared class `unclear`.
- [Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (`open-framework-aluminophosphate`): 188 values; provider-declared class `open`.
- [IZA Database of Zeolite Structures](https://www.iza-structure.org/databases/) (`iza-zeolite`): 169 values; provider-declared class `restricted`.
- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 23 values; provider-declared class `unclear`.
- [OBELiX](https://github.com/NRC-Mila/OBELiX/tree/main/data) (`obelix`): 5 values; provider-declared class `open`. Only five ionic-conductivity rows appear in the property manifest. This is an extracted subset, not the full OBELiX dataset.

Other denominators (not added to the ranking):

- 7,463,710 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): spacegroup_number: 9,658,652 value rows; 7,463,710 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 2,446,625 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Carolina Materials Database](http://www.carolinamatdb.org/) (checked 2026-11-01): MateriaViva source ID carolina: 214,141 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 116,582 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud MC3D](https://archive.materialscloud.org/records/szjaf-cfv74) (checked 2026-11-01): MateriaViva source ID mc3d: 46,818 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materiae](https://cmpdc.iphy.ac.cn/materiae/) (checked 2026-11-01): MateriaViva source ID materiae: 42,724 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 30,418 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 15,596 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (checked 2026-11-01): MateriaViva source ID snumat: 12,913 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 5,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: SuperBand](https://github.com/ljcj007/SuperBand) (checked 2026-11-01): MateriaViva source ID superband: 3,170 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (checked 2026-11-01): MateriaViva source ID mc2d: 2,913 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 2,629 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 1,049 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (checked 2026-11-01): MateriaViva source ID aflow-prototypes: 934 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: HEX high-pressure elemental crystal structures](https://doi.org/10.6084/m9.figshare.25403968.v1) (checked 2026-11-01): MateriaViva source ID hex-high-pressure: 725 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: OpenMX AB2 2D structure map](https://www.openmx-square.org/2d-ab2/) (checked 2026-11-01): MateriaViva source ID openmx-2d-ab2: 323 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (checked 2026-11-01): MateriaViva source ID open-framework-aluminophosphate: 188 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: IZA Database of Zeolite Structures](https://www.iza-structure.org/databases/) (checked 2026-11-01): MateriaViva source ID iza-zeolite: 169 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 23 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: OBELiX](https://github.com/NRC-Mila/OBELiX/tree/main/data) (checked 2026-11-01): MateriaViva source ID obelix: 5 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Only five ionic-conductivity rows appear in the property manifest. This is an extracted subset, not the full OBELiX dataset.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, spacegroup_number, spacegroup, crystal symmetry, crystallography.

<a id="materiaviva-property-energy-above-hull"></a>
## MateriaViva — Energy above convex hull

Source-reported energy above convex hull values in eV/atom, retained separately for each source and method. Computed hull references and competing phase sets differ among sources and methods; this is not a guarantee of physical stability. Direct access through MateriaViva; 7,259,115 linked structures and 12 original sources.

**Size:** 8,895,858 property values (source wording: 8,895,858).

**Scope:** energy_above_hull.parquet: numeric; 7,259,115 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Energy above convex hull; eV/atom; Thermodynamic properties and stability; energy_above_hull; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_above_hull.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_above_hull.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_above_hull.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_above_hull.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,273 values; provider-declared class `open`.
- [Open Quantum Materials Database](https://oqmd.org/download/) (`oqmd`): 1,244,891 values; provider-declared class `open`.
- [Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (`matbench-discovery`): 495,482 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,205 values; provider-declared class `open`.
- [CAMD 2022 coarse-grained discovery set (Ye, Lei, Aykol, Montoya), via ODBX](https://doi.org/10.6084/m9.figshare.19601956.v1) (`camd`): 137,167 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 116,582 values; provider-declared class `open`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 5,872 values; provider-declared class `open`.
- [Wren coordinate-free coarse-graining set (Goodall et al.), via ODBX](https://doi.org/10.5281/zenodo.6345276) (`wren`): 4,705 values; provider-declared class `open`.
- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 3,232 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,255 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 1,049 values; provider-declared class `open`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 145 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 7,259,115 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): energy_above_hull: 8,895,858 value rows; 7,259,115 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open Quantum Materials Database](https://oqmd.org/download/) (checked 2026-11-01): MateriaViva source ID oqmd: 1,244,891 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (checked 2026-11-01): MateriaViva source ID matbench-discovery: 495,482 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,205 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CAMD 2022 coarse-grained discovery set (Ye, Lei, Aykol, Montoya), via ODBX](https://doi.org/10.6084/m9.figshare.19601956.v1) (checked 2026-11-01): MateriaViva source ID camd: 137,167 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 116,582 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 5,872 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Wren coordinate-free coarse-graining set (Goodall et al.), via ODBX](https://doi.org/10.5281/zenodo.6345276) (checked 2026-11-01): MateriaViva source ID wren: 4,705 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 3,232 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 1,049 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 145 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, energy_above_hull, e hull, Ehull, convex hull distance, phase stability.

<a id="materiaviva-property-total-magnetization"></a>
## MateriaViva — Total magnetization

Source-reported total magnetization values in μB, retained separately for each source and method. Direct access through MateriaViva; 6,048,431 linked structures and 8 original sources.

**Size:** 7,064,021 property values (source wording: 7,064,021).

**Scope:** total_magnetization.parquet: numeric; 6,048,431 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Total magnetization; μB; Magnetic and spin properties; total_magnetization; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_magnetization.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_magnetization.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_magnetization.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/total_magnetization.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,273 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,211 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 109,553 values; provider-declared class `open`.
- [ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (`elementa`): 30,230 values; provider-declared class `noncommercial`. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 25,544 values; provider-declared class `open`.
- [2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (`2dmatpedia`): 6,521 values; provider-declared class `open`.
- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 5,434 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,255 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 6,048,431 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): total_magnetization: 7,064,021 value rows; 6,048,431 distinct structure references; unit μB; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,211 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 109,553 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (checked 2026-11-01): MateriaViva source ID elementa: 30,230 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 25,544 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: 2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (checked 2026-11-01): MateriaViva source ID 2dmatpedia: 6,521 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 5,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, total_magnetization, total magnetic moment, spin magnetization, magnetism.

<a id="materiaviva-property-dos-at-fermi"></a>
## MateriaViva — Density of states at Fermi level

Source-reported density of states at fermi level values in states/eV, retained separately for each source and method. The manifest unit is states/eV; normalization by cell, formula unit, spin, or atom must be checked upstream. Direct access through MateriaViva; 5,909,981 linked structures and 2 original sources.

**Size:** 6,794,075 property values (source wording: 6,794,075).

**Scope:** dos_at_fermi.parquet: numeric; 5,909,981 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Density of states at Fermi level; states/eV; Electronic and optical properties; dos_at_fermi; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dos_at_fermi.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dos_at_fermi.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dos_at_fermi.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dos_at_fermi.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,714,809 values; provider-declared class `open`.
- [Materiae](https://cmpdc.iphy.ac.cn/materiae/) (`materiae`): 79,266 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 5,909,981 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): dos_at_fermi: 6,794,075 value rows; 5,909,981 distinct structure references; unit states/eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,714,809 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materiae](https://cmpdc.iphy.ac.cn/materiae/) (checked 2026-11-01): MateriaViva source ID materiae: 79,266 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, dos_at_fermi, DOS at Ef, electronic density of states, Fermi level.

<a id="materiaviva-property-band-gap-direct"></a>
## MateriaViva — Direct electronic band gap

Source-reported direct electronic band gap values in eV, retained separately for each source and method. This is a direct-gap energy table, distinct from the Boolean is_gap_direct classification. Direct access through MateriaViva; 5,894,763 linked structures and 3 original sources.

**Size:** 6,719,595 property values (source wording: 6,719,595).

**Scope:** band_gap_direct.parquet: numeric; 5,894,763 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Direct electronic band gap; eV; Electronic and optical properties; band_gap_direct; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap_direct.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap_direct.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap_direct.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/band_gap_direct.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,273 values; provider-declared class `open`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 2,242 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 2,080 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 5,894,763 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): band_gap_direct: 6,719,595 value rows; 5,894,763 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 2,242 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 2,080 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, band_gap_direct, direct bandgap, direct energy gap, optical semiconductor.

<a id="materiaviva-property-phase-separation-energy"></a>
## MateriaViva — Phase separation energy

Source-reported phase separation energy values in eV/atom, retained separately for each source and method. Direct access through MateriaViva; 5,894,220 linked structures and 1 original source.

**Size:** 6,715,271 property values (source wording: 6,715,271).

**Scope:** phase_separation_energy.parquet: numeric; 5,894,220 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Phase separation energy; eV/atom; Thermodynamic properties and stability; phase_separation_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phase_separation_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phase_separation_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phase_separation_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phase_separation_energy.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 6,715,271 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 5,894,220 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): phase_separation_energy: 6,715,271 value rows; 5,894,220 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 6,715,271 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, phase_separation_energy, phase segregation energy, phase stability.

<a id="materiaviva-property-volume-per-atom"></a>
## MateriaViva — Volume per atom

Source-reported volume per atom values in Å³/atom, retained separately for each source and method. Direct access through MateriaViva; 2,702,251 linked structures and 2 original sources.

**Size:** 5,303,898 property values (source wording: 5,303,898).

**Scope:** volume_per_atom.parquet: numeric; 2,702,251 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Volume per atom; Å³/atom; Chemical and structural descriptors; volume_per_atom; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/volume_per_atom.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/volume_per_atom.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/volume_per_atom.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/volume_per_atom.parquet).

**Original sources / indirect access:**

- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 2,857,273 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 2,446,625 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 2,702,251 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): volume_per_atom: 5,303,898 value rows; 2,702,251 distinct structure references; unit Å³/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 2,857,273 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 2,446,625 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, volume_per_atom, atomic volume, crystal volume per atom.

<a id="materiaviva-property-max-residual-force"></a>
## MateriaViva — Maximum residual force

Source-reported maximum residual force values in eV/Å, retained separately for each source and method. This is a calculation-convergence diagnostic, not a force-field training dataset or a material-intrinsic property; maximum/component conventions require source inspection. Direct access through MateriaViva; 2,989,301 linked structures and 2 original sources.

**Size:** 3,235,999 property values (source wording: 3,235,999).

**Scope:** max_residual_force.parquet: numeric; 2,989,301 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum residual force; eV/Å; Calculation and refinement metadata; max_residual_force; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_force.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_force.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_force.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_force.parquet).

**Original sources / indirect access:**

- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 3,205,769 values; provider-declared class `open`.
- [ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (`elementa`): 30,230 values; provider-declared class `noncommercial`. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.

Other denominators (not added to the ranking):

- 2,989,301 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): max_residual_force: 3,235,999 value rows; 2,989,301 distinct structure references; unit eV/Å; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 3,205,769 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (checked 2026-11-01): MateriaViva source ID elementa: 30,230 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Calculation and refinement metadata, max_residual_force, force convergence, relaxation force, residual atomic force.

<a id="materiaviva-property-structure-prototype"></a>
## MateriaViva — Structure prototype

Text descriptor for structure prototype, retained with its original source and method labels. Direct access through MateriaViva; 2,255,376 linked structures and 11 original sources.

**Size:** 3,007,443 property values (source wording: 3,007,443).

**Scope:** structure_prototype.parquet: text descriptor; 2,255,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Structure prototype; unit not specified / unitless; Chemical and structural descriptors; structure_prototype; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prototype.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prototype.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prototype.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prototype.parquet).

**Original sources / indirect access:**

- [AFLOW](https://aflow.org/) (`aflow`): 2,446,625 values; provider-declared class `unclear`.
- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (`matbench-discovery`): 247,741 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 9,241 values; provider-declared class `open`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 8,804 values; provider-declared class `open`.
- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 5,563 values; provider-declared class `open`.
- [AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (`aflow-prototypes`): 934 values; provider-declared class `open`.
- [CURATED-COFs](https://github.com/danieleongari/CURATED-COFs) (`curated-cof`): 684 values; provider-declared class `open`.
- [IZA Database of Zeolite Structures](https://www.iza-structure.org/databases/) (`iza-zeolite`): 169 values; provider-declared class `restricted`.
- [Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (`open-framework-aluminophosphate`): 49 values; provider-declared class `open`.
- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 23 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 2,255,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): structure_prototype: 3,007,443 value rows; 2,255,376 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 2,446,625 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Matbench Discovery / WBM](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) (checked 2026-11-01): MateriaViva source ID matbench-discovery: 247,741 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 9,241 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 8,804 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 5,563 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (checked 2026-11-01): MateriaViva source ID aflow-prototypes: 934 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CURATED-COFs](https://github.com/danieleongari/CURATED-COFs) (checked 2026-11-01): MateriaViva source ID curated-cof: 684 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: IZA Database of Zeolite Structures](https://www.iza-structure.org/databases/) (checked 2026-11-01): MateriaViva source ID iza-zeolite: 169 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (checked 2026-11-01): MateriaViva source ID open-framework-aluminophosphate: 49 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 23 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, structure_prototype, crystal prototype, structural type, crystal structure type.

<a id="materiaviva-property-density"></a>
## MateriaViva — Mass density

Source-reported mass density values in g/cm³, retained separately for each source and method. Direct access through MateriaViva; 1,914,229 linked structures and 9 original sources.

**Size:** 2,675,966 property values (source wording: 2,675,966).

**Scope:** density.parquet: numeric; 1,914,229 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Mass density; g/cm³; Chemical and structural descriptors; density; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/density.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/density.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/density.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/density.parquet).

**Original sources / indirect access:**

- [AFLOW](https://aflow.org/) (`aflow`): 2,446,625 values; provider-declared class `unclear`.
- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 136,008 values; provider-declared class `open`.
- [Inorganic Crystal Structure Database](https://icsd.fiz-karlsruhe.de/) (`icsd`): 44,115 values; provider-declared class `restricted`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 25,544 values; provider-declared class `open`.
- [American Mineralogist Crystal Structure Database](https://rruff.geo.arizona.edu/AMS/amcsd.php) (`amcsd`): 13,733 values; provider-declared class `unclear`. Historical AMCSD registry route is retained. Modern RRUFF catalog route is related, but record-level migration or accession correspondence is not independently established here.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.
- [Webmineral](https://webmineral.com/) (`webmineral`): 263 values; provider-declared class `unclear`. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.
- [Theoretical Crystallography Open Database](https://www.crystallography.net/tcod/) (`tcod`): 39 values; provider-declared class `open`.
- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 23 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 1,914,229 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): density: 2,675,966 value rows; 1,914,229 distinct structure references; unit g/cm³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 2,446,625 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 136,008 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Inorganic Crystal Structure Database](https://icsd.fiz-karlsruhe.de/) (checked 2026-11-01): MateriaViva source ID icsd: 44,115 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 25,544 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: American Mineralogist Crystal Structure Database](https://rruff.geo.arizona.edu/AMS/amcsd.php) (checked 2026-11-01): MateriaViva source ID amcsd: 13,733 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Historical AMCSD registry route is retained. Modern RRUFF catalog route is related, but record-level migration or accession correspondence is not independently established here.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Webmineral](https://webmineral.com/) (checked 2026-11-01): MateriaViva source ID webmineral: 263 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.
- [Original source: Theoretical Crystallography Open Database](https://www.crystallography.net/tcod/) (checked 2026-11-01): MateriaViva source ID tcod: 39 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 23 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, density, material density, crystal density.

<a id="materiaviva-property-co2-uptake"></a>
## MateriaViva — Carbon dioxide uptake

Source-reported carbon dioxide uptake values in mol/kg, retained separately for each source and method. Direct access through MateriaViva; 415,108 linked structures and 2 original sources.

**Size:** 1,405,390 property values (source wording: 1,405,390).

**Scope:** co2_uptake.parquet: numeric; 415,108 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Carbon dioxide uptake; mol/kg; Adsorption and porous materials; co2_uptake; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_uptake.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_uptake.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_uptake.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_uptake.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 1,150,394 values; provider-declared class `open`.
- [Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (`hmof`): 254,996 values; provider-declared class `open`. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.

Other denominators (not added to the ranking):

- 415,108 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): co2_uptake: 1,405,390 value rows; 415,108 distinct structure references; unit mol/kg; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 1,150,394 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (checked 2026-11-01): MateriaViva source ID hmof: 254,996 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, co2_uptake, CO2 adsorption, carbon capture, gas storage.

<a id="materiaviva-property-co2-heat-of-adsorption"></a>
## MateriaViva — Carbon dioxide heat of adsorption

Source-reported carbon dioxide heat of adsorption values in kJ/mol, retained separately for each source and method. Direct access through MateriaViva; 286,229 linked structures and 1 original source.

**Size:** 1,142,345 property values (source wording: 1,142,345).

**Scope:** co2_heat_of_adsorption.parquet: numeric; 286,229 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Carbon dioxide heat of adsorption; kJ/mol; Adsorption and porous materials; co2_heat_of_adsorption; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_heat_of_adsorption.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_heat_of_adsorption.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_heat_of_adsorption.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_heat_of_adsorption.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 1,142,345 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 286,229 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): co2_heat_of_adsorption: 1,142,345 value rows; 286,229 distinct structure references; unit kJ/mol; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 1,142,345 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, co2_heat_of_adsorption, CO2 adsorption enthalpy, carbon capture, heat of adsorption.

<a id="materiaviva-property-magnetization-per-atom"></a>
## MateriaViva — Magnetization per atom

Source-reported magnetization per atom values in μB/atom, retained separately for each source and method. Direct access through MateriaViva; 918,672 linked structures and 1 original source.

**Size:** 960,839 property values (source wording: 960,839).

**Scope:** magnetization_per_atom.parquet: numeric; 918,672 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetization per atom; μB/atom; Magnetic and spin properties; magnetization_per_atom; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_atom.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_atom.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_atom.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_atom.parquet).

**Original sources / indirect access:**

- [Open Quantum Materials Database](https://oqmd.org/download/) (`oqmd`): 960,839 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 918,672 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): magnetization_per_atom: 960,839 value rows; 918,672 distinct structure references; unit μB/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Open Quantum Materials Database](https://oqmd.org/download/) (checked 2026-11-01): MateriaViva source ID oqmd: 960,839 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, magnetization_per_atom, atomic magnetic moment, spin moment per atom, magnetism.

<a id="materiaviva-property-poisson-ratio"></a>
## MateriaViva — Poisson ratio

Source-reported poisson ratio values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 183,873 linked structures and 5 original sources.

**Size:** 882,331 property values (source wording: 882,331).

**Scope:** poisson_ratio.parquet: numeric; 183,873 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Poisson ratio; unit not specified / unitless; Mechanical and elastic properties; poisson_ratio; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/poisson_ratio.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/poisson_ratio.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/poisson_ratio.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/poisson_ratio.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 815,782 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 40,438 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 18,255 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 7,839 values; provider-declared class `unclear`.
- [Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (`hadb`): 17 values; provider-declared class `unclear`. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

Other denominators (not added to the ranking):

- 183,873 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): poisson_ratio: 882,331 value rows; 183,873 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 815,782 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 40,438 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 18,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,839 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (checked 2026-11-01): MateriaViva source ID hadb: 17 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, poisson_ratio, Poisson's ratio, elastic transverse contraction.

<a id="materiaviva-property-largest-cavity-diameter"></a>
## MateriaViva — Largest cavity diameter

Source-reported largest cavity diameter values in Å, retained separately for each source and method. Direct access through MateriaViva; 463,975 linked structures and 6 original sources.

**Size:** 493,874 property values (source wording: 493,874).

**Scope:** largest_cavity_diameter.parquet: numeric; 463,975 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Largest cavity diameter; Å; Adsorption and porous materials; largest_cavity_diameter; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_cavity_diameter.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_cavity_diameter.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_cavity_diameter.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_cavity_diameter.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (`hmof`): 127,498 values; provider-declared class `open`. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 41,942 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 25,544 values; provider-declared class `open`.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.
- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,664 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 463,975 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): largest_cavity_diameter: 493,874 value rows; 463,975 distinct structure references; unit Å; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (checked 2026-11-01): MateriaViva source ID hmof: 127,498 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 41,942 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 25,544 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,664 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, largest_cavity_diameter, LCD, pore cavity size, largest included sphere.

<a id="materiaviva-property-pore-limiting-diameter"></a>
## MateriaViva — Pore limiting diameter

Source-reported pore limiting diameter values in Å, retained separately for each source and method. Direct access through MateriaViva; 463,975 linked structures and 6 original sources.

**Size:** 493,874 property values (source wording: 493,874).

**Scope:** pore_limiting_diameter.parquet: numeric; 463,975 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Pore limiting diameter; Å; Adsorption and porous materials; pore_limiting_diameter; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_limiting_diameter.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_limiting_diameter.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_limiting_diameter.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_limiting_diameter.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (`hmof`): 127,498 values; provider-declared class `open`. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 41,942 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 25,544 values; provider-declared class `open`.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.
- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,664 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 463,975 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): pore_limiting_diameter: 493,874 value rows; 463,975 distinct structure references; unit Å; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (checked 2026-11-01): MateriaViva source ID hmof: 127,498 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 41,942 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 25,544 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,664 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, pore_limiting_diameter, PLD, pore aperture, gas accessible pore size.

<a id="materiaviva-property-void-fraction"></a>
## MateriaViva — Void fraction

Source-reported void fraction values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 445,463 linked structures and 5 original sources.

**Size:** 468,330 property values (source wording: 468,330).

**Scope:** void_fraction.parquet: numeric; 445,463 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Void fraction; unit not specified / unitless; Adsorption and porous materials; void_fraction; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/void_fraction.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/void_fraction.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/void_fraction.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/void_fraction.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (`hmof`): 127,498 values; provider-declared class `open`. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 41,942 values; provider-declared class `open`.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.
- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,664 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 445,463 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): void_fraction: 468,330 value rows; 445,463 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (checked 2026-11-01): MateriaViva source ID hmof: 127,498 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 41,942 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,664 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, void_fraction, porosity, accessible void fraction, void volume fraction.

<a id="materiaviva-property-surface-area-gravimetric"></a>
## MateriaViva — Gravimetric surface area

Source-reported gravimetric surface area values in m²/g, retained separately for each source and method. Direct access through MateriaViva; 420,616 linked structures and 4 original sources.

**Size:** 426,130 property values (source wording: 426,130).

**Scope:** surface_area_gravimetric.parquet: numeric; 420,616 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Gravimetric surface area; m²/g; Adsorption and porous materials; surface_area_gravimetric; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_gravimetric.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_gravimetric.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_gravimetric.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_gravimetric.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (`hmof`): 127,498 values; provider-declared class `open`. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.
- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,406 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 420,616 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): surface_area_gravimetric: 426,130 value rows; 420,616 distinct structure references; unit m²/g; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (checked 2026-11-01): MateriaViva source ID hmof: 127,498 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,406 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, surface_area_gravimetric, specific surface area, gas adsorption surface, area per mass.

<a id="materiaviva-property-dimensionality"></a>
## MateriaViva — Structural dimensionality

Text descriptor for structural dimensionality, retained with its original source and method labels. Direct access through MateriaViva; 394,328 linked structures and 11 original sources.

**Size:** 419,324 property values (source wording: 419,324).

**Scope:** dimensionality.parquet: text descriptor; 394,328 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Structural dimensionality; unit not specified / unitless; Chemical and structural descriptors; dimensionality; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dimensionality.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dimensionality.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dimensionality.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dimensionality.parquet).

**Original sources / indirect access:**

- [Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (`alexandria`): 151,149 values; provider-declared class `open`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 119,660 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 115,983 values; provider-declared class `open`.
- [GNoME](https://github.com/google-deepmind/materials_discovery) (`gnome`): 16,188 values; provider-declared class `noncommercial`.
- [2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (`2dmatpedia`): 6,521 values; provider-declared class `open`.
- [Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (`c2db`): 3,530 values; provider-declared class `open`.
- [Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (`mc2d`): 3,192 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,537 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 1,049 values; provider-declared class `open`.
- [OpenMX AB2 2D structure map](https://www.openmx-square.org/2d-ab2/) (`openmx-2d-ab2`): 327 values; provider-declared class `unclear`.
- [Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (`open-framework-aluminophosphate`): 188 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 394,328 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): dimensionality: 419,324 value rows; 394,328 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Alexandria Materials Database](https://alexandria.icams.rub.de/datasets.html) (checked 2026-11-01): MateriaViva source ID alexandria: 151,149 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 119,660 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 115,983 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: GNoME](https://github.com/google-deepmind/materials_discovery) (checked 2026-11-01): MateriaViva source ID gnome: 16,188 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: 2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (checked 2026-11-01): MateriaViva source ID 2dmatpedia: 6,521 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (checked 2026-11-01): MateriaViva source ID c2db: 3,530 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (checked 2026-11-01): MateriaViva source ID mc2d: 3,192 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,537 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 1,049 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: OpenMX AB2 2D structure map](https://www.openmx-square.org/2d-ab2/) (checked 2026-11-01): MateriaViva source ID openmx-2d-ab2: 327 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (checked 2026-11-01): MateriaViva source ID open-framework-aluminophosphate: 188 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, dimensionality, 2D, 3D, layered materials.

<a id="materiaviva-property-youngs-modulus"></a>
## MateriaViva — Young's modulus

Source-reported young's modulus values in GPa, retained separately for each source and method. Direct access through MateriaViva; 136,002 linked structures and 2 original sources.

**Size:** 406,893 property values (source wording: 406,893).

**Scope:** youngs_modulus.parquet: numeric; 136,002 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Young's modulus; GPa; Mechanical and elastic properties; youngs_modulus; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/youngs_modulus.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/youngs_modulus.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/youngs_modulus.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/youngs_modulus.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 406,876 values; provider-declared class `open`.
- [Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (`hadb`): 17 values; provider-declared class `unclear`. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

Other denominators (not added to the ranking):

- 136,002 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): youngs_modulus: 406,893 value rows; 136,002 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 406,876 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (checked 2026-11-01): MateriaViva source ID hadb: 17 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, youngs_modulus, Young modulus, tensile modulus, elastic stiffness.

<a id="materiaviva-property-pore-volume"></a>
## MateriaViva — Pore volume

Source-reported pore volume values in cm³/g, retained separately for each source and method. Direct access through MateriaViva; 292,971 linked structures and 2 original sources.

**Size:** 297,226 property values (source wording: 297,226).

**Scope:** pore_volume.parquet: numeric; 292,971 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Pore volume; cm³/g; Adsorption and porous materials; pore_volume; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_volume.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_volume.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_volume.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_volume.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 292,971 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): pore_volume: 297,226 value rows; 292,971 distinct structure references; unit cm³/g; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, pore_volume, porosity volume, specific pore volume.

<a id="materiaviva-property-n2-uptake"></a>
## MateriaViva — Nitrogen uptake

Source-reported nitrogen uptake values in mol/kg, retained separately for each source and method. Direct access through MateriaViva; 288,862 linked structures and 2 original sources.

**Size:** 289,129 property values (source wording: 289,129).

**Scope:** n2_uptake.parquet: numeric; 288,862 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Nitrogen uptake; mol/kg; Adsorption and porous materials; n2_uptake; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_uptake.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_uptake.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_uptake.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_uptake.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.
- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,519 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 288,862 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): n2_uptake: 289,129 value rows; 288,862 distinct structure references; unit mol/kg; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,519 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, n2_uptake, N2 adsorption, nitrogen storage, gas storage.

<a id="materiaviva-property-co2-n2-selectivity"></a>
## MateriaViva — Carbon dioxide / nitrogen selectivity

Source-reported carbon dioxide / nitrogen selectivity values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 287,610 linked structures and 1 original source.

**Size:** 287,610 property values (source wording: 287,610).

**Scope:** co2_n2_selectivity.parquet: numeric; 287,610 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Carbon dioxide / nitrogen selectivity; unit not specified / unitless; Adsorption and porous materials; co2_n2_selectivity; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_n2_selectivity.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_n2_selectivity.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_n2_selectivity.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/co2_n2_selectivity.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 287,610 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): co2_n2_selectivity: 287,610 value rows; 287,610 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, co2_n2_selectivity, CO2 N2 selectivity, carbon capture, gas separation.

<a id="materiaviva-property-working-capacity-temperature-swing"></a>
## MateriaViva — Temperature-swing working capacity

Source-reported temperature-swing working capacity values in mol/kg, retained separately for each source and method. Direct access through MateriaViva; 287,610 linked structures and 1 original source.

**Size:** 287,610 property values (source wording: 287,610).

**Scope:** working_capacity_temperature_swing.parquet: numeric; 287,610 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Temperature-swing working capacity; mol/kg; Adsorption and porous materials; working_capacity_temperature_swing; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_temperature_swing.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_temperature_swing.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_temperature_swing.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_temperature_swing.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 287,610 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): working_capacity_temperature_swing: 287,610 value rows; 287,610 distinct structure references; unit mol/kg; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, working_capacity_temperature_swing, TSA, temperature swing adsorption, gas working capacity.

<a id="materiaviva-property-working-capacity-vacuum-swing"></a>
## MateriaViva — Vacuum-swing working capacity

Source-reported vacuum-swing working capacity values in mol/kg, retained separately for each source and method. Direct access through MateriaViva; 287,610 linked structures and 1 original source.

**Size:** 287,610 property values (source wording: 287,610).

**Scope:** working_capacity_vacuum_swing.parquet: numeric; 287,610 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Vacuum-swing working capacity; mol/kg; Adsorption and porous materials; working_capacity_vacuum_swing; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_vacuum_swing.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_vacuum_swing.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_vacuum_swing.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_capacity_vacuum_swing.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 287,610 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 287,610 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): working_capacity_vacuum_swing: 287,610 value rows; 287,610 distinct structure references; unit mol/kg; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 287,610 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, working_capacity_vacuum_swing, VSA, vacuum swing adsorption, gas working capacity.

<a id="materiaviva-property-n2-heat-of-adsorption"></a>
## MateriaViva — Nitrogen heat of adsorption

Source-reported nitrogen heat of adsorption values in kJ/mol, retained separately for each source and method. Direct access through MateriaViva; 285,827 linked structures and 1 original source.

**Size:** 285,827 property values (source wording: 285,827).

**Scope:** n2_heat_of_adsorption.parquet: numeric; 285,827 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Nitrogen heat of adsorption; kJ/mol; Adsorption and porous materials; n2_heat_of_adsorption; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_heat_of_adsorption.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_heat_of_adsorption.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_heat_of_adsorption.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/n2_heat_of_adsorption.parquet).

**Original sources / indirect access:**

- [Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (`mof-carbon-capture`): 285,827 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 285,827 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): n2_heat_of_adsorption: 285,827 value rows; 285,827 distinct structure references; unit kJ/mol; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOFs for wet flue-gas carbon capture](https://archive.materialscloud.org/record/2018.0016/v3) (checked 2026-11-01): MateriaViva source ID mof-carbon-capture: 285,827 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, n2_heat_of_adsorption, N2 adsorption enthalpy, gas adsorption heat.

<a id="materiaviva-property-is-gap-direct"></a>
## MateriaViva — Direct band gap flag

Source-reported 0/1 flag for direct band gap; criteria depend on the upstream dataset. Direct access through MateriaViva; 195,861 linked structures and 3 original sources.

**Size:** 264,982 property values (source wording: 264,982).

**Scope:** is_gap_direct.parquet: boolean (0/1); 195,861 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Direct band gap flag; unit not specified / unitless; Electronic and optical properties; is_gap_direct; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_gap_direct.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_gap_direct.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_gap_direct.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_gap_direct.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,205 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 69,474 values; provider-declared class `open`.
- [SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (`snumat`): 25,303 values; provider-declared class `open`. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.

Other denominators (not added to the ranking):

- 195,861 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): is_gap_direct: 264,982 value rows; 195,861 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,205 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 69,474 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (checked 2026-11-01): MateriaViva source ID snumat: 25,303 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, is_gap_direct, direct bandgap, direct semiconductor, optical transition.

<a id="materiaviva-property-dielectric-constant-electronic"></a>
## MateriaViva — Electronic dielectric constant

Source-reported electronic dielectric constant values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 213,121 linked structures and 5 original sources.

**Size:** 262,400 property values (source wording: 262,400).

**Scope:** dielectric_constant_electronic.parquet: numeric; 213,121 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Electronic dielectric constant; unit not specified / unitless; Dielectric and electromechanical properties; dielectric_constant_electronic; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_electronic.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_electronic.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_electronic.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_electronic.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 136,008 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 107,215 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 9,105 values; provider-declared class `open`.
- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 7,695 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 2,377 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 213,121 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): dielectric_constant_electronic: 262,400 value rows; 213,121 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 136,008 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 107,215 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 9,105 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 7,695 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 2,377 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Dielectric and electromechanical properties, dielectric_constant_electronic, high frequency permittivity, epsilon infinity, electronic permittivity.

<a id="materiaviva-property-measurement-temperature"></a>
## MateriaViva — Measurement temperature

Source-reported measurement temperature values in K, retained separately for each source and method. Direct access through MateriaViva; 238,161 linked structures and 1 original source.

**Size:** 244,260 property values (source wording: 244,260).

**Scope:** measurement_temperature.parquet: numeric; 238,161 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Measurement temperature; K; Calculation and refinement metadata; measurement_temperature; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_temperature.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_temperature.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_temperature.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_temperature.parquet).

**Original sources / indirect access:**

- [Crystallography Open Database](https://www.crystallography.net/cod/) (`cod`): 244,260 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 238,161 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): measurement_temperature: 244,260 value rows; 238,161 distinct structure references; unit K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Crystallography Open Database](https://www.crystallography.net/cod/) (checked 2026-11-01): MateriaViva source ID cod: 244,260 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Calculation and refinement metadata, measurement_temperature, experimental temperature, temperature conditions.

<a id="materiaviva-property-bulk-modulus-vrh"></a>
## MateriaViva — Bulk modulus — Voigt–Reuss–Hill

Source-reported bulk modulus — voigt–reuss–hill values in GPa, retained separately for each source and method. Direct access through MateriaViva; 184,040 linked structures and 7 original sources.

**Size:** 202,894 property values (source wording: 202,894).

**Scope:** bulk_modulus_vrh.parquet: numeric; 184,040 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Bulk modulus — Voigt–Reuss–Hill; GPa; Mechanical and elastic properties; bulk_modulus_vrh; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_vrh.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_vrh.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_vrh.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_vrh.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 135,948 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 40,694 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 18,255 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 7,839 values; provider-declared class `unclear`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 121 values; provider-declared class `open`.
- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 20 values; provider-declared class `unclear`.
- [Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (`hadb`): 17 values; provider-declared class `unclear`. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

Other denominators (not added to the ranking):

- 184,040 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): bulk_modulus_vrh: 202,894 value rows; 184,040 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 135,948 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 40,694 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 18,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,839 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 121 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 20 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (checked 2026-11-01): MateriaViva source ID hadb: 17 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, bulk_modulus_vrh, VRH bulk modulus, Hill average bulk modulus.

<a id="materiaviva-property-shear-modulus-vrh"></a>
## MateriaViva — Shear modulus — Voigt–Reuss–Hill

Source-reported shear modulus — voigt–reuss–hill values in GPa, retained separately for each source and method. Direct access through MateriaViva; 181,088 linked structures and 6 original sources.

**Size:** 199,927 property values (source wording: 199,927).

**Scope:** shear_modulus_vrh.parquet: numeric; 181,088 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Shear modulus — Voigt–Reuss–Hill; GPa; Mechanical and elastic properties; shear_modulus_vrh; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_vrh.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_vrh.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_vrh.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_vrh.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 133,001 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 40,694 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 18,255 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 7,839 values; provider-declared class `unclear`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 121 values; provider-declared class `open`.
- [Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (`hadb`): 17 values; provider-declared class `unclear`. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

Other denominators (not added to the ranking):

- 181,088 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): shear_modulus_vrh: 199,927 value rows; 181,088 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 133,001 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 40,694 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 18,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,839 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 121 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Hard-coating Alloys Database](https://doi.org/10.1016/j.tsf.2022.139627) (checked 2026-11-01): MateriaViva source ID hadb: 17 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Registry points to the source article and reports data available on request; no independently verified public bulk download is asserted.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, shear_modulus_vrh, VRH shear modulus, Hill average shear modulus.

<a id="materiaviva-property-experimentally-observed"></a>
## MateriaViva — Experimentally observed flag

Source-reported 0/1 flag for experimentally observed; criteria depend on the upstream dataset. A source provenance flag indicates an experimental association, not validation of every property value in the aggregate. Direct access through MateriaViva; 187,946 linked structures and 2 original sources.

**Size:** 192,278 property values (source wording: 192,278).

**Scope:** experimentally_observed.parquet: boolean (0/1); 187,946 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Experimentally observed flag; unit not specified / unitless; Chemical and structural descriptors; experimentally_observed; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/experimentally_observed.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/experimentally_observed.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/experimentally_observed.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/experimentally_observed.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,211 values; provider-declared class `open`.
- [Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (`qmof`): 22,067 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 187,946 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): experimentally_observed: 192,278 value rows; 187,946 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,211 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Quantum MOF Database](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): MateriaViva source ID qmof: 22,067 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, experimentally_observed, experimental existence, synthesized material, experimental evidence.

<a id="materiaviva-property-surface-area-volumetric"></a>
## MateriaViva — Volumetric surface area

Source-reported volumetric surface area values in m²/cm³, retained separately for each source and method. Direct access through MateriaViva; 157,821 linked structures and 4 original sources.

**Size:** 180,462 property values (source wording: 180,462).

**Scope:** surface_area_volumetric.parquet: numeric; 157,821 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Volumetric surface area; m²/cm³; Adsorption and porous materials; surface_area_volumetric; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_volumetric.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_volumetric.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_volumetric.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_area_volumetric.parquet).

**Original sources / indirect access:**

- [Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (`hmof`): 127,498 values; provider-declared class `open`. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 41,942 values; provider-declared class `open`.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.
- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,406 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 157,821 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): surface_area_volumetric: 180,462 value rows; 157,821 distinct structure references; unit m²/cm³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Hypothetical MOF database (JARVIS figshare re-upload)](https://figshare.com/articles/dataset/15127758) (checked 2026-11-01): MateriaViva source ID hmof: 127,498 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use the exact JARVIS-Atoms repack cited by MateriaViva, not an assumed current snapshot of the original Wilmer portal.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 41,942 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,406 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, surface_area_volumetric, surface area per volume, porous surface area.

<a id="materiaviva-property-fermi-energy"></a>
## MateriaViva — Fermi energy

Source-reported fermi energy values in eV, retained separately for each source and method. Direct access through MateriaViva; 169,258 linked structures and 2 original sources.

**Size:** 173,661 property values (source wording: 173,661).

**Scope:** fermi_energy.parquet: numeric; 169,258 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Fermi energy; eV; Electronic and optical properties; fermi_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/fermi_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/fermi_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/fermi_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/fermi_energy.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,131 values; provider-declared class `open`.
- [Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (`c2db`): 3,530 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 169,258 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): fermi_energy: 173,661 value rows; 169,258 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,131 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (checked 2026-11-01): MateriaViva source ID c2db: 3,530 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, fermi_energy, Fermi level, Ef, electronic chemical potential.

<a id="materiaviva-property-magnetization-per-volume"></a>
## MateriaViva — Magnetization per volume

Source-reported magnetization per volume values in μB/Å³, retained separately for each source and method. Direct access through MateriaViva; 166,028 linked structures and 1 original source.

**Size:** 170,211 property values (source wording: 170,211).

**Scope:** magnetization_per_volume.parquet: numeric; 166,028 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetization per volume; μB/Å³; Magnetic and spin properties; magnetization_per_volume; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_volume.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_volume.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_volume.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetization_per_volume.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,211 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 166,028 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): magnetization_per_volume: 170,211 value rows; 166,028 distinct structure references; unit μB/Å³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,211 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, magnetization_per_volume, magnetization density, magnetic moment density, magnetism.

<a id="materiaviva-property-is-stable"></a>
## MateriaViva — Stability flag

Source-reported 0/1 flag for stability; criteria depend on the upstream dataset. Retain the original source stability criterion; a Boolean classification does not establish dynamical, chemical, and experimental stability together. Direct access through MateriaViva; 166,028 linked structures and 1 original source.

**Size:** 170,211 property values (source wording: 170,211).

**Scope:** is_stable.parquet: boolean (0/1); 166,028 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Stability flag; unit not specified / unitless; Thermodynamic properties and stability; is_stable; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_stable.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_stable.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_stable.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_stable.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,211 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 166,028 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): is_stable: 170,211 value rows; 166,028 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,211 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, is_stable, stable phase, thermodynamic stability, stable material.

<a id="materiaviva-property-is-metal"></a>
## MateriaViva — Metallicity flag

Source-reported 0/1 flag for metallicity; criteria depend on the upstream dataset. Direct access through MateriaViva; 165,951 linked structures and 2 original sources.

**Size:** 170,153 property values (source wording: 170,153).

**Scope:** is_metal.parquet: boolean (0/1); 165,951 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Metallicity flag; unit not specified / unitless; Electronic and optical properties; is_metal; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_metal.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_metal.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_metal.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/is_metal.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 170,131 values; provider-declared class `open`.
- [Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (`amdb`): 22 values; provider-declared class `restricted`. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

Other denominators (not added to the ranking):

- 165,951 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): is_metal: 170,153 value rows; 165,951 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 170,131 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (checked 2026-11-01): MateriaViva source ID amdb: 22 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, is_metal, metallic material, metal classification, electrical conductor.

<a id="materiaviva-property-magnetic-ordering"></a>
## MateriaViva — Magnetic ordering

Text descriptor for magnetic ordering, retained with its original source and method labels. Direct access through MateriaViva; 145,010 linked structures and 4 original sources.

**Size:** 155,422 property values (source wording: 155,422).

**Scope:** magnetic_ordering.parquet: text descriptor; 145,010 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetic ordering; unit not specified / unitless; Magnetic and spin properties; magnetic_ordering; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_ordering.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_ordering.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_ordering.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_ordering.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 137,053 values; provider-declared class `open`.
- [SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (`snumat`): 12,913 values; provider-declared class `open`. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.
- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 5,434 values; provider-declared class `open`.
- [Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (`amdb`): 22 values; provider-declared class `restricted`. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

Other denominators (not added to the ranking):

- 145,010 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): magnetic_ordering: 155,422 value rows; 145,010 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 137,053 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: SNUMAT hybrid-functional database](https://figshare.com/articles/dataset/21713885) (checked 2026-11-01): MateriaViva source ID snumat: 12,913 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Use exact MateriaViva-cited JARVIS SNUMAT repack 21713885, not the separately cataloged original hybrid-gap file 12839240.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 5,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (checked 2026-11-01): MateriaViva source ID amdb: 22 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, magnetic_ordering, ferromagnetic, antiferromagnetic, ferrimagnetic, magnetic order.

<a id="materiaviva-property-decomposition-energy"></a>
## MateriaViva — Decomposition energy

Source-reported decomposition energy values in eV/atom, retained separately for each source and method. The sign and reference decomposition depend on the source; do not automatically equate this field with energy_above_hull. Direct access through MateriaViva; 62,430 linked structures and 3 original sources.

**Size:** 153,566 property values (source wording: 153,566).

**Scope:** decomposition_energy.parquet: numeric; 62,430 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Decomposition energy; eV/atom; Thermodynamic properties and stability; decomposition_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposition_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposition_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposition_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposition_energy.parquet).

**Original sources / indirect access:**

- [GNoME](https://github.com/google-deepmind/materials_discovery) (`gnome`): 108,300 values; provider-declared class `noncommercial`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 39,832 values; provider-declared class `open`.
- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 5,434 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 62,430 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): decomposition_energy: 153,566 value rows; 62,430 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: GNoME](https://github.com/google-deepmind/materials_discovery) (checked 2026-11-01): MateriaViva source ID gnome: 108,300 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 39,832 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 5,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, decomposition_energy, phase decomposition energy, thermodynamic stability.

<a id="materiaviva-property-dielectric-constant-total"></a>
## MateriaViva — Total dielectric constant

Source-reported total dielectric constant values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 148,795 linked structures and 5 original sources.

**Size:** 152,653 property values (source wording: 152,653).

**Scope:** dielectric_constant_total.parquet: numeric; 148,795 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Total dielectric constant; unit not specified / unitless; Dielectric and electromechanical properties; dielectric_constant_total; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_total.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_total.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_total.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_total.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 135,518 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 9,105 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 6,799 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,072 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Theoretical Crystallography Open Database](https://www.crystallography.net/tcod/) (`tcod`): 159 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 148,795 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): dielectric_constant_total: 152,653 value rows; 148,795 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 135,518 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 9,105 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 6,799 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,072 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Original source: Theoretical Crystallography Open Database](https://www.crystallography.net/tcod/) (checked 2026-11-01): MateriaViva source ID tcod: 159 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Dielectric and electromechanical properties, dielectric_constant_total, static permittivity, total permittivity, epsilon.

<a id="materiaviva-property-bulk-modulus-voigt"></a>
## MateriaViva — Bulk modulus — Voigt

Source-reported bulk modulus — voigt values in GPa, retained separately for each source and method. Direct access through MateriaViva; 151,469 linked structures and 3 original sources.

**Size:** 151,596 property values (source wording: 151,596).

**Scope:** bulk_modulus_voigt.parquet: numeric; 151,469 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Bulk modulus — Voigt; GPa; Mechanical and elastic properties; bulk_modulus_voigt; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_voigt.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_voigt.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_voigt.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_voigt.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 135,955 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 121 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 151,469 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): bulk_modulus_voigt: 151,596 value rows; 151,469 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 135,955 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 121 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, bulk_modulus_voigt, Voigt bulk modulus, elastic compressibility.

<a id="materiaviva-property-bulk-modulus-reuss"></a>
## MateriaViva — Bulk modulus — Reuss

Source-reported bulk modulus — reuss values in GPa, retained separately for each source and method. Direct access through MateriaViva; 151,409 linked structures and 3 original sources.

**Size:** 151,536 property values (source wording: 151,536).

**Scope:** bulk_modulus_reuss.parquet: numeric; 151,409 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Bulk modulus — Reuss; GPa; Mechanical and elastic properties; bulk_modulus_reuss; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_reuss.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_reuss.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_reuss.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_reuss.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 135,895 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 121 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 151,409 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): bulk_modulus_reuss: 151,536 value rows; 151,409 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 135,895 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 121 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, bulk_modulus_reuss, Reuss bulk modulus, elastic compressibility.

<a id="materiaviva-property-sound-velocity-longitudinal"></a>
## MateriaViva — Longitudinal sound velocity

Source-reported longitudinal sound velocity values in m/s, retained separately for each source and method. Direct access through MateriaViva; 151,357 linked structures and 2 original sources.

**Size:** 151,400 property values (source wording: 151,400).

**Scope:** sound_velocity_longitudinal.parquet: numeric; 151,357 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Longitudinal sound velocity; m/s; Mechanical and elastic properties; sound_velocity_longitudinal; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_longitudinal.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_longitudinal.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_longitudinal.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_longitudinal.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 135,880 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 151,357 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): sound_velocity_longitudinal: 151,400 value rows; 151,357 distinct structure references; unit m/s; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 135,880 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, sound_velocity_longitudinal, longitudinal acoustic velocity, compressional wave speed.

<a id="materiaviva-property-shear-modulus-voigt"></a>
## MateriaViva — Shear modulus — Voigt

Source-reported shear modulus — voigt values in GPa, retained separately for each source and method. Direct access through MateriaViva; 149,810 linked structures and 3 original sources.

**Size:** 149,937 property values (source wording: 149,937).

**Scope:** shear_modulus_voigt.parquet: numeric; 149,810 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Shear modulus — Voigt; GPa; Mechanical and elastic properties; shear_modulus_voigt; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_voigt.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_voigt.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_voigt.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_voigt.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 134,296 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 121 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 149,810 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): shear_modulus_voigt: 149,937 value rows; 149,810 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 134,296 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 121 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, shear_modulus_voigt, Voigt shear modulus, elastic shear stiffness.

<a id="materiaviva-property-sound-velocity-transverse"></a>
## MateriaViva — Transverse sound velocity

Source-reported transverse sound velocity values in m/s, retained separately for each source and method. Direct access through MateriaViva; 148,475 linked structures and 2 original sources.

**Size:** 148,518 property values (source wording: 148,518).

**Scope:** sound_velocity_transverse.parquet: numeric; 148,475 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Transverse sound velocity; m/s; Mechanical and elastic properties; sound_velocity_transverse; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_transverse.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_transverse.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_transverse.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/sound_velocity_transverse.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 132,998 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 148,475 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): sound_velocity_transverse: 148,518 value rows; 148,475 distinct structure references; unit m/s; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 132,998 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, sound_velocity_transverse, transverse acoustic velocity, shear wave speed.

<a id="materiaviva-property-framework-density"></a>
## MateriaViva — Framework T-atom density

Source-reported framework t-atom density values in T/1000 Å³, retained separately for each source and method. T denotes framework tetrahedral atoms; this number density differs from the mass-density table. Direct access through MateriaViva; 148,195 linked structures and 3 original sources.

**Size:** 148,197 property values (source wording: 148,197).

**Scope:** framework_density.parquet: numeric; 148,195 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Framework T-atom density; T/1000 Å³; Adsorption and porous materials; framework_density; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_density.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_density.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_density.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_density.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 136,008 values; provider-declared class `open`.
- [Predicted Crystallography Open Database](https://www.crystallography.net/pcod/) (`pcod`): 12,001 values; provider-declared class `open`.
- [Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (`open-framework-aluminophosphate`): 188 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 148,195 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): framework_density: 148,197 value rows; 148,195 distinct structure references; unit T/1000 Å³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 136,008 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Predicted Crystallography Open Database](https://www.crystallography.net/pcod/) (checked 2026-11-01): MateriaViva source ID pcod: 12,001 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (checked 2026-11-01): MateriaViva source ID open-framework-aluminophosphate: 188 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, framework_density, zeolite framework density, tetrahedral atom density, T per volume.

<a id="materiaviva-property-shear-modulus-reuss"></a>
## MateriaViva — Shear modulus — Reuss

Source-reported shear modulus — reuss values in GPa, retained separately for each source and method. Direct access through MateriaViva; 146,499 linked structures and 3 original sources.

**Size:** 146,626 property values (source wording: 146,626).

**Scope:** shear_modulus_reuss.parquet: numeric; 146,499 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Shear modulus — Reuss; GPa; Mechanical and elastic properties; shear_modulus_reuss; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_reuss.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_reuss.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_reuss.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shear_modulus_reuss.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 130,985 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.
- [NOMAD Repository and Archive](https://nomad-lab.eu/) (`nomad`): 121 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 146,499 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): shear_modulus_reuss: 146,626 value rows; 146,499 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 130,985 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NOMAD Repository and Archive](https://nomad-lab.eu/) (checked 2026-11-01): MateriaViva source ID nomad: 121 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, shear_modulus_reuss, Reuss shear modulus, elastic shear stiffness.

<a id="materiaviva-property-chemical-name"></a>
## MateriaViva — Chemical name

Text descriptor for chemical name, retained with its original source and method labels. Direct access through MateriaViva; 106,371 linked structures and 3 original sources.

**Size:** 141,432 property values (source wording: 141,432).

**Scope:** chemical_name.parquet: text descriptor; 106,371 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Chemical name; unit not specified / unitless; Chemical and structural descriptors; chemical_name; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/chemical_name.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/chemical_name.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/chemical_name.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/chemical_name.parquet).

**Original sources / indirect access:**

- [Crystallography Open Database](https://www.crystallography.net/cod/) (`cod`): 97,227 values; provider-declared class `open`.
- [Inorganic Crystal Structure Database](https://icsd.fiz-karlsruhe.de/) (`icsd`): 44,078 values; provider-declared class `restricted`.
- [Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (`open-framework-aluminophosphate`): 127 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 106,371 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): chemical_name: 141,432 value rows; 106,371 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Crystallography Open Database](https://www.crystallography.net/cod/) (checked 2026-11-01): MateriaViva source ID cod: 97,227 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Inorganic Crystal Structure Database](https://icsd.fiz-karlsruhe.de/) (checked 2026-11-01): MateriaViva source ID icsd: 44,078 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (checked 2026-11-01): MateriaViva source ID open-framework-aluminophosphate: 127 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, chemical_name, compound name, chemical nomenclature.

<a id="materiaviva-property-energy-per-t-atom"></a>
## MateriaViva — Energy per framework T atom

Source-reported energy per framework t atom values in kJ/mol, retained separately for each source and method. The source key denotes a framework T-atom energy and reports kJ/mol; the reference state and molar normalization require the Deem-zeolites source definition. Direct access through MateriaViva; 136,008 linked structures and 1 original source.

**Size:** 136,008 property values (source wording: 136,008).

**Scope:** energy_per_t_atom.parquet: numeric; 136,008 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Energy per framework T atom; kJ/mol; Adsorption and porous materials; energy_per_t_atom; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_per_t_atom.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_per_t_atom.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_per_t_atom.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_per_t_atom.parquet).

**Original sources / indirect access:**

- [Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (`deem-zeolites`): 136,008 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 136,008 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): energy_per_t_atom: 136,008 value rows; 136,008 distinct structure references; unit kJ/mol; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Deem PCOD hypothetical zeolites v2.1](https://zenodo.org/records/8035241) (checked 2026-11-01): MateriaViva source ID deem-zeolites: 136,008 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, energy_per_t_atom, zeolite energy, T atom energy, tetrahedral framework energy.

<a id="materiaviva-property-decomposes-to"></a>
## MateriaViva — Decomposition products

Text descriptor for decomposition products, retained with its original source and method labels. Direct access through MateriaViva; 126,700 linked structures and 1 original source.

**Size:** 130,373 property values (source wording: 130,373).

**Scope:** decomposes_to.parquet: text descriptor; 126,700 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Decomposition products; unit not specified / unitless; Thermodynamic properties and stability; decomposes_to; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposes_to.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposes_to.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposes_to.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/decomposes_to.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 130,373 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 126,700 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): decomposes_to: 130,373 value rows; 126,700 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 130,373 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, decomposes_to, decomposes to, phase decomposition, competing phases.

<a id="materiaviva-property-topology-class"></a>
## MateriaViva — Topological class

Text descriptor for topological class, retained with its original source and method labels. Direct access through MateriaViva; 49,811 linked structures and 2 original sources.

**Size:** 126,094 property values (source wording: 126,094).

**Scope:** topology_class.parquet: text descriptor; 49,811 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Topological class; unit not specified / unitless; Electronic and optical properties; topology_class; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_class.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_class.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_class.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_class.parquet).

**Original sources / indirect access:**

- [Materiae](https://cmpdc.iphy.ac.cn/materiae/) (`materiae`): 76,853 values; provider-declared class `unclear`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 49,241 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 49,811 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): topology_class: 126,094 value rows; 49,811 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materiae](https://cmpdc.iphy.ac.cn/materiae/) (checked 2026-11-01): MateriaViva source ID materiae: 76,853 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 49,241 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, topology_class, topological classification, topological insulator, band topology.

<a id="materiaviva-property-average-oxidation-states"></a>
## MateriaViva — Average oxidation states

Text descriptor for average oxidation states, retained with its original source and method labels. Direct access through MateriaViva; 120,998 linked structures and 1 original source.

**Size:** 124,820 property values (source wording: 124,820).

**Scope:** average_oxidation_states.parquet: text descriptor; 120,998 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Average oxidation states; unit not specified / unitless; Chemical and structural descriptors; average_oxidation_states; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_oxidation_states.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_oxidation_states.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_oxidation_states.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_oxidation_states.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 124,820 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 120,998 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): average_oxidation_states: 124,820 value rows; 120,998 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 124,820 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, average_oxidation_states, valence, oxidation state, average valence.

<a id="materiaviva-property-oxidation-states"></a>
## MateriaViva — Oxidation states

Text descriptor for oxidation states, retained with its original source and method labels. Direct access through MateriaViva; 120,998 linked structures and 1 original source.

**Size:** 124,820 property values (source wording: 124,820).

**Scope:** oxidation_states.parquet: text descriptor; 120,998 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Oxidation states; unit not specified / unitless; Chemical and structural descriptors; oxidation_states; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/oxidation_states.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/oxidation_states.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/oxidation_states.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/oxidation_states.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 124,820 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 120,998 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): oxidation_states: 124,820 value rows; 120,998 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 124,820 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, oxidation_states, valence states, oxidation numbers, ionic valence.

<a id="materiaviva-property-predicted-synthesizable"></a>
## MateriaViva — Predicted synthesizability flag

Source-reported 0/1 flag for predicted synthesizability; criteria depend on the upstream dataset. This property-table entry is itself a prediction flag; its inclusion in properties/ does not make it an experimental synthesis outcome. Direct access through MateriaViva; 94,797 linked structures and 1 original source.

**Size:** 98,303 property values (source wording: 98,303).

**Scope:** predicted_synthesizable.parquet: boolean (0/1); 94,797 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Predicted synthesizability flag; unit not specified / unitless; Chemical and structural descriptors; predicted_synthesizable; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/predicted_synthesizable.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/predicted_synthesizable.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/predicted_synthesizable.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/predicted_synthesizable.parquet).

**Original sources / indirect access:**

- [CSLLM non-synthesizable screening set](https://doi.org/10.6084/m9.figshare.29086931) (`csllm-negatives`): 98,303 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 94,797 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): predicted_synthesizable: 98,303 value rows; 94,797 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: CSLLM non-synthesizable screening set](https://doi.org/10.6084/m9.figshare.29086931) (checked 2026-11-01): MateriaViva source ID csllm-negatives: 98,303 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, predicted_synthesizable, synthesis prediction, synthesizability, synthetic accessibility.

<a id="materiaviva-property-cbm"></a>
## MateriaViva — Conduction band minimum

Source-reported conduction band minimum values in eV, retained separately for each source and method. Direct access through MateriaViva; 92,582 linked structures and 1 original source.

**Size:** 95,095 property values (source wording: 95,095).

**Scope:** cbm.parquet: numeric; 92,582 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Conduction band minimum; eV; Electronic and optical properties; cbm; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/cbm.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/cbm.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/cbm.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/cbm.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 95,095 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 92,582 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): cbm: 95,095 value rows; 92,582 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 95,095 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, cbm, CBM, conduction band edge, band alignment.

<a id="materiaviva-property-vbm"></a>
## MateriaViva — Valence band maximum

Source-reported valence band maximum values in eV, retained separately for each source and method. Direct access through MateriaViva; 92,582 linked structures and 1 original source.

**Size:** 95,095 property values (source wording: 95,095).

**Scope:** vbm.parquet: numeric; 92,582 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Valence band maximum; eV; Electronic and optical properties; vbm; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/vbm.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/vbm.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/vbm.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/vbm.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 95,095 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 92,582 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): vbm: 95,095 value rows; 92,582 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 95,095 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, vbm, VBM, valence band edge, band alignment.

<a id="materiaviva-property-topology-invariant"></a>
## MateriaViva — Topological invariant

Text descriptor for topological invariant, retained with its original source and method labels. Direct access through MateriaViva; 44,199 linked structures and 2 original sources.

**Size:** 82,861 property values (source wording: 82,861).

**Scope:** topology_invariant.parquet: text descriptor; 44,199 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Topological invariant; unit not specified / unitless; Electronic and optical properties; topology_invariant; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_invariant.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_invariant.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_invariant.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/topology_invariant.parquet).

**Original sources / indirect access:**

- [Materiae](https://cmpdc.iphy.ac.cn/materiae/) (`materiae`): 49,445 values; provider-declared class `unclear`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 33,416 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 44,199 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): topology_invariant: 82,861 value rows; 44,199 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materiae](https://cmpdc.iphy.ac.cn/materiae/) (checked 2026-11-01): MateriaViva source ID materiae: 49,445 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 33,416 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, topology_invariant, topological index, topological invariant, band topology.

<a id="materiaviva-property-magnetic-species"></a>
## MateriaViva — Magnetic species

Text descriptor for magnetic species, retained with its original source and method labels. Direct access through MateriaViva; 67,681 linked structures and 1 original source.

**Size:** 69,385 property values (source wording: 69,385).

**Scope:** magnetic_species.parquet: text descriptor; 67,681 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetic species; unit not specified / unitless; Magnetic and spin properties; magnetic_species; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_species.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_species.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_species.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_species.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 69,385 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 67,681 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): magnetic_species: 69,385 value rows; 67,681 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 69,385 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, magnetic_species, magnetic elements, magnetic ions, spin bearing species.

<a id="materiaviva-property-seebeck-coefficient"></a>
## MateriaViva — Seebeck coefficient

Source-reported seebeck coefficient values in μV/K, retained separately for each source and method. Retain carrier concentration, carrier type, temperature, and tensor or averaging conventions. Direct access through MateriaViva; 31,097 linked structures and 2 original sources.

**Size:** 67,176 property values (source wording: 67,176).

**Scope:** seebeck_coefficient.parquet: numeric; 31,097 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Seebeck coefficient; μV/K; Thermoelectric properties; seebeck_coefficient; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/seebeck_coefficient.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/seebeck_coefficient.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/seebeck_coefficient.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/seebeck_coefficient.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 65,346 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,830 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 31,097 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): seebeck_coefficient: 67,176 value rows; 31,097 distinct structure references; unit μV/K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 65,346 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,830 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermoelectric properties, seebeck_coefficient, thermopower, thermoelectric voltage, S coefficient.

<a id="materiaviva-property-power-factor"></a>
## MateriaViva — Thermoelectric power factor

Source-reported thermoelectric power factor values in μW/cm·K², retained separately for each source and method. Retain carrier concentration, doping sign, temperature, and transport assumptions; this is not the dimensionless thermoelectric figure of merit ZT. Direct access through MateriaViva; 31,094 linked structures and 2 original sources.

**Size:** 67,172 property values (source wording: 67,172).

**Scope:** power_factor.parquet: numeric; 31,094 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Thermoelectric power factor; μW/cm·K²; Thermoelectric properties; power_factor; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/power_factor.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/power_factor.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/power_factor.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/power_factor.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 65,346 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,826 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 31,094 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): power_factor: 67,172 value rows; 31,094 distinct structure references; unit μW/cm·K²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 65,346 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,826 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermoelectric properties, power_factor, Seebeck squared conductivity, S squared sigma, thermoelectric transport.

<a id="materiaviva-property-has-imaginary-phonon"></a>
## MateriaViva — Imaginary phonon flag

Source-reported 0/1 flag for imaginary phonon; criteria depend on the upstream dataset. Direct access through MateriaViva; 39,513 linked structures and 4 original sources.

**Size:** 64,437 property values (source wording: 64,437).

**Scope:** has_imaginary_phonon.parquet: boolean (0/1); 39,513 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Imaginary phonon flag; unit not specified / unitless; Thermal and vibrational properties; has_imaginary_phonon; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_imaginary_phonon.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_imaginary_phonon.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_imaginary_phonon.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_imaginary_phonon.parquet).

**Original sources / indirect access:**

- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 30,383 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 19,937 values; provider-declared class `open`.
- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 13,896 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 221 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 39,513 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): has_imaginary_phonon: 64,437 value rows; 39,513 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 30,383 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 19,937 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 13,896 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 221 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, has_imaginary_phonon, phonon instability, imaginary frequency, soft mode.

<a id="materiaviva-property-phonon-min-frequency"></a>
## MateriaViva — Minimum phonon frequency

Source-reported minimum phonon frequency values in THz, retained separately for each source and method. Direct access through MateriaViva; 39,513 linked structures and 4 original sources.

**Size:** 64,437 property values (source wording: 64,437).

**Scope:** phonon_min_frequency.parquet: numeric; 39,513 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Minimum phonon frequency; THz; Thermal and vibrational properties; phonon_min_frequency; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_min_frequency.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_min_frequency.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_min_frequency.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_min_frequency.parquet).

**Original sources / indirect access:**

- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 30,383 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 19,937 values; provider-declared class `open`.
- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 13,896 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 221 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 39,513 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): phonon_min_frequency: 64,437 value rows; 39,513 distinct structure references; unit THz; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 30,383 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 19,937 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 13,896 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 221 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, phonon_min_frequency, phonon band minimum, soft mode, vibrational frequency.

<a id="materiaviva-property-phonon-max-frequency"></a>
## MateriaViva — Maximum phonon frequency

Source-reported maximum phonon frequency values in THz, retained separately for each source and method. Direct access through MateriaViva; 39,491 linked structures and 4 original sources.

**Size:** 64,394 property values (source wording: 64,394).

**Scope:** phonon_max_frequency.parquet: numeric; 39,491 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum phonon frequency; THz; Thermal and vibrational properties; phonon_max_frequency; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_max_frequency.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_max_frequency.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_max_frequency.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_max_frequency.parquet).

**Original sources / indirect access:**

- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 30,383 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 19,894 values; provider-declared class `open`.
- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 13,896 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 221 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 39,491 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): phonon_max_frequency: 64,394 value rows; 39,491 distinct structure references; unit THz; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 30,383 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 19,894 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 13,896 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 221 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, phonon_max_frequency, phonon band maximum, vibrational frequency, phonon spectrum.

<a id="materiaviva-property-largest-free-path-diameter"></a>
## MateriaViva — Largest free path diameter

Source-reported largest free path diameter values in Å, retained separately for each source and method. Keep the upstream geometric definition; do not merge automatically with pore_limiting_diameter despite related pore metrics. Direct access through MateriaViva; 30,179 linked structures and 2 original sources.

**Size:** 51,554 property values (source wording: 51,554).

**Scope:** largest_free_path_diameter.parquet: numeric; 30,179 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Largest free path diameter; Å; Adsorption and porous materials; largest_free_path_diameter; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_free_path_diameter.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_free_path_diameter.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_free_path_diameter.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/largest_free_path_diameter.parquet).

**Original sources / indirect access:**

- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 41,938 values; provider-declared class `open`.
- [CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (`core-mof`): 9,616 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 30,179 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): largest_free_path_diameter: 51,554 value rows; 30,179 distinct structure references; unit Å; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 41,938 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: CoRE MOF 2019 (public ASR/FSR)](https://zenodo.org/records/3677685) (checked 2026-11-01): MateriaViva source ID core-mof: 9,616 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, largest_free_path_diameter, free sphere diameter, porous free path.

<a id="materiaviva-property-pore-channel-count"></a>
## MateriaViva — Pore channel count

Source-reported pore channel count values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 27,089 linked structures and 1 original source.

**Size:** 41,942 property values (source wording: 41,942).

**Scope:** pore_channel_count.parquet: numeric; 27,089 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Pore channel count; unit not specified / unitless; Adsorption and porous materials; pore_channel_count; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_channel_count.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_channel_count.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_channel_count.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pore_channel_count.parquet).

**Original sources / indirect access:**

- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 41,942 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 27,089 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): pore_channel_count: 41,942 value rows; 27,089 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 41,942 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, pore_channel_count, porous channel number, pore connectivity, MOF channels.

<a id="materiaviva-property-lattice-thermal-conductivity"></a>
## MateriaViva — Lattice thermal conductivity

Source-reported lattice thermal conductivity values in W/m·K, retained separately for each source and method. Temperature, tensor averaging, isotope treatment, and calculation conventions are source dependent. Direct access through MateriaViva; 21,219 linked structures and 2 original sources.

**Size:** 39,461 property values (source wording: 39,461).

**Scope:** lattice_thermal_conductivity.parquet: numeric; 21,219 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Lattice thermal conductivity; W/m·K; Thermal and vibrational properties; lattice_thermal_conductivity; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 31,040 values; provider-declared class `open`.
- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 8,421 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 21,219 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): lattice_thermal_conductivity: 39,461 value rows; 21,219 distinct structure references; unit W/m·K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 31,040 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 8,421 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, lattice_thermal_conductivity, LTC, kappa L, phonon thermal transport, thermal conductivity.

<a id="materiaviva-property-symmetry-indicators"></a>
## MateriaViva — Symmetry indicators

Text descriptor for symmetry indicators, retained with its original source and method labels. Direct access through MateriaViva; 24,901 linked structures and 1 original source.

**Size:** 36,516 property values (source wording: 36,516).

**Scope:** symmetry_indicators.parquet: text descriptor; 24,901 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Symmetry indicators; unit not specified / unitless; Electronic and optical properties; symmetry_indicators; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/symmetry_indicators.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/symmetry_indicators.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/symmetry_indicators.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/symmetry_indicators.parquet).

**Original sources / indirect access:**

- [Materiae](https://cmpdc.iphy.ac.cn/materiae/) (`materiae`): 36,516 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 24,901 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): symmetry_indicators: 36,516 value rows; 24,901 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materiae](https://cmpdc.iphy.ac.cn/materiae/) (checked 2026-11-01): MateriaViva source ID materiae: 36,516 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, symmetry_indicators, topological symmetry indicators, topological materials, band topology.

<a id="materiaviva-property-max-residual-stress"></a>
## MateriaViva — Maximum residual stress

Source-reported maximum residual stress values in eV/Å³, retained separately for each source and method. This is a calculation-convergence diagnostic; the manifest uses eV/Å³, and the residual norm/component convention requires source inspection. Direct access through MateriaViva; 30,230 linked structures and 1 original source.

**Size:** 30,230 property values (source wording: 30,230).

**Scope:** max_residual_stress.parquet: numeric; 30,230 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum residual stress; eV/Å³; Calculation and refinement metadata; max_residual_stress; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_stress.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_stress.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_stress.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_residual_stress.parquet).

**Original sources / indirect access:**

- [ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (`elementa`): 30,230 values; provider-declared class `noncommercial`. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.

Other denominators (not added to the ranking):

- 30,230 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): max_residual_stress: 30,230 value rows; 30,230 distinct structure references; unit eV/Å³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: ELEMENTA and ELEMENTA Spin](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (checked 2026-11-01): MateriaViva source ID elementa: 30,230 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Source alias groups ELEMENTA and ELEMENTA Spin; the manifest does not assign property counts to each subrelease.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Calculation and refinement metadata, max_residual_stress, stress convergence, relaxation stress, residual stress.

<a id="materiaviva-property-tc-superconducting"></a>
## MateriaViva — Superconducting critical temperature

Source-reported superconducting critical temperature values in K, retained separately for each source and method. The sources mix experimental associations and computed superconducting critical temperatures; retain source/method labels and do not pool them as equivalent measurements. Direct access through MateriaViva; 4,092 linked structures and 4 original sources.

**Size:** 26,613 property values (source wording: 26,613).

**Scope:** tc_superconducting.parquet: numeric; 4,092 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Superconducting critical temperature; K; Superconductivity properties; tc_superconducting; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/tc_superconducting.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/tc_superconducting.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/tc_superconducting.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/tc_superconducting.parquet).

**Original sources / indirect access:**

- [3DSC superconductors](https://github.com/aimat-lab/3DSC) (`3dsc`): 17,797 values; provider-declared class `open`. MateriaViva registry identifies 3DSC_MP licensing only. Do not infer that these property rows distribute or grant access to the ICSD coordinate release.
- [SuperBand](https://github.com/ljcj007/SuperBand) (`superband`): 5,815 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,527 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 1,474 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 4,092 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): tc_superconducting: 26,613 value rows; 4,092 distinct structure references; unit K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: 3DSC superconductors](https://github.com/aimat-lab/3DSC) (checked 2026-11-01): MateriaViva source ID 3dsc: 17,797 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. MateriaViva registry identifies 3DSC_MP licensing only. Do not infer that these property rows distribute or grant access to the ICSD coordinate release.
- [Original source: SuperBand](https://github.com/ljcj007/SuperBand) (checked 2026-11-01): MateriaViva source ID superband: 5,815 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,527 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 1,474 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Superconductivity properties, tc_superconducting, Tc, critical temperature, superconductor, superconductivity, transition temperature.

<a id="materiaviva-property-heat-of-formation"></a>
## MateriaViva — Heat of formation

Source-reported heat of formation values in eV/atom, retained separately for each source and method. Kept separate from formation_energy_per_atom; source reference states and thermodynamic conventions must be retained. Direct access through MateriaViva; 24,570 linked structures and 1 original source.

**Size:** 24,944 property values (source wording: 24,944).

**Scope:** heat_of_formation.parquet: numeric; 24,570 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Heat of formation; eV/atom; Thermodynamic properties and stability; heat_of_formation; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_of_formation.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_of_formation.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_of_formation.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_of_formation.parquet).

**Original sources / indirect access:**

- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 24,944 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 24,570 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): heat_of_formation: 24,944 value rows; 24,570 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 24,944 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, heat_of_formation, formation enthalpy, formation energy, CMR formation heat.

<a id="materiaviva-property-mineral-name"></a>
## MateriaViva — Mineral name

Text descriptor for mineral name, retained with its original source and method labels. Direct access through MateriaViva; 4,682 linked structures and 6 original sources.

**Size:** 24,103 property values (source wording: 24,103).

**Scope:** mineral_name.parquet: text descriptor; 4,682 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Mineral name; unit not specified / unitless; Chemical and structural descriptors; mineral_name; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mineral_name.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mineral_name.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mineral_name.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mineral_name.parquet).

**Original sources / indirect access:**

- [American Mineralogist Crystal Structure Database](https://rruff.geo.arizona.edu/AMS/amcsd.php) (`amcsd`): 9,680 values; provider-declared class `unclear`. Historical AMCSD registry route is retained. Modern RRUFF catalog route is related, but record-level migration or accession correspondence is not independently established here.
- [Crystallography Open Database](https://www.crystallography.net/cod/) (`cod`): 9,151 values; provider-declared class `open`.
- [Inorganic Crystal Structure Database](https://icsd.fiz-karlsruhe.de/) (`icsd`): 3,802 values; provider-declared class `restricted`.
- [RRUFF](https://www.rruff.net/) (`rruff`): 937 values; provider-declared class `restricted`. Modern RRUFF access route from existing catalog; provider registry retains its archived historical licensing-evidence URL. Native accession-level correspondence was not re-audited.
- [Webmineral](https://webmineral.com/) (`webmineral`): 284 values; provider-declared class `unclear`. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.
- [AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (`aflow-prototypes`): 249 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 4,682 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): mineral_name: 24,103 value rows; 4,682 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: American Mineralogist Crystal Structure Database](https://rruff.geo.arizona.edu/AMS/amcsd.php) (checked 2026-11-01): MateriaViva source ID amcsd: 9,680 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Historical AMCSD registry route is retained. Modern RRUFF catalog route is related, but record-level migration or accession correspondence is not independently established here.
- [Original source: Crystallography Open Database](https://www.crystallography.net/cod/) (checked 2026-11-01): MateriaViva source ID cod: 9,151 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Inorganic Crystal Structure Database](https://icsd.fiz-karlsruhe.de/) (checked 2026-11-01): MateriaViva source ID icsd: 3,802 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: RRUFF](https://www.rruff.net/) (checked 2026-11-01): MateriaViva source ID rruff: 937 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Modern RRUFF access route from existing catalog; provider registry retains its archived historical licensing-evidence URL. Native accession-level correspondence was not re-audited.
- [Original source: Webmineral](https://webmineral.com/) (checked 2026-11-01): MateriaViva source ID webmineral: 284 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.
- [Original source: AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (checked 2026-11-01): MateriaViva source ID aflow-prototypes: 249 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, mineral_name, mineral identity, mineralogy.

<a id="materiaviva-property-debye-temperature"></a>
## MateriaViva — Debye temperature

Source-reported debye temperature values in K, retained separately for each source and method. Direct access through MateriaViva; 18,914 linked structures and 2 original sources.

**Size:** 23,387 property values (source wording: 23,387).

**Scope:** debye_temperature.parquet: numeric; 18,914 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Debye temperature; K; Thermal and vibrational properties; debye_temperature; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/debye_temperature.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/debye_temperature.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/debye_temperature.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/debye_temperature.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 15,520 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 7,867 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 18,914 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): debye_temperature: 23,387 value rows; 18,914 distinct structure references; unit K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 15,520 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,867 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, debye_temperature, phonon temperature, Debye model.

<a id="materiaviva-property-heat-capacity"></a>
## MateriaViva — Heat capacity

Source-reported heat capacity values in J/mol·K, retained separately for each source and method. The manifest does not establish constant-pressure versus constant-volume or the temperature; retain source and method conditions. Direct access through MateriaViva; 20,280 linked structures and 2 original sources.

**Size:** 21,761 property values (source wording: 21,761).

**Scope:** heat_capacity.parquet: numeric; 20,280 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Heat capacity; J/mol·K; Thermal and vibrational properties; heat_capacity; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_capacity.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_capacity.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_capacity.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/heat_capacity.parquet).

**Original sources / indirect access:**

- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 13,896 values; provider-declared class `open`.
- [AFLOW](https://aflow.org/) (`aflow`): 7,865 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 20,280 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): heat_capacity: 21,761 value rows; 20,280 distinct structure references; unit J/mol·K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 13,896 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,865 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, heat_capacity, specific heat, molar heat capacity, thermal properties.

<a id="materiaviva-property-average-voltage"></a>
## MateriaViva — Average battery voltage

Source-reported average battery voltage values in V, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** average_voltage.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Average battery voltage; V; Battery and ionic transport properties; average_voltage; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_voltage.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_voltage.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_voltage.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/average_voltage.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): average_voltage: 20,671 value rows; 17,376 distinct structure references; unit V; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, average_voltage, electrode voltage, electrochemical potential, battery voltage.

<a id="materiaviva-property-battery-formula"></a>
## MateriaViva — Battery formula

Text descriptor for battery formula, retained with its original source and method labels. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** battery_formula.parquet: text descriptor; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Battery formula; unit not specified / unitless; Battery and ionic transport properties; battery_formula; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/battery_formula.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/battery_formula.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/battery_formula.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/battery_formula.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): battery_formula: 20,671 value rows; 17,376 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, battery_formula, electrode formula, battery composition.

<a id="materiaviva-property-electrode-stability-charged"></a>
## MateriaViva — Charged electrode stability

Source-reported charged electrode stability values in eV/atom, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** electrode_stability_charged.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Charged electrode stability; eV/atom; Battery and ionic transport properties; electrode_stability_charged; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_charged.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_charged.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_charged.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_charged.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): electrode_stability_charged: 20,671 value rows; 17,376 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, electrode_stability_charged, charged state stability, electrode energy above hull.

<a id="materiaviva-property-electrode-stability-discharged"></a>
## MateriaViva — Discharged electrode stability

Source-reported discharged electrode stability values in eV/atom, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** electrode_stability_discharged.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Discharged electrode stability; eV/atom; Battery and ionic transport properties; electrode_stability_discharged; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_discharged.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_discharged.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_discharged.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_stability_discharged.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): electrode_stability_discharged: 20,671 value rows; 17,376 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, electrode_stability_discharged, discharged state stability, electrode energy above hull.

<a id="materiaviva-property-electrode-volume-change"></a>
## MateriaViva — Electrode volume change

Source-reported electrode volume change values in fraction, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** electrode_volume_change.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Electrode volume change; fraction; Battery and ionic transport properties; electrode_volume_change; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_volume_change.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_volume_change.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_volume_change.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electrode_volume_change.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): electrode_volume_change: 20,671 value rows; 17,376 distinct structure references; unit fraction; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, electrode_volume_change, battery volume expansion, intercalation volume change.

<a id="materiaviva-property-capacity-gravimetric"></a>
## MateriaViva — Gravimetric battery capacity

Source-reported gravimetric battery capacity values in mAh/g, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** capacity_gravimetric.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Gravimetric battery capacity; mAh/g; Battery and ionic transport properties; capacity_gravimetric; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_gravimetric.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_gravimetric.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_gravimetric.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_gravimetric.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): capacity_gravimetric: 20,671 value rows; 17,376 distinct structure references; unit mAh/g; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, capacity_gravimetric, specific capacity, electrode capacity, charge storage.

<a id="materiaviva-property-energy-density-gravimetric"></a>
## MateriaViva — Gravimetric battery energy density

Source-reported gravimetric battery energy density values in Wh/kg, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** energy_density_gravimetric.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Gravimetric battery energy density; Wh/kg; Battery and ionic transport properties; energy_density_gravimetric; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_gravimetric.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_gravimetric.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_gravimetric.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_gravimetric.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): energy_density_gravimetric: 20,671 value rows; 17,376 distinct structure references; unit Wh/kg; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, energy_density_gravimetric, specific energy, Wh per kg, battery energy.

<a id="materiaviva-property-max-voltage-step"></a>
## MateriaViva — Maximum battery voltage step

Source-reported maximum battery voltage step values in V, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** max_voltage_step.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum battery voltage step; V; Battery and ionic transport properties; max_voltage_step; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_voltage_step.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_voltage_step.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_voltage_step.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/max_voltage_step.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): max_voltage_step: 20,671 value rows; 17,376 distinct structure references; unit V; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, max_voltage_step, voltage profile, largest voltage step, electrode voltage.

<a id="materiaviva-property-num-voltage-steps"></a>
## MateriaViva — Number of battery voltage steps

Source-reported number of battery voltage steps values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** num_voltage_steps.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Number of battery voltage steps; unit not specified / unitless; Battery and ionic transport properties; num_voltage_steps; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/num_voltage_steps.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/num_voltage_steps.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/num_voltage_steps.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/num_voltage_steps.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): num_voltage_steps: 20,671 value rows; 17,376 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, num_voltage_steps, voltage profile steps, electrode voltage plateaus.

<a id="materiaviva-property-capacity-volumetric"></a>
## MateriaViva — Volumetric battery capacity

Source-reported volumetric battery capacity values in mAh/cm³, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** capacity_volumetric.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Volumetric battery capacity; mAh/cm³; Battery and ionic transport properties; capacity_volumetric; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_volumetric.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_volumetric.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_volumetric.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/capacity_volumetric.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): capacity_volumetric: 20,671 value rows; 17,376 distinct structure references; unit mAh/cm³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, capacity_volumetric, volumetric capacity, electrode capacity, charge storage.

<a id="materiaviva-property-energy-density-volumetric"></a>
## MateriaViva — Volumetric battery energy density

Source-reported volumetric battery energy density values in Wh/L, retained separately for each source and method. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** energy_density_volumetric.parquet: numeric; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Volumetric battery energy density; Wh/L; Battery and ionic transport properties; energy_density_volumetric; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_volumetric.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_volumetric.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_volumetric.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/energy_density_volumetric.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): energy_density_volumetric: 20,671 value rows; 17,376 distinct structure references; unit Wh/L; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, energy_density_volumetric, energy per volume, Wh per L, battery energy.

<a id="materiaviva-property-working-ion"></a>
## MateriaViva — Working battery ion

Text descriptor for working battery ion, retained with its original source and method labels. Direct access through MateriaViva; 17,376 linked structures and 1 original source.

**Size:** 20,671 property values (source wording: 20,671).

**Scope:** working_ion.parquet: text descriptor; 17,376 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Working battery ion; unit not specified / unitless; Battery and ionic transport properties; working_ion; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_ion.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_ion.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_ion.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/working_ion.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 20,671 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 17,376 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): working_ion: 20,671 value rows; 17,376 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 20,671 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, working_ion, mobile battery ion, intercalating ion, charge carrier.

<a id="materiaviva-property-framework-bond-dissociation-energy"></a>
## MateriaViva — Framework bond dissociation energy

Source-reported framework bond dissociation energy values in eV/atom, retained separately for each source and method. The manifest uses eV/atom; inspect the FAIR-MOFs definition before interpreting it as an individual bond dissociation energy. Direct access through MateriaViva; 20,194 linked structures and 1 original source.

**Size:** 20,243 property values (source wording: 20,243).

**Scope:** framework_bond_dissociation_energy.parquet: numeric; 20,194 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Framework bond dissociation energy; eV/atom; Adsorption and porous materials; framework_bond_dissociation_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_bond_dissociation_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_bond_dissociation_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_bond_dissociation_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/framework_bond_dissociation_energy.parquet).

**Original sources / indirect access:**

- [FAIR-MOFs](https://zenodo.org/records/13254307) (`fair-mofs`): 20,243 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 20,194 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): framework_bond_dissociation_energy: 20,243 value rows; 20,194 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: FAIR-MOFs](https://zenodo.org/records/13254307) (checked 2026-11-01): MateriaViva source ID fair-mofs: 20,243 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, framework_bond_dissociation_energy, MOF bond strength, bond breaking energy, framework stability.

<a id="materiaviva-property-elastic-anisotropy"></a>
## MateriaViva — Elastic anisotropy

Source-reported elastic anisotropy values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 18,182 linked structures and 1 original source.

**Size:** 18,255 property values (source wording: 18,255).

**Scope:** elastic_anisotropy.parquet: numeric; 18,182 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Elastic anisotropy; unit not specified / unitless; Mechanical and elastic properties; elastic_anisotropy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elastic_anisotropy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elastic_anisotropy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elastic_anisotropy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elastic_anisotropy.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 18,255 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 18,182 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): elastic_anisotropy: 18,255 value rows; 18,182 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 18,255 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, elastic_anisotropy, elastic anisotropy index, mechanical anisotropy.

<a id="materiaviva-property-nmr-efg-max"></a>
## MateriaViva — Maximum electric field gradient

Source-reported maximum electric field gradient values in V/m², retained separately for each source and method. This is a maximum electric-field-gradient summary in V/m², not a complete EFG tensor, NMR spectrum, or chemical shift. Direct access through MateriaViva; 16,175 linked structures and 1 original source.

**Size:** 17,636 property values (source wording: 17,636).

**Scope:** nmr_efg_max.parquet: numeric; 16,175 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum electric field gradient; V/m²; Electronic and optical properties; nmr_efg_max; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/nmr_efg_max.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/nmr_efg_max.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/nmr_efg_max.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/nmr_efg_max.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 17,636 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 16,175 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): nmr_efg_max: 17,636 value rows; 16,175 distinct structure references; unit V/m²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 17,636 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, nmr_efg_max, NMR EFG, nuclear magnetic resonance, electric field gradient, quadrupolar interaction.

<a id="materiaviva-property-dielectric-constant-ionic"></a>
## MateriaViva — Ionic dielectric constant

Source-reported ionic dielectric constant values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 13,361 linked structures and 3 original sources.

**Size:** 17,104 property values (source wording: 17,104).

**Scope:** dielectric_constant_ionic.parquet: numeric; 13,361 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Ionic dielectric constant; unit not specified / unitless; Dielectric and electromechanical properties; dielectric_constant_ionic; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_ionic.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_ionic.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_ionic.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dielectric_constant_ionic.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 9,105 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 6,927 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,072 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 13,361 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): dielectric_constant_ionic: 17,104 value rows; 13,361 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 9,105 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 6,927 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,072 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Dielectric and electromechanical properties, dielectric_constant_ionic, ionic permittivity, lattice dielectric contribution.

<a id="materiaviva-property-spillage"></a>
## MateriaViva — Spin–orbit spillage

Source-reported spin–orbit spillage values; the manifest supplies no unit, so retain the upstream definition and normalization. A spin–orbit wavefunction-overlap screening metric, not a direct topological invariant or proof of a topological phase. Direct access through MateriaViva; 16,003 linked structures and 2 original sources.

**Size:** 16,656 property values (source wording: 16,656).

**Scope:** spillage.parquet: numeric; 16,003 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Spin–orbit spillage; unit not specified / unitless; Electronic and optical properties; spillage; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spillage.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spillage.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spillage.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/spillage.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 15,952 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 704 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 16,003 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): spillage: 16,656 value rows; 16,003 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 15,952 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 704 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, spillage, SOC spillage, spin orbit coupling, topological screening.

<a id="materiaviva-property-refractive-index"></a>
## MateriaViva — Refractive index

Source-reported refractive index values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 13,287 linked structures and 3 original sources.

**Size:** 15,273 property values (source wording: 15,273).

**Scope:** refractive_index.parquet: numeric; 13,287 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Refractive index; unit not specified / unitless; Electronic and optical properties; refractive_index; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/refractive_index.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/refractive_index.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/refractive_index.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/refractive_index.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 9,104 values; provider-declared class `open`.
- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 6,050 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [Webmineral](https://webmineral.com/) (`webmineral`): 119 values; provider-declared class `unclear`. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.

Other denominators (not added to the ranking):

- 13,287 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): refractive_index: 15,273 value rows; 13,287 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 9,104 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 6,050 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.
- [Original source: Webmineral](https://webmineral.com/) (checked 2026-11-01): MateriaViva source ID webmineral: 119 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, refractive_index, optical index, refraction, optical materials.

<a id="materiaviva-property-slme"></a>
## MateriaViva — Spectroscopic limited maximum efficiency

Source-reported spectroscopic limited maximum efficiency values in %, retained separately for each source and method. A modeled photovoltaic efficiency metric reported in percent; it is not a measured device power-conversion efficiency. Direct access through MateriaViva; 12,430 linked structures and 2 original sources.

**Size:** 13,715 property values (source wording: 13,715).

**Scope:** slme.parquet: numeric; 12,430 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Spectroscopic limited maximum efficiency; %; Electronic and optical properties; slme; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/slme.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/slme.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/slme.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/slme.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 13,504 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 211 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 12,430 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): slme: 13,715 value rows; 12,430 distinct structure references; unit %; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 13,504 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 211 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, slme, SLME, solar cell efficiency, photovoltaic efficiency.

<a id="materiaviva-property-structure-prediction-r-factor"></a>
## MateriaViva — Structure-prediction R factor

Source-reported structure-prediction r factor values; the manifest supplies no unit, so retain the upstream definition and normalization. A source-defined structure-prediction metric, distinct from the crystallographic r_factor table; retain its original definition. Direct access through MateriaViva; 12,415 linked structures and 1 original source.

**Size:** 12,415 property values (source wording: 12,415).

**Scope:** structure_prediction_r_factor.parquet: numeric; 12,415 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Structure-prediction R factor; unit not specified / unitless; Calculation and refinement metadata; structure_prediction_r_factor; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prediction_r_factor.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prediction_r_factor.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prediction_r_factor.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/structure_prediction_r_factor.parquet).

**Original sources / indirect access:**

- [Predicted Crystallography Open Database](https://www.crystallography.net/pcod/) (`pcod`): 12,415 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 12,415 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): structure_prediction_r_factor: 12,415 value rows; 12,415 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Predicted Crystallography Open Database](https://www.crystallography.net/pcod/) (checked 2026-11-01): MateriaViva source ID pcod: 12,415 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Calculation and refinement metadata, structure_prediction_r_factor, predicted structure R factor, PCOD R factor, structure prediction.

<a id="materiaviva-property-piezoelectric-modulus"></a>
## MateriaViva — Piezoelectric modulus

Source-reported piezoelectric modulus values in C/m², retained separately for each source and method. The manifest uses C/m², consistent with a piezoelectric stress coefficient; do not relabel it as a pC/N strain coefficient or assume a complete tensor. Direct access through MateriaViva; 8,663 linked structures and 2 original sources.

**Size:** 10,974 property values (source wording: 10,974).

**Scope:** piezoelectric_modulus.parquet: numeric; 8,663 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Piezoelectric modulus; C/m²; Dielectric and electromechanical properties; piezoelectric_modulus; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_modulus.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_modulus.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_modulus.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_modulus.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 6,921 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 4,053 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 8,663 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): piezoelectric_modulus: 10,974 value rows; 8,663 distinct structure references; unit C/m²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 6,921 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 4,053 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Dielectric and electromechanical properties, piezoelectric_modulus, piezoelectric coefficient, piezoelectric tensor, polar materials.

<a id="materiaviva-property-lattice-thermal-conductivity-coherence"></a>
## MateriaViva — Lattice thermal conductivity — coherence contribution

Source-reported lattice thermal conductivity — coherence contribution values in W/m·K, retained separately for each source and method. A source-defined coherence contribution; it is not necessarily interchangeable with a separately reported total lattice conductivity. Direct access through MateriaViva; 7,689 linked structures and 1 original source.

**Size:** 8,434 property values (source wording: 8,434).

**Scope:** lattice_thermal_conductivity_coherence.parquet: numeric; 7,689 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Lattice thermal conductivity — coherence contribution; W/m·K; Thermal and vibrational properties; lattice_thermal_conductivity_coherence; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_coherence.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_coherence.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_coherence.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_coherence.parquet).

**Original sources / indirect access:**

- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 8,434 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 7,689 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): lattice_thermal_conductivity_coherence: 8,434 value rows; 7,689 distinct structure references; unit W/m·K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 8,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, lattice_thermal_conductivity_coherence, coherent thermal transport, kappa coherence, Wigner thermal conductivity.

<a id="materiaviva-property-lattice-thermal-conductivity-particle"></a>
## MateriaViva — Lattice thermal conductivity — particle contribution

Source-reported lattice thermal conductivity — particle contribution values in W/m·K, retained separately for each source and method. A source-defined particle contribution; it is not necessarily interchangeable with a separately reported total lattice conductivity. Direct access through MateriaViva; 7,678 linked structures and 1 original source.

**Size:** 8,420 property values (source wording: 8,420).

**Scope:** lattice_thermal_conductivity_particle.parquet: numeric; 7,678 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Lattice thermal conductivity — particle contribution; W/m·K; Thermal and vibrational properties; lattice_thermal_conductivity_particle; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_particle.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_particle.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_particle.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/lattice_thermal_conductivity_particle.parquet).

**Original sources / indirect access:**

- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 8,420 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 7,678 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): lattice_thermal_conductivity_particle: 8,420 value rows; 7,678 distinct structure references; unit W/m·K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 8,420 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, lattice_thermal_conductivity_particle, particle thermal transport, kappa particle, phonon gas contribution.

<a id="materiaviva-property-eos-bulk-modulus"></a>
## MateriaViva — Equation-of-state bulk modulus

Source-reported equation-of-state bulk modulus values in GPa, retained separately for each source and method. Retained separately from bulk_modulus_eos; source fitting conventions and data populations can differ. Direct access through MateriaViva; 8,060 linked structures and 1 original source.

**Size:** 8,350 property values (source wording: 8,350).

**Scope:** eos_bulk_modulus.parquet: numeric; 8,060 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Equation-of-state bulk modulus; GPa; Mechanical and elastic properties; eos_bulk_modulus; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/eos_bulk_modulus.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/eos_bulk_modulus.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/eos_bulk_modulus.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/eos_bulk_modulus.parquet).

**Original sources / indirect access:**

- [Phonix anharmonic phonon database](https://phonix-db.org/) (`phonix`): 8,350 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 8,060 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): eos_bulk_modulus: 8,350 value rows; 8,060 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Phonix anharmonic phonon database](https://phonix-db.org/) (checked 2026-11-01): MateriaViva source ID phonix: 8,350 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, eos_bulk_modulus, EOS bulk modulus, compressibility, PHONIX bulk modulus.

<a id="materiaviva-property-thermal-conductivity"></a>
## MateriaViva — Thermal conductivity

Source-reported thermal conductivity values in W/m·K, retained separately for each source and method. The normalized name does not specify electronic versus lattice contributions, tensor averaging, or temperature; keep it separate from lattice_thermal_conductivity unless the AFLOW definition establishes equivalence. Direct access through MateriaViva; 7,710 linked structures and 1 original source.

**Size:** 7,867 property values (source wording: 7,867).

**Scope:** thermal_conductivity.parquet: numeric; 7,710 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Thermal conductivity; W/m·K; Thermal and vibrational properties; thermal_conductivity; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_conductivity.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_conductivity.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_conductivity.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_conductivity.parquet).

**Original sources / indirect access:**

- [AFLOW](https://aflow.org/) (`aflow`): 7,867 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 7,710 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): thermal_conductivity: 7,867 value rows; 7,710 distinct structure references; unit W/m·K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,867 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, thermal_conductivity, thermal transport, kappa, heat conduction, AFLOW thermal conductivity.

<a id="materiaviva-property-thermal-expansion"></a>
## MateriaViva — Thermal expansion coefficient

Source-reported thermal expansion coefficient values in 1/K, retained separately for each source and method. The scalar 1/K unit alone does not specify linear versus volumetric expansion, temperature, or tensor convention. Direct access through MateriaViva; 7,708 linked structures and 1 original source.

**Size:** 7,865 property values (source wording: 7,865).

**Scope:** thermal_expansion.parquet: numeric; 7,708 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Thermal expansion coefficient; 1/K; Thermal and vibrational properties; thermal_expansion; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_expansion.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_expansion.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_expansion.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/thermal_expansion.parquet).

**Original sources / indirect access:**

- [AFLOW](https://aflow.org/) (`aflow`): 7,865 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 7,708 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): thermal_expansion: 7,865 value rows; 7,708 distinct structure references; unit 1/K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: AFLOW](https://aflow.org/) (checked 2026-11-01): MateriaViva source ID aflow: 7,865 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, thermal_expansion, thermal expansivity, expansion coefficient, temperature expansion.

<a id="materiaviva-property-born-effective-charge-max"></a>
## MateriaViva — Maximum Born effective charge

Source-reported maximum born effective charge values in e, retained separately for each source and method. This is a scalar maximum summary, not the complete Born effective-charge tensor. Direct access through MateriaViva; 7,558 linked structures and 1 original source.

**Size:** 7,741 property values (source wording: 7,741).

**Scope:** born_effective_charge_max.parquet: numeric; 7,558 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum Born effective charge; e; Dielectric and electromechanical properties; born_effective_charge_max; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/born_effective_charge_max.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/born_effective_charge_max.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/born_effective_charge_max.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/born_effective_charge_max.parquet).

**Original sources / indirect access:**

- [NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (`phonondb`): 7,741 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 7,558 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): born_effective_charge_max: 7,741 value rows; 7,558 distinct structure references; unit e; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIMS MDR phonon database (phonondb)](https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en) (checked 2026-11-01): MateriaViva source ID phonondb: 7,741 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Dielectric and electromechanical properties, born_effective_charge_max, dynamical charge, Born charge, Z star.

<a id="materiaviva-property-exfoliation-energy"></a>
## MateriaViva — Exfoliation energy

Source-reported exfoliation energy values in meV/atom, retained separately for each source and method. Direct access through MateriaViva; 5,824 linked structures and 3 original sources.

**Size:** 6,815 property values (source wording: 6,815).

**Scope:** exfoliation_energy.parquet: numeric; 5,824 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Exfoliation energy; meV/atom; Surface and interface properties; exfoliation_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/exfoliation_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/exfoliation_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/exfoliation_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/exfoliation_energy.parquet).

**Original sources / indirect access:**

- [2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (`2dmatpedia`): 4,693 values; provider-declared class `open`.
- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 1,257 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 865 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 5,824 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): exfoliation_energy: 6,815 value rows; 5,824 distinct structure references; unit meV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: 2DMatPedia](https://doi.org/10.6084/m9.figshare.7699910.v3) (checked 2026-11-01): MateriaViva source ID 2dmatpedia: 4,693 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 1,257 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 865 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, exfoliation_energy, layer exfoliation, 2D materials, cleavage energy.

<a id="materiaviva-property-gllbsc-derivative-discontinuity"></a>
## MateriaViva — GLLB-SC derivative discontinuity

Source-reported gllb-sc derivative discontinuity values in eV, retained separately for each source and method. Direct access through MateriaViva; 6,183 linked structures and 1 original source.

**Size:** 6,571 property values (source wording: 6,571).

**Scope:** gllbsc_derivative_discontinuity.parquet: numeric; 6,183 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** GLLB-SC derivative discontinuity; eV; Electronic and optical properties; gllbsc_derivative_discontinuity; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/gllbsc_derivative_discontinuity.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/gllbsc_derivative_discontinuity.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/gllbsc_derivative_discontinuity.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/gllbsc_derivative_discontinuity.parquet).

**Original sources / indirect access:**

- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 6,571 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 6,183 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): gllbsc_derivative_discontinuity: 6,571 value rows; 6,183 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 6,571 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, gllbsc_derivative_discontinuity, GLLBSC, band gap correction, exchange correlation discontinuity.

<a id="materiaviva-property-birefringence"></a>
## MateriaViva — Birefringence

Source-reported birefringence values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 4,796 linked structures and 1 original source.

**Size:** 6,050 property values (source wording: 6,050).

**Scope:** birefringence.parquet: numeric; 4,796 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Birefringence; unit not specified / unitless; Electronic and optical properties; birefringence; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/birefringence.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/birefringence.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/birefringence.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/birefringence.parquet).

**Original sources / indirect access:**

- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 6,050 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 4,796 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): birefringence: 6,050 value rows; 4,796 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 6,050 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, birefringence, optical anisotropy, refractive index difference.

<a id="materiaviva-property-effective-mass-electron"></a>
## MateriaViva — Electron effective mass

Source-reported electron effective mass values in m_e, retained separately for each source and method. The table is a normalized effective-mass summary; directional, tensor, and extremum conventions depend on the source. Direct access through MateriaViva; 5,209 linked structures and 3 original sources.

**Size:** 5,701 property values (source wording: 5,701).

**Scope:** effective_mass_electron.parquet: numeric; 5,209 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Electron effective mass; m_e; Electronic and optical properties; effective_mass_electron; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_electron.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_electron.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_electron.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_electron.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 4,769 values; provider-declared class `open`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 830 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 102 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 5,209 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): effective_mass_electron: 5,701 value rows; 5,209 distinct structure references; unit m_e; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 4,769 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 830 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 102 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, effective_mass_electron, electron mobility, conduction effective mass, m star.

<a id="materiaviva-property-effective-mass-hole"></a>
## MateriaViva — Hole effective mass

Source-reported hole effective mass values in m_e, retained separately for each source and method. The table is a normalized effective-mass summary; directional, tensor, and extremum conventions depend on the source. Direct access through MateriaViva; 5,193 linked structures and 3 original sources.

**Size:** 5,687 property values (source wording: 5,687).

**Scope:** effective_mass_hole.parquet: numeric; 5,193 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Hole effective mass; m_e; Electronic and optical properties; effective_mass_hole; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_hole.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_hole.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_hole.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/effective_mass_hole.parquet).

**Original sources / indirect access:**

- [NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (`jarvis-dft`): 4,770 values; provider-declared class `open`.
- [DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (`cmr-static`): 830 values; provider-declared class `open`.
- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 87 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 5,193 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): effective_mass_hole: 5,687 value rows; 5,193 distinct structure references; unit m_e; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS-DFT 3D](https://doi.org/10.6084/m9.figshare.6815699) (checked 2026-11-01): MateriaViva source ID jarvis-dft: 4,770 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: DTU Computational Materials Repository](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): MateriaViva source ID cmr-static: 830 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 87 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, effective_mass_hole, hole mobility, valence effective mass, m star.

<a id="materiaviva-property-superconductor-class"></a>
## MateriaViva — Superconductor class

Text descriptor for superconductor class, retained with its original source and method labels. Direct access through MateriaViva; 1,918 linked structures and 1 original source.

**Size:** 5,540 property values (source wording: 5,540).

**Scope:** superconductor_class.parquet: text descriptor; 1,918 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Superconductor class; unit not specified / unitless; Superconductivity properties; superconductor_class; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/superconductor_class.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/superconductor_class.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/superconductor_class.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/superconductor_class.parquet).

**Original sources / indirect access:**

- [3DSC superconductors](https://github.com/aimat-lab/3DSC) (`3dsc`): 5,540 values; provider-declared class `open`. MateriaViva registry identifies 3DSC_MP licensing only. Do not infer that these property rows distribute or grant access to the ICSD coordinate release.

Other denominators (not added to the ranking):

- 1,918 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): superconductor_class: 5,540 value rows; 1,918 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: 3DSC superconductors](https://github.com/aimat-lab/3DSC) (checked 2026-11-01): MateriaViva source ID 3dsc: 5,540 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. MateriaViva registry identifies 3DSC_MP licensing only. Do not infer that these property rows distribute or grant access to the ICSD coordinate release.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Superconductivity properties, superconductor_class, superconductivity family, superconducting material type, superconductor classification.

<a id="materiaviva-property-magnetic-polarization"></a>
## MateriaViva — Magnetic polarization

Source-reported magnetic polarization values in T, retained separately for each source and method. Direct access through MateriaViva; 5,309 linked structures and 1 original source.

**Size:** 5,434 property values (source wording: 5,434).

**Scope:** magnetic_polarization.parquet: numeric; 5,309 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetic polarization; T; Magnetic and spin properties; magnetic_polarization; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_polarization.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_polarization.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_polarization.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_polarization.parquet).

**Original sources / indirect access:**

- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 5,434 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 5,309 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): magnetic_polarization: 5,434 value rows; 5,309 distinct structure references; unit T; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 5,434 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, magnetic_polarization, magnetic induction, polarization T, permanent magnet.

<a id="materiaviva-property-interlayer-binding-energy"></a>
## MateriaViva — Interlayer binding energy

Source-reported interlayer binding energy values in meV/Å², retained separately for each source and method. Direct access through MateriaViva; 3,086 linked structures and 1 original source.

**Size:** 4,712 property values (source wording: 4,712).

**Scope:** interlayer_binding_energy.parquet: numeric; 3,086 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Interlayer binding energy; meV/Å²; Surface and interface properties; interlayer_binding_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/interlayer_binding_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/interlayer_binding_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/interlayer_binding_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/interlayer_binding_energy.parquet).

**Original sources / indirect access:**

- [Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (`mc2d`): 4,712 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 3,086 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): interlayer_binding_energy: 4,712 value rows; 3,086 distinct structure references; unit meV/Å²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Cloud MC2D](https://archive.materialscloud.org/records/17gf6-84915) (checked 2026-11-01): MateriaViva source ID mc2d: 4,712 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, interlayer_binding_energy, layer adhesion, layered materials, van der Waals binding.

<a id="materiaviva-property-measurement-pressure"></a>
## MateriaViva — Measurement pressure

Source-reported measurement pressure values in GPa, retained separately for each source and method. Direct access through MateriaViva; 1,303 linked structures and 2 original sources.

**Size:** 4,443 property values (source wording: 4,443).

**Scope:** measurement_pressure.parquet: numeric; 1,303 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Measurement pressure; GPa; Calculation and refinement metadata; measurement_pressure; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_pressure.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_pressure.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_pressure.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measurement_pressure.parquet).

**Original sources / indirect access:**

- [Crystallography Open Database](https://www.crystallography.net/cod/) (`cod`): 3,712 values; provider-declared class `open`.
- [HEX high-pressure elemental crystal structures](https://doi.org/10.6084/m9.figshare.25403968.v1) (`hex-high-pressure`): 731 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 1,303 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): measurement_pressure: 4,443 value rows; 1,303 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Crystallography Open Database](https://www.crystallography.net/cod/) (checked 2026-11-01): MateriaViva source ID cod: 3,712 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: HEX high-pressure elemental crystal structures](https://doi.org/10.6084/m9.figshare.25403968.v1) (checked 2026-11-01): MateriaViva source ID hex-high-pressure: 731 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Calculation and refinement metadata, measurement_pressure, experimental pressure, pressure conditions, high pressure.

<a id="materiaviva-property-work-function"></a>
## MateriaViva — Work function

Source-reported work function values in eV, retained separately for each source and method. Direct access through MateriaViva; 3,725 linked structures and 2 original sources.

**Size:** 4,225 property values (source wording: 4,225).

**Scope:** work_function.parquet: numeric; 3,725 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Work function; eV; Electronic and optical properties; work_function; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_function.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_function.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_function.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_function.parquet).

**Original sources / indirect access:**

- [Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (`c2db`): 3,530 values; provider-declared class `open`.
- [Materials Project](https://materialsproject.org/) (`materials-project`): 695 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 3,725 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): work_function: 4,225 value rows; 3,725 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Computational 2D Materials Database](https://2dhub.org/c2db/c2db.html) (checked 2026-11-01): MateriaViva source ID c2db: 3,530 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 695 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, work_function, electron emission energy, vacuum level, photoemission.

<a id="materiaviva-property-piezoelectric-max-direction"></a>
## MateriaViva — Direction of maximum piezoelectric response

Text descriptor for direction of maximum piezoelectric response, retained with its original source and method labels. Direct access through MateriaViva; 3,979 linked structures and 1 original source.

**Size:** 4,053 property values (source wording: 4,053).

**Scope:** piezoelectric_max_direction.parquet: text descriptor; 3,979 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Direction of maximum piezoelectric response; unit not specified / unitless; Dielectric and electromechanical properties; piezoelectric_max_direction; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_max_direction.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_max_direction.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_max_direction.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/piezoelectric_max_direction.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 4,053 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 3,979 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): piezoelectric_max_direction: 4,053 value rows; 3,979 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 4,053 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Dielectric and electromechanical properties, piezoelectric_max_direction, piezoelectric orientation, maximum piezoelectric direction.

<a id="materiaviva-property-continuous-symmetry-measure"></a>
## MateriaViva — Continuous symmetry measure

Source-reported continuous symmetry measure values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 3,740 linked structures and 1 original source.

**Size:** 3,940 property values (source wording: 3,940).

**Scope:** continuous_symmetry_measure.parquet: numeric; 3,740 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Continuous symmetry measure; unit not specified / unitless; Chemical and structural descriptors; continuous_symmetry_measure; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/continuous_symmetry_measure.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/continuous_symmetry_measure.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/continuous_symmetry_measure.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/continuous_symmetry_measure.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 3,940 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 3,740 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): continuous_symmetry_measure: 3,940 value rows; 3,740 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 3,940 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, continuous_symmetry_measure, CSM, local symmetry, coordination distortion.

<a id="materiaviva-property-coordination-environments"></a>
## MateriaViva — Coordination environments

Text descriptor for coordination environments, retained with its original source and method labels. Direct access through MateriaViva; 3,740 linked structures and 1 original source.

**Size:** 3,940 property values (source wording: 3,940).

**Scope:** coordination_environments.parquet: text descriptor; 3,740 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Coordination environments; unit not specified / unitless; Chemical and structural descriptors; coordination_environments; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/coordination_environments.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/coordination_environments.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/coordination_environments.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/coordination_environments.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 3,940 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 3,740 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): coordination_environments: 3,940 value rows; 3,740 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 3,940 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, coordination_environments, local coordination, coordination geometry.

<a id="materiaviva-property-shg-coefficient"></a>
## MateriaViva — Second-harmonic generation coefficient

Source-reported second-harmonic generation coefficient values in pm/V, retained separately for each source and method. A source-defined scalar second-harmonic generation coefficient in pm/V; tensor component, frequency, and convention require upstream inspection. Direct access through MateriaViva; 2,566 linked structures and 1 original source.

**Size:** 3,429 property values (source wording: 3,429).

**Scope:** shg_coefficient.parquet: numeric; 2,566 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Second-harmonic generation coefficient; pm/V; Electronic and optical properties; shg_coefficient; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shg_coefficient.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shg_coefficient.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shg_coefficient.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/shg_coefficient.parquet).

**Original sources / indirect access:**

- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 3,429 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 2,566 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): shg_coefficient: 3,429 value rows; 2,566 distinct structure references; unit pm/V; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 3,429 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, shg_coefficient, SHG, nonlinear optical coefficient, second order optical response.

<a id="materiaviva-property-migration-barrier"></a>
## MateriaViva — Ion migration barrier

Source-reported ion migration barrier values in eV, retained separately for each source and method. Keep the original migrating species, pathway, and calculation or measurement conditions; the scalar energy alone does not specify ionic conductivity. Direct access through MateriaViva; 214 linked structures and 1 original source.

**Size:** 2,985 property values (source wording: 2,985).

**Scope:** migration_barrier.parquet: numeric; 214 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Ion migration barrier; eV; Battery and ionic transport properties; migration_barrier; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/migration_barrier.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/migration_barrier.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/migration_barrier.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/migration_barrier.parquet).

**Original sources / indirect access:**

- [Solid-electrolyte screening platform](https://doi.org/10.6084/m9.figshare.12011412.v1) (`spse`): 2,985 values; provider-declared class `unclear`. Property provenance is the SPSE ion-transport dataset; structure licensing and availability are separate from migration-barrier access. Exact figshare release is already verified in the canonical catalog.

Other denominators (not added to the ranking):

- 214 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): migration_barrier: 2,985 value rows; 214 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Solid-electrolyte screening platform](https://doi.org/10.6084/m9.figshare.12011412.v1) (checked 2026-11-01): MateriaViva source ID spse: 2,985 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Property provenance is the SPSE ion-transport dataset; structure licensing and availability are separate from migration-barrier access. Exact figshare release is already verified in the canonical catalog.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, migration_barrier, diffusion barrier, activation energy, ionic transport, migration energy.

<a id="materiaviva-property-electron-phonon-coupling"></a>
## MateriaViva — Electron–phonon coupling

Source-reported electron–phonon coupling values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 1,431 linked structures and 1 original source.

**Size:** 1,526 property values (source wording: 1,526).

**Scope:** electron_phonon_coupling.parquet: numeric; 1,431 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Electron–phonon coupling; unit not specified / unitless; Superconductivity properties; electron_phonon_coupling; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electron_phonon_coupling.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electron_phonon_coupling.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electron_phonon_coupling.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/electron_phonon_coupling.parquet).

**Original sources / indirect access:**

- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,526 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 1,431 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): electron_phonon_coupling: 1,526 value rows; 1,431 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,526 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Superconductivity properties, electron_phonon_coupling, EPC, lambda, electron phonon interaction, superconductivity.

<a id="materiaviva-property-phonon-log-average-frequency"></a>
## MateriaViva — Logarithmic average phonon frequency

Source-reported logarithmic average phonon frequency values in K, retained separately for each source and method. Reported in kelvin as a frequency-equivalent temperature; do not interpret the values directly as THz. Direct access through MateriaViva; 1,431 linked structures and 1 original source.

**Size:** 1,526 property values (source wording: 1,526).

**Scope:** phonon_log_average_frequency.parquet: numeric; 1,431 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Logarithmic average phonon frequency; K; Superconductivity properties; phonon_log_average_frequency; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_log_average_frequency.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_log_average_frequency.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_log_average_frequency.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/phonon_log_average_frequency.parquet).

**Original sources / indirect access:**

- [NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (`jarvis-specialized-structures`): 1,526 values; provider-declared class `open`. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

Other denominators (not added to the ranking):

- 1,431 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): phonon_log_average_frequency: 1,526 value rows; 1,431 distinct structure references; unit K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NIST JARVIS specialized structure datasets](https://jarvis-tools.readthedocs.io/en/master/databases.html) (checked 2026-11-01): MateriaViva source ID jarvis-specialized-structures: 1,526 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped source alias spans specialized JARVIS datasets. Registry evidence URL 6815705 is specifically the JARVIS-DFT 2D release, not a manifest of all specialized inputs. Link to the JARVIS dataset index for access; native record IDs/methods are needed to resolve individual subreleases.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Superconductivity properties, phonon_log_average_frequency, omega log, log phonon frequency, EPC, superconductivity.

<a id="materiaviva-property-magnetic-anisotropy-constant"></a>
## MateriaViva — Magnetic anisotropy constant

Source-reported magnetic anisotropy constant values in MJ/m³, retained separately for each source and method. Direct access through MateriaViva; 1,489 linked structures and 1 original source.

**Size:** 1,521 property values (source wording: 1,521).

**Scope:** magnetic_anisotropy_constant.parquet: numeric; 1,489 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetic anisotropy constant; MJ/m³; Magnetic and spin properties; magnetic_anisotropy_constant; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_anisotropy_constant.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_anisotropy_constant.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_anisotropy_constant.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/magnetic_anisotropy_constant.parquet).

**Original sources / indirect access:**

- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 1,521 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 1,489 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): magnetic_anisotropy_constant: 1,521 value rows; 1,489 distinct structure references; unit MJ/m³; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 1,521 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, magnetic_anisotropy_constant, magnetocrystalline anisotropy, MAE, anisotropy energy density.

<a id="materiaviva-property-easy-axis"></a>
## MateriaViva — Magnetic easy axis

Text descriptor for magnetic easy axis, retained with its original source and method labels. The manifest flags 1,521 values in an unexpected column for this property; inspect the actual Parquet schema and value placement before use. Direct access through MateriaViva; 1,489 linked structures and 1 original source.

**Size:** 1,521 property values (source wording: 1,521).

**Scope:** easy_axis.parquet: text descriptor; 1,489 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Magnetic easy axis; unit not specified / unitless; Magnetic and spin properties; easy_axis; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/easy_axis.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/easy_axis.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/easy_axis.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/easy_axis.parquet).

**Original sources / indirect access:**

- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 1,521 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 1,489 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): easy_axis: 1,521 value rows; 1,489 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 1,521 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.
- Manifest flags 1,521 easy_axis values in an unexpected upstream column. The downloaded export was checked: its value column is string-typed, populated in all 1,521 rows, with 1,489 distinct material IDs. This diagnostic is not evidence of missing exported values.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, easy_axis, easy magnetization direction, magnetic anisotropy direction.

<a id="materiaviva-property-ar-uptake"></a>
## MateriaViva — Argon uptake

Source-reported argon uptake values in mol/kg, retained separately for each source and method. Direct access through MateriaViva; 1,252 linked structures and 1 original source.

**Size:** 1,519 property values (source wording: 1,519).

**Scope:** ar_uptake.parquet: numeric; 1,252 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Argon uptake; mol/kg; Adsorption and porous materials; ar_uptake; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ar_uptake.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ar_uptake.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ar_uptake.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ar_uptake.parquet).

**Original sources / indirect access:**

- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,519 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 1,252 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): ar_uptake: 1,519 value rows; 1,252 distinct structure references; unit mol/kg; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,519 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, ar_uptake, Ar adsorption, gas storage, argon adsorption.

<a id="materiaviva-property-h2-uptake"></a>
## MateriaViva — Hydrogen uptake

Source-reported hydrogen uptake values in g/L, retained separately for each source and method. Direct access through MateriaViva; 106 linked structures and 1 original source.

**Size:** 1,160 property values (source wording: 1,160).

**Scope:** h2_uptake.parquet: numeric; 106 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Hydrogen uptake; g/L; Adsorption and porous materials; h2_uptake; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/h2_uptake.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/h2_uptake.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/h2_uptake.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/h2_uptake.parquet).

**Original sources / indirect access:**

- [MOFX-DB](https://mof.tech.northwestern.edu/) (`mofx-db`): 1,160 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 106 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): h2_uptake: 1,160 value rows; 106 distinct structure references; unit g/L; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: MOFX-DB](https://mof.tech.northwestern.edu/) (checked 2026-11-01): MateriaViva source ID mofx-db: 1,160 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Adsorption and porous materials, h2_uptake, H2 adsorption, hydrogen storage, gas storage.

<a id="materiaviva-property-dynamically-stable"></a>
## MateriaViva — Dynamical stability flag

Source-reported 0/1 flag for dynamical stability; criteria depend on the upstream dataset. Direct access through MateriaViva; 1,023 linked structures and 1 original source.

**Size:** 1,049 property values (source wording: 1,049).

**Scope:** dynamically_stable.parquet: boolean (0/1); 1,023 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Dynamical stability flag; unit not specified / unitless; Thermal and vibrational properties; dynamically_stable; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dynamically_stable.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dynamically_stable.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dynamically_stable.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/dynamically_stable.parquet).

**Original sources / indirect access:**

- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 1,049 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 1,023 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): dynamically_stable: 1,049 value rows; 1,023 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 1,049 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermal and vibrational properties, dynamically_stable, phonon stability, dynamically stable.

<a id="materiaviva-property-layer-group-number"></a>
## MateriaViva — Layer group number

Source-reported layer group number values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 1,023 linked structures and 1 original source.

**Size:** 1,049 property values (source wording: 1,049).

**Scope:** layer_group_number.parquet: numeric; 1,023 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Layer group number; unit not specified / unitless; Chemical and structural descriptors; layer_group_number; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/layer_group_number.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/layer_group_number.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/layer_group_number.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/layer_group_number.parquet).

**Original sources / indirect access:**

- [2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (`bidb`): 1,049 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 1,023 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): layer_group_number: 1,049 value rows; 1,023 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: 2DHub van der Waals Bilayer Database](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): MateriaViva source ID bidb: 1,049 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, layer_group_number, 2D symmetry, layer group, crystallography.

<a id="materiaviva-property-pearson-symbol"></a>
## MateriaViva — Pearson symbol

Text descriptor for pearson symbol, retained with its original source and method labels. Direct access through MateriaViva; 942 linked structures and 2 original sources.

**Size:** 957 property values (source wording: 957).

**Scope:** pearson_symbol.parquet: text descriptor; 942 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Pearson symbol; unit not specified / unitless; Chemical and structural descriptors; pearson_symbol; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pearson_symbol.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pearson_symbol.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pearson_symbol.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/pearson_symbol.parquet).

**Original sources / indirect access:**

- [AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (`aflow-prototypes`): 934 values; provider-declared class `open`.
- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 23 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 942 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): pearson_symbol: 957 value rows; 942 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (checked 2026-11-01): MateriaViva source ID aflow-prototypes: 934 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 23 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, pearson_symbol, Pearson notation, crystal lattice symbol, crystallography.

<a id="materiaviva-property-surface-energy"></a>
## MateriaViva — Surface energy

Source-reported surface energy values in J/m², retained separately for each source and method. Direct access through MateriaViva; 232 linked structures and 1 original source.

**Size:** 695 property values (source wording: 695).

**Scope:** surface_energy.parquet: numeric; 232 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Surface energy; J/m²; Surface and interface properties; surface_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_energy.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 695 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 232 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): surface_energy: 695 value rows; 232 distinct structure references; unit J/m²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 695 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, surface_energy, surface formation energy, facet energy, surface stability.

<a id="materiaviva-property-bulk-modulus-eos"></a>
## MateriaViva — Bulk modulus from equation of state

Source-reported bulk modulus from equation of state values in GPa, retained separately for each source and method. Retained under its own normalized key; do not assume equivalence with the separate eos_bulk_modulus table or identical fitting conventions. Direct access through MateriaViva; 428 linked structures and 1 original source.

**Size:** 428 property values (source wording: 428).

**Scope:** bulk_modulus_eos.parquet: numeric; 428 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Bulk modulus from equation of state; GPa; Mechanical and elastic properties; bulk_modulus_eos; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_eos.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_eos.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_eos.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_eos.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 428 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 428 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): bulk_modulus_eos: 428 value rows; 428 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 428 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, bulk_modulus_eos, EOS bulk modulus, compressibility.

<a id="materiaviva-property-bulk-modulus-pressure-derivative"></a>
## MateriaViva — Pressure derivative of bulk modulus

Source-reported pressure derivative of bulk modulus values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 428 linked structures and 1 original source.

**Size:** 428 property values (source wording: 428).

**Scope:** bulk_modulus_pressure_derivative.parquet: numeric; 428 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Pressure derivative of bulk modulus; unit not specified / unitless; Mechanical and elastic properties; bulk_modulus_pressure_derivative; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_pressure_derivative.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_pressure_derivative.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_pressure_derivative.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/bulk_modulus_pressure_derivative.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 428 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 428 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): bulk_modulus_pressure_derivative: 428 value rows; 428 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 428 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, bulk_modulus_pressure_derivative, B prime, K prime, equation of state.

<a id="materiaviva-property-strukturbericht"></a>
## MateriaViva — Strukturbericht designation

Text descriptor for strukturbericht designation, retained with its original source and method labels. Direct access through MateriaViva; 355 linked structures and 1 original source.

**Size:** 356 property values (source wording: 356).

**Scope:** strukturbericht.parquet: text descriptor; 355 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Strukturbericht designation; unit not specified / unitless; Chemical and structural descriptors; strukturbericht; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/strukturbericht.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/strukturbericht.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/strukturbericht.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/strukturbericht.parquet).

**Original sources / indirect access:**

- [AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (`aflow-prototypes`): 356 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 355 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): strukturbericht: 356 value rows; 355 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: AFLOW Encyclopedia of Crystallographic Prototypes](https://github.com/aflow-org/aflow_prototype_encyclopedia) (checked 2026-11-01): MateriaViva source ID aflow-prototypes: 356 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, strukturbericht, Strukturbericht symbol, structure type designation.

<a id="materiaviva-property-mohs-hardness"></a>
## MateriaViva — Mohs hardness

Source-reported mohs hardness values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 264 linked structures and 1 original source.

**Size:** 267 property values (source wording: 267).

**Scope:** mohs_hardness.parquet: numeric; 264 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Mohs hardness; unit not specified / unitless; Mechanical and elastic properties; mohs_hardness; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mohs_hardness.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mohs_hardness.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mohs_hardness.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/mohs_hardness.parquet).

**Original sources / indirect access:**

- [Webmineral](https://webmineral.com/) (`webmineral`): 267 values; provider-declared class `unclear`. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.

Other denominators (not added to the ranking):

- 264 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): mohs_hardness: 267 value rows; 264 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Webmineral](https://webmineral.com/) (checked 2026-11-01): MateriaViva source ID webmineral: 267 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider web database; the registry class is unclear and public browsing does not imply an open bulk data license.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, mohs_hardness, scratch hardness, mineral hardness, Mohs scale.

<a id="materiaviva-property-has-reconstructed-surface"></a>
## MateriaViva — Surface reconstruction flag

Source-reported 0/1 flag for surface reconstruction; criteria depend on the upstream dataset. Direct access through MateriaViva; 232 linked structures and 1 original source.

**Size:** 237 property values (source wording: 237).

**Scope:** has_reconstructed_surface.parquet: boolean (0/1); 232 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Surface reconstruction flag; unit not specified / unitless; Surface and interface properties; has_reconstructed_surface; boolean (0/1).

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_reconstructed_surface.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_reconstructed_surface.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_reconstructed_surface.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/has_reconstructed_surface.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 237 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 232 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): has_reconstructed_surface: 237 value rows; 232 distinct structure references; unit not specified / unitless; kind bool; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 237 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, has_reconstructed_surface, reconstructed surface, surface reconstruction.

<a id="materiaviva-property-surface-anisotropy"></a>
## MateriaViva — Surface anisotropy

Source-reported surface anisotropy values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 226 linked structures and 1 original source.

**Size:** 229 property values (source wording: 229).

**Scope:** surface_anisotropy.parquet: numeric; 226 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Surface anisotropy; unit not specified / unitless; Surface and interface properties; surface_anisotropy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_anisotropy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_anisotropy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_anisotropy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/surface_anisotropy.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 229 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 226 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): surface_anisotropy: 229 value rows; 226 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 229 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, surface_anisotropy, surface energy anisotropy, Wulff morphology.

<a id="materiaviva-property-wulff-shape-factor"></a>
## MateriaViva — Wulff shape factor

Source-reported wulff shape factor values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 226 linked structures and 1 original source.

**Size:** 229 property values (source wording: 229).

**Scope:** wulff_shape_factor.parquet: numeric; 226 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Wulff shape factor; unit not specified / unitless; Surface and interface properties; wulff_shape_factor; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/wulff_shape_factor.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/wulff_shape_factor.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/wulff_shape_factor.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/wulff_shape_factor.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 229 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 226 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): wulff_shape_factor: 229 value rows; 226 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 229 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, wulff_shape_factor, equilibrium crystal morphology, Wulff construction, shape factor.

<a id="materiaviva-property-measured-chemistry"></a>
## MateriaViva — Measured chemistry

Text descriptor for measured chemistry, retained with its original source and method labels. Direct access through MateriaViva; 138 linked structures and 1 original source.

**Size:** 201 property values (source wording: 201).

**Scope:** measured_chemistry.parquet: text descriptor; 138 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Measured chemistry; unit not specified / unitless; Chemical and structural descriptors; measured_chemistry; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measured_chemistry.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measured_chemistry.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measured_chemistry.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/measured_chemistry.parquet).

**Original sources / indirect access:**

- [RRUFF](https://www.rruff.net/) (`rruff`): 201 values; provider-declared class `restricted`. Modern RRUFF access route from existing catalog; provider registry retains its archived historical licensing-evidence URL. Native accession-level correspondence was not re-audited.

Other denominators (not added to the ranking):

- 138 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): measured_chemistry: 201 value rows; 138 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: RRUFF](https://www.rruff.net/) (checked 2026-11-01): MateriaViva source ID rruff: 201 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Modern RRUFF access route from existing catalog; provider registry retains its archived historical licensing-evidence URL. Native accession-level correspondence was not re-audited.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Chemical and structural descriptors, measured_chemistry, measured composition, chemical analysis, mineral chemistry.

<a id="materiaviva-property-r-factor"></a>
## MateriaViva — Crystallographic R factor

Source-reported crystallographic r factor values; the manifest supplies no unit, so retain the upstream definition and normalization. This is a source-defined refinement agreement metric, distinct from structure_prediction_r_factor; verify scaling and refinement conventions upstream. Direct access through MateriaViva; 183 linked structures and 1 original source.

**Size:** 185 property values (source wording: 185).

**Scope:** r_factor.parquet: numeric; 183 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Crystallographic R factor; unit not specified / unitless; Calculation and refinement metadata; r_factor; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/r_factor.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/r_factor.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/r_factor.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/r_factor.parquet).

**Original sources / indirect access:**

- [Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (`open-framework-aluminophosphate`): 185 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 183 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): r_factor: 185 value rows; 183 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Open-framework aluminophosphate database](https://figshare.com/articles/dataset/Database_of_Open-Framework_Aluminophosphate_Structures/7822574) (checked 2026-11-01): MateriaViva source ID open-framework-aluminophosphate: 185 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Calculation and refinement metadata, r_factor, refinement residual, R factor, crystallographic agreement.

<a id="materiaviva-property-grain-boundary-energy"></a>
## MateriaViva — Grain boundary energy

Source-reported grain boundary energy values in J/m², retained separately for each source and method. Direct access through MateriaViva; 106 linked structures and 1 original source.

**Size:** 164 property values (source wording: 164).

**Scope:** grain_boundary_energy.parquet: numeric; 106 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Grain boundary energy; J/m²; Surface and interface properties; grain_boundary_energy; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_energy.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_energy.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_energy.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_energy.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 164 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 106 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): grain_boundary_energy: 164 value rows; 106 distinct structure references; unit J/m²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 164 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, grain_boundary_energy, GB energy, interface energy, grain boundaries.

<a id="materiaviva-property-elf-max"></a>
## MateriaViva — Maximum electron localization function

Source-reported maximum electron localization function values; the manifest supplies no unit, so retain the upstream definition and normalization. Direct access through MateriaViva; 145 linked structures and 1 original source.

**Size:** 145 property values (source wording: 145).

**Scope:** elf_max.parquet: numeric; 145 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum electron localization function; unit not specified / unitless; Electronic and optical properties; elf_max; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elf_max.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elf_max.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elf_max.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/elf_max.parquet).

**Original sources / indirect access:**

- [Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (`materials-cloud-archive-static`): 145 values; provider-declared class `open`. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

Other denominators (not added to the ranking):

- 145 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): elf_max: 145 value rows; 145 distinct structure references; unit not specified / unitless; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Cloud Archive static datasets (zt-z4, 1z-pd, ed-g2, m0-zg)](https://archive.materialscloud.org/) (checked 2026-11-01): MateriaViva source ID materials-cloud-archive-static: 145 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Grouped alias contains four Materials Cloud records. Manifest source counts are not apportioned by these records. All four original record DOI routes are retained below.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Electronic and optical properties, elf_max, ELF, electron localization, chemical bonding.

<a id="materiaviva-property-grain-boundary-types"></a>
## MateriaViva — Grain boundary types

Text descriptor for grain boundary types, retained with its original source and method labels. Direct access through MateriaViva; 106 linked structures and 1 original source.

**Size:** 106 property values (source wording: 106).

**Scope:** grain_boundary_types.parquet: text descriptor; 106 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Grain boundary types; unit not specified / unitless; Surface and interface properties; grain_boundary_types; text descriptor.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_types.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_types.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_types.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/grain_boundary_types.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 106 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 106 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): grain_boundary_types: 106 value rows; 106 distinct structure references; unit not specified / unitless; kind text; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 106 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.
- The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, grain_boundary_types, GB character, grain boundary classification.

<a id="materiaviva-property-work-of-separation"></a>
## MateriaViva — Work of separation

Source-reported work of separation values in J/m², retained separately for each source and method. Direct access through MateriaViva; 106 linked structures and 1 original source.

**Size:** 106 property values (source wording: 106).

**Scope:** work_of_separation.parquet: numeric; 106 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Work of separation; J/m²; Surface and interface properties; work_of_separation; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_of_separation.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_of_separation.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_of_separation.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/work_of_separation.parquet).

**Original sources / indirect access:**

- [Materials Project](https://materialsproject.org/) (`materials-project`): 106 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 106 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): work_of_separation: 106 value rows; 106 distinct structure references; unit J/m²; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Materials Project](https://materialsproject.org/) (checked 2026-11-01): MateriaViva source ID materials-project: 106 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Surface and interface properties, work_of_separation, interface separation energy, interfacial adhesion, cleavage work.

<a id="materiaviva-property-relative-energy-to-diamond"></a>
## MateriaViva — Energy relative to diamond

Source-reported energy relative to diamond values in eV/atom, retained separately for each source and method. Direct access through MateriaViva; 21 linked structures and 1 original source.

**Size:** 23 property values (source wording: 23).

**Scope:** relative_energy_to_diamond.parquet: numeric; 21 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Energy relative to diamond; eV/atom; Thermodynamic properties and stability; relative_energy_to_diamond; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/relative_energy_to_diamond.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/relative_energy_to_diamond.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/relative_energy_to_diamond.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/relative_energy_to_diamond.parquet).

**Original sources / indirect access:**

- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 23 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 21 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): relative_energy_to_diamond: 23 value rows; 21 distinct structure references; unit eV/atom; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 23 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Thermodynamic properties and stability, relative_energy_to_diamond, carbon allotrope energy, diamond reference, relative energy.

<a id="materiaviva-property-altermagnetic-split-fraction"></a>
## MateriaViva — Altermagnetic splitting fraction

Source-reported altermagnetic splitting fraction values in %, retained separately for each source and method. The manifest reports a percentage splitting metric; its precise population and threshold must be checked at the original source. Direct access through MateriaViva; 22 linked structures and 1 original source.

**Size:** 22 property values (source wording: 22).

**Scope:** altermagnetic_split_fraction.parquet: numeric; 22 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Altermagnetic splitting fraction; %; Magnetic and spin properties; altermagnetic_split_fraction; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_split_fraction.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_split_fraction.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_split_fraction.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_split_fraction.parquet).

**Original sources / indirect access:**

- [Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (`amdb`): 22 values; provider-declared class `restricted`. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

Other denominators (not added to the ranking):

- 22 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): altermagnetic_split_fraction: 22 value rows; 22 distinct structure references; unit %; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (checked 2026-11-01): MateriaViva source ID amdb: 22 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, altermagnetic_split_fraction, altermagnetism, spin splitting fraction.

<a id="materiaviva-property-altermagnetic-splitting-avg"></a>
## MateriaViva — Average altermagnetic splitting

Source-reported average altermagnetic splitting values in eV, retained separately for each source and method. Direct access through MateriaViva; 22 linked structures and 1 original source.

**Size:** 22 property values (source wording: 22).

**Scope:** altermagnetic_splitting_avg.parquet: numeric; 22 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Average altermagnetic splitting; eV; Magnetic and spin properties; altermagnetic_splitting_avg; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_avg.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_avg.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_avg.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_avg.parquet).

**Original sources / indirect access:**

- [Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (`amdb`): 22 values; provider-declared class `restricted`. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

Other denominators (not added to the ranking):

- 22 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): altermagnetic_splitting_avg: 22 value rows; 22 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (checked 2026-11-01): MateriaViva source ID amdb: 22 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, altermagnetic_splitting_avg, altermagnetism, average spin splitting.

<a id="materiaviva-property-altermagnetic-splitting-max"></a>
## MateriaViva — Maximum altermagnetic splitting

Source-reported maximum altermagnetic splitting values in eV, retained separately for each source and method. Direct access through MateriaViva; 22 linked structures and 1 original source.

**Size:** 22 property values (source wording: 22).

**Scope:** altermagnetic_splitting_max.parquet: numeric; 22 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Maximum altermagnetic splitting; eV; Magnetic and spin properties; altermagnetic_splitting_max; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Includes provider-declared noncommercial or restricted sources..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_max.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_max.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_max.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/altermagnetic_splitting_max.parquet).

**Original sources / indirect access:**

- [Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (`amdb`): 22 values; provider-declared class `restricted`. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

Other denominators (not added to the ranking):

- 22 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): altermagnetic_splitting_max: 22 value rows; 22 distinct structure references; unit eV; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Anyterial Altermagnets Database](https://altermagnets.anyterial.se/) (checked 2026-11-01): MateriaViva source ID amdb: 22 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Provider legal page limits CC BY-SA terms to individual entries and non-substantial database extracts; aggregate availability does not establish unrestricted bulk reuse.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, altermagnetic_splitting_max, altermagnetism, maximum spin splitting.

<a id="materiaviva-property-hardness-vickers"></a>
## MateriaViva — Vickers hardness

Source-reported vickers hardness values in GPa, retained separately for each source and method. Direct access through MateriaViva; 18 linked structures and 1 original source.

**Size:** 20 property values (source wording: 20).

**Scope:** hardness_vickers.parquet: numeric; 18 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Vickers hardness; GPa; Mechanical and elastic properties; hardness_vickers; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class. Some upstream rights are not verified..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/hardness_vickers.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/hardness_vickers.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/hardness_vickers.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/hardness_vickers.parquet).

**Original sources / indirect access:**

- [Samara Carbon Allotrope Database](https://www.sacada.info/) (`sacada`): 20 values; provider-declared class `unclear`.

Other denominators (not added to the ranking):

- 18 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): hardness_vickers: 20 value rows; 18 distinct structure references; unit GPa; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: Samara Carbon Allotrope Database](https://www.sacada.info/) (checked 2026-11-01): MateriaViva source ID sacada: 20 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Mechanical and elastic properties, hardness_vickers, indentation hardness, HV, hard materials.

<a id="materiaviva-property-curie-temperature"></a>
## MateriaViva — Curie temperature

Source-reported curie temperature values in K, retained separately for each source and method. Direct access through MateriaViva; 6 linked structures and 1 original source.

**Size:** 6 property values (source wording: 6).

**Scope:** curie_temperature.parquet: numeric; 6 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Curie temperature; K; Magnetic and spin properties; curie_temperature; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/curie_temperature.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/curie_temperature.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/curie_temperature.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/curie_temperature.parquet).

**Original sources / indirect access:**

- [NovoMag magnetic materials database](https://zenodo.org/records/17399362) (`novomag`): 6 values; provider-declared class `open`.

Other denominators (not added to the ranking):

- 6 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): curie_temperature: 6 value rows; 6 distinct structure references; unit K; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: NovoMag magnetic materials database](https://zenodo.org/records/17399362) (checked 2026-11-01): MateriaViva source ID novomag: 6 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Magnetic and spin properties, curie_temperature, magnetic transition temperature, ferromagnetism, Curie point.

<a id="materiaviva-property-ionic-conductivity"></a>
## MateriaViva — Ionic conductivity

Source-reported ionic conductivity values in S/cm, retained separately for each source and method. Conductivity depends on temperature and measurement or calculation conditions; the normalized table alone does not establish a room-temperature benchmark. Direct access through MateriaViva; 5 linked structures and 1 original source.

**Size:** 5 property values (source wording: 5).

**Scope:** ionic_conductivity.parquet: numeric; 5 distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.

**Release:** MateriaViva Open property export; revision 6010a086ade47c2c99d1b2dca3a944c3996959a4. **Year:** 2026.

**Provenance:** source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row. **Structure availability:** `structure_linked`.

**Labels/content:** Ionic conductivity; S/cm; Battery and ionic transport properties; ionic_conductivity; numeric.

**Access:** open. **Dataset license:** Per-row upstream terms; retain licence and licence_class..

**Official routes:** [homepage](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ionic_conductivity.parquet) · [data](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ionic_conductivity.parquet) · [parent](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) · [manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json)

**Direct access source:** [MateriaViva file](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ionic_conductivity.parquet) · [Parquet download](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/resolve/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/ionic_conductivity.parquet).

**Original sources / indirect access:**

- [OBELiX](https://github.com/NRC-Mila/OBELiX/tree/main/data) (`obelix`): 5 values; provider-declared class `open`. Only five ionic-conductivity rows appear in the property manifest. This is an extracted subset, not the full OBELiX dataset.

Other denominators (not added to the ranking):

- 5 linked structures: Distinct material_id references in this property table; overlaps other properties.

**Evidence:**

- [MateriaViva pinned property manifest](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/properties/MANIFEST.json) (checked 2026-11-01): ionic_conductivity: 5 value rows; 5 distinct structure references; unit S/cm; kind num; full source-row counts retained.
- [MateriaViva property schema and provenance](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/README.md) (checked 2026-11-01): One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.
- [MateriaViva upstream source declarations](https://huggingface.co/datasets/AI4QC/MateriaViva-Open/blob/6010a086ade47c2c99d1b2dca3a944c3996959a4/licences.json) (checked 2026-11-01): Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.
- [Original source: OBELiX](https://github.com/NRC-Mila/OBELiX/tree/main/data) (checked 2026-11-01): MateriaViva source ID obelix: 5 rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. Only five ionic-conductivity rows appear in the property manifest. This is an extracted subset, not the full OBELiX dataset.

**Reuse and interpretation notes:**

- A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.
- Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.
- Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.
- Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.

**Tags:** MateriaViva, MaterialViva, Matvina, MateriaViva-property-subset, materiaviva-properties-20261101, Battery and ionic transport properties, ionic_conductivity, ion conductivity, solid electrolyte, solid state electrolyte, ion transport.
