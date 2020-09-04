from Tokenizer import *


class Parser:

    tokens = None

    @staticmethod
    def parseTerm():
        result = 0
        Parser.tokens.selectNext()
        while(Parser.tokens.actual.token_type == 'INT'):
            result = Parser.tokens.actual.token_value
            Parser.tokens.selectNext()
            while(Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV'):
                if Parser.tokens.actual.token_type == 'MULT':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.token_type == 'INT':
                        result *= Parser.tokens.actual.token_value
                    else:
                        raise ValueError(
                            'A token of type INT must come after a token of type MULT')
                elif Parser.tokens.actual.token_type == 'DIV':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.token_type == 'INT':
                        result = int(result / Parser.tokens.actual.token_value)
                    else:
                        raise ValueError(
                            'A token of type INT must come after a token of type DIV')
                Parser.tokens.selectNext()
            return result
        raise ValueError('Term must start with a token of type INT')

    @staticmethod
    def parseExpression():
        result = 0
        result = Parser.parseTerm()
        while(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS'):
            if Parser.tokens.actual.token_type == 'PLUS':
                result += Parser.parseTerm()
            elif Parser.tokens.actual.token_type == 'MINUS':
                result -= Parser.parseTerm()
        if(Parser.tokens.actual.token_type == 'EOF'):
            return result
        else:
            raise ValueError('Ended Before EOF')

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        return Parser.parseExpression()
