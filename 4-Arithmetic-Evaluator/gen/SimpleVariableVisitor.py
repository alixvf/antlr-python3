from antlr4 import *
if "." in __name__:
    from .SimpleVariableParser import SimpleVariableParser
else:
    from SimpleVariableParser import SimpleVariableParser

# This class defines a complete generic visitor for a parse tree produced by SimpleVariableParser.

class SimpleVariableVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleVariableParser#start.
    def visitStart(self, ctx:SimpleVariableParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleVariableParser#varDecl.
    def visitVarDecl(self, ctx:SimpleVariableParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleVariableParser#printStmt.
    def visitPrintStmt(self, ctx:SimpleVariableParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleVariableParser#arithmeticExpr_.
    def visitArithmeticExpr_(self, ctx:SimpleVariableParser.ArithmeticExpr_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleVariableParser#arithmeticTerm_.
    def visitArithmeticTerm_(self, ctx:SimpleVariableParser.ArithmeticTerm_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleVariableParser#arithmeticFactor.
    def visitArithmeticFactor(self, ctx:SimpleVariableParser.ArithmeticFactorContext):
        return self.visitChildren(ctx)



del SimpleVariableParser