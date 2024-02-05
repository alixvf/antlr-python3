from gen.ExprParser import ExprParser
from gen.ExprListener import ExprListener


class MyCustomListener(ExprListener):
    def __init__(self):
        self.value = 0

    def exitFact1(self, ctx: ExprParser.Fact1Context):
        ctx.val = ctx.getChild(0).val

    def exitFact2(self, ctx: ExprParser.Fact2Context):
        ctx.val = float(ctx.getText())

    def exitFact3(self, ctx: ExprParser.Fact3Context):
        ctx.val = float(ctx.getChild(1).val)

    def exitTerm1(self, ctx: ExprParser.Term1Context):
        ctx.val = ctx.getChild(0).val * ctx.getChild(2).val

    def exitTerm2(self, ctx: ExprParser.Term1Context):
        ctx.val = ctx.getChild(0).val / ctx.getChild(2).val

    def exitTerm3(self, ctx: ExprParser.Term3Context):
        ctx.val = ctx.getChild(0).val

    def exitExpr1(self, ctx: ExprParser.Expr1Context):
        ctx.val = ctx.getChild(0).val + ctx.getChild(2).val

    def exitExpr2(self, ctx: ExprParser.Expr1Context):
        ctx.val = ctx.getChild(0).val - ctx.getChild(2).val

    def exitExpr3(self, ctx: ExprParser.Expr1Context):
        ctx.val = ctx.getChild(0).val

    def exitStart(self, ctx: ExprParser.StartContext):
        self.value = ctx.getChild(2).val
