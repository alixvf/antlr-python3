from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#start.
    def visitStart(self, ctx:ExprParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr3.
    def visitExpr3(self, ctx:ExprParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr2.
    def visitExpr2(self, ctx:ExprParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr1.
    def visitExpr1(self, ctx:ExprParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term2.
    def visitTerm2(self, ctx:ExprParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term3.
    def visitTerm3(self, ctx:ExprParser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term1.
    def visitTerm1(self, ctx:ExprParser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fact1.
    def visitFact1(self, ctx:ExprParser.Fact1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fact2.
    def visitFact2(self, ctx:ExprParser.Fact2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fact3.
    def visitFact3(self, ctx:ExprParser.Fact3Context):
        return self.visitChildren(ctx)



del ExprParser