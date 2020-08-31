import sys
from Parser import *

code = ""
for i in range(1, len(sys.argv)):
    code += sys.argv[i]
code = code.replace("'", "")
print(Parser.run(code))
