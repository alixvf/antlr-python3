from gen.TypeCheckerListener import TypeCheckerListener
from gen.TypeCheckerParser import TypeCheckerParser


class CustomTypeCheckerListener(TypeCheckerListener):
    def is_string(self, fact_type):
        return fact_type == "STRING"

    def is_integer(self, fact_type):
        return fact_type == "INTEGER"

    def is_float(self, fact_type):
        return fact_type == "FLOAT"

    def exitFactString(self, ctx: TypeCheckerParser.FactStringContext):
        ctx.type = "STRING"

    def exitFactInteger(self, ctx: TypeCheckerParser.FactIntegerContext):
        ctx.type = "INTEGER"

    def exitFactFloat(self, ctx: TypeCheckerParser.FactFloatContext):
        ctx.type = "FLOAT"

    def exitFactExpr(self, ctx: TypeCheckerParser.FactExprContext):
        ctx.type = ctx.getChild(1).type

    def exitTerm1(self, ctx: TypeCheckerParser.Term1Context):
        if self.is_string(ctx.term().type) or self.is_string(ctx.fact().type):
            raise Exception("Type Error: String cannot be multiplied")
        elif self.is_float(ctx.term().type) or self.is_float(ctx.fact().type):
            ctx.type = "FLOAT"
        else:
            ctx.type = "INT"

    def exitTerm2(self, ctx: TypeCheckerParser.Term2Context):
        if self.is_string(ctx.term().type) or self.is_string(ctx.fact().type):
            raise Exception("Type Error: String cannot be divided")
        elif self.is_float(ctx.term().type) or self.is_float(ctx.fact().type):
            ctx.type = "FLOAT"
        else:
            ctx.type = "INT"

    def exitTerm3(self, ctx: TypeCheckerParser.Term3Context):
        ctx.type = ctx.fact().type

    def exitExpr1(self, ctx: TypeCheckerParser.Expr1Context):
        if self.is_string(ctx.expr().type):
            ctx.type = "STRING"
        elif self.is_string(ctx.term().type):
            raise Exception("Type Error: numeric value cannot be concatenated with string")
        elif self.is_float(ctx.expr().type) or self.is_float(ctx.term().type):
            ctx.type = "FLOAT"
        else:
            ctx.type = "INT"

    def exitExpr2(self, ctx: TypeCheckerParser.Expr2Context):
        if self.is_string(ctx.expr().type) or self.is_string(ctx.term().type):
            raise Exception("Type Error: String cannot be subtracted")
        elif self.is_float(ctx.expr().type) or self.is_float(ctx.term().type):
            ctx.type = "FLOAT"
        else:
            ctx.type = "INT"

    def exitExpr3(self, ctx: TypeCheckerParser.Expr3Context):
        ctx.type = ctx.term().type

    def exitStart(self, ctx: TypeCheckerParser.StartContext):
        print("Overall type:", ctx.expr().type)
