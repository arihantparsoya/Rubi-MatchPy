from matchpy import Constraint, substitute
from sympy import sympify

class FreeQ(Constraint):
    def __init__(self, vars, x):
        self.vars = frozenset(v.name for v in vars)
        self.x = x

    def __call__(self, substitution):
        for v in self.vars:
            if self.x in substitution[v]:
                return False
        return True

    @property
    def variables(self):
        return self.vars

    def with_renamed_vars(self, renaming):
        copy = FreeQ([], self.x)
        copy.vars = frozenset(renaming.get(v, v) for v in self.vars)
        return copy

    def __eq__(self, other):
        return isinstance(other, FreeQ) and other.vars == self.vars and other.x == self.x

    def __hash__(self):
        return hash((self.vars, self.x))

class NonzeroQ(Constraint):
    def __init__(self, expr, vars):
        self.expr = expr
        self.vars = frozenset(v.name for v in vars)

    def __call__(self, substitution):
        return sympify(str(substitute(self.expr, substitution))) != 0

    @property
    def variables(self):
        return self.vars

    def with_renamed_vars(self, renaming):
        copy = NonzeroQ(self.expr, [])
        copy.vars = frozenset(renaming.get(v, v) for v in self.vars)
        return copy

    def __eq__(self, other):
        return isinstance(other, NonzeroQ) and other.vars == self.vars and other.expr == self.expr

    def __hash__(self):
        return hash(self.vars)

