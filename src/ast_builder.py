# -*- coding: utf-8 -*-
"""
Простой AST-builder для MiniOberon (под твою грамматику MiniOberon.g4).
Строит деревья в виде словарей/списков (уровень новичка, много комментариев).
"""

from generated.MiniOberonVisitor import MiniOberonVisitor
from generated.MiniOberonParser import MiniOberonParser


# ------------------------- Вспомогательные функции -------------------------

def _strip_quotes(s: str) -> str:
    """Снять внешние кавычки у строкового литерала. Экранирование можно доработать позже."""
    if len(s) >= 2 and s[0] == s[-1] == '"':
        return s[1:-1]
    return s


def _try_int(txt: str):
    """Попробовать преобразовать размерность массива в int (если это число), иначе вернуть строку."""
    try:
        return int(txt)
    except ValueError:
        return txt


def _fold_left_binops(first_node, ops, rest_nodes):
    """
    Свернуть цепочку бинарных операций в левую ассоциативность.
    Пример: first (+) n1 (+) n2  =>  BinOp('+', BinOp('+', first, n1), n2)
    """
    node = first_node
    for op_token, rhs in zip(ops, rest_nodes):
        op = op_token.getText()
        node = {"type": "BinOp", "op": op, "left": node, "right": rhs}
    return node


# ------------------------------- AST-builder -------------------------------

class AstBuilderVisitor(MiniOberonVisitor):
    # ---------- program / module / block ----------

    def visitProgram(self, ctx: MiniOberonParser.ProgramContext):
        mod = self.visit(ctx.module())
        return {"type": "Program", "module": mod}

    def visitModule(self, ctx: MiniOberonParser.ModuleContext):
        name = ctx.IDENT(0).getText()
        block = self.visit(ctx.block())
        end_name = ctx.IDENT(1).getText()
        return {"type": "Module", "name": name, "end": end_name, "block": block}

    def visitBlock(self, ctx: MiniOberonParser.BlockContext):
        decls = self.visit(ctx.declarations()) if ctx.declarations() else []
        body = None
        # В блоке может быть опциональный BEGIN ... END
        if ctx.statseq():
            body = self.visit(ctx.statseq())
        return {"type": "Block", "decls": decls, "body": body}

    def visitDeclarations(self, ctx: MiniOberonParser.DeclarationsContext):
        # (constsec | typesec | varsec | procdecl)*
        items = []
        for ch in ctx.getChildren():
            node = self.visit(ch)
            if node is None:
                continue
            if isinstance(node, list):
                items.extend(node)
            else:
                items.append(node)
        return items

    # ---------- CONST / TYPE / VAR ----------

    def visitConstsec(self, ctx: MiniOberonParser.ConstsecContext):
        decls = []
        for c in ctx.constdecl():
            decls.append(self.visit(c))
        return {"type": "ConstSec", "decls": decls}

    def visitConstdecl(self, ctx: MiniOberonParser.ConstdeclContext):
        name = ctx.IDENT().getText()
        value = self.visit(ctx.expr())
        return {"type": "ConstDecl", "name": name, "value": value}

    def visitTypesec(self, ctx: MiniOberonParser.TypesecContext):
        decls = []
        for t in ctx.typedecl():
            decls.append(self.visit(t))
        return {"type": "TypeSec", "decls": decls}

    def visitTypedecl(self, ctx: MiniOberonParser.TypedeclContext):
        name = ctx.IDENT().getText()
        ty = self.visit(ctx.type_())
        return {"type": "TypeDecl", "name": name, "value": ty}

    def visitVarsec(self, ctx: MiniOberonParser.VarsecContext):
        decls = []
        for vd in ctx.vardecl():
            decls.append(self.visit(vd))
        return {"type": "VarSec", "decls": decls}

    def visitVardecl(self, ctx: MiniOberonParser.VardeclContext):
        # identlist ':' type_
        id_tokens = ctx.identlist().IDENT()
        if isinstance(id_tokens, list):
            names = [t.getText() for t in id_tokens]
        else:
            names = [id_tokens.getText()]
        ty = self.visit(ctx.type_())
        return {"type": "VarDecl", "names": names, "var_type": ty}

    # ------------------------- Типы -------------------------

    def visitType_(self, ctx: MiniOberonParser.Type_Context):
        if ctx.basetype():
            return self.visit(ctx.basetype())
        if ctx.arraytype():
            return self.visit(ctx.arraytype())
        if ctx.recordtype():
            return self.visit(ctx.recordtype())
        # именованный тип (aliased)
        return {"type": "NamedType", "name": ctx.IDENT().getText()}

    def visitBasetype(self, ctx: MiniOberonParser.BasetypeContext):
        # INTEGER | REAL | STRING
        return {"type": "BaseType", "name": ctx.getText()}

    def visitArraytype(self, ctx: MiniOberonParser.ArraytypeContext):
        dims = self.visit(ctx.dimlist())
        elem = self.visit(ctx.elemtype())
        return {"type": "ArrayType", "dims": dims, "elem": elem}

    def visitDimlist(self, ctx: MiniOberonParser.DimlistContext):
        items = []
        for d in ctx.dimitem():
            items.append(self.visit(d))
        return items

    def visitDimitem(self, ctx: MiniOberonParser.DimitemContext):
        # IDENT | INTLIT
        txt = ctx.getText()
        return _try_int(txt)

    def visitElemtype(self, ctx: MiniOberonParser.ElemtypeContext):
        if ctx.basetype():
            return self.visit(ctx.basetype())
        if ctx.arraytype():
            return self.visit(ctx.arraytype())
        return {"type": "NamedType", "name": ctx.IDENT().getText()}

    def visitRecordtype(self, ctx: MiniOberonParser.RecordtypeContext):
        # RECORD (identlist ':' type_ ';')* END
        fields = []
        # В g4 нет отдельных подправил для полей, обойдёмся прямым доступом
        # Соберём по парам (identlist, type_) из дочерних контекстов
        for i in range(len(ctx.children)):
            ch = ctx.children[i]
            if isinstance(ch, MiniOberonParser.IdentlistContext):
                # имена полей
                ids = ch.IDENT()
                if isinstance(ids, list):
                    names = [t.getText() for t in ids]
                else:
                    names = [ids.getText()]
                # следующий значимый узел — type_
                # (между ними есть ':' , после type_ — ';')
                # поэтому ищем ближайший type_ вправо
                ty = None
                for j in range(i + 1, len(ctx.children)):
                    if isinstance(ctx.children[j], MiniOberonParser.Type_Context):
                        ty = self.visit(ctx.children[j])
                        break
                fields.append({"names": names, "field_type": ty})
        return {"type": "RecordType", "fields": fields}

    # ----------------- Процедуры / Функции -----------------

    def visitProcdecl(self, ctx: MiniOberonParser.ProcdeclContext):
        # Альтернатива 1: PROCEDURE IDENT '(' paramlist? ')' ';' block IDENT ';'
        # Альтернатива 2: FUNCTION  IDENT '(' paramlist? ')' ':' type_ ';' block IDENT ';'
        text = ctx.getText()
        is_function = ctx.FUNCTION() is not None

        name = ctx.IDENT(0).getText()
        closing = ctx.IDENT(len(ctx.IDENT()) - 1).getText()

        params = []
        if ctx.paramlist():
            params = self.visit(ctx.paramlist())

        ret_type = None
        if is_function:
            ret_type = self.visit(ctx.type_())

        body = self.visit(ctx.block())

        if is_function:
            return {
                "type": "FunctionDecl",
                "name": name,
                "params": params,
                "return_type": ret_type,
                "body": body,
                "end": closing,
            }
        else:
            return {
                "type": "ProcedureDecl",
                "name": name,
                "params": params,
                "body": body,
                "end": closing,
            }

    def visitParamlist(self, ctx: MiniOberonParser.ParamlistContext):
        items = []
        for p in ctx.param():
            items.append(self.visit(p))
        return items

    def visitParam(self, ctx: MiniOberonParser.ParamContext):
        byref = ctx.VAR() is not None
        id_tokens = ctx.identlist().IDENT()
        names = [t.getText() for t in id_tokens] if isinstance(id_tokens, list) else [id_tokens.getText()]
        ty = self.visit(ctx.type_())
        return {"type": "Param", "names": names, "byref": byref, "param_type": ty}

    def visitIdentlist(self, ctx: MiniOberonParser.IdentlistContext):
        ids = ctx.IDENT()
        if isinstance(ids, list):
            return [t.getText() for t in ids]
        return [ids.getText()]

    # --------------------------- Операторы ---------------------------

    def visitStatseq(self, ctx: MiniOberonParser.StatseqContext):
        stmts = []
        for st in ctx.statement():
            node = self.visit(st)
            if node is not None:
                stmts.append(node)
        return {"type": "StatSeq", "stmts": stmts}

    def visitStatement(self, ctx: MiniOberonParser.StatementContext):
        # Делегируем конкретным методам
        for ch in ctx.getChildren():
            node = self.visit(ch)
            if node is not None:
                return node
        return None

    def visitAssign(self, ctx: MiniOberonParser.AssignContext):
        left = self.visit(ctx.designator())
        right = self.visit(ctx.expr())
        return {"type": "Assign", "left": left, "right": right}

    def visitCall(self, ctx: MiniOberonParser.CallContext):
        fname = ctx.IDENT().getText()
        args = []
        if ctx.arglist():
            for e in ctx.arglist().expr():
                args.append(self.visit(e))
        return {"type": "Call", "name": fname, "args": args}

    def visitIfstmt(self, ctx: MiniOberonParser.IfstmtContext):
        cond = self.visit(ctx.expr(0))
        then_body = self.visit(ctx.statseq(0))

        # ELSIF-блоки
        elifs = []
        # Кол-во ELSIF равно числу пар (expr, statseq) после THEN
        # expr(1..n), statseq(1..n)
        n_elsif = len(ctx.ELSIF())
        for i in range(n_elsif):
            econd = self.visit(ctx.expr(i + 1))
            ebody = self.visit(ctx.statseq(i + 1))
            elifs.append({"cond": econd, "body": ebody})

        # ELSE (если есть) — последний statseq
        else_body = None
        if ctx.ELSE():
            else_body = self.visit(ctx.statseq(len(ctx.statseq()) - 1))

        return {"type": "If", "cond": cond, "then": then_body, "elifs": elifs, "else": else_body}

    def visitWhilestmt(self, ctx: MiniOberonParser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.statseq())
        return {"type": "While", "cond": cond, "body": body}

    def visitForstmt(self, ctx: MiniOberonParser.ForstmtContext):
        varname = ctx.IDENT().getText()
        start = self.visit(ctx.expr(0))
        stop = self.visit(ctx.expr(1))
        step = self.visit(ctx.expr(2)) if ctx.BY() else None
        body = self.visit(ctx.statseq())
        return {"type": "For", "var": varname, "start": start, "stop": stop, "step": step, "body": body}

    def visitReturnstmt(self, ctx: MiniOberonParser.ReturnstmtContext):
        value = self.visit(ctx.expr()) if ctx.expr() else None
        return {"type": "Return", "value": value}

    # --------------------- Дизайнаторы и селекторы ---------------------

    def visitDesignator(self, ctx: MiniOberonParser.DesignatorContext):
        base = ctx.IDENT().getText()
        sels = []
        if ctx.selectors():
            sels = self.visit(ctx.selectors())
        return {"type": "Designator", "base": base, "selectors": sels}

    def visitSelectors(self, ctx: MiniOberonParser.SelectorsContext):
        items = []
        for s in ctx.selector():
            items.append(self.visit(s))
        return items

    def visitSelector(self, ctx: MiniOberonParser.SelectorContext):
        if ctx.exprlist():
            # индексирование: [exprlist]
            args = self.visit(ctx.exprlist())
            return {"type": "Index", "args": args}
        # поле: . IDENT
        return {"type": "Field", "name": ctx.IDENT().getText()}

    def visitExprlist(self, ctx: MiniOberonParser.ExprlistContext):
        return [self.visit(e) for e in ctx.expr()]

    # ------------------------ Выражения ------------------------

    def visitExpr(self, ctx: MiniOberonParser.ExprContext):
        # simpleexpr (relop simpleexpr)?
        left = self.visit(ctx.simpleexpr(0))
        if ctx.relop():
            op = ctx.relop().getText()
            right = self.visit(ctx.simpleexpr(1))
            return {"type": "BinOp", "op": op, "left": left, "right": right}
        return left

    def visitSimpleexpr(self, ctx: MiniOberonParser.SimpleexprContext):
        # sign? term (addop term)*
        term0 = self.visit(ctx.term(0))

        # Унарный знак
        if ctx.sign():
            s = ctx.sign().getText()
            if s == '-':
                term0 = {"type": "UnOp", "op": "-", "expr": term0}
            else:
                # унарный плюс можно просто проигнорировать
                term0 = {"type": "UnOp", "op": "+", "expr": term0}

        # Цепочка +/-
        n_terms = len(ctx.term())
        if n_terms > 1:
            ops = ctx.addop()
            rest = [self.visit(ctx.term(i)) for i in range(1, n_terms)]
            term0 = _fold_left_binops(term0, ops, rest)

        return term0

    def visitTerm(self, ctx: MiniOberonParser.TermContext):
        # factor (mulop factor)*
        f0 = self.visit(ctx.factor(0))
        n_factors = len(ctx.factor())
        if n_factors > 1:
            ops = ctx.mulop()
            rest = [self.visit(ctx.factor(i)) for i in range(1, n_factors)]
            f0 = _fold_left_binops(f0, ops, rest)
        return f0

    def visitFactor(self, ctx: MiniOberonParser.FactorContext):
        # number | STRINGLIT | boollit | call | designator | '(' expr ')'
        if ctx.number():
            return self.visit(ctx.number())

        if ctx.STRINGLIT():
            txt = ctx.STRINGLIT().getText()
            return {"type": "String", "value": _strip_quotes(txt)}

        if ctx.boollit():
            return self.visit(ctx.boollit())

        if ctx.call():
            return self.visit(ctx.call())

        if ctx.designator():
            return self.visit(ctx.designator())

        if ctx.expr():
            return self.visit(ctx.expr())

        return {"type": "UnknownFactor", "text": ctx.getText()}

    def visitBoollit(self, ctx: MiniOberonParser.BoollitContext):
        txt = ctx.getText()
        return {"type": "Bool", "value": txt == "TRUE"}

    def visitNumber(self, ctx: MiniOberonParser.NumberContext):
        txt = ctx.getText()
        if 'e' in txt.lower() or '.' in txt:
            try:
                return {"type": "Real", "value": float(txt)}
            except ValueError:
                # если вдруг не распарсилось — вернём как строку
                return {"type": "RealText", "text": txt}
        else:
            return {"type": "Int", "value": int(txt)}
