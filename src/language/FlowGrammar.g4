grammar FlowGrammar;

start: diagramExpression;

// lexer stuff
DIAGRAM:'diagram';
END: 'end';
RELATIONS: 'relations';
FOLLOWS: '->';
Alphabet: [a-zA-Z]+;
STRING_LIT: '"' ('\\'[bfrnt\\"]|~[\r\t\n\\"])* '"';
STRING_LIT_NO_QUOTES: [a-zA-Z\\.0-9]+;
// parser stuff
diagramExpression: DIAGRAM diagramBody END;

diagramBody
    : diagramElements relationships; 

diagramElements
    : diagramElement diagramElements?;

diagramElement:
    elementName elementBody END;

elementName: elementType elementAlias;

elementType: Alphabet;

elementAlias: Alphabet;

elementBody
    : bodyExpression elementBody?;

bodyExpression
    : STRING_LIT_NO_QUOTES;

relationships
    : RELATIONS relationshipsBody+ END;

relationshipsBody
    : elementAliasFrom FOLLOWS elementAliasTo;

elementAliasFrom
    : elementAlias;

elementAliasTo
    : elementAlias;

WS : [ \n\t]+ -> skip;