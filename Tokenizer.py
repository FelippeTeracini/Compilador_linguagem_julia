from Token import *


class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = None
        self.selectNext()

    def selectNext(self):
        if(self.position < len(self.origin)):
            current_token = self.origin[self.position]
            if(current_token == ' '):
                self.position += 1
                self.selectNext()
            elif(current_token.isnumeric()):
                if(self.position + 1 < len(self.origin)):
                    while(self.origin[self.position + 1].isnumeric()):
                        self.position += 1
                        current_token += self.origin[self.position]
                        if(self.position + 1 >= len(self.origin)):
                            break
                self.actual = Token('INT', int(current_token))
                self.position += 1
            elif(current_token.isalpha()):
                if(self.position + 1 < len(self.origin)):
                    while(self.origin[self.position + 1].isalpha() or self.origin[self.position + 1].isnumeric() or self.origin[self.position + 1] == "_"):
                        self.position += 1
                        current_token += self.origin[self.position]
                        if(self.position + 1 >= len(self.origin)):
                            break
                if(current_token == "println"):
                    self.actual = Token('PRINT', current_token)
                else:
                    self.actual = Token('IDENTIFIER', current_token)
                self.position += 1
            elif(current_token == "\n"):
                self.actual = Token("END_LINE", '')
                self.position += 1
            elif(current_token == "="):
                self.actual = Token('SET_EQUAL', current_token)
                self.position += 1
            elif(current_token == '-'):
                self.actual = Token('MINUS', current_token)
                self.position += 1
            elif(current_token == '+'):
                self.actual = Token('PLUS', current_token)
                self.position += 1
            elif(current_token == '*'):
                self.actual = Token('MULT', current_token)
                self.position += 1
            elif(current_token == '/'):
                self.actual = Token('DIV', current_token)
                self.position += 1
            elif(current_token == '('):
                self.actual = Token('OPEN_P', current_token)
                self.position += 1
            elif(current_token == ')'):
                self.actual = Token('CLOSE_P', current_token)
                self.position += 1
            elif(current_token == ''):
                self.actual = Token('EOF', current_token)
                self.position += 1
            else:
                raise ValueError('Invalid Token')
        else:
            self.actual = Token('EOF', '')
