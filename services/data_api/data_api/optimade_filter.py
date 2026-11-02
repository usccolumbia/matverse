"""Compile the official OPTIMADE grammar to bound DuckDB predicates.

No user-provided SQL or identifier is interpolated. Unsupported nested properties
and correlated list queries fail explicitly rather than silently misfiltering.
"""
import json

from lark import Tree
from optimade.filterparser import LarkParser


FIELDS = {"id": "id", "type": "'structures'", "immutable_id": "immutable_id", "last_modified": "last_modified",
          "elements": "elements", "nelements": "nelements", "elements_ratios": "elements_ratios",
          "chemical_formula_descriptive": "chemical_formula_descriptive",
          "chemical_formula_reduced": "chemical_formula_reduced", "chemical_formula_hill": "NULL",
          "chemical_formula_anonymous": "chemical_formula_anonymous", "nsites": "nsites",
          "nperiodic_dimensions": "nperiodic_dimensions", "structure_features": "structure_features",
          "dimension_types": "[1,1,1]", "assemblies": "NULL",
          "space_group_it_number": "NULL", "space_group_symbol_hall": "NULL",
          "space_group_symbol_hermann_mauguin": "NULL", "space_group_symbol_hermann_mauguin_extended": "NULL",
          "space_group_symmetry_operations_xyz": "NULL"}
LISTS = {"elements", "elements_ratios", "structure_features", "dimension_types"}
COMPARISONS = {"=", "!=", "<", "<=", ">", ">="}


class FilterCompiler:
    def __init__(self):
        self.args = []
        self.unknown = set()

    def literal(self, value):
        self.args.append(value)
        return "?"

    def prop(self, node):
        name = '.'.join(str(x) for x in node.children)
        if name not in FIELDS:
            if name.startswith("_") and name.count("_") >= 2:
                self.unknown.add(name)
                return "NULL", name
            raise ValueError(f"Unsupported OPTIMADE property: {name}")
        return FIELDS[name], name

    def scalar(self, node):
        if not isinstance(node, Tree):
            return self.literal(str(node))
        kind = str(node.data)
        if kind in ("value", "non_string_value", "constant"):
            return self.scalar(node.children[0])
        if kind == "property":
            return self.prop(node)[0]
        if kind == "string":
            return self.literal(json.loads(str(node.children[0])))
        if kind in ("number", "signed_int"):
            value = ''.join(str(c) for c in node.children)
            return self.literal(float(value) if any(c in value for c in '.eE') else int(value))
        raise ValueError(f"Unsupported OPTIMADE scalar: {kind}")

    def rhs(self, column, name, node):
        kind = str(node.data)
        c = node.children
        if kind == "value_op_rhs":
            op = str(c[0])
            if op not in COMPARISONS:
                raise ValueError("Invalid comparison")
            return f"({column} {op} {self.scalar(c[1])})"
        if kind == "known_op_rhs":
            return f"({column} IS {'NOT ' if str(c[-1]) == 'KNOWN' else ''}NULL)"
        if kind == "fuzzy_string_op_rhs":
            operator = str(c[0])
            fn = {"CONTAINS": "contains", "STARTS": "starts_with", "BEGINS": "starts_with", "ENDS": "ends_with"}.get(operator)
            if not fn:
                raise ValueError("Unsupported string operator")
            return f"{fn}({column}, {self.scalar(c[-1])})"
        if kind == "length_op_rhs":
            op = str(c[-2]) if len(c) == 3 else "="
            if op not in COMPARISONS:
                raise ValueError("Invalid length comparison")
            return f"(len({column}) {op} {self.scalar(c[-1])})"
        if kind == "set_op_rhs":
            if name not in LISTS and column != "NULL":
                raise ValueError("HAS requires a list property")
            if column == "NULL":
                return "NULL"
            mode = str(c[1]) if len(c) >= 3 and str(c[1]) in ("ALL","ANY","ONLY") else "ANY"
            values = list(c[-1].children) if isinstance(c[-1],Tree) and c[-1].data == "value_list" else list(c[1:])
            predicates = []
            op = "="
            for value in values:
                if not isinstance(value,Tree):
                    token = str(value)
                    if token in COMPARISONS:
                        op = token
                    elif token not in ("ALL","ANY","ONLY"):
                        raise ValueError("Unsupported list comparison")
                    continue
                if isinstance(value,Tree) and value.data == "value":
                    predicates.append(f"x {op} {self.scalar(value)}")
                    op = "="
                elif isinstance(value,Tree) and value.data == "value_op_rhs":
                    predicates.append(self.rhs("x", "", value))
                else:
                    raise ValueError("Unsupported list predicate")
            if mode == "ONLY":
                # Every value must occur and every list element must be represented.
                # Bind twice because the generated predicate occurs twice in SQL.
                first = self.args[-len(predicates):]
                self.args.extend(first)
                any_expr = " OR ".join(predicates)
                return "(" + " AND ".join(f"EXISTS(SELECT 1 FROM unnest({column}) q(x) WHERE {p})" for p in predicates) + f" AND NOT EXISTS(SELECT 1 FROM unnest({column}) q(x) WHERE NOT ({any_expr})))"
            join = " AND " if mode == "ALL" else " OR "
            return "(" + join.join(f"EXISTS(SELECT 1 FROM unnest({column}) q(x) WHERE {p})" for p in predicates) + ")"
        raise ValueError(f"Unsupported OPTIMADE filter operator: {kind}")

    def walk(self, node):
        kind = str(node.data)
        c = node.children
        if kind in ("filter", "comparison"):
            return self.walk(c[0])
        if kind == "expression":
            return '(' + ' OR '.join(self.walk(x) for x in c) + ')'
        if kind == "expression_clause":
            return '(' + ' AND '.join(self.walk(x) for x in c) + ')'
        if kind == "expression_phrase":
            return '(NOT ' + self.walk(c[-1]) + ')' if len(c) == 2 else self.walk(c[0])
        if kind == "property_first_comparison":
            column, name = self.prop(c[0])
            return self.rhs(column,name,c[1])
        if kind == "constant_first_comparison":
            op = str(c[1])
            if op not in COMPARISONS:
                raise ValueError("Invalid comparison")
            return f"({self.scalar(c[0])} {op} {self.scalar(c[2])})"
        raise ValueError(f"Unsupported OPTIMADE filter expression: {kind}")

    def compile(self, text):
        if not text:
            return "TRUE", [], []
        if len(text) > 4096:
            raise ValueError("Filter exceeds 4096 characters")
        try:
            tree = LarkParser(version=(1,2,0)).parse(text)
            sql = self.walk(tree)
        except ValueError:
            raise
        except Exception:
            raise ValueError("Invalid OPTIMADE filter syntax")
        return sql, self.args, sorted(self.unknown)
