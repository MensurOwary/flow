from antlr4 import *

from FlowGrammarLexer import *
from FlowGrammarParser import *
from listener import *

input = """diagram
rect a
    title.Candidate
end

rect b
    a.b
end

rect c
    c.d
end

relations
    a->b
    d->c
    x->a
    y->a
end

end
"""
lexer = FlowGrammarLexer(InputStream(input))
parser = FlowGrammarParser(CommonTokenStream(lexer))
# parser.setTrace(True)
listener = ConcreteListener()
walker = ParseTreeWalker()
walker.walk(listener, parser.start())

import json
print(json.dumps(listener.get(), default=lambda x: x.__dict__, indent=4))
