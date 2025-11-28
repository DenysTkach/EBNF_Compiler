# Generated from grammar/MiniOberon.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniOberonParser import MiniOberonParser
else:
    from MiniOberonParser import MiniOberonParser

# This class defines a complete listener for a parse tree produced by MiniOberonParser.
class MiniOberonListener(ParseTreeListener):

    # Enter a parse tree produced by MiniOberonParser#program.
    def enterProgram(self, ctx:MiniOberonParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#program.
    def exitProgram(self, ctx:MiniOberonParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#module.
    def enterModule(self, ctx:MiniOberonParser.ModuleContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#module.
    def exitModule(self, ctx:MiniOberonParser.ModuleContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#block.
    def enterBlock(self, ctx:MiniOberonParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#block.
    def exitBlock(self, ctx:MiniOberonParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#declarations.
    def enterDeclarations(self, ctx:MiniOberonParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#declarations.
    def exitDeclarations(self, ctx:MiniOberonParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#constsec.
    def enterConstsec(self, ctx:MiniOberonParser.ConstsecContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#constsec.
    def exitConstsec(self, ctx:MiniOberonParser.ConstsecContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#constdecl.
    def enterConstdecl(self, ctx:MiniOberonParser.ConstdeclContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#constdecl.
    def exitConstdecl(self, ctx:MiniOberonParser.ConstdeclContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#typesec.
    def enterTypesec(self, ctx:MiniOberonParser.TypesecContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#typesec.
    def exitTypesec(self, ctx:MiniOberonParser.TypesecContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#typedecl.
    def enterTypedecl(self, ctx:MiniOberonParser.TypedeclContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#typedecl.
    def exitTypedecl(self, ctx:MiniOberonParser.TypedeclContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#varsec.
    def enterVarsec(self, ctx:MiniOberonParser.VarsecContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#varsec.
    def exitVarsec(self, ctx:MiniOberonParser.VarsecContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#vardecl.
    def enterVardecl(self, ctx:MiniOberonParser.VardeclContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#vardecl.
    def exitVardecl(self, ctx:MiniOberonParser.VardeclContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#type_.
    def enterType_(self, ctx:MiniOberonParser.Type_Context):
        pass

    # Exit a parse tree produced by MiniOberonParser#type_.
    def exitType_(self, ctx:MiniOberonParser.Type_Context):
        pass


    # Enter a parse tree produced by MiniOberonParser#basetype.
    def enterBasetype(self, ctx:MiniOberonParser.BasetypeContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#basetype.
    def exitBasetype(self, ctx:MiniOberonParser.BasetypeContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#arraytype.
    def enterArraytype(self, ctx:MiniOberonParser.ArraytypeContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#arraytype.
    def exitArraytype(self, ctx:MiniOberonParser.ArraytypeContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#dimlist.
    def enterDimlist(self, ctx:MiniOberonParser.DimlistContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#dimlist.
    def exitDimlist(self, ctx:MiniOberonParser.DimlistContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#dimitem.
    def enterDimitem(self, ctx:MiniOberonParser.DimitemContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#dimitem.
    def exitDimitem(self, ctx:MiniOberonParser.DimitemContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#elemtype.
    def enterElemtype(self, ctx:MiniOberonParser.ElemtypeContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#elemtype.
    def exitElemtype(self, ctx:MiniOberonParser.ElemtypeContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#recordtype.
    def enterRecordtype(self, ctx:MiniOberonParser.RecordtypeContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#recordtype.
    def exitRecordtype(self, ctx:MiniOberonParser.RecordtypeContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#procdecl.
    def enterProcdecl(self, ctx:MiniOberonParser.ProcdeclContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#procdecl.
    def exitProcdecl(self, ctx:MiniOberonParser.ProcdeclContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#paramlist.
    def enterParamlist(self, ctx:MiniOberonParser.ParamlistContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#paramlist.
    def exitParamlist(self, ctx:MiniOberonParser.ParamlistContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#param.
    def enterParam(self, ctx:MiniOberonParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#param.
    def exitParam(self, ctx:MiniOberonParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#identlist.
    def enterIdentlist(self, ctx:MiniOberonParser.IdentlistContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#identlist.
    def exitIdentlist(self, ctx:MiniOberonParser.IdentlistContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#statseq.
    def enterStatseq(self, ctx:MiniOberonParser.StatseqContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#statseq.
    def exitStatseq(self, ctx:MiniOberonParser.StatseqContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#statement.
    def enterStatement(self, ctx:MiniOberonParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#statement.
    def exitStatement(self, ctx:MiniOberonParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#assign.
    def enterAssign(self, ctx:MiniOberonParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#assign.
    def exitAssign(self, ctx:MiniOberonParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#call.
    def enterCall(self, ctx:MiniOberonParser.CallContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#call.
    def exitCall(self, ctx:MiniOberonParser.CallContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#arglist.
    def enterArglist(self, ctx:MiniOberonParser.ArglistContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#arglist.
    def exitArglist(self, ctx:MiniOberonParser.ArglistContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#ifstmt.
    def enterIfstmt(self, ctx:MiniOberonParser.IfstmtContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#ifstmt.
    def exitIfstmt(self, ctx:MiniOberonParser.IfstmtContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#whilestmt.
    def enterWhilestmt(self, ctx:MiniOberonParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#whilestmt.
    def exitWhilestmt(self, ctx:MiniOberonParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#forstmt.
    def enterForstmt(self, ctx:MiniOberonParser.ForstmtContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#forstmt.
    def exitForstmt(self, ctx:MiniOberonParser.ForstmtContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#returnstmt.
    def enterReturnstmt(self, ctx:MiniOberonParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#returnstmt.
    def exitReturnstmt(self, ctx:MiniOberonParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#designator.
    def enterDesignator(self, ctx:MiniOberonParser.DesignatorContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#designator.
    def exitDesignator(self, ctx:MiniOberonParser.DesignatorContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#selectors.
    def enterSelectors(self, ctx:MiniOberonParser.SelectorsContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#selectors.
    def exitSelectors(self, ctx:MiniOberonParser.SelectorsContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#selector.
    def enterSelector(self, ctx:MiniOberonParser.SelectorContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#selector.
    def exitSelector(self, ctx:MiniOberonParser.SelectorContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#exprlist.
    def enterExprlist(self, ctx:MiniOberonParser.ExprlistContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#exprlist.
    def exitExprlist(self, ctx:MiniOberonParser.ExprlistContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#expr.
    def enterExpr(self, ctx:MiniOberonParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#expr.
    def exitExpr(self, ctx:MiniOberonParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#relop.
    def enterRelop(self, ctx:MiniOberonParser.RelopContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#relop.
    def exitRelop(self, ctx:MiniOberonParser.RelopContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#simpleexpr.
    def enterSimpleexpr(self, ctx:MiniOberonParser.SimpleexprContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#simpleexpr.
    def exitSimpleexpr(self, ctx:MiniOberonParser.SimpleexprContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#sign.
    def enterSign(self, ctx:MiniOberonParser.SignContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#sign.
    def exitSign(self, ctx:MiniOberonParser.SignContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#addop.
    def enterAddop(self, ctx:MiniOberonParser.AddopContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#addop.
    def exitAddop(self, ctx:MiniOberonParser.AddopContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#term.
    def enterTerm(self, ctx:MiniOberonParser.TermContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#term.
    def exitTerm(self, ctx:MiniOberonParser.TermContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#mulop.
    def enterMulop(self, ctx:MiniOberonParser.MulopContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#mulop.
    def exitMulop(self, ctx:MiniOberonParser.MulopContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#factor.
    def enterFactor(self, ctx:MiniOberonParser.FactorContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#factor.
    def exitFactor(self, ctx:MiniOberonParser.FactorContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#boollit.
    def enterBoollit(self, ctx:MiniOberonParser.BoollitContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#boollit.
    def exitBoollit(self, ctx:MiniOberonParser.BoollitContext):
        pass


    # Enter a parse tree produced by MiniOberonParser#number.
    def enterNumber(self, ctx:MiniOberonParser.NumberContext):
        pass

    # Exit a parse tree produced by MiniOberonParser#number.
    def exitNumber(self, ctx:MiniOberonParser.NumberContext):
        pass



del MiniOberonParser