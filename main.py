from Parser import *

testes = ['1+2', '3-2', '1+2-3', '11+22-33', '789    +345   -    123']
for i in testes:
    print(Parser.run(i))
