# Generated from grammar/MiniOberon.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniOberonParser import MiniOberonParser
else:
    from MiniOberonParser import MiniOberonParser

# This class defines a complete generic visitor for a parse tree produced by MiniOberonParser.

class MiniOberonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniOberonParser#program.
    def visitProgram(self, ctx:MiniOberonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#module.
    def visitModule(self, ctx:MiniOberonParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#block.
    def visitBlock(self, ctx:MiniOberonParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#declarations.
    def visitDeclarations(self, ctx:MiniOberonParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#constsec.
    def visitConstsec(self, ctx:MiniOberonParser.ConstsecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#constdecl.
    def visitConstdecl(self, ctx:MiniOberonParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#typesec.
    def visitTypesec(self, ctx:MiniOberonParser.TypesecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#typedecl.
    def visitTypedecl(self, ctx:MiniOberonParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#varsec.
    def visitVarsec(self, ctx:MiniOberonParser.VarsecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#vardecl.
    def visitVardecl(self, ctx:MiniOberonParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#type_.
    def visitType_(self, ctx:MiniOberonParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#basetype.
    def visitBasetype(self, ctx:MiniOberonParser.BasetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#arraytype.
    def visitArraytype(self, ctx:MiniOberonParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#dimlist.
    def visitDimlist(self, ctx:MiniOberonParser.DimlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#dimitem.
    def visitDimitem(self, ctx:MiniOberonParser.DimitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#elemtype.
    def visitElemtype(self, ctx:MiniOberonParser.ElemtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#recordtype.
    def visitRecordtype(self, ctx:MiniOberonParser.RecordtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#procdecl.
    def visitProcdecl(self, ctx:MiniOberonParser.ProcdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#paramlist.
    def visitParamlist(self, ctx:MiniOberonParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#param.
    def visitParam(self, ctx:MiniOberonParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#identlist.
    def visitIdentlist(self, ctx:MiniOberonParser.IdentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#statseq.
    def visitStatseq(self, ctx:MiniOberonParser.StatseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#statement.
    def visitStatement(self, ctx:MiniOberonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#assign.
    def visitAssign(self, ctx:MiniOberonParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#call.
    def visitCall(self, ctx:MiniOberonParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#arglist.
    def visitArglist(self, ctx:MiniOberonParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#ifstmt.
    def visitIfstmt(self, ctx:MiniOberonParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#whilestmt.
    def visitWhilestmt(self, ctx:MiniOberonParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#forstmt.
    def visitForstmt(self, ctx:MiniOberonParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniOberonParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#designator.
    def visitDesignator(self, ctx:MiniOberonParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#selectors.
    def visitSelectors(self, ctx:MiniOberonParser.SelectorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#selector.
    def visitSelector(self, ctx:MiniOberonParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#exprlist.
    def visitExprlist(self, ctx:MiniOberonParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#expr.
    def visitExpr(self, ctx:MiniOberonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#relop.
    def visitRelop(self, ctx:MiniOberonParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#simpleexpr.
    def visitSimpleexpr(self, ctx:MiniOberonParser.SimpleexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#sign.
    def visitSign(self, ctx:MiniOberonParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#addop.
    def visitAddop(self, ctx:MiniOberonParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#term.
    def visitTerm(self, ctx:MiniOberonParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#mulop.
    def visitMulop(self, ctx:MiniOberonParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#factor.
    def visitFactor(self, ctx:MiniOberonParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#boollit.
    def visitBoollit(self, ctx:MiniOberonParser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniOberonParser#number.
    def visitNumber(self, ctx:MiniOberonParser.NumberContext):
        return self.visitChildren(ctx)



del MiniOberonParser