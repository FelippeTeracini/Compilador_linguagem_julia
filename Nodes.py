from SymbolTable import *
from Assembler import *

symbol_table = SymbolTable()
assembler = Assembler()


class Node():

    id = -1

    def __init__(self, value):
        self.value = value
        self.children = []
        self.id = Node.getId()

    def evaluate(self):
        pass

    @staticmethod
    def getId():
        Node.id += 1
        return Node.id


class BinOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None, None]
        self.id = Node.getId()

    def evaluate(self):

        if self.value == "+":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"ADD EAX, EBX")
            assembler.addLine(f"MOV EBX, EAX")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     return [children0[0] + children1[0], 'Int']
            # else:
            #     raise ValueError('+ Operation not valid for String')

        elif self.value == "-":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"SUB EAX, EBX")
            assembler.addLine(f"MOV EBX, EAX")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     return [children0[0] - children1[0], 'Int']
            # else:
            #     raise ValueError('- Operation not valid for String')

        elif self.value == "*":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"IMUL EBX")
            assembler.addLine(f"MOV EBX, EAX")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     return [children0[0] * children1[0], 'Int']
            # else:
            #     if(children0[1] == 'Bool'):
            #         if(children0[0] == 1):
            #             children0[0] = 'true'
            #         elif(children0[0] == 0):
            #             children0[0] = 'false'

            #     if(children1[1] == 'Bool'):
            #         if(children1[0] == 1):
            #             children1[0] = 'true'
            #         elif(children1[0] == 0):
            #             children1[0] = 'false'

            #     return [str(children0[0]) + str(children1[0]), 'String']

        elif self.value == "/":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"DIV EBX")
            assembler.addLine(f"MOV EBX, EAX")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     return [int(children0[0] / children1[0]), 'Int']
            # else:
            #     raise ValueError('/ Operation not valid for String')

        elif self.value == "||":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"OR EAX, EBX")
            assembler.addLine(f"MOV EBX, EAX")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     if(children0[0] or children1[0]):
            #         return [1, 'Bool']
            #     else:
            #         return [0, 'Bool']
            # else:
            #     raise ValueError('|| Operation not valid for String')

        elif self.value == "&&":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"AND EAX, EBX")
            assembler.addLine(f"MOV EBX, EAX")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     if(children0[0] and children1[0]):
            #         return [1, 'Bool']
            #     else:
            #         return [0, 'Bool']
            # else:
            #     raise ValueError('&& Operation not valid for String')

        elif self.value == "==":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"CMP EAX, EBX")
            assembler.addLine(f"CALL binop_je")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[0] == children1[0]):
            #     return [1, 'Bool']
            # else:
            #     return [0, 'Bool']

        elif self.value == ">":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"CMP EAX, EBX")
            assembler.addLine(f"CALL binop_jg")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     if(children0[0] > children1[0]):
            #         return [1, 'Bool']
            #     else:
            #         return [0, 'Bool']
            # else:
            #     raise ValueError('> Operation not valid for String')

        elif self.value == "<":
            self.children[0].evaluate()
            assembler.addLine(f"PUSH EBX")
            self.children[1].evaluate()
            assembler.addLine(f"POP EAX")
            assembler.addLine(f"CMP EAX, EBX")
            assembler.addLine(f"CALL binop_jl")

            # children0 = self.children[0].evaluate()
            # children1 = self.children[1].evaluate()
            # if(children0[1] != 'String' and children1[1] != 'String'):
            #     if(children0[0] < children1[0]):
            #         return [1, 'Bool']
            #     else:
            #         return [0, 'Bool']
            # else:
            #     raise ValueError('< Operation not valid for String')


class UnOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None]
        self.id = Node.getId()

    def evaluate(self):
        if self.value == "+":
            self.children[0].evaluate()
            assembler.addLine(f"MOV EBX, EAX")
        elif self.value == "-":
            self.children[0].evaluate()
            assembler.addLine(f"IMUL -1")
            assembler.addLine(f"MOV EBX, EAX")
        elif self.value == "!":
            self.children[0].evaluate()
            assembler.addLine(f"NOT EAX")
            assembler.addLine(f"MOV EBX, EAX")
        # evl = self.children[0].evaluate()
        # if self.value == "+":
        #     return [evl[0], 'Int']

        # elif self.value == "-":
        #     return [- evl[0], 'Int']

        # elif self.value == "!":
        #     if(not evl[0]):
        #         return [1, 'Bool']
        #     else:
        #         return [0, 'Bool']


class IntVal(Node):

    def __init__(self, value):
        self.value = value
        self.id = Node.getId()

    def evaluate(self):
        assembler.addLine(f"MOV EBX, {self.value}")
        # return [self.value, 'Int']


class BoolVal(Node):

    def __init__(self, value):
        self.value = value
        if(self.value != "true" and self.value != "false"):
            raise ValueError("BoolVal can only be true or false")
        self.id = Node.getId()

    def evaluate(self):
        if(self.value == 'true'):
            assembler.addLine(f"MOV EBX, True")
            # return [1, 'Bool']
        elif(self.value == 'false'):
            assembler.addLine(f"MOV EBX, False")
            # return [0, 'Bool']
            # class StringVal(Node):

            #     def __init__(self, value):
            #         self.value = value
            #         self.id = Node.getId()

            #     def evaluate(self):
            #         return [self.value, 'String']


class NoOp(Node):

    def __init__(self):
        self.id = Node.getId()

    def evaluate(self):
        assembler.addLine(f"NOP")


class Assignement(Node):
    def __init__(self):
        self.children = [None, None]
        self.id = Node.getId()

    def evaluate(self):
        self.children[1].evaluate()
        pos = symbol_table.get_pos(self.children[0].value)
        assembler.addLine(f"MOV [EBP-{pos}], EBX")
        # s_type = symbol_table.get_type(self.children[0].value)
        # evl = self.children[1].evaluate()
        # if(evl[1] == s_type):
        #     symbol_table.set_symbol(
        #         self.children[0].value, evl[0])
        # else:
        #     raise ValueError('Incompatible symbol type and value')


class TypeAssignement(Node):
    def __init__(self):
        self.children = [None, None]
        self.id = Node.getId()

    def evaluate(self):
        assembler.addLine(f"PUSH DWORD 0")
        symbol_table.set_type(
            self.children[0].value, self.children[1])


class Identifier(Node):
    def __init__(self, value):
        self.value = value
        self.id = Node.getId()

    def evaluate(self):
        pos = symbol_table.get_pos(self.value)
        assembler.addLine(f"MOV EBX, [EBP-{pos}]")
        # return symbol_table.get_symbol(self.value)


class Statement(Node):
    def __init__(self):
        self.children = []
        self.id = Node.getId()

    def evaluate(self):
        for child in self.children:
            child.evaluate()


class Print(Node):
    def __init__(self):
        self.children = [None]
        self.id = Node.getId()

    def evaluate(self):
        # evl = self.children[0].evaluate()
        self.children[0].evaluate()
        assembler.addLine(f"PUSH EBX")
        assembler.addLine(f"CALL print")
        assembler.addLine(f"POP EBX")
        # prt = evl[0]
        # if(evl[1] == 'Bool'):
        #     if(evl[0] == 1):
        #         prt = 'true'
        #     elif(evl[0] == 0):
        #         prt = 'false'

        # print(prt)


# class ReadLine(Node):
#     def __init__(self):
#         self.id = Node.getId()

#     def evaluate(self):
#         return [int(input()), 'Int']


class While(Node):
    def __init__(self):
        self.children = [None, None]
        self.id = Node.getId()

    def evaluate(self):
        assembler.addLine(f"LOOP_{self.id}:")
        self.children[0].evaluate()
        assembler.addLine(f"CMP EBX, False")
        assembler.addLine(f"JE EXIT_{self.id}")
        self.children[1].evaluate()
        assembler.addLine(f"JMP LOOP_{self.id}")
        assembler.addLine(f"EXIT_{self.id}:")
        # while(self.children[0].evaluate()[0]):
        #     self.children[1].evaluate()


class If(Node):
    def __init__(self):
        self.children = [None, None, None]
        self.id = Node.getId()

    def evaluate(self):
        self.children[0].evaluate()
        assembler.addLine(f"CMP EBX, False")
        assembler.addLine(f"JE EXIT_{self.id}")
        self.children[1].evaluate()
        assembler.addLine(f"EXIT_{self.id}:")
        if(self.children[2]):
            self.children[2].evaluate()
        # if(self.children[0].evaluate()[0]):
        #     self.children[1].evaluate()
        # else:
        #     if(self.children[2]):
        #         self.children[2].evaluate()


class Else(Node):
    def __init__(self):
        self.children = [None]
        self.id = Node.getId()

    def evaluate(self):
        self.children[0].evaluate()
        # return self.children[0].evaluate()
