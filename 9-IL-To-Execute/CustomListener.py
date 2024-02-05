from gen.TACParser import TACParser
from gen.TACListener import TACListener
from ILMapper import ILMapper


class MyCustomListener(TACListener):

    def __init__(self):
        self.reg_counter = -1
        self.used_regs = 0
        self.il_code = ""
        self.il_header = ""
        self.il_footer = ""

    def create_temp_reg(self):
        self.reg_counter += 1
        self.used_regs += 1
        return 'T' + str(self.reg_counter)

    def manage_reg(self, ctx):
        if ILMapper.is_temp_reg(ctx.getChild(0).reg):
            if ILMapper.is_temp_reg(ctx.getChild(2).reg):
                self.reg_counter -= 1
                ctx.reg = ctx.getChild(0).reg
            else:
                ctx.reg = ctx.getChild(0).reg
        else:
            if ILMapper.is_temp_reg(ctx.getChild(2).reg):
                ctx.reg = ctx.getChild(2).reg
            else:
                ctx.reg = self.create_temp_reg()

    def exitStart(self, ctx: TACParser.StartContext):
        self.il_header = ILMapper.get_msil_header(self.used_regs)
        self.il_footer = ILMapper.get_msil_footer()

        with open("a.il", "w") as my_file:
            my_file.write(self.il_header)
            my_file.write(self.il_code)
            my_file.write(self.il_footer)

        # print(self.il_header)
        # print(self.il_code)
        # print(self.il_footer)

    def exitExprPlus(self, ctx: TACParser.ExprPlusContext):
        self.manage_reg(ctx)
        self.il_code += ILMapper.add(ctx.reg, ctx.expr().reg, ctx.term().reg)
        print(ctx.reg, '=', ctx.expr().reg, '+', ctx.term().reg)

    def exitExprMinus(self, ctx: TACParser.ExprMinusContext):
        self.manage_reg(ctx)
        self.il_code += ILMapper.sub(ctx.reg, ctx.expr().reg, ctx.term().reg)
        print(ctx.reg, '=', ctx.expr().reg, '-', ctx.term().reg)

    def exitExprT(self, ctx: TACParser.ExprTContext):
        ctx.reg = ctx.term().reg

    def exitTermDiv(self, ctx: TACParser.TermDivContext):
        self.manage_reg(ctx)
        self.il_code += ILMapper.div(ctx.reg, ctx.term().reg, ctx.fact().reg)
        print(ctx.reg, '=', ctx.term().reg, '/', ctx.fact().reg)

    def exitTermF(self, ctx: TACParser.TermFContext):
        ctx.reg = ctx.fact().reg

    def exitTermMul(self, ctx: TACParser.TermMulContext):
        self.manage_reg(ctx)
        self.il_code += ILMapper.mul(ctx.reg, ctx.term().reg, ctx.fact().reg)
        print(ctx.reg, '=', ctx.term().reg, '*', ctx.fact().reg)

    def exitFactId(self, ctx: TACParser.FactIdContext):
        ctx.reg = ctx.getText()

    def exitFactNum(self, ctx: TACParser.FactNumContext):
        ctx.reg = ctx.getText()

    def exitFactE(self, ctx: TACParser.FactEContext):
        ctx.reg = ctx.expr().reg
