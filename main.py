import sys
from Parser import *
from PrePro import *
from Nodes import assembler


file = open(sys.argv[1], "r")
code = file.read()
code = PrePro().filter(code)
ast = Parser.run(code)
ast.evaluate()
assembler.flush()
