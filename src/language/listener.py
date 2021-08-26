from FlowGrammarListener import *
from FlowGrammarParser import *
from model import *

class ConcreteListener(FlowGrammarListener):

    def __init__(self) -> None:
        super().__init__()
        self.__diagram = None
        self.__stack = []

    def get(self):
        return self.__diagram

    # Enter a parse tree produced by FlowGrammarParser#start.
    def enterStart(self, ctx:FlowGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#start.
    def exitStart(self, ctx:FlowGrammarParser.StartContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#diagramExpression.
    def enterDiagramExpression(self, ctx:FlowGrammarParser.DiagramExpressionContext):
        self.__diagram = Diagram([], None)
        self.__stack.append(self.__diagram)

    # Exit a parse tree produced by FlowGrammarParser#diagramExpression.
    def exitDiagramExpression(self, ctx:FlowGrammarParser.DiagramExpressionContext):
        self.__stack.pop()


    # Enter a parse tree produced by FlowGrammarParser#diagramBody.
    def enterDiagramBody(self, ctx:FlowGrammarParser.DiagramBodyContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#diagramBody.
    def exitDiagramBody(self, ctx:FlowGrammarParser.DiagramBodyContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#diagramElements.
    def enterDiagramElements(self, ctx:FlowGrammarParser.DiagramElementsContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#diagramElements.
    def exitDiagramElements(self, ctx:FlowGrammarParser.DiagramElementsContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#diagramElement.
    def enterDiagramElement(self, ctx:FlowGrammarParser.DiagramElementContext):
        type = ctx.elementName().elementType().getText()
        alias = ctx.elementName().elementAlias().getText()
        de = DiagramElement(type, alias, [])
        
        prev = self.__stack[-1]
        prev.elements.append(de)

        self.__stack.append(de)

    # Exit a parse tree produced by FlowGrammarParser#diagramElement.
    def exitDiagramElement(self, ctx:FlowGrammarParser.DiagramElementContext):
        self.__stack.pop()


    # Enter a parse tree produced by FlowGrammarParser#elementName.
    def enterElementName(self, ctx:FlowGrammarParser.ElementNameContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#elementName.
    def exitElementName(self, ctx:FlowGrammarParser.ElementNameContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#elementType.
    def enterElementType(self, ctx:FlowGrammarParser.ElementTypeContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#elementType.
    def exitElementType(self, ctx:FlowGrammarParser.ElementTypeContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#elementAlias.
    def enterElementAlias(self, ctx:FlowGrammarParser.ElementAliasContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#elementAlias.
    def exitElementAlias(self, ctx:FlowGrammarParser.ElementAliasContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#elementBody.
    def enterElementBody(self, ctx:FlowGrammarParser.ElementBodyContext):
        expr = ctx.bodyExpression().getText()
        prev = self.__stack[-1]
        prev.calls.append(expr)

    # Exit a parse tree produced by FlowGrammarParser#elementBody.
    def exitElementBody(self, ctx:FlowGrammarParser.ElementBodyContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#bodyExpression.
    def enterBodyExpression(self, ctx:FlowGrammarParser.BodyExpressionContext):
        pass

    # Exit a parse tree produced by FlowGrammarParser#bodyExpression.
    def exitBodyExpression(self, ctx:FlowGrammarParser.BodyExpressionContext):
        pass


    # Enter a parse tree produced by FlowGrammarParser#relationships.
    def enterRelationships(self, ctx:FlowGrammarParser.RelationshipsContext):
        r = Relations([])
        self.__stack[-1].relations = r
        self.__stack.append(r)

    # Exit a parse tree produced by FlowGrammarParser#relationships.
    def exitRelationships(self, ctx:FlowGrammarParser.RelationshipsContext):
        self.__stack.pop()


    # Enter a parse tree produced by FlowGrammarParser#relationshipsBody.
    def enterRelationshipsBody(self, ctx:FlowGrammarParser.RelationshipsBodyContext):
        aliasFrom = ctx.elementAliasFrom().getText()
        aliasTo = ctx.elementAliasTo().getText()
        t = (aliasFrom, aliasTo)
        self.__stack[-1].relations.append(t)

    # Exit a parse tree produced by FlowGrammarParser#relationshipsBody.
    def exitRelationshipsBody(self, ctx:FlowGrammarParser.RelationshipsBodyContext):
        pass