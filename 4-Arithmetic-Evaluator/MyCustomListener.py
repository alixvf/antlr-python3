from gen.SimpleVariableListener import SimpleVariableListener
from gen.SimpleVariableParser import SimpleVariableParser


class MyCustomListener(SimpleVariableListener):
    variables = {}

    def __int__(self):
        self.variables = {}

    def exitVarDecl(self, ctx: SimpleVariableParser.StmtContext):
        __name = ctx.getChild(1).getText()
        __type = ctx.getChild(0).getText()
        __value = ctx.getChild(3).getText()
        if __type == "int":
            try:
                __value = int(__value)
            except:
                raise Exception("Syntax Error: line " + str(ctx.start.line) + ",column " + str(
                    ctx.start.column) + " " + "Type mismatch [int]")

        elif __type == "float":
            try:
                __value = float(__value)
            except:
                raise Exception("Syntax Error: line " + str(ctx.start.line) + ",column " + str(ctx.start.column) + " " + "Type mismatch [float]")
        if self.variables.get(__name) is not None:
            raise Exception("Error: redeclration of variable ,line " + str(ctx.start.line) + ",column " + str(
                ctx.start.column))

        self.variables[__name] = {
            "type": __type,
            "value": __value,
        }

    def exitPrintStmt(self, ctx: SimpleVariableParser.PrintStmtContext):
        print(self.exitArithmeticExpr_(ctx.getChild(2)))

    def exitArithmeticExpr_(self, ctx: SimpleVariableParser.ArithmeticExpr_Context):
        result = self.exitArithmeticTerm_(ctx.getChild(0))
        if ctx.getChildCount() == 1:
            return result

        for i in range(0, ctx.getChildCount() - 2, 2):
            op = ctx.getChild(i + 1).getText()
            if op == '+':
                result += self.exitArithmeticTerm_(ctx.getChild(i + 2))
            elif op == '-':
                result -= self.exitArithmeticTerm_(ctx.getChild(i + 2))
        return result

    def exitArithmeticTerm_(self, ctx: SimpleVariableParser.ArithmeticTerm_Context):
        if ctx.getChildCount() == 1:
            return self.exitArithmeticFactor(ctx.getChild(0))

        temp = self.exitArithmeticFactor(ctx.getChild(0))
        for i in range(0, ctx.getChildCount() - 2, 2):
            op = ctx.getChild(1).getText()
            if op == '*':
                temp *= self.exitArithmeticFactor(ctx.getChild(i + 2))
            elif op == '/':
                temp /= self.exitArithmeticFactor(ctx.getChild(i + 2))
        return temp

    def exitArithmeticFactor(self, ctx: SimpleVariableParser.ArithmeticFactorContext):
        if ctx.getChildCount() == 1:
            if ctx.getChild(0).getText() in self.variables:
                return self.variables[ctx.getChild(0).getText()]["value"]
            else:
                try:
                    _ = float(ctx.getChild(0).getText())
                except:
                    raise Exception("Error: line " + str(ctx.start.line) + ",column " + str(ctx.start.column) + " " + "Undefined variable")
                return float(ctx.getChild(0).getText())
        return self.exitArithmeticExpr_(ctx.getChild(1))
