class SymbolTable:

    def __init__(self):
        self.symbol_table = {}

    def set_symbol(self, symbol, symbol_value):
        if symbol in self.symbol_table.keys():
            self.symbol_table[symbol][0] = symbol_value
        else:
            raise ValueError(f'Symbol {symbol} not defined')

    def get_symbol(self, symbol):
        if symbol in self.symbol_table.keys():
            if(self.symbol_table[symbol][0] is not None):
                return self.symbol_table[symbol]
            else:
                raise ValueError(f'Symbol {symbol} has no value')
        else:
            raise ValueError(f'Symbol {symbol} not in symbol table')

    def set_type(self, symbol, symbol_type):
        self.symbol_table[symbol] = [None, symbol_type]

    def get_type(self, symbol):
        if symbol in self.symbol_table.keys():
            return self.symbol_table[symbol][1]
        else:
            raise ValueError(f'Symbol {symbol} not in symbol table')
