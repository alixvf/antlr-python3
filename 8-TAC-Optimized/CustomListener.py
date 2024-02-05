from gen.TACParser import TACParser
from gen.TACListener import TACListener


class MyCustomListener(TACListener):

    def __init__(self):
        self.reg_counter = 0

    def create_temp_reg(self):
        self.reg_counter += 1
        return 'T' + str(self.reg_counter)

    def is_temp_reg(self, code):
        return str.startswith(code, "T")

    def remove_temp_reg(self):
        self.reg_counter -= 1

    def exitExprPlus(self, ctx: TACParser.ExprPlusContext):
        if self.is_temp_reg(ctx.expr().reg) and not self.is_temp_reg(ctx.term().reg):
            ctx.reg = ctx.expr().reg
        elif not self.is_temp_reg(ctx.expr().reg) and self.is_temp_reg(ctx.term().reg):
            ctx.reg = ctx.term().reg
        elif self.is_temp_reg(ctx.expr().reg) and self.is_temp_reg(ctx.term().reg):
            if self.is_temp_reg(ctx.term().reg):
                self.remove_temp_reg()
            ctx.reg = ctx.expr().reg
        else:
            ctx.reg = self.create_temp_reg()

        print(ctx.reg, '=', ctx.expr().reg, '+', ctx.term().reg)

    def exitExprMinus(self, ctx: TACParser.ExprMinusContext):
        if self.is_temp_reg(ctx.expr().reg) and not self.is_temp_reg(ctx.term().reg):
            ctx.reg = ctx.expr().reg
        elif not self.is_temp_reg(ctx.expr().reg) and self.is_temp_reg(ctx.term().reg):
            ctx.reg = ctx.term().reg
        elif self.is_temp_reg(ctx.expr().reg) and self.is_temp_reg(ctx.term().reg):
            if self.is_temp_reg(ctx.term().reg):
                self.remove_temp_reg()
            ctx.reg = ctx.expr().reg
        else:
            ctx.reg = self.create_temp_reg()

        print(ctx.reg, '=', ctx.expr().reg, '-', ctx.term().reg)

    def exitExprT(self, ctx: TACParser.ExprTContext):
        ctx.reg = ctx.term().reg

    def exitTermDiv(self, ctx: TACParser.TermDivContext):
        if self.is_temp_reg(ctx.term().reg) and not self.is_temp_reg(ctx.fact().reg):
            ctx.reg = ctx.term().reg
        elif not self.is_temp_reg(ctx.term().reg) and self.is_temp_reg(ctx.fact().reg):
            ctx.reg = ctx.fact().reg
        elif self.is_temp_reg(ctx.term().reg) and self.is_temp_reg(ctx.fact().reg):
            if self.is_temp_reg(ctx.fact().reg):
                self.remove_temp_reg()
            ctx.reg = ctx.term().reg
        else:
            ctx.reg = self.create_temp_reg()

        print(ctx.reg, '=', ctx.term().reg, '/', ctx.fact().reg)

    def exitTermF(self, ctx: TACParser.TermFContext):
        ctx.reg = ctx.fact().reg

    def exitTermMul(self, ctx: TACParser.TermMulContext):
        if self.is_temp_reg(ctx.getChild(0).reg) and not self.is_temp_reg(ctx.fact().reg):
            ctx.reg = ctx.term().reg
        elif not self.is_temp_reg(ctx.term().reg) and self.is_temp_reg(ctx.fact().reg):
            ctx.reg = ctx.fact().reg
        elif self.is_temp_reg(ctx.term().reg) and self.is_temp_reg(ctx.fact().reg):
            if self.is_temp_reg(ctx.fact().reg):
                self.remove_temp_reg()
            ctx.reg = ctx.term().reg
        else:
            ctx.reg = self.create_temp_reg()

        print(ctx.reg, '=', ctx.term().reg, '*', ctx.fact().reg)

    def exitFactId(self, ctx: TACParser.FactIdContext):
        ctx.reg = ctx.getText()

    def exitFactNum(self, ctx: TACParser.FactNumContext):
        ctx.reg = ctx.getText()

    def exitFactE(self, ctx: TACParser.FactEContext):
        ctx.reg = ctx.expr().reg
