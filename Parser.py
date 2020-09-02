from Tokenizer import *


class Parser:

    tokens = None

    @staticmethod
    def parseExpression():
        result = 0
        Parser.tokens.selectNext()
        while(Parser.tokens.actual.token_type == 'INT'):
            result = Parser.tokens.actual.token_value
            Parser.tokens.selectNext()
            while(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS'):
                if Parser.tokens.actual.token_type == 'PLUS':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.token_type == 'INT':
                        result += Parser.tokens.actual.token_value
                    else:
                        raise ValueError(
                            'A token of type INT must come after a token of type PLUS')
                elif Parser.tokens.actual.token_type == 'MINUS':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.token_type == 'INT':
                        result -= Parser.tokens.actual.token_value
                    else:
                        raise ValueError(
                            'A token of type INT must come after a token of type MINUS')
                Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'EOF'):
                return result
            else:
                raise ValueError('Ended Before EOF')
        raise ValueError('Must start with a token of type INT')

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        return Parser.parseExpression()
