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


class UnOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None]

    def evaluate(self):
        if self.value == "+":
            return self.children[0].evaluate()

        elif self.value == "-":
            return - self.children[0].evaluate()


class IntVal(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class NoOp(Node):

    def __init__(self, value):
        self.value = value

    def evalueate(self):
        return self.value
