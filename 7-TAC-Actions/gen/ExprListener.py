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


    # Enter a parse tree produced by ExprParser#expr_Plus_Term.
    def enterExpr_Plus_Term(self, ctx:ExprParser.Expr_Plus_TermContext):
        pass

    # Exit a parse tree produced by ExprParser#expr_Plus_Term.
    def exitExpr_Plus_Term(self, ctx:ExprParser.Expr_Plus_TermContext):
        pass


    # Enter a parse tree produced by ExprParser#expr_Minus_Term.
    def enterExpr_Minus_Term(self, ctx:ExprParser.Expr_Minus_TermContext):
        pass

    # Exit a parse tree produced by ExprParser#expr_Minus_Term.
    def exitExpr_Minus_Term(self, ctx:ExprParser.Expr_Minus_TermContext):
        pass


    # Enter a parse tree produced by ExprParser#expr_Term.
    def enterExpr_Term(self, ctx:ExprParser.Expr_TermContext):
        pass

    # Exit a parse tree produced by ExprParser#expr_Term.
    def exitExpr_Term(self, ctx:ExprParser.Expr_TermContext):
        pass


    # Enter a parse tree produced by ExprParser#term_Mul_Factor.
    def enterTerm_Mul_Factor(self, ctx:ExprParser.Term_Mul_FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#term_Mul_Factor.
    def exitTerm_Mul_Factor(self, ctx:ExprParser.Term_Mul_FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#term_Div_Factor.
    def enterTerm_Div_Factor(self, ctx:ExprParser.Term_Div_FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#term_Div_Factor.
    def exitTerm_Div_Factor(self, ctx:ExprParser.Term_Div_FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#term_Factor.
    def enterTerm_Factor(self, ctx:ExprParser.Term_FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#term_Factor.
    def exitTerm_Factor(self, ctx:ExprParser.Term_FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#factor_Id.
    def enterFactor_Id(self, ctx:ExprParser.Factor_IdContext):
        pass

    # Exit a parse tree produced by ExprParser#factor_Id.
    def exitFactor_Id(self, ctx:ExprParser.Factor_IdContext):
        pass


    # Enter a parse tree produced by ExprParser#factor_Number.
    def enterFactor_Number(self, ctx:ExprParser.Factor_NumberContext):
        pass

    # Exit a parse tree produced by ExprParser#factor_Number.
    def exitFactor_Number(self, ctx:ExprParser.Factor_NumberContext):
        pass


    # Enter a parse tree produced by ExprParser#factor_Expr.
    def enterFactor_Expr(self, ctx:ExprParser.Factor_ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#factor_Expr.
    def exitFactor_Expr(self, ctx:ExprParser.Factor_ExprContext):
        pass



del ExprParser