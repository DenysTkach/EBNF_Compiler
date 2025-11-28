# -*- coding: utf-8 -*-
"""
Simple semantic checker for MiniOberon.
Designed for the AST built by ast_builder.AstBuilderVisitor.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


# ------------------------- Exception -------------------------

class SemanticError(Exception):
    """Semantic analysis error (convenient to catch in frontend.py)."""
    pass


# ------------------------- Types -------------------------

# Internal type representation:
# - basic types: string 'INTEGER' / 'REAL' / 'STRING' / 'BOOLEAN'
# - array: {'kind': 'array', 'dims': N, 'elem': <type>}
# - record: {'kind': 'record', 'fields': {name: <type>, ...}}

def types_equal(t1: Any, t2: Any) -> bool:
    """Compare types (without automatic conversions)."""
    # basic types are just strings
    if isinstance(t1, str) and isinstance(t2, str):
        return t1 == t2

    if not isinstance(t1, dict) or not isinstance(t2, dict):
        return False

    if t1.get("kind") != t2.get("kind"):
        return False

    if t1["kind"] == "array":
        return (
            t1["dims"] == t2["dims"]
            and types_equal(t1["elem"], t2["elem"])
        )

    if t1["kind"] == "record":
        f1 = t1["fields"]
        f2 = t2["fields"]
        if set(f1.keys()) != set(f2.keys()):
            return False
        return all(types_equal(f1[k], f2[k]) for k in f1.keys())

    return False


def is_numeric(t: Any) -> bool:
    return t in ("INTEGER", "REAL")


# ------------------------- Symbols and scopes -------------------------

@dataclass
class ParamDef:
    name: str
    type: Any
    byref: bool  # True if parameter is declared as VAR


@dataclass
class Symbol:
    name: str
    kind: str              # 'var' | 'const' | 'type' | 'proc' | 'func' | 'param'
    type: Any = None       # for var/const/param/func
    params: List[ParamDef] = None  # for proc/func
    value: Any = None      # for constants (optional)


class Scope:
    def __init__(self, parent: Optional["Scope"] = None):
        self.parent: Optional[Scope] = parent
        self.symbols: Dict[str, Symbol] = {}

    # ---- define and lookup ----

    def define(self, sym: Symbol):
        if sym.name in self.symbols:
            raise SemanticError(f"Duplicate declaration of identifier '{sym.name}'")
        self.symbols[sym.name] = sym

    def lookup(self, name: str) -> Optional[Symbol]:
        scope: Optional[Scope] = self
        while scope is not None:
            if name in scope.symbols:
                return scope.symbols[name]
            scope = scope.parent
        return None


# ------------------------- Main analyzer class -------------------------

class SemanticAnalyzer:
    def __init__(self):
        # global scope
        self.global_scope = Scope(parent=None)
        # current scope (changes when entering a block/procedure/function)
        self.current_scope: Scope = self.global_scope
        # current procedure/function (for RETURN checks)
        self.current_proc: Optional[Symbol] = None

        # register some builtin functions/procedures if needed
        self._init_builtins()

    # ---- public entry ----

    def analyze(self, ast: Dict[str, Any]):
        """Main entry: run semantics on program AST."""
        if ast.get("type") != "Program":
            raise SemanticError("Expected a node of type Program")

        self._visit_program(ast)

    # ------------------------- builtins -------------------------

    def _init_builtins(self):
        """Very simple builtin procedures/functions (optional)."""
        # Output procedures
        self.global_scope.define(Symbol(
            name="WriteString",
            kind="proc",
            params=[ParamDef("s", "STRING", byref=False)],
        ))

        self.global_scope.define(Symbol(
            name="WriteInt",
            kind="proc",
            params=[ParamDef("x", "INTEGER", byref=False)],
        ))

        self.global_scope.define(Symbol(
            name="WriteReal",
            kind="proc",
            params=[ParamDef("x", "REAL", byref=False)],
        ))

        self.global_scope.define(Symbol(
            name="WriteLn",
            kind="proc",
            params=[]
        ))

        # Input functions
        self.global_scope.define(Symbol(
            name="ReadInt",
            kind="func",
            type="INTEGER",
            params=[]
        ))

        self.global_scope.define(Symbol(
            name="ReadReal",
            kind="func",
            type="REAL",
            params=[]
        ))

        self.global_scope.define(Symbol(
            name="ReadString",
            kind="func",
            type="STRING",
            params=[]
        ))

        # Type conversion functions
        self.global_scope.define(Symbol(
            name="IntToReal",
            kind="func",
            type="REAL",
            params=[ParamDef("x", "INTEGER", byref=False)]
        ))

        self.global_scope.define(Symbol(
            name="RealToInt",
            kind="func",
            type="INTEGER",
            params=[ParamDef("x", "REAL", byref=False)]
        ))

        self.global_scope.define(Symbol(
            name="IntToString",
            kind="func",
            type="STRING",
            params=[ParamDef("x", "INTEGER", byref=False)]
        ))

        self.global_scope.define(Symbol(
            name="RealToString",
            kind="func",
            type="STRING",
            params=[ParamDef("x", "REAL", byref=False)]
        ))

    # ------------------------- Helper "visits" -------------------------

    # program / module / block

    def _visit_program(self, node: Dict[str, Any]):
        self._visit_module(node["module"])

    def _visit_module(self, node: Dict[str, Any]):
        name = node["name"]
        end = node["end"]
        if name != end:
            raise SemanticError(
                f"Module name in END must match the header: '{name}' vs '{end}'"
            )

        # module block uses the global scope without creating a new Scope
        block = node["block"]
        self._visit_block(block, self.global_scope, is_module=True)

    def _visit_block(self, node: Dict[str, Any], parent_scope: Scope, is_module: bool = False):
        """
        Block:
        - create (or not) a new scope
        - first predeclare procedures/functions (for recursion/nesting)
        - then handle CONST/TYPE/VAR declarations and procedure/function bodies
        - then check the statement part (BEGIN ... END)
        """
        if is_module:
            local_scope = parent_scope
        else:
            local_scope = Scope(parent=parent_scope)

        saved_scope = self.current_scope
        self.current_scope = local_scope

        decls: List[Dict[str, Any]] = node.get("decls", [])

        # 1) predeclare only procedures/functions
        self._predeclare_procs_funcs(decls)

        # 2) process CONST/TYPE/VAR sections and procedure/function bodies
        self._analyze_decls(decls)

        # 3) statement part
        body = node.get("body")
        if body is not None:
            self._visit_statseq(body)

        self.current_scope = saved_scope

    # --------------------- Predeclare procedures/functions ---------------------

    def _predeclare_procs_funcs(self, decls: List[Dict[str, Any]]):
        for d in decls:
            if d["type"] in ("ProcedureDecl", "FunctionDecl"):
                name = d["name"]

                # collect ParamDef list
                param_defs: List[ParamDef] = []
                for p in d.get("params", []):
                    p_type_ast = p["param_type"]
                    p_type = self._resolve_type(p_type_ast, self.current_scope)
                    byref = p["byref"]
                    for pname in p["names"]:
                        param_defs.append(ParamDef(pname, p_type, byref))

                if d["type"] == "FunctionDecl":
                    ret_type = self._resolve_type(d["return_type"], self.current_scope)
                    sym = Symbol(
                        name=name,
                        kind="func",
                        type=ret_type,
                        params=param_defs,
                    )
                else:
                    sym = Symbol(
                        name=name,
                        kind="proc",
                        type=None,
                        params=param_defs,
                    )

                self.current_scope.define(sym)

    # --------------------- Analyze declaration sections ---------------------

    def _analyze_decls(self, decls: List[Dict[str, Any]]):
        for d in decls:
            kind = d["type"]
            if kind == "ConstSec":
                self._visit_constsec(d)
            elif kind == "TypeSec":
                self._visit_typesec(d)
            elif kind == "VarSec":
                self._visit_varsec(d)
            elif kind in ("ProcedureDecl", "FunctionDecl"):
                self._visit_proc_or_func(d)
            else:
                # just in case — ignore unknown
                pass

    # ---- CONST ----

    def _visit_constsec(self, node: Dict[str, Any]):
        for c in node["decls"]:
            self._visit_constdecl(c)

    def _visit_constdecl(self, node: Dict[str, Any]):
        name = node["name"]
        expr = node["value"]
        t = self._expr_type(expr)

        # We could also try to evaluate the value, but type is enough for semantics
        sym = Symbol(name=name, kind="const", type=t)
        self.current_scope.define(sym)

    # ---- TYPE ----

    def _visit_typesec(self, node: Dict[str, Any]):
        for tdecl in node["decls"]:
            self._visit_typedecl(tdecl)

    def _visit_typedecl(self, node: Dict[str, Any]):
        name = node["name"]
        # first add a "placeholder" to avoid duplicate declarations
        if self.current_scope.lookup(name) and name in self.current_scope.symbols:
            raise SemanticError(f"Duplicate type declaration '{name}' in the same scope")

        # real type
        real_type = self._resolve_type(node["value"], self.current_scope)
        sym = Symbol(name=name, kind="type", type=real_type)
        self.current_scope.define(sym)

    # ---- VAR ----

    def _visit_varsec(self, node: Dict[str, Any]):
        for v in node["decls"]:
            self._visit_vardecl(v)

    def _visit_vardecl(self, node: Dict[str, Any]):
        var_type_ast = node["var_type"]
        var_type = self._resolve_type(var_type_ast, self.current_scope)

        for name in node["names"]:
            sym = Symbol(name=name, kind="var", type=var_type)
            self.current_scope.define(sym)

    # ---- PROCEDURE / FUNCTION ----

    def _visit_proc_or_func(self, node: Dict[str, Any]):
        name = node["name"]
        sym = self.current_scope.lookup(name)
        if sym is None or sym.kind not in ("proc", "func"):
            raise SemanticError(
                f"Internal error: procedure/function symbol '{name}' not found"
            )

        # create scope for procedure/function body
        local_scope = Scope(parent=self.current_scope)

        # add parameters to local scope
        for p in sym.params or []:
            psym = Symbol(name=p.name, kind="param", type=p.type)
            local_scope.define(psym)

        # now analyze the body block
        saved_scope = self.current_scope
        saved_proc = self.current_proc

        self.current_scope = local_scope
        self.current_proc = sym

        body_block = node["body"]
        # the block already has its own declarations (local vars + nested procedures)
        self._visit_block(body_block, local_scope, is_module=False)

        self.current_scope = saved_scope
        self.current_proc = saved_proc

    # ------------------------- AST type -> internal type -------------------------

    def _resolve_type(self, tnode: Dict[str, Any], scope: Scope) -> Any:
        """Convert type AST node to internal representation."""
        tkind = tnode["type"]

        # basic type
        if tkind == "BaseType":
            name = tnode["name"]  # 'INTEGER' / 'REAL' / 'STRING' / 'BOOLEAN'
            if name not in ("INTEGER", "REAL", "STRING", "BOOLEAN"):
                raise SemanticError(f"Unknown basic type '{name}'")
            return name

        # array
        if tkind == "ArrayType":
            dims_ast = tnode["dims"]  # list of ints or identifiers
            # number of dimensions — length of the list
            dims = len(dims_ast)

            elem_type_ast = tnode["elem"]
            elem_type = self._resolve_type(elem_type_ast, scope)

            # we could also check that dimensions are integer constants
            return {"kind": "array", "dims": dims, "elem": elem_type}

        # record
        if tkind == "RecordType":
            fields: Dict[str, Any] = {}
            for f in tnode["fields"]:
                f_type = self._resolve_type(f["field_type"], scope)
                for name in f["names"]:
                    if name in fields:
                        raise SemanticError(
                            f"Duplicate field declaration '{name}' in record"
                        )
                    fields[name] = f_type
            return {"kind": "record", "fields": fields}

        # named type (TYPE T = ...)
        if tkind == "NamedType":
            name = tnode["name"]
            sym = scope.lookup(name)
            if sym is None or sym.kind != "type":
                raise SemanticError(f"Unknown type '{name}'")
            return sym.type

        raise SemanticError(f"Unknown type kind: {tkind}")

    # ------------------------- Statement part -------------------------

    def _visit_statseq(self, node: Dict[str, Any]):
        for st in node.get("stmts", []):
            self._visit_statement(st)

    def _visit_statement(self, st: Dict[str, Any]):
        stype = st["type"]
        if stype == "Assign":
            self._visit_assign(st)
        elif stype == "Call":
            self._visit_call(st, used_as_expr=False)
        elif stype == "If":
            self._visit_if(st)
        elif stype == "While":
            self._visit_while(st)
        elif stype == "For":
            self._visit_for(st)
        elif stype == "Return":
            self._visit_return(st)
        else:
            # unknown/empty statement — ignore
            pass

    # ---- Assign ----

    def _visit_assign(self, node: Dict[str, Any]):
        left = node["left"]
        right = node["right"]

        ltype = self._designator_type(left, require_variable=True)
        rtype = self._expr_type(right)

        if not types_equal(ltype, rtype):
            raise SemanticError(
                f"Incompatible types in assignment: "
                f"{self._type_str(ltype)} := {self._type_str(rtype)}"
            )

    # ---- Call ----

    def _visit_call(self, node: Dict[str, Any], used_as_expr: bool):
        name = node["name"]
        sym = self.current_scope.lookup(name)
        if sym is None:
            raise SemanticError(f"Call to unknown function/procedure '{name}'")

        if sym.kind not in ("proc", "func"):
            raise SemanticError(
                f"Identifier '{name}' is neither a procedure nor a function"
            )

        if used_as_expr and sym.kind != "func":
            raise SemanticError(
                f"Procedure '{name}' does not return a value and "
                f"cannot be used in an expression"
            )

        args = node.get("args", [])
        params = sym.params or []

        if len(args) != len(params):
            raise SemanticError(
                f"Invalid number of arguments in call to '{name}': "
                f"expected {len(params)}, got {len(args)}"
            )

        # compare argument types one by one
        for i, (a, p) in enumerate(zip(args, params)):
            atype = self._expr_type(a)
            if not types_equal(atype, p.type):
                raise SemanticError(
                    f"Incompatible type of argument #{i+1} in call to '{name}': "
                    f"expected {self._type_str(p.type)}, got {self._type_str(atype)}"
                )
            if p.byref:
                # by-ref arguments must be variables (designator)
                if a.get("type") != "Designator":
                    raise SemanticError(
                        f"Argument #{i+1} in call to '{name}' must be a variable "
                        f"(VAR parameter)"
                    )

        # if used in expression, return function type
        return sym.type if sym.kind == "func" else None

    # ---- If ----

    def _visit_if(self, node: Dict[str, Any]):
        cond_type = self._expr_type(node["cond"])
        if cond_type != "BOOLEAN":
            raise SemanticError(
                f"IF condition must have type BOOLEAN, got {self._type_str(cond_type)}"
            )

        self._visit_statseq(node["then"])
        for e in node.get("elifs", []):
            et = self._expr_type(e["cond"])
            if et != "BOOLEAN":
                raise SemanticError(
                    f"ELSIF condition must have type BOOLEAN, got {self._type_str(et)}"
                )
            self._visit_statseq(e["body"])

        else_body = node.get("else")
        if else_body is not None:
            self._visit_statseq(else_body)

    # ---- While ----

    def _visit_while(self, node: Dict[str, Any]):
        ct = self._expr_type(node["cond"])
        if ct != "BOOLEAN":
            raise SemanticError(
                f"WHILE condition must have type BOOLEAN, got {self._type_str(ct)}"
            )
        self._visit_statseq(node["body"])

    # ---- For ----

    def _visit_for(self, node: Dict[str, Any]):
        varname = node["var"]
        sym = self.current_scope.lookup(varname)
        if sym is None or sym.kind not in ("var", "param"):
            raise SemanticError(f"FOR loop variable '{varname}' is not declared")

        if sym.type != "INTEGER":
            raise SemanticError("FOR loop variable must be of type INTEGER")

        t_start = self._expr_type(node["start"])
        t_stop = self._expr_type(node["stop"])
        if t_start != "INTEGER" or t_stop != "INTEGER":
            raise SemanticError("FOR loop bounds must be of type INTEGER")

        if node.get("step") is not None:
            t_step = self._expr_type(node["step"])
            if t_step != "INTEGER":
                raise SemanticError("FOR loop step (BY ...) must be of type INTEGER")

        self._visit_statseq(node["body"])

    # ---- Return ----

    def _visit_return(self, node: Dict[str, Any]):
        if self.current_proc is None:
            raise SemanticError("RETURN statement outside a function/procedure")

        value = node["value"]
        if self.current_proc.kind == "proc":
            # procedure — no return value
            if value is not None:
                raise SemanticError(
                    "Procedure cannot return a value (RETURN expr is not allowed)"
                )
        else:
            # function — must use RETURN expr
            if value is None:
                raise SemanticError(
                    "Function must return a value (RETURN expr is required)"
                )
            vt = self._expr_type(value)
            if not types_equal(vt, self.current_proc.type):
                raise SemanticError(
                    f"Invalid return type: expected "
                    f"{self._type_str(self.current_proc.type)}, got {self._type_str(vt)}"
                )

    # ------------------------- Expressions -------------------------

    def _expr_type(self, node: Dict[str, Any]) -> Any:
        ntype = node["type"]

        # literals
        if ntype == "Int":
            return "INTEGER"
        if ntype == "Real":
            return "REAL"
        if ntype == "String":
            return "STRING"
        if ntype == "Bool":
            return "BOOLEAN"

        # designator
        if ntype == "Designator":
            return self._designator_type(node, require_variable=False)

        # function call
        if ntype == "Call":
            return self._visit_call(node, used_as_expr=True)

        # unary operations
        if ntype == "UnOp":
            op = node["op"]
            et = self._expr_type(node["expr"])
            if op in ("+", "-"):
                if not is_numeric(et):
                    raise SemanticError(
                        f"Unary operator '{op}' is applicable only to numbers, "
                        f"got {self._type_str(et)}"
                    )
                return et
            raise SemanticError(f"Unknown unary operator '{op}'")

        # binary operations
        if ntype == "BinOp":
            op = node["op"]
            lt = self._expr_type(node["left"])
            rt = self._expr_type(node["right"])

            # arithmetic
            if op in ("+", "-", "*", "/"):
                if not (is_numeric(lt) and is_numeric(rt)):
                    raise SemanticError(
                        f"Arithmetic operator '{op}' is applicable only to numbers "
                        f"(INTEGER/REAL), got {self._type_str(lt)} and {self._type_str(rt)}"
                    )
                if not types_equal(lt, rt):
                    raise SemanticError(
                        f"Operator '{op}' does not allow mixing types "
                        f"(INTEGER with REAL, etc.)"
                    )
                # result has the same type
                return lt

            # comparisons
            if op in ("=", "#", "<", "<=", ">", ">="):
                if not types_equal(lt, rt):
                    raise SemanticError(
                        f"Comparison operator '{op}' requires equal types, "
                        f"got {self._type_str(lt)} and {self._type_str(rt)}"
                    )
                # return BOOLEAN
                return "BOOLEAN"

            raise SemanticError(f"Unknown binary operator '{op}'")

        if ntype == "UnknownFactor":
            raise SemanticError(
                f"Unsupported factor in expression: {node.get('text')}"
            )

        raise SemanticError(f"Unknown expression kind: {ntype}")

    # ------------------------- Designator -------------------------

    def _designator_type(self, node: Dict[str, Any], require_variable: bool) -> Any:
        """
        Determine type of a designator (x, a[0], r.f, etc.).
        If require_variable=True, using func/proc/type is forbidden.
        """
        base_name = node["base"]
        sym = self.current_scope.lookup(base_name)
        if sym is None:
            raise SemanticError(f"Unknown variable/constant '{base_name}'")

        if sym.kind in ("proc", "func", "type") and require_variable:
            raise SemanticError(
                f"Identifier '{base_name}' is not a variable/constant"
            )

        if sym.kind not in ("var", "const", "param"):
            # if this is a function call (Call), we should not get here
            raise SemanticError(
                f"Identifier '{base_name}' is not a valid designator"
            )

        t = sym.type
        selectors = node.get("selectors", [])

        for sel in selectors:
            stype = sel["type"]
            if stype == "Index":
                if not (isinstance(t, dict) and t.get("kind") == "array"):
                    raise SemanticError(
                        f"Indexing is applicable only to arrays, got {self._type_str(t)}"
                    )

                # check that indices are INTEGER
                for arg in sel["args"]:
                    at = self._expr_type(arg)
                    if at != "INTEGER":
                        raise SemanticError(
                            f"Array index must have type INTEGER, "
                            f"got {self._type_str(at)}"
                        )

                used_dims = len(sel["args"])
                if used_dims > t["dims"]:
                    raise SemanticError("Too many indices for array")

                if used_dims == t["dims"]:
                    # element type
                    t = t["elem"]
                else:
                    # remaining array with lower dimension
                    t = {
                        "kind": "array",
                        "dims": t["dims"] - used_dims,
                        "elem": t["elem"],
                    }

            elif stype == "Field":
                if not (isinstance(t, dict) and t.get("kind") == "record"):
                    raise SemanticError(
                        f"Field access '.' is applicable only to records, "
                        f"got {self._type_str(t)}"
                    )
                fname = sel["name"]
                fields = t["fields"]
                if fname not in fields:
                    raise SemanticError(f"Record does not contain field '{fname}'")
                t = fields[fname]

            else:
                raise SemanticError(f"Unknown selector: {stype}")

        return t

    # ------------------------- Type-to-string utility -------------------------

    def _type_str(self, t: Any) -> str:
        if isinstance(t, str):
            return t
        if isinstance(t, dict):
            if t.get("kind") == "array":
                return f"ARRAY[{t['dims']}] OF {self._type_str(t['elem'])}"
            if t.get("kind") == "record":
                return "RECORD{...}"
        return str(t)
