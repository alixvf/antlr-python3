# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,68,
        0,8,1,0,0,0,2,13,1,0,0,0,4,34,1,0,0,0,6,64,1,0,0,0,8,9,5,8,0,0,9,
        10,5,7,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,
        0,14,15,3,4,2,0,15,16,6,1,-1,0,16,31,1,0,0,0,17,18,10,3,0,0,18,19,
        5,3,0,0,19,20,3,4,2,0,20,21,6,1,-1,0,21,22,6,1,-1,0,22,30,1,0,0,
        0,23,24,10,2,0,0,24,25,5,4,0,0,25,26,3,4,2,0,26,27,6,1,-1,0,27,28,
        6,1,-1,0,28,30,1,0,0,0,29,17,1,0,0,0,29,23,1,0,0,0,30,33,1,0,0,0,
        31,29,1,0,0,0,31,32,1,0,0,0,32,3,1,0,0,0,33,31,1,0,0,0,34,35,6,2,
        -1,0,35,36,3,6,3,0,36,37,6,2,-1,0,37,52,1,0,0,0,38,39,10,3,0,0,39,
        40,5,5,0,0,40,41,3,6,3,0,41,42,6,2,-1,0,42,43,6,2,-1,0,43,51,1,0,
        0,0,44,45,10,2,0,0,45,46,5,6,0,0,46,47,3,6,3,0,47,48,6,2,-1,0,48,
        49,6,2,-1,0,49,51,1,0,0,0,50,38,1,0,0,0,50,44,1,0,0,0,51,54,1,0,
        0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,0,54,52,1,0,0,0,55,56,
        5,8,0,0,56,65,6,3,-1,0,57,58,5,9,0,0,58,65,6,3,-1,0,59,60,5,1,0,
        0,60,61,3,2,1,0,61,62,5,2,0,0,62,63,6,3,-1,0,63,65,1,0,0,0,64,55,
        1,0,0,0,64,57,1,0,0,0,64,59,1,0,0,0,65,7,1,0,0,0,5,29,31,50,52,64
    ]

class ExprParser ( Parser ):

    grammarFileName = "TAC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Plus", "MINUS", 
                      "MUL", "DIVIDE", "ASSIGN", "Id", "Number", "Whitespace", 
                      "Newline" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "start", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Plus=3
    MINUS=4
    MUL=5
    DIVIDE=6
    ASSIGN=7
    Id=8
    Number=9
    Whitespace=10
    Newline=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    temp_counter = 0

    def create_temp(self, temp_counter):
        self.temp_counter +=1
        return 'T' + str(self.temp_counter)

    def remove_temp(self):
        self.temp_counter -= 1

    def get_temp(self):
        return 'T' + str(self.temp_counter)




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(ExprParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ExprParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(ExprParser.Id)
            self.state = 9
            self.match(ExprParser.ASSIGN)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.code = str()


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.code = ctx.code


    class Expr_Plus_TermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.e2 = None # ExprContext
            self.t1 = None # TermContext
            self.copyFrom(ctx)

        def Plus(self):
            return self.getToken(ExprParser.Plus, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_Plus_Term" ):
                listener.enterExpr_Plus_Term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_Plus_Term" ):
                listener.exitExpr_Plus_Term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_Plus_Term" ):
                return visitor.visitExpr_Plus_Term(self)
            else:
                return visitor.visitChildren(self)


    class Expr_Minus_TermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.e2 = None # ExprContext
            self.t1 = None # TermContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_Minus_Term" ):
                listener.enterExpr_Minus_Term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_Minus_Term" ):
                listener.exitExpr_Minus_Term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_Minus_Term" ):
                return visitor.visitExpr_Minus_Term(self)
            else:
                return visitor.visitChildren(self)


    class Expr_TermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.t1 = None # TermContext
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_Term" ):
                listener.enterExpr_Term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_Term" ):
                listener.exitExpr_Term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_Term" ):
                return visitor.visitExpr_Term(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.Expr_TermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            localctx.t1 = self.term(0)
            localctx.code = localctx.t1.code
            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.Expr_Plus_TermContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.e2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        self.match(ExprParser.Plus)
                        self.state = 19
                        localctx.t1 = self.term(0)
                        localctx.code = self.create_temp(self.temp_counter)
                        print(localctx.code, '=', localctx.e2.code, '+', localctx.t1.code)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.Expr_Minus_TermContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.e2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 24
                        self.match(ExprParser.MINUS)
                        self.state = 25
                        localctx.t1 = self.term(0)
                        localctx.code = self.create_temp(self.temp_counter)
                        print(localctx.code, '=', localctx.e2.code, '-', localctx.t1.code)
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.code = str()


        def getRuleIndex(self):
            return ExprParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.code = ctx.code


    class Term_Mul_FactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TermContext
            super().__init__(parser)
            self.t2 = None # TermContext
            self.f1 = None # FactorContext
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)
        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(ExprParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_Mul_Factor" ):
                listener.enterTerm_Mul_Factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_Mul_Factor" ):
                listener.exitTerm_Mul_Factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_Mul_Factor" ):
                return visitor.visitTerm_Mul_Factor(self)
            else:
                return visitor.visitChildren(self)


    class Term_Div_FactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TermContext
            super().__init__(parser)
            self.t2 = None # TermContext
            self.f1 = None # FactorContext
            self.copyFrom(ctx)

        def DIVIDE(self):
            return self.getToken(ExprParser.DIVIDE, 0)
        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(ExprParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_Div_Factor" ):
                listener.enterTerm_Div_Factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_Div_Factor" ):
                listener.exitTerm_Div_Factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_Div_Factor" ):
                return visitor.visitTerm_Div_Factor(self)
            else:
                return visitor.visitChildren(self)


    class Term_FactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TermContext
            super().__init__(parser)
            self.f1 = None # FactorContext
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ExprParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_Factor" ):
                listener.enterTerm_Factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_Factor" ):
                listener.exitTerm_Factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_Factor" ):
                return visitor.visitTerm_Factor(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.Term_FactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 35
            localctx.f1 = self.factor()
            localctx.code = localctx.f1.code
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.Term_Mul_FactorContext(self, ExprParser.TermContext(self, _parentctx, _parentState))
                        localctx.t2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        self.match(ExprParser.MUL)
                        self.state = 40
                        localctx.f1 = self.factor()
                        localctx.code = self.create_temp(self.temp_counter)
                        print(localctx.code, '=', localctx.t2.code, '*', localctx.f1.code)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.Term_Div_FactorContext(self, ExprParser.TermContext(self, _parentctx, _parentState))
                        localctx.t2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 44
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 45
                        self.match(ExprParser.DIVIDE)
                        self.state = 46
                        localctx.f1 = self.factor()
                        localctx.code = self.create_temp(self.temp_counter)
                        print(localctx.code, '=', localctx.t2.code, '/', localctx.f1.code)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.code = str()


        def getRuleIndex(self):
            return ExprParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.code = ctx.code



    class Factor_NumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FactorContext
            super().__init__(parser)
            self._Number = None # Token
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(ExprParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_Number" ):
                listener.enterFactor_Number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_Number" ):
                listener.exitFactor_Number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_Number" ):
                return visitor.visitFactor_Number(self)
            else:
                return visitor.visitChildren(self)


    class Factor_IdContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FactorContext
            super().__init__(parser)
            self._Id = None # Token
            self.copyFrom(ctx)

        def Id(self):
            return self.getToken(ExprParser.Id, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_Id" ):
                listener.enterFactor_Id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_Id" ):
                listener.exitFactor_Id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_Id" ):
                return visitor.visitFactor_Id(self)
            else:
                return visitor.visitChildren(self)


    class Factor_ExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FactorContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_Expr" ):
                listener.enterFactor_Expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_Expr" ):
                listener.exitFactor_Expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_Expr" ):
                return visitor.visitFactor_Expr(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = ExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = ExprParser.Factor_IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                localctx._Id = self.match(ExprParser.Id)
                localctx.code = (None if localctx._Id is None else localctx._Id.text)
                pass
            elif token in [9]:
                localctx = ExprParser.Factor_NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                localctx._Number = self.match(ExprParser.Number)
                localctx.code = (None if localctx._Number is None else localctx._Number.text)
                pass
            elif token in [1]:
                localctx = ExprParser.Factor_ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(ExprParser.T__0)
                self.state = 60
                localctx._expr = self.expr(0)
                self.state = 61
                self.match(ExprParser.T__1)
                localctx.code = localctx._expr.code
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




