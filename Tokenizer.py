from Token import *


class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = -1
        self.actual = None

    def selectNext(self):
        self.position += 1
        if(self.position < len(self.origin)):
            token_current_value = self.origin[self.position]
            # Skipping spaces
            while(token_current_value == ' '):
                self.position += 1
                if(self.position < len(self.origin)):
                    token_current_value = self.origin[self.position]
                else:
                    token_current_value = ''
            # Check if number token
            if(token_current_value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                token_value = token_current_value
                # Create integer out of tokens
                if(self.position + 1 < len(self.origin)):
                    while(self.origin[self.position + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                        self.position += 1
                        if(self.position < len(self.origin)):
                            token_current_value = self.origin[self.position]
                            token_value += token_current_value
                        else:
                            token_current_value = ''
                        if(self.position + 1 >= len(self.origin)):
                            break

                token_value = int(token_value)
                token_type = 'INT'
            # Check if plus token
            elif(token_current_value == '+'):
                token_value = token_current_value
                token_type = 'PLUS'
            # Check if minus token
            elif(token_current_value == '-'):
                token_value = token_current_value
                token_type = 'MINUS'
            elif(token_current_value == ''):
                token_value = ''
                token_type = 'EOF'
            # Invalid Token
            else:
                raise ValueError('Invalid Token')
        # Create EOF token
        else:
            token_value = ''
            token_type = 'EOF'
        self.actual = Token(token_type, token_value)
