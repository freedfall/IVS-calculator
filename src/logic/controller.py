import eel
from expression_parser import Analyser

analyser =  Analyser()

@eel.expose
def calculate(expr):
    result = analyser.analyse(expr)
    analyser.reinitialize_stack()
    return result