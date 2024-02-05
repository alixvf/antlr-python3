from gen.BasicExprVisitor import BasicExprVisitor


class EvalVisitor(BasicExprVisitor):

    def visitStart(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return l[0].getText()
        elif len(l) == 3:
            return self.visit(l[0]) + self.visit(l[2])
