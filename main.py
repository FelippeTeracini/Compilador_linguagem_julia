import sys
from Parser import *
from PrePro import *

code = sys.argv[1]
code = PrePro().filter(code)
print(Parser.run(code))
