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
        if self.value == "+":
            return self.children[0].evaluate() + self.children[1].evaluate()

        elif self.value == "-":
            return self.children[0].evaluate() - self.children[1].evaluate()

        elif self.value == "*":
            return self.children[0].evaluate() * self.children[1].evaluate()

        elif self.value == "/":
            return int(self.children[0].evaluate() / self.children[1].evaluate())

        elif self.value == "||":
            return self.children[0].evaluate() or self.children[1].evaluate()

        elif self.value == "&&":
            return self.children[0].evaluate() and self.children[1].evaluate()

        elif self.value == "==":
            return self.children[0].evaluate() == self.children[1].evaluate()

        elif self.value == ">":
            return self.children[0].evaluate() > self.children[1].evaluate()

        elif self.value == "<":
            return self.children[0].evaluate() < self.children[1].evaluate()


class UnOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None]

    def evaluate(self):
        if self.value == "+":
            return self.children[0].evaluate()

        elif self.value == "-":
            return - self.children[0].evaluate()

        elif self.value == "!":
            return not self.children[0].evaluate()


class IntVal(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class NoOp(Node):

    def __init__(self):
        pass

    def evaluate(self):
        pass


class Assignement(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self):
        symbol_table.set_symbol(
            self.children[0].value, self.children[1].evaluate())


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
        print(self.children[0].evaluate())


class ReadLine(Node):
    def __init__(self):
        pass

    def evaluate(self):
        return int(input())


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
