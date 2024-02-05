from antlr4 import *
if "." in __name__:
    from .SimpleVariableParser import SimpleVariableParser
else:
    from SimpleVariableParser import SimpleVariableParser

# This class defines a complete listener for a parse tree produced by SimpleVariableParser.
class SimpleVariableListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleVariableParser#start.
    def enterStart(self, ctx:SimpleVariableParser.StartContext):
        pass

    # Exit a parse tree produced by SimpleVariableParser#start.
    def exitStart(self, ctx:SimpleVariableParser.StartContext):
        pass


    # Enter a parse tree produced by SimpleVariableParser#varDecl.
    def enterVarDecl(self, ctx:SimpleVariableParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SimpleVariableParser#varDecl.
    def exitVarDecl(self, ctx:SimpleVariableParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SimpleVariableParser#printStmt.
    def enterPrintStmt(self, ctx:SimpleVariableParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by SimpleVariableParser#printStmt.
    def exitPrintStmt(self, ctx:SimpleVariableParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by SimpleVariableParser#arithmeticExpr_.
    def enterArithmeticExpr_(self, ctx:SimpleVariableParser.ArithmeticExpr_Context):
        pass

    # Exit a parse tree produced by SimpleVariableParser#arithmeticExpr_.
    def exitArithmeticExpr_(self, ctx:SimpleVariableParser.ArithmeticExpr_Context):
        pass


    # Enter a parse tree produced by SimpleVariableParser#arithmeticTerm_.
    def enterArithmeticTerm_(self, ctx:SimpleVariableParser.ArithmeticTerm_Context):
        pass

    # Exit a parse tree produced by SimpleVariableParser#arithmeticTerm_.
    def exitArithmeticTerm_(self, ctx:SimpleVariableParser.ArithmeticTerm_Context):
        pass


    # Enter a parse tree produced by SimpleVariableParser#arithmeticFactor.
    def enterArithmeticFactor(self, ctx:SimpleVariableParser.ArithmeticFactorContext):
        pass

    # Exit a parse tree produced by SimpleVariableParser#arithmeticFactor.
    def exitArithmeticFactor(self, ctx:SimpleVariableParser.ArithmeticFactorContext):
        pass



del SimpleVariableParser