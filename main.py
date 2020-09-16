import sys
from Parser import *
from PrePro import *


file = open(sys.argv[1], "r")
code = file.read()
code = PrePro().filter(code)
ast = Parser.run(code)
print(ast.evaluate())
