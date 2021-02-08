import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.SkylineVisitor import SkylineVisitor

from skyline import Skyline

#comprovarem el missatge que ens ha escrit l'usuari i l'interpretarem
def comprova_mis(s, vis):
    
    input_stream = InputStream(s)

    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root() 
    
    s = Skyline()
    
    s = vis.visit(tree)
    
    
    
    return s
    