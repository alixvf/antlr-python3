from antlr4 import *
if "." in __name__:
    from .BasicExprParser import BasicExprParser
else:
    from BasicExprParser import BasicExprParser

# This class defines a complete listener for a parse tree produced by BasicExprParser.
class BasicExprListener(ParseTreeListener):

    # Enter a parse tree produced by BasicExprParser#start.
    def enterStart(self, ctx:BasicExprParser.StartContext):
        pass

    # Exit a parse tree produced by BasicExprParser#start.
    def exitStart(self, ctx:BasicExprParser.StartContext):
        pass


    # Enter a parse tree produced by BasicExprParser#expr.
    def enterExpr(self, ctx:BasicExprParser.ExprContext):
        pass

    # Exit a parse tree produced by BasicExprParser#expr.
    def exitExpr(self, ctx:BasicExprParser.ExprContext):
        pass



del BasicExprParser