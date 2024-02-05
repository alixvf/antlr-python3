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
        4,1,17,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,29,8,1,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,3,1,3,1,3,5,
        3,42,8,3,10,3,12,3,45,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,54,8,4,
        1,4,0,0,5,0,2,4,6,8,0,3,1,0,1,2,1,0,8,9,1,0,10,11,57,0,11,1,0,0,
        0,2,28,1,0,0,0,4,30,1,0,0,0,6,38,1,0,0,0,8,53,1,0,0,0,10,12,3,2,
        1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,
        1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,7,0,0,0,18,19,5,12,0,0,
        19,20,5,3,0,0,20,21,5,14,0,0,21,29,5,4,0,0,22,23,5,5,0,0,23,24,5,
        6,0,0,24,25,3,4,2,0,25,26,5,7,0,0,26,27,5,4,0,0,27,29,1,0,0,0,28,
        17,1,0,0,0,28,22,1,0,0,0,29,3,1,0,0,0,30,35,3,6,3,0,31,32,7,1,0,
        0,32,34,3,6,3,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,5,1,0,0,0,37,35,1,0,0,0,38,43,3,8,4,0,39,40,7,2,0,0,40,
        42,3,8,4,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,
        0,44,7,1,0,0,0,45,43,1,0,0,0,46,54,1,0,0,0,47,48,5,6,0,0,48,49,3,
        4,2,0,49,50,5,7,0,0,50,54,1,0,0,0,51,54,5,14,0,0,52,54,5,12,0,0,
        53,46,1,0,0,0,53,47,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,9,1,0,
        0,0,5,13,28,35,43,53
    ]

class SimpleVariableParser ( Parser ):

    grammarFileName = "SimpleVariable.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'='", "';'", "'print'", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "IdentifierNondigit", "NUMBER", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_stmt = 1
    RULE_arithmeticExpr = 2
    RULE_arithmeticTerm = 3
    RULE_arithmeticFactor = 4

    ruleNames =  [ "start", "stmt", "arithmeticExpr", "arithmeticTerm", 
                   "arithmeticFactor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    IDENTIFIER=12
    IdentifierNondigit=13
    NUMBER=14
    WS=15
    COMMENT=16
    LINE_COMMENT=17

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

        def EOF(self):
            return self.getToken(SimpleVariableParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleVariableParser.StmtContext)
            else:
                return self.getTypedRuleContext(SimpleVariableParser.StmtContext,i)


        def getRuleIndex(self):
            return SimpleVariableParser.RULE_start

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

        localctx = SimpleVariableParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stmt()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0)):
                    break

            self.state = 15
            self.match(SimpleVariableParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleVariableParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleVariableParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticExpr(self):
            return self.getTypedRuleContext(SimpleVariableParser.ArithmeticExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleVariableParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(SimpleVariableParser.IDENTIFIER, 0)
        def NUMBER(self):
            return self.getToken(SimpleVariableParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = SimpleVariableParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                localctx = SimpleVariableParser.VarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 18
                self.match(SimpleVariableParser.IDENTIFIER)
                self.state = 19
                self.match(SimpleVariableParser.T__2)
                self.state = 20
                self.match(SimpleVariableParser.NUMBER)
                self.state = 21
                self.match(SimpleVariableParser.T__3)
                pass
            elif token in [5]:
                localctx = SimpleVariableParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(SimpleVariableParser.T__4)
                self.state = 23
                self.match(SimpleVariableParser.T__5)
                self.state = 24
                self.arithmeticExpr()
                self.state = 25
                self.match(SimpleVariableParser.T__6)
                self.state = 26
                self.match(SimpleVariableParser.T__3)
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


    class ArithmeticExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleVariableParser.RULE_arithmeticExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArithmeticExpr_Context(ArithmeticExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleVariableParser.ArithmeticExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleVariableParser.ArithmeticTermContext)
            else:
                return self.getTypedRuleContext(SimpleVariableParser.ArithmeticTermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr_" ):
                listener.enterArithmeticExpr_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr_" ):
                listener.exitArithmeticExpr_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr_" ):
                return visitor.visitArithmeticExpr_(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticExpr(self):

        localctx = SimpleVariableParser.ArithmeticExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arithmeticExpr)
        self._la = 0 # Token type
        try:
            localctx = SimpleVariableParser.ArithmeticExpr_Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.arithmeticTerm()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 31
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 32
                self.arithmeticTerm()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleVariableParser.RULE_arithmeticTerm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArithmeticTerm_Context(ArithmeticTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleVariableParser.ArithmeticTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleVariableParser.ArithmeticFactorContext)
            else:
                return self.getTypedRuleContext(SimpleVariableParser.ArithmeticFactorContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticTerm_" ):
                listener.enterArithmeticTerm_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticTerm_" ):
                listener.exitArithmeticTerm_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticTerm_" ):
                return visitor.visitArithmeticTerm_(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticTerm(self):

        localctx = SimpleVariableParser.ArithmeticTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmeticTerm)
        self._la = 0 # Token type
        try:
            localctx = SimpleVariableParser.ArithmeticTerm_Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.arithmeticFactor()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 39
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.arithmeticFactor()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpr(self):
            return self.getTypedRuleContext(SimpleVariableParser.ArithmeticExprContext,0)


        def NUMBER(self):
            return self.getToken(SimpleVariableParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(SimpleVariableParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SimpleVariableParser.RULE_arithmeticFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticFactor" ):
                listener.enterArithmeticFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticFactor" ):
                listener.exitArithmeticFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticFactor" ):
                return visitor.visitArithmeticFactor(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticFactor(self):

        localctx = SimpleVariableParser.ArithmeticFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arithmeticFactor)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(SimpleVariableParser.T__5)
                self.state = 48
                self.arithmeticExpr()
                self.state = 49
                self.match(SimpleVariableParser.T__6)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(SimpleVariableParser.NUMBER)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.match(SimpleVariableParser.IDENTIFIER)
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





