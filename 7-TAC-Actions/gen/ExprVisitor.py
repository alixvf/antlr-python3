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


    # Visit a parse tree produced by ExprParser#expr_Plus_Term.
    def visitExpr_Plus_Term(self, ctx:ExprParser.Expr_Plus_TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr_Minus_Term.
    def visitExpr_Minus_Term(self, ctx:ExprParser.Expr_Minus_TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr_Term.
    def visitExpr_Term(self, ctx:ExprParser.Expr_TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term_Mul_Factor.
    def visitTerm_Mul_Factor(self, ctx:ExprParser.Term_Mul_FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term_Div_Factor.
    def visitTerm_Div_Factor(self, ctx:ExprParser.Term_Div_FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term_Factor.
    def visitTerm_Factor(self, ctx:ExprParser.Term_FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor_Id.
    def visitFactor_Id(self, ctx:ExprParser.Factor_IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor_Number.
    def visitFactor_Number(self, ctx:ExprParser.Factor_NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor_Expr.
    def visitFactor_Expr(self, ctx:ExprParser.Factor_ExprContext):
        return self.visitChildren(ctx)



del ExprParser