from antlr4 import *
if "." in __name__:
    from .BasicExprParser import BasicExprParser
else:
    from BasicExprParser import BasicExprParser

# This class defines a complete generic visitor for a parse tree produced by BasicExprParser.

class BasicExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicExprParser#start.
    def visitStart(self, ctx:BasicExprParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicExprParser#expr.
    def visitExpr(self, ctx:BasicExprParser.ExprContext):
        return self.visitChildren(ctx)



del BasicExprParser