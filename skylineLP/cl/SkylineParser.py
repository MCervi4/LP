# Generated from Skyline.g by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\20")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4 \n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\61\n\4\f\4\16\4\64")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\6\6C\n\6\r\6\16\6D\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6T\n\6\3\6\2\3\6\7\2\4\6\b\n")
        buf.write("\2\2\\\2\16\3\2\2\2\4\22\3\2\2\2\6\37\3\2\2\2\b\65\3\2")
        buf.write("\2\2\nS\3\2\2\2\f\17\5\6\4\2\r\17\5\4\3\2\16\f\3\2\2\2")
        buf.write("\16\r\3\2\2\2\17\20\3\2\2\2\20\21\7\2\2\3\21\3\3\2\2\2")
        buf.write("\22\23\7\17\2\2\23\24\7\16\2\2\24\25\5\6\4\2\25\5\3\2")
        buf.write("\2\2\26\27\b\4\1\2\27\30\7\f\2\2\30 \5\6\4\n\31\32\7\3")
        buf.write("\2\2\32\33\5\6\4\2\33\34\7\4\2\2\34 \3\2\2\2\35 \5\n\6")
        buf.write("\2\36 \7\17\2\2\37\26\3\2\2\2\37\31\3\2\2\2\37\35\3\2")
        buf.write("\2\2\37\36\3\2\2\2 \62\3\2\2\2!\"\f\t\2\2\"#\7\r\2\2#")
        buf.write("\61\5\6\4\n$%\f\7\2\2%&\7\13\2\2&\61\5\6\4\b\'(\f\b\2")
        buf.write("\2()\7\r\2\2)\61\7\n\2\2*+\f\6\2\2+,\7\13\2\2,\61\7\n")
        buf.write("\2\2-.\f\5\2\2./\7\f\2\2/\61\7\n\2\2\60!\3\2\2\2\60$\3")
        buf.write("\2\2\2\60\'\3\2\2\2\60*\3\2\2\2\60-\3\2\2\2\61\64\3\2")
        buf.write("\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\7\3\2\2\2\64\62\3")
        buf.write("\2\2\2\65\66\7\3\2\2\66\67\7\n\2\2\678\7\5\2\289\7\n\2")
        buf.write("\29:\7\5\2\2:;\7\n\2\2;<\7\4\2\2<\t\3\2\2\2=T\5\b\5\2")
        buf.write(">?\7\6\2\2?B\5\b\5\2@A\7\5\2\2AC\5\b\5\2B@\3\2\2\2CD\3")
        buf.write("\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2FG\7\7\2\2GT\3\2\2")
        buf.write("\2HI\7\b\2\2IJ\7\n\2\2JK\7\5\2\2KL\7\n\2\2LM\7\5\2\2M")
        buf.write("N\7\n\2\2NO\7\5\2\2OP\7\n\2\2PQ\7\5\2\2QR\7\n\2\2RT\7")
        buf.write("\t\2\2S=\3\2\2\2S>\3\2\2\2SH\3\2\2\2T\13\3\2\2\2\b\16")
        buf.write("\37\60\62DS")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'['", "']'", "'{'", 
                     "'}'", "<INVALID>", "'+'", "'-'", "'*'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "MES", "MENYS", "PER", "ASIG", "VAR", "WS" ]

    RULE_root = 0
    RULE_asig = 1
    RULE_expr = 2
    RULE_creacio_simple = 3
    RULE_creacio = 4

    ruleNames =  [ "root", "asig", "expr", "creacio_simple", "creacio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUM=8
    MES=9
    MENYS=10
    PER=11
    ASIG=12
    VAR=13
    WS=14

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def asig(self):
            return self.getTypedRuleContext(SkylineParser.AsigContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 10
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 11
                self.asig()
                pass


            self.state = 14
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def ASIG(self):
            return self.getToken(SkylineParser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_asig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsig" ):
                return visitor.visitAsig(self)
            else:
                return visitor.visitChildren(self)




    def asig(self):

        localctx = SkylineParser.AsigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_asig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SkylineParser.VAR)
            self.state = 17
            self.match(SkylineParser.ASIG)
            self.state = 18
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def creacio(self):
            return self.getTypedRuleContext(SkylineParser.CreacioContext,0)


        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def PER(self):
            return self.getToken(SkylineParser.PER, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 21
                self.match(SkylineParser.MENYS)
                self.state = 22
                self.expr(8)
                pass

            elif la_ == 2:
                self.state = 23
                self.match(SkylineParser.T__0)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 3:
                self.state = 27
                self.creacio()
                pass

            elif la_ == 4:
                self.state = 28
                self.match(SkylineParser.VAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 32
                        self.match(SkylineParser.PER)
                        self.state = 33
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        self.match(SkylineParser.MES)
                        self.state = 36
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        self.match(SkylineParser.PER)
                        self.state = 39
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(SkylineParser.MES)
                        self.state = 42
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        self.match(SkylineParser.MENYS)
                        self.state = 45
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Creacio_simpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_creacio_simple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreacio_simple" ):
                return visitor.visitCreacio_simple(self)
            else:
                return visitor.visitChildren(self)




    def creacio_simple(self):

        localctx = SkylineParser.Creacio_simpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_creacio_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(SkylineParser.T__0)
            self.state = 52
            self.match(SkylineParser.NUM)
            self.state = 53
            self.match(SkylineParser.T__2)
            self.state = 54
            self.match(SkylineParser.NUM)
            self.state = 55
            self.match(SkylineParser.T__2)
            self.state = 56
            self.match(SkylineParser.NUM)
            self.state = 57
            self.match(SkylineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def creacio_simple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.Creacio_simpleContext)
            else:
                return self.getTypedRuleContext(SkylineParser.Creacio_simpleContext,i)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_creacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreacio" ):
                return visitor.visitCreacio(self)
            else:
                return visitor.visitChildren(self)




    def creacio(self):

        localctx = SkylineParser.CreacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_creacio)
        self._la = 0 # Token type
        try:
            self.state = 81
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.creacio_simple()

            elif token in [SkylineParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(SkylineParser.T__3)
                self.state = 61
                self.creacio_simple()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 62
                    self.match(SkylineParser.T__2)
                    self.state = 63
                    self.creacio_simple()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SkylineParser.T__2):
                        break

                self.state = 68
                self.match(SkylineParser.T__4)

            elif token in [SkylineParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(SkylineParser.T__5)
                self.state = 71
                self.match(SkylineParser.NUM)
                self.state = 72
                self.match(SkylineParser.T__2)
                self.state = 73
                self.match(SkylineParser.NUM)
                self.state = 74
                self.match(SkylineParser.T__2)
                self.state = 75
                self.match(SkylineParser.NUM)
                self.state = 76
                self.match(SkylineParser.T__2)
                self.state = 77
                self.match(SkylineParser.NUM)
                self.state = 78
                self.match(SkylineParser.T__2)
                self.state = 79
                self.match(SkylineParser.NUM)
                self.state = 80
                self.match(SkylineParser.T__6)

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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




