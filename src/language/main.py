from antlr4 import *

from FlowGrammarLexer import *
from FlowGrammarParser import *
from listener import *
from model import *
from schemdraw import flow, Drawing

def diagramElementInfo(e: DiagramElement):
    name = list(filter(lambda x: "title." in x, e.calls))[0].split(".")[1]
    color = list(filter(lambda x: "color." in x, e.calls))[0].split(".")[1]
    return {
        "type": e.type,
        "label": name,
        "color": color
    }

def visualize(diag: Diagram):
    d = dict()
    for e in diag.elements:
        el = diagramElementInfo(e)
        d[e.alias] = {
            "flowObject": el,
            "element": e
        }
    arrows = dict()
    for _from, _to in diag.relations.relations:
        arrows[_from] = _to
    
    chart = Drawing(fontsize=11)

    for k, v in d.items():
        obj = None
        type = v["flowObject"]["type"]
        if type == "rect":
            obj = flow.Box()
        elif type == "data":
            obj = flow.Data()
        color = v["flowObject"]["color"]
        el = obj.label(v["flowObject"]["label"]).anchor("W").color(f"#{color}")
        chart += el
        if k in arrows:
            a = flow.Arrow().right().at(el.E)
            chart += a
    
    chart.draw()

if __name__ == "__main__":
    with open("demo.flow") as f:
        input = f.read() 
    lexer = FlowGrammarLexer(InputStream(input))
    parser = FlowGrammarParser(CommonTokenStream(lexer))
    # parser.setTrace(True)
    listener = ConcreteListener()
    walker = ParseTreeWalker()
    walker.walk(listener, parser.start())

    visualize(listener.get())
