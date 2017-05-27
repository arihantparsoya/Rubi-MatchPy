from matchpy import Wildcard, Pattern, ReplacementRule, is_match, replace_all, ManyToOneReplacer

from operation import Int, Mul, Add, Pow, Log
from symbol import VariableSymbol, ConstantSymbol
from constraint import FreeQ, NonzeroQ


a, b, c, d, e, f, g, h, x = map(VariableSymbol, 'abcdefghx')
n, m = map(VariableSymbol, 'nm')
a_, b_, c_, d_, e_, f_, g_, h_ = map(Wildcard.dot, 'abcdefgh')
n_, m_ = map(Wildcard.dot, 'nm')

x_ = Wildcard.symbol('x')
u_ = Wildcard.symbol('u')

one = ConstantSymbol(1)
m_one = ConstantSymbol(-1)

pattern1 = Pattern(Int(Mul(a_, Pow(x_, -1)), x), FreeQ((a,), x))
rule1 = ReplacementRule(pattern1, lambda a, x: Mul(a, Log(x)))

pattern2 = Pattern(Int(Pow(x_, m_), x), FreeQ((m,), x), NonzeroQ(Add(m_, one), (m,)))
rule2 = ReplacementRule(pattern2, lambda m, x: Mul(Pow(x, Add(m, one)), Pow(Add(m, one), m_one)))

rubi = ManyToOneReplacer(rule1)
rubi.add(*rule2)

test = [
    [Int(Pow(x, one), x), Mul(Pow(Add(one, one), m_one), Pow(x, Add(one, one)))],
    [Int(Mul(a, Pow(x, -1)), x), Mul(Log(x), a)]
]

for i in test:
    assert rubi.replace(i[0]) == i[1]
