from Tokenizer import *
from Nodes import *


class Parser:

    tokens = None

    @staticmethod
    def parseFactor():
        if(Parser.tokens.actual.token_type == 'INT'):
            result = IntVal(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            return result
        elif(Parser.tokens.actual.token_type == 'IDENTIFIER'):
            result = Identifier(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            return result
        elif(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS'):
            result = UnOp(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            result.children[0] = Parser.parseFactor()
            return result
        elif(Parser.tokens.actual.token_type == 'OPEN_P'):
            Parser.tokens.selectNext()
            result = Parser.parseExpression()
            if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                Parser.tokens.selectNext()
                return result
            else:
                raise ValueError('( must have a matching )')
        elif(Parser.tokens.actual.token_type == 'CLOSE_P'):
            raise ValueError(') can not come before a matching (')
        else:
            raise ValueError('Invalid token for FACTOR')

    @staticmethod
    def parseTerm():
        result = Parser.parseFactor()
        while(Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV'):
            if Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV':
                node = BinOp(Parser.tokens.actual.token_value)
                node.children[0] = result
                result = node
                Parser.tokens.selectNext()
                result.children[1] = Parser.parseFactor()
        return result

    @staticmethod
    def parseExpression():
        result = Parser.parseTerm()
        while(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS'):
            if Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS':
                node = BinOp(Parser.tokens.actual.token_value)
                node.children[0] = result
                result = node
                Parser.tokens.selectNext()
                result.children[1] = Parser.parseTerm()
        return result

    @staticmethod
    def parseCommand():
        node = NoOp()
        if(Parser.tokens.actual.token_type == 'IDENTIFIER'):
            identifier = Identifier(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'SET_EQUAL'):
                Parser.tokens.selectNext()
                node = Assignement()
                node.children[0] = identifier
                node.children[1] = Parser.parseExpression()
            else:
                raise ValueError(
                    "IDENTIFIER token needs SET_EQUAL token after in COMMAND")
        elif(Parser.tokens.actual.token_type == 'PRINT'):
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'OPEN_P'):
                Parser.tokens.selectNext()
                node = Print()
                node.children[0] = Parser.parseExpression()
                if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                    Parser.tokens.selectNext()
                    return node
                else:
                    raise ValueError('( must have a matching )')
            else:
                raise ValueError('PRINT token needs to be followed by (')

        if(Parser.tokens.actual.token_type == 'END_LINE'):
            Parser.tokens.selectNext()
            return node
        else:
            raise ValueError("Needs END_LINE token")

    @staticmethod
    def parseBlock():
        node = Statement()
        while(Parser.tokens.actual.token_type != 'EOF'):
            node.children.append(Parser.parseCommand())
        return node

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        result = Parser.parseBlock()
        if(Parser.tokens.actual.token_type == 'EOF'):
            return result
        else:
            raise ValueError('Ended Before EOF')
