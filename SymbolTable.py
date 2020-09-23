class SymbolTable:

    def __init__(self):
        self.symbol_table = {}

    def set_symbol(self, symbol, value):
        self.symbol_table[symbol] = value

    def get_symbol(self, symbol):
        if symbol in self.symbol_table.keys():
            return self.symbol_table[symbol]
        else:
            raise ValueError('Symbol not in symbol table')
