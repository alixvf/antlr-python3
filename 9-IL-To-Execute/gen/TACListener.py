from antlr4 import *
if "." in __name__:
    from .TACParser import TACParser
else:
    from TACParser import TACParser

# This class defines a complete listener for a parse tree produced by TACParser.
class TACListener(ParseTreeListener):

    # Enter a parse tree produced by TACParser#start.
    def enterStart(self, ctx:TACParser.StartContext):
        pass

    # Exit a parse tree produced by TACParser#start.
    def exitStart(self, ctx:TACParser.StartContext):
        pass


    # Enter a parse tree produced by TACParser#exprPlus.
    def enterExprPlus(self, ctx:TACParser.ExprPlusContext):
        pass

    # Exit a parse tree produced by TACParser#exprPlus.
    def exitExprPlus(self, ctx:TACParser.ExprPlusContext):
        pass


    # Enter a parse tree produced by TACParser#exprMinus.
    def enterExprMinus(self, ctx:TACParser.ExprMinusContext):
        pass

    # Exit a parse tree produced by TACParser#exprMinus.
    def exitExprMinus(self, ctx:TACParser.ExprMinusContext):
        pass


    # Enter a parse tree produced by TACParser#exprT.
    def enterExprT(self, ctx:TACParser.ExprTContext):
        pass

    # Exit a parse tree produced by TACParser#exprT.
    def exitExprT(self, ctx:TACParser.ExprTContext):
        pass


    # Enter a parse tree produced by TACParser#termDiv.
    def enterTermDiv(self, ctx:TACParser.TermDivContext):
        pass

    # Exit a parse tree produced by TACParser#termDiv.
    def exitTermDiv(self, ctx:TACParser.TermDivContext):
        pass


    # Enter a parse tree produced by TACParser#termF.
    def enterTermF(self, ctx:TACParser.TermFContext):
        pass

    # Exit a parse tree produced by TACParser#termF.
    def exitTermF(self, ctx:TACParser.TermFContext):
        pass


    # Enter a parse tree produced by TACParser#termMul.
    def enterTermMul(self, ctx:TACParser.TermMulContext):
        pass

    # Exit a parse tree produced by TACParser#termMul.
    def exitTermMul(self, ctx:TACParser.TermMulContext):
        pass


    # Enter a parse tree produced by TACParser#factId.
    def enterFactId(self, ctx:TACParser.FactIdContext):
        pass

    # Exit a parse tree produced by TACParser#factId.
    def exitFactId(self, ctx:TACParser.FactIdContext):
        pass


    # Enter a parse tree produced by TACParser#factNum.
    def enterFactNum(self, ctx:TACParser.FactNumContext):
        pass

    # Exit a parse tree produced by TACParser#factNum.
    def exitFactNum(self, ctx:TACParser.FactNumContext):
        pass


    # Enter a parse tree produced by TACParser#factE.
    def enterFactE(self, ctx:TACParser.FactEContext):
        pass

    # Exit a parse tree produced by TACParser#factE.
    def exitFactE(self, ctx:TACParser.FactEContext):
        pass



del TACParser