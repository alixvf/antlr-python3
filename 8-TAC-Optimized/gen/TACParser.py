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
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,51,0,
        8,1,0,0,0,2,13,1,0,0,0,4,27,1,0,0,0,6,47,1,0,0,0,8,9,5,8,0,0,9,10,
        5,7,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,
        14,15,3,4,2,0,15,24,1,0,0,0,16,17,10,3,0,0,17,18,5,3,0,0,18,23,3,
        4,2,0,19,20,10,2,0,0,20,21,5,4,0,0,21,23,3,4,2,0,22,16,1,0,0,0,22,
        19,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,
        0,26,24,1,0,0,0,27,28,6,2,-1,0,28,29,3,6,3,0,29,38,1,0,0,0,30,31,
        10,3,0,0,31,32,5,5,0,0,32,37,3,6,3,0,33,34,10,2,0,0,34,35,5,6,0,
        0,35,37,3,6,3,0,36,30,1,0,0,0,36,33,1,0,0,0,37,40,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,48,5,8,0,0,42,
        48,5,9,0,0,43,44,5,1,0,0,44,45,3,2,1,0,45,46,5,2,0,0,46,48,1,0,0,
        0,47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,48,7,1,0,0,0,5,22,24,
        36,38,47
    ]

class TACParser ( Parser ):

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
    RULE_fact = 3

    ruleNames =  [ "start", "expr", "term", "fact" ]

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




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(TACParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(TACParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TACParser.ExprContext,0)


        def EOF(self):
            return self.getToken(TACParser.EOF, 0)

        def getRuleIndex(self):
            return TACParser.RULE_start

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

        localctx = TACParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(TACParser.Id)
            self.state = 9
            self.match(TACParser.ASSIGN)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(TACParser.EOF)
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
            self.reg = str()


        def getRuleIndex(self):
            return TACParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.reg = ctx.reg


    class ExprPlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TACParser.ExprContext,0)

        def Plus(self):
            return self.getToken(TACParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(TACParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPlus" ):
                listener.enterExprPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPlus" ):
                listener.exitExprPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPlus" ):
                return visitor.visitExprPlus(self)
            else:
                return visitor.visitChildren(self)


    class ExprMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TACParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(TACParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(TACParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMinus" ):
                listener.enterExprMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMinus" ):
                listener.exitExprMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMinus" ):
                return visitor.visitExprMinus(self)
            else:
                return visitor.visitChildren(self)


    class ExprTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TACParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprT" ):
                listener.enterExprT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprT" ):
                listener.exitExprT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprT" ):
                return visitor.visitExprT(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TACParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TACParser.ExprTContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = TACParser.ExprPlusContext(self, TACParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 17
                        self.match(TACParser.Plus)
                        self.state = 18
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = TACParser.ExprMinusContext(self, TACParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 20
                        self.match(TACParser.MINUS)
                        self.state = 21
                        self.term(0)
                        pass

             
                self.state = 26
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
            self.reg = str()


        def getRuleIndex(self):
            return TACParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.reg = ctx.reg


    class TermDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TACParser.TermContext,0)

        def DIVIDE(self):
            return self.getToken(TACParser.DIVIDE, 0)
        def fact(self):
            return self.getTypedRuleContext(TACParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermDiv" ):
                listener.enterTermDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermDiv" ):
                listener.exitTermDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermDiv" ):
                return visitor.visitTermDiv(self)
            else:
                return visitor.visitChildren(self)


    class TermFContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(TACParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermF" ):
                listener.enterTermF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermF" ):
                listener.exitTermF(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermF" ):
                return visitor.visitTermF(self)
            else:
                return visitor.visitChildren(self)


    class TermMulContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TACParser.TermContext,0)

        def MUL(self):
            return self.getToken(TACParser.MUL, 0)
        def fact(self):
            return self.getTypedRuleContext(TACParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermMul" ):
                listener.enterTermMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermMul" ):
                listener.exitTermMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermMul" ):
                return visitor.visitTermMul(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TACParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TACParser.TermFContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 28
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = TACParser.TermMulContext(self, TACParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        self.match(TACParser.MUL)
                        self.state = 32
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = TACParser.TermDivContext(self, TACParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.match(TACParser.DIVIDE)
                        self.state = 35
                        self.fact()
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.reg = str()


        def getRuleIndex(self):
            return TACParser.RULE_fact

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.reg = ctx.reg



    class FactNumContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(TACParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactNum" ):
                listener.enterFactNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactNum" ):
                listener.exitFactNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactNum" ):
                return visitor.visitFactNum(self)
            else:
                return visitor.visitChildren(self)


    class FactEContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TACParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactE" ):
                listener.enterFactE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactE" ):
                listener.exitFactE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactE" ):
                return visitor.visitFactE(self)
            else:
                return visitor.visitChildren(self)


    class FactIdContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Id(self):
            return self.getToken(TACParser.Id, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactId" ):
                listener.enterFactId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactId" ):
                listener.exitFactId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactId" ):
                return visitor.visitFactId(self)
            else:
                return visitor.visitChildren(self)



    def fact(self):

        localctx = TACParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = TACParser.FactIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(TACParser.Id)
                pass
            elif token in [9]:
                localctx = TACParser.FactNumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(TACParser.Number)
                pass
            elif token in [1]:
                localctx = TACParser.FactEContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(TACParser.T__0)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(TACParser.T__1)
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
         




