from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#start.
    def enterStart(self, ctx:ExprParser.StartContext):
        pass

    # Exit a parse tree produced by ExprParser#start.
    def exitStart(self, ctx:ExprParser.StartContext):
        pass


    # Enter a parse tree produced by ExprParser#expr3.
    def enterExpr3(self, ctx:ExprParser.Expr3Context):
        pass

    # Exit a parse tree produced by ExprParser#expr3.
    def exitExpr3(self, ctx:ExprParser.Expr3Context):
        pass


    # Enter a parse tree produced by ExprParser#expr2.
    def enterExpr2(self, ctx:ExprParser.Expr2Context):
        pass

    # Exit a parse tree produced by ExprParser#expr2.
    def exitExpr2(self, ctx:ExprParser.Expr2Context):
        pass


    # Enter a parse tree produced by ExprParser#expr1.
    def enterExpr1(self, ctx:ExprParser.Expr1Context):
        pass

    # Exit a parse tree produced by ExprParser#expr1.
    def exitExpr1(self, ctx:ExprParser.Expr1Context):
        pass


    # Enter a parse tree produced by ExprParser#term2.
    def enterTerm2(self, ctx:ExprParser.Term2Context):
        pass

    # Exit a parse tree produced by ExprParser#term2.
    def exitTerm2(self, ctx:ExprParser.Term2Context):
        pass


    # Enter a parse tree produced by ExprParser#term3.
    def enterTerm3(self, ctx:ExprParser.Term3Context):
        pass

    # Exit a parse tree produced by ExprParser#term3.
    def exitTerm3(self, ctx:ExprParser.Term3Context):
        pass


    # Enter a parse tree produced by ExprParser#term1.
    def enterTerm1(self, ctx:ExprParser.Term1Context):
        pass

    # Exit a parse tree produced by ExprParser#term1.
    def exitTerm1(self, ctx:ExprParser.Term1Context):
        pass


    # Enter a parse tree produced by ExprParser#fact1.
    def enterFact1(self, ctx:ExprParser.Fact1Context):
        pass

    # Exit a parse tree produced by ExprParser#fact1.
    def exitFact1(self, ctx:ExprParser.Fact1Context):
        pass


    # Enter a parse tree produced by ExprParser#fact2.
    def enterFact2(self, ctx:ExprParser.Fact2Context):
        pass

    # Exit a parse tree produced by ExprParser#fact2.
    def exitFact2(self, ctx:ExprParser.Fact2Context):
        pass


    # Enter a parse tree produced by ExprParser#fact3.
    def enterFact3(self, ctx:ExprParser.Fact3Context):
        pass

    # Exit a parse tree produced by ExprParser#fact3.
    def exitFact3(self, ctx:ExprParser.Fact3Context):
        pass



del ExprParser