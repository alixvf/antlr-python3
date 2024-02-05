from antlr4 import *
if "." in __name__:
    from .ArithmeticExpressionParser import ArithmeticExpressionParser
else:
    from ArithmeticExpressionParser import ArithmeticExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticExpressionParser.

class ArithmeticExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticExpressionParser#start.
    def visitStart(self, ctx:ArithmeticExpressionParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#expr.
    def visitExpr(self, ctx:ArithmeticExpressionParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#term.
    def visitTerm(self, ctx:ArithmeticExpressionParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor.
    def visitFactor(self, ctx:ArithmeticExpressionParser.FactorContext):
        return self.visitChildren(ctx)



del ArithmeticExpressionParser