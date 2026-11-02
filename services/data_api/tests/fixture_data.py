import json
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq

REV = "a" * 40
CIF = """data_Si
_cell_length_a 5.43
_cell_length_b 5.43
_cell_length_c 5.43
_cell_angle_alpha 90
_cell_angle_beta 90
_cell_angle_gamma 90
_symmetry_space_group_name_H-M 'P 1'
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
Si1 Si 0 0 0 1
Si2 Si 0.25 0.25 0.25 1
"""


def create(root):
    from data_api.mirror import digest
    from data_api.build_catalog import build
    from data_api.build_optimade import build as build_optimade
    release = Path(root) / "releases" / REV
    up = release / "upstream"
    for name in ["data","properties","predictions"]:
        (up/name).mkdir(parents=True,exist_ok=True)
    rows = []
    for i in range(3):
        rows.append({"material_id": f"mat-{i}", "formula": "Si", "chemical_system": "Si",
                     "elements": ["Si"], "dataset": "candidate", "material_family": None,
                     "n_elements":1, "n_sites":1, "spacegroup_number":1,
                     "spacegroup_symbol":"P1", "crystal_system":"cubic",
                     "lattice_a":5.43,"lattice_b":5.43,"lattice_c":5.43,
                     "lattice_alpha":90.,"lattice_beta":90.,"lattice_gamma":90.,"volume":160.,"density":2.3,
                     "licence":"CC-BY-4.0","licence_from":"oqmd",
                     "open_sources": ["oqmd","materials-project"] if i==0 else ["oqmd"] if i==1 else ["materials-project"],
                     "open_source_ids":[f"oqmd:{i}"],"other_sources":[],
                     "origin_source":"oqmd" if i<2 else "legacy-local","origin_open":i<2,
                     "cif":CIF})
    pq.write_table(pa.Table.from_pylist(rows),up/'data/structures-00000.parquet',row_group_size=2)
    values=[{"material_id":"mat-0","value":1.1,"method":"PBE","source":"oqmd","source_native_id":"1","licence":"CC-BY-4.0","licence_class":"open"},
            {"material_id":"mat-0","value":1.3,"method":"HSE","source":"materials-project","source_native_id":"mp-1","licence":"CC-BY-4.0","licence_class":"open"},
            {"material_id":"mat-1","value":2.2,"method":"PBE","source":"oqmd","source_native_id":"2","licence":"CC-BY-4.0","licence_class":"open"},
            {"material_id":"mat-2","value":3.3,"method":"PBE","source":"restricted-db","source_native_id":"r-1","licence":"restricted","licence_class":"restricted"}]
    pq.write_table(pa.Table.from_pylist(values),up/'properties/band_gap.parquet')
    (up/'properties/MANIFEST.json').write_text(json.dumps({"rows":4,"properties":1,"per_property":{"band_gap":{"rows":4,"structures":3,"unit":"eV","kind":"num","sources":{"oqmd":2,"materials-project":1,"restricted-db":1}}}}))
    pq.write_table(pa.Table.from_pylist([{"material_id":"mat-0","value":5.5},{"material_id":"mat-2","value":6.6}]),up/'predictions/test__gga.parquet')
    (up/'predictions/test__gga.json').write_text(json.dumps({"model":"test","warning":"ML estimates"}))
    (up/'predictions/MANIFEST.json').write_text(json.dumps({"rows_total":2,"tasks":{"test__gga":{"state":"done","rows":2,"declared_domain":"pool-wide"}}}))
    (up/'licences.json').write_text(json.dumps({"oqmd":{"licence":"CC-BY-4.0"},"materials-project":{"licence":"CC-BY-4.0"}}))
    entries=[{"path":str(p.relative_to(up)),"bytes":p.stat().st_size,"sha256":digest(p)} for p in up.rglob('*') if p.is_file()]
    (release/'mirror_receipt.json').write_text(json.dumps({"revision":REV,"repo":"AI4QC/MateriaViva-Open","files":entries,"bytes":sum(e['bytes'] for e in entries)}))
    build(root,REV)
    build_optimade(root,REV,workers=1)
    return release


if __name__ == "__main__":
    import sys
    create(sys.argv[1])
