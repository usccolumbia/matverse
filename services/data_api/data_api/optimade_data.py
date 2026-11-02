"""Normalize the stored CIF, not upstream primitive-cell metadata, for OPTIMADE."""
from collections import defaultdict
from fractions import Fraction
from functools import reduce
import json
import math

import gemmi


def attributes(cif, material_id, revision):
    block = gemmi.cif.read_string(cif).sole_block()
    small = gemmi.make_small_structure_from_block(block)
    if not small.cell.is_crystal() or small.cell.volume <= 0:
        raise ValueError("invalid_cell")
    sites = small.get_all_unit_cell_sites()
    if not sites:
        raise ValueError("missing_sites")
    if len(sites) > 20000:
        raise ValueError("site_limit")
    grouped = {}
    for site in sites:
        symbol = site.element.name
        if site.element.atomic_number < 1 or not math.isfinite(site.occ) or site.occ < 0:
            raise ValueError("unknown_element_or_occupancy")
        if site.occ == 0:
            continue
        pos = tuple(round(float(v) % 1, 7) % 1 for v in site.fract.tolist())
        if not all(math.isfinite(x) for x in pos):
            raise ValueError("invalid_position")
        group = grouped.setdefault(pos, defaultdict(float))
        group[symbol] += float(site.occ)
    composition = defaultdict(float)
    species = []
    species_lookup = {}
    species_at_sites = []
    positions = []
    disorder = False
    for pos, contents in grouped.items():
        total = sum(contents.values())
        if total > 1.001:
            raise ValueError("overoccupied_or_duplicate_site")
        # Small round-off deviations are normalized; substantive partial occupancy
        # remains explicit with a vacancy species, as required by OPTIMADE.
        if abs(total - 1) < 0.001:
            contents = {k: v/total for k,v in contents.items()}
            total = 1.0
        for symbol, occ in contents.items():
            composition[symbol] += occ
        if total < 1.0:
            contents = {**contents, "vacancy": 1-total}
        symbols = sorted(contents)
        concentrations = [contents[s] for s in symbols]
        disorder |= len(symbols) > 1
        key = tuple(zip(symbols, [round(x, 10) for x in concentrations]))
        if key not in species_lookup:
            name = f"site_type_{len(species)}"
            species_lookup[key] = name
            species.append({"name": name, "chemical_symbols": symbols, "concentration": concentrations})
        species_at_sites.append(species_lookup[key])
        positions.append(small.cell.orthogonalize(gemmi.Fractional(*pos)).tolist())
    elements = sorted(composition)
    if not elements:
        raise ValueError("empty_composition")
    total = sum(composition.values())
    fractions = [Fraction(composition[e]).limit_denominator(1000) for e in elements]
    denominator = math.lcm(*(x.denominator for x in fractions))
    integers = [int(f * denominator) for f in fractions]
    gcd = reduce(math.gcd, integers)
    integers = [n//gcd for n in integers]
    reduced = ''.join(e + (str(n) if n != 1 else '') for e,n in zip(elements,integers))
    anonymous = ''.join(chr(65+i)+(str(n) if n != 1 else '') for i,n in enumerate(sorted(integers,reverse=True)))
    matrix = small.cell.orth.mat.tolist()
    lattice = [[matrix[j][i] for j in range(3)] for i in range(3)]
    return {"immutable_id": f"{material_id}@{revision}",
            "last_modified": "2026-10-24T01:26:51Z", "elements": elements,
            "nelements": len(elements), "elements_ratios": [composition[e]/total for e in elements],
            "chemical_formula_descriptive": reduced, "chemical_formula_reduced": reduced,
            "chemical_formula_hill": None, "chemical_formula_anonymous": anonymous,
            "dimension_types": [1,1,1], "nperiodic_dimensions": 3,
            "lattice_vectors": lattice, "cartesian_site_positions": positions,
            "nsites": len(positions), "species": species, "species_at_sites": species_at_sites,
            "assemblies": None, "structure_features": ["disorder"] if disorder else []}
