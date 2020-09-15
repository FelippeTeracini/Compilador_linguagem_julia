from Tokenizer import *


class Parser:

    tokens = None

    @staticmethod
    def parseFactor():
        result = 0
        if(Parser.tokens.actual.token_type == 'INT'):
            result = Parser.tokens.actual.token_value
            Parser.tokens.selectNext()
            return result
        elif(Parser.tokens.actual.token_type == 'PLUS'):
            Parser.tokens.selectNext()
            result = Parser.parseFactor()
            return result
        elif(Parser.tokens.actual.token_type == 'MINUS'):
            Parser.tokens.selectNext()
            result = -(Parser.parseFactor())
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
        result = 0
        result = Parser.parseFactor()
        while(Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV'):
            if Parser.tokens.actual.token_type == 'MULT':
                Parser.tokens.selectNext()
                result *= Parser.parseFactor()
            elif Parser.tokens.actual.token_type == 'DIV':
                Parser.tokens.selectNext()
                result = int(result/Parser.parseFactor())
        return result

    @staticmethod
    def parseExpression():
        result = 0
        result = Parser.parseTerm()
        while(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS'):
            if Parser.tokens.actual.token_type == 'PLUS':
                Parser.tokens.selectNext()
                result += Parser.parseTerm()
            elif Parser.tokens.actual.token_type == 'MINUS':
                Parser.tokens.selectNext()
                result -= Parser.parseTerm()
        return result

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        result = Parser.parseExpression()
        if(Parser.tokens.actual.token_type == 'EOF'):
            return result
        else:
            raise ValueError('Ended Before EOF')
