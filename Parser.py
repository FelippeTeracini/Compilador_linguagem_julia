from Tokenizer import *


class Parser:

    tokens = None

    @staticmethod
    def parseFactor():
        result = 0
        Parser.tokens.selectNext()
        if(Parser.tokens.actual.token_type == 'INT'):
            result = Parser.tokens.actual.token_value
            return result
        elif(Parser.tokens.actual.token_type == 'PLUS'):
            result = Parser.parseFactor()
            return result
        elif(Parser.tokens.actual.token_type == 'MINUS'):
            result = -(Parser.parseFactor())
            return result
        elif(Parser.tokens.actual.token_type == 'OPEN_P'):
            result = Parser.parseExpression()
            if(Parser.tokens.actual.token_type == 'CLOSE_P'):
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
        Parser.tokens.selectNext()
        while(Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV'):
            if Parser.tokens.actual.token_type == 'MULT':
                result *= Parser.parseFactor()
            elif Parser.tokens.actual.token_type == 'DIV':
                result = int(result/Parser.parseFactor())
            Parser.tokens.selectNext()
        return result

    @staticmethod
    def parseExpression():
        result = 0
        result = Parser.parseTerm()
        while(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS' or Parser.tokens.actual.token_type == 'CLOSE_P'):
            if Parser.tokens.actual.token_type == 'PLUS':
                result += Parser.parseTerm()
            elif Parser.tokens.actual.token_type == 'MINUS':
                result -= Parser.parseTerm()
            elif Parser.tokens.actual.token_type == 'CLOSE_P':
                return result
        if(Parser.tokens.actual.token_type == 'EOF'):
            return result
        else:
            raise ValueError('Ended Before EOF')

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        return Parser.parseExpression()
