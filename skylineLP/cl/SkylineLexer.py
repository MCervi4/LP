# Generated from Skyline.g by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\20")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\6\t/\n\t\r\t\16\t\60\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\7\16>\n\16\f\16")
        buf.write("\16\16A\13\16\3\17\6\17D\n\17\r\17\16\17E\3\17\3\17\2")
        buf.write("\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\")
        buf.write("c|\4\2\f\f\"\"K\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17+\3")
        buf.write("\2\2\2\21.\3\2\2\2\23\62\3\2\2\2\25\64\3\2\2\2\27\66\3")
        buf.write("\2\2\2\318\3\2\2\2\33;\3\2\2\2\35C\3\2\2\2\37 \7*\2\2")
        buf.write(" \4\3\2\2\2!\"\7+\2\2\"\6\3\2\2\2#$\7.\2\2$\b\3\2\2\2")
        buf.write("%&\7]\2\2&\n\3\2\2\2\'(\7_\2\2(\f\3\2\2\2)*\7}\2\2*\16")
        buf.write("\3\2\2\2+,\7\177\2\2,\20\3\2\2\2-/\t\2\2\2.-\3\2\2\2/")
        buf.write("\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\22\3\2\2\2\62")
        buf.write("\63\7-\2\2\63\24\3\2\2\2\64\65\7/\2\2\65\26\3\2\2\2\66")
        buf.write("\67\7,\2\2\67\30\3\2\2\289\7<\2\29:\7?\2\2:\32\3\2\2\2")
        buf.write(";?\t\3\2\2<>\t\4\2\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3")
        buf.write("\2\2\2@\34\3\2\2\2A?\3\2\2\2BD\t\5\2\2CB\3\2\2\2DE\3\2")
        buf.write("\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\17\2\2H\36\3\2")
        buf.write("\2\2\6\2\60?E\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    NUM = 8
    MES = 9
    MENYS = 10
    PER = 11
    ASIG = 12
    VAR = 13
    WS = 14

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'['", "']'", "'{'", "'}'", "'+'", "'-'", 
            "'*'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "MENYS", "PER", "ASIG", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NUM", "MES", "MENYS", "PER", "ASIG", "VAR", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


