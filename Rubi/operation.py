from matchpy import Operation, Arity

class Int(Operation):
    name = "Int"
    arity = Arity.variadic
    associative = False
    def __str__(self):
        return 'Int({}, {})'.format(self.operands[0], self.operands[1])

class Mul(Operation):
    name = "Mul"
    arity = Arity.variadic
    associative = True
    commutative = True
    one_identity = True

class Add(Operation):
    name = "Add"
    arity = Arity.variadic
    associative = True
    commutative = True
    one_identity = True

class Pow(Operation):
    name = "Pow"
    arity = Arity.variadic
    associative = False
    commutative = False

class Log(Operation):
    name = "log"
    arity = Arity.unary
    def __str__(self):
        return 'log({})'.format(self.operands[0])
