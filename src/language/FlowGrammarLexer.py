# Generated from FlowGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\6\6.\n\6\r\6\16\6/\3\7\3\7\3\7\3\7\7\7\66")
        buf.write("\n\7\f\7\16\79\13\7\3\7\3\7\3\b\6\b>\n\b\r\b\16\b?\3\t")
        buf.write("\6\tC\n\t\r\t\16\tD\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\3\2\7\4\2C\\c|\t\2$$^^ddhhppttvv\6\2\13")
        buf.write("\f\17\17$$^^\7\2\60\60\62;C\\^^c|\4\2\13\f\"\"\2L\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2")
        buf.write("\2\5\33\3\2\2\2\7\37\3\2\2\2\t)\3\2\2\2\13-\3\2\2\2\r")
        buf.write("\61\3\2\2\2\17=\3\2\2\2\21B\3\2\2\2\23\24\7f\2\2\24\25")
        buf.write("\7k\2\2\25\26\7c\2\2\26\27\7i\2\2\27\30\7t\2\2\30\31\7")
        buf.write("c\2\2\31\32\7o\2\2\32\4\3\2\2\2\33\34\7g\2\2\34\35\7p")
        buf.write("\2\2\35\36\7f\2\2\36\6\3\2\2\2\37 \7t\2\2 !\7g\2\2!\"")
        buf.write("\7n\2\2\"#\7c\2\2#$\7v\2\2$%\7k\2\2%&\7q\2\2&\'\7p\2\2")
        buf.write("\'(\7u\2\2(\b\3\2\2\2)*\7/\2\2*+\7@\2\2+\n\3\2\2\2,.\t")
        buf.write("\2\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\f")
        buf.write("\3\2\2\2\61\67\7$\2\2\62\63\7^\2\2\63\66\t\3\2\2\64\66")
        buf.write("\n\4\2\2\65\62\3\2\2\2\65\64\3\2\2\2\669\3\2\2\2\67\65")
        buf.write("\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7$\2\2;\16")
        buf.write("\3\2\2\2<>\t\5\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2")
        buf.write("\2\2@\20\3\2\2\2AC\t\6\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2")
        buf.write("\2DE\3\2\2\2EF\3\2\2\2FG\b\t\2\2G\22\3\2\2\2\b\2/\65\67")
        buf.write("?D\3\b\2\2")
        return buf.getvalue()


class FlowGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DIAGRAM = 1
    END = 2
    RELATIONS = 3
    FOLLOWS = 4
    Alphabet = 5
    STRING_LIT = 6
    STRING_LIT_NO_QUOTES = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'diagram'", "'end'", "'relations'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "DIAGRAM", "END", "RELATIONS", "FOLLOWS", "Alphabet", "STRING_LIT", 
            "STRING_LIT_NO_QUOTES", "WS" ]

    ruleNames = [ "DIAGRAM", "END", "RELATIONS", "FOLLOWS", "Alphabet", 
                  "STRING_LIT", "STRING_LIT_NO_QUOTES", "WS" ]

    grammarFileName = "FlowGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


