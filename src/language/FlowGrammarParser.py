# Generated from FlowGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("M\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5")
        buf.write("\3\5\5\5*\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\5\n9\n\n\3\13\3\13\3\f\3\f\6\f?\n\f\r\f\16")
        buf.write("\f@\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\2")
        buf.write("\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2A\2\36")
        buf.write("\3\2\2\2\4 \3\2\2\2\6$\3\2\2\2\b\'\3\2\2\2\n+\3\2\2\2")
        buf.write("\f/\3\2\2\2\16\62\3\2\2\2\20\64\3\2\2\2\22\66\3\2\2\2")
        buf.write("\24:\3\2\2\2\26<\3\2\2\2\30D\3\2\2\2\32H\3\2\2\2\34J\3")
        buf.write("\2\2\2\36\37\5\4\3\2\37\3\3\2\2\2 !\7\3\2\2!\"\5\6\4\2")
        buf.write("\"#\7\4\2\2#\5\3\2\2\2$%\5\b\5\2%&\5\26\f\2&\7\3\2\2\2")
        buf.write("\')\5\n\6\2(*\5\b\5\2)(\3\2\2\2)*\3\2\2\2*\t\3\2\2\2+")
        buf.write(",\5\f\7\2,-\5\22\n\2-.\7\4\2\2.\13\3\2\2\2/\60\5\16\b")
        buf.write("\2\60\61\5\20\t\2\61\r\3\2\2\2\62\63\7\7\2\2\63\17\3\2")
        buf.write("\2\2\64\65\7\7\2\2\65\21\3\2\2\2\668\5\24\13\2\679\5\22")
        buf.write("\n\28\67\3\2\2\289\3\2\2\29\23\3\2\2\2:;\7\t\2\2;\25\3")
        buf.write("\2\2\2<>\7\5\2\2=?\5\30\r\2>=\3\2\2\2?@\3\2\2\2@>\3\2")
        buf.write("\2\2@A\3\2\2\2AB\3\2\2\2BC\7\4\2\2C\27\3\2\2\2DE\5\32")
        buf.write("\16\2EF\7\6\2\2FG\5\34\17\2G\31\3\2\2\2HI\5\20\t\2I\33")
        buf.write("\3\2\2\2JK\5\20\t\2K\35\3\2\2\2\5)8@")
        return buf.getvalue()


class FlowGrammarParser ( Parser ):

    grammarFileName = "FlowGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'diagram'", "'end'", "'relations'", "'->'" ]

    symbolicNames = [ "<INVALID>", "DIAGRAM", "END", "RELATIONS", "FOLLOWS", 
                      "Alphabet", "STRING_LIT", "STRING_LIT_NO_QUOTES", 
                      "WS" ]

    RULE_start = 0
    RULE_diagramExpression = 1
    RULE_diagramBody = 2
    RULE_diagramElements = 3
    RULE_diagramElement = 4
    RULE_elementName = 5
    RULE_elementType = 6
    RULE_elementAlias = 7
    RULE_elementBody = 8
    RULE_bodyExpression = 9
    RULE_relationships = 10
    RULE_relationshipsBody = 11
    RULE_elementAliasFrom = 12
    RULE_elementAliasTo = 13

    ruleNames =  [ "start", "diagramExpression", "diagramBody", "diagramElements", 
                   "diagramElement", "elementName", "elementType", "elementAlias", 
                   "elementBody", "bodyExpression", "relationships", "relationshipsBody", 
                   "elementAliasFrom", "elementAliasTo" ]

    EOF = Token.EOF
    DIAGRAM=1
    END=2
    RELATIONS=3
    FOLLOWS=4
    Alphabet=5
    STRING_LIT=6
    STRING_LIT_NO_QUOTES=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def diagramExpression(self):
            return self.getTypedRuleContext(FlowGrammarParser.DiagramExpressionContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = FlowGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.diagramExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagramExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIAGRAM(self):
            return self.getToken(FlowGrammarParser.DIAGRAM, 0)

        def diagramBody(self):
            return self.getTypedRuleContext(FlowGrammarParser.DiagramBodyContext,0)


        def END(self):
            return self.getToken(FlowGrammarParser.END, 0)

        def getRuleIndex(self):
            return FlowGrammarParser.RULE_diagramExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagramExpression" ):
                listener.enterDiagramExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagramExpression" ):
                listener.exitDiagramExpression(self)




    def diagramExpression(self):

        localctx = FlowGrammarParser.DiagramExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_diagramExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(FlowGrammarParser.DIAGRAM)
            self.state = 31
            self.diagramBody()
            self.state = 32
            self.match(FlowGrammarParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagramBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def diagramElements(self):
            return self.getTypedRuleContext(FlowGrammarParser.DiagramElementsContext,0)


        def relationships(self):
            return self.getTypedRuleContext(FlowGrammarParser.RelationshipsContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_diagramBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagramBody" ):
                listener.enterDiagramBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagramBody" ):
                listener.exitDiagramBody(self)




    def diagramBody(self):

        localctx = FlowGrammarParser.DiagramBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_diagramBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.diagramElements()
            self.state = 35
            self.relationships()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagramElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def diagramElement(self):
            return self.getTypedRuleContext(FlowGrammarParser.DiagramElementContext,0)


        def diagramElements(self):
            return self.getTypedRuleContext(FlowGrammarParser.DiagramElementsContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_diagramElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagramElements" ):
                listener.enterDiagramElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagramElements" ):
                listener.exitDiagramElements(self)




    def diagramElements(self):

        localctx = FlowGrammarParser.DiagramElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_diagramElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.diagramElement()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FlowGrammarParser.Alphabet:
                self.state = 38
                self.diagramElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagramElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementName(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementNameContext,0)


        def elementBody(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementBodyContext,0)


        def END(self):
            return self.getToken(FlowGrammarParser.END, 0)

        def getRuleIndex(self):
            return FlowGrammarParser.RULE_diagramElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagramElement" ):
                listener.enterDiagramElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagramElement" ):
                listener.exitDiagramElement(self)




    def diagramElement(self):

        localctx = FlowGrammarParser.DiagramElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_diagramElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.elementName()
            self.state = 42
            self.elementBody()
            self.state = 43
            self.match(FlowGrammarParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementType(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementTypeContext,0)


        def elementAlias(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementAliasContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_elementName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementName" ):
                listener.enterElementName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementName" ):
                listener.exitElementName(self)




    def elementName(self):

        localctx = FlowGrammarParser.ElementNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elementName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.elementType()
            self.state = 46
            self.elementAlias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Alphabet(self):
            return self.getToken(FlowGrammarParser.Alphabet, 0)

        def getRuleIndex(self):
            return FlowGrammarParser.RULE_elementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementType" ):
                listener.enterElementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementType" ):
                listener.exitElementType(self)




    def elementType(self):

        localctx = FlowGrammarParser.ElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elementType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(FlowGrammarParser.Alphabet)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Alphabet(self):
            return self.getToken(FlowGrammarParser.Alphabet, 0)

        def getRuleIndex(self):
            return FlowGrammarParser.RULE_elementAlias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAlias" ):
                listener.enterElementAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAlias" ):
                listener.exitElementAlias(self)




    def elementAlias(self):

        localctx = FlowGrammarParser.ElementAliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elementAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(FlowGrammarParser.Alphabet)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodyExpression(self):
            return self.getTypedRuleContext(FlowGrammarParser.BodyExpressionContext,0)


        def elementBody(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementBodyContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_elementBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementBody" ):
                listener.enterElementBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementBody" ):
                listener.exitElementBody(self)




    def elementBody(self):

        localctx = FlowGrammarParser.ElementBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elementBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.bodyExpression()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FlowGrammarParser.STRING_LIT_NO_QUOTES:
                self.state = 53
                self.elementBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT_NO_QUOTES(self):
            return self.getToken(FlowGrammarParser.STRING_LIT_NO_QUOTES, 0)

        def getRuleIndex(self):
            return FlowGrammarParser.RULE_bodyExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyExpression" ):
                listener.enterBodyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyExpression" ):
                listener.exitBodyExpression(self)




    def bodyExpression(self):

        localctx = FlowGrammarParser.BodyExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bodyExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(FlowGrammarParser.STRING_LIT_NO_QUOTES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationshipsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RELATIONS(self):
            return self.getToken(FlowGrammarParser.RELATIONS, 0)

        def END(self):
            return self.getToken(FlowGrammarParser.END, 0)

        def relationshipsBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowGrammarParser.RelationshipsBodyContext)
            else:
                return self.getTypedRuleContext(FlowGrammarParser.RelationshipsBodyContext,i)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_relationships

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationships" ):
                listener.enterRelationships(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationships" ):
                listener.exitRelationships(self)




    def relationships(self):

        localctx = FlowGrammarParser.RelationshipsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relationships)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(FlowGrammarParser.RELATIONS)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.relationshipsBody()
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FlowGrammarParser.Alphabet):
                    break

            self.state = 64
            self.match(FlowGrammarParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationshipsBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementAliasFrom(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementAliasFromContext,0)


        def FOLLOWS(self):
            return self.getToken(FlowGrammarParser.FOLLOWS, 0)

        def elementAliasTo(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementAliasToContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_relationshipsBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationshipsBody" ):
                listener.enterRelationshipsBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationshipsBody" ):
                listener.exitRelationshipsBody(self)




    def relationshipsBody(self):

        localctx = FlowGrammarParser.RelationshipsBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relationshipsBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.elementAliasFrom()
            self.state = 67
            self.match(FlowGrammarParser.FOLLOWS)
            self.state = 68
            self.elementAliasTo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAliasFromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementAlias(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementAliasContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_elementAliasFrom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAliasFrom" ):
                listener.enterElementAliasFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAliasFrom" ):
                listener.exitElementAliasFrom(self)




    def elementAliasFrom(self):

        localctx = FlowGrammarParser.ElementAliasFromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elementAliasFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.elementAlias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAliasToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementAlias(self):
            return self.getTypedRuleContext(FlowGrammarParser.ElementAliasContext,0)


        def getRuleIndex(self):
            return FlowGrammarParser.RULE_elementAliasTo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAliasTo" ):
                listener.enterElementAliasTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAliasTo" ):
                listener.exitElementAliasTo(self)




    def elementAliasTo(self):

        localctx = FlowGrammarParser.ElementAliasToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elementAliasTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.elementAlias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





