from SymbolTable import *

symbol_table = SymbolTable()


class Node():

    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self):
        pass


class BinOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None, None]

    def evaluate(self):
        children0 = self.children[0].evaluate()
        children1 = self.children[1].evaluate()

        if self.value == "+":
            return [children0[0] + children1[0], 'Int']

        elif self.value == "-":
            return [children0[0] - children1[0], 'Int']

        elif self.value == "*":
            return [children0[0] * children1[0], 'Int']

        elif self.value == "/":
            return [int(children0[0] / children1[0]), 'Int']

        elif self.value == "||":
            if(children0[0] or children1[0]):
                return [1, 'Bool']
            else:
                return [0, 'Bool']

        elif self.value == "&&":
            if(children0[0] and children1[0]):
                return [1, 'Bool']
            else:
                return [0, 'Bool']

        elif self.value == "==":
            if(children0[0] == children1[0]):
                return [1, 'Bool']
            else:
                return [0, 'Bool']

        elif self.value == ">":
            if(children0[0] > children1[0]):
                return [1, 'Bool']
            else:
                return [0, 'Bool']

        elif self.value == "<":
            if(children0[0] < children1[0]):
                return [1, 'Bool']
            else:
                return [0, 'Bool']


class UnOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None]

    def evaluate(self):
        evl = self.children[0].evaluate()
        if self.value == "+":
            return [evl[0], 'Int']

        elif self.value == "-":
            return [- evl[0], 'Int']

        elif self.value == "!":
            if(not evl[0]):
                return [1, 'Bool']
            else:
                return [0, 'Bool']


class IntVal(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return [self.value, 'Int']


class BoolVal(Node):

    def __init__(self, value):
        self.value = value
        if(self.value != "true" and self.value != "false"):
            raise ValueError("BoolVal can only be true or false")

    def evaluate(self):
        if(self.value == 'true'):
            return [1, 'Bool']
        elif(self.value == 'false'):
            return [0, 'Bool']


class NoOp(Node):

    def __init__(self):
        pass

    def evaluate(self):
        pass


class Assignement(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self):
        s_type = symbol_table.get_type(self.children[0].value)
        evl = self.children[1].evaluate()
        if(evl[1] == s_type):
            symbol_table.set_symbol(
                self.children[0].value, evl[0])
        else:
            raise ValueError('Incompatible symbol type and value')


class TypeAssignement(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self):
        symbol_table.set_type(
            self.children[0].value, self.children[1])


class Identifier(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return symbol_table.get_symbol(self.value)


class Statement(Node):
    def __init__(self):
        self.children = []

    def evaluate(self):
        for child in self.children:
            child.evaluate()


class Print(Node):
    def __init__(self):
        self.children = [None]

    def evaluate(self):
        evl = self.children[0].evaluate()
        prt = evl[0]
        if(evl[1] == 'Bool'):
            if(evl[0] == 1):
                prt = 'true'
            elif(evl[0] == 0):
                prt = 'false'

        print(prt)


class ReadLine(Node):
    def __init__(self):
        pass

    def evaluate(self):
        return [int(input()), 'Int']


class While(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self):
        while(self.children[0].evaluate()):
            self.children[1].evaluate()


class If(Node):
    def __init__(self):
        self.children = [None, None, None]

    def evaluate(self):
        if(self.children[0].evaluate()):
            self.children[1].evaluate()
        else:
            if(self.children[2]):
                self.children[2].evaluate()


class Else(Node):
    def __init__(self):
        self.children = [None]

    def evaluate(self):
        return self.children[0].evaluate()
