from Token import *


class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = None

    def selectNext(self):
        if(self.position < len(self.origin)):
            current_token = self.origin[self.position]
            if(current_token == ' '):
                self.position += 1
                self.selectNext()
            elif(current_token in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                if(self.position + 1 < len(self.origin)):
                    while(self.origin[self.position + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                        self.position += 1
                        current_token += self.origin[self.position]
                        if(self.position + 1 >= len(self.origin)):
                            break
                self.actual = Token('INT', int(current_token))
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
