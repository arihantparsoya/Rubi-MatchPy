from matchpy import Symbol

class VariableSymbol(Symbol):
    pass

class ConstantSymbol(Symbol):
    def __init__(self, value):
        super().__init__(str(value))
        self.value = value

