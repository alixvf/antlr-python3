from antlr4 import *
if "." in __name__:
    from .TACParser import TACParser
else:
    from TACParser import TACParser

# This class defines a complete generic visitor for a parse tree produced by TACParser.

class TACVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TACParser#start.
    def visitStart(self, ctx:TACParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#exprPlus.
    def visitExprPlus(self, ctx:TACParser.ExprPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#exprMinus.
    def visitExprMinus(self, ctx:TACParser.ExprMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#exprT.
    def visitExprT(self, ctx:TACParser.ExprTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#termDiv.
    def visitTermDiv(self, ctx:TACParser.TermDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#termF.
    def visitTermF(self, ctx:TACParser.TermFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#termMul.
    def visitTermMul(self, ctx:TACParser.TermMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#factId.
    def visitFactId(self, ctx:TACParser.FactIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#factNum.
    def visitFactNum(self, ctx:TACParser.FactNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#factE.
    def visitFactE(self, ctx:TACParser.FactEContext):
        return self.visitChildren(ctx)



del TACParser