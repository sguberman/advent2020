from pyparsing import *

ppc = pyparsing_common
ParserElement.enablePackrat()


class EvalConstant:
    def __init__(self, tokens):
        self.value = tokens[0]

    def eval(self):
        return int(self.value)


def operatorOperands(tokenlist):
    it = iter(tokenlist)
    while True:
        try:
            yield (next(it), next(it))
        except StopIteration:
            break


class EvalOp:
    def __init__(self, tokens):
        self.value = tokens[0]

    def eval(self):
        result = self.value[0].eval()
        for op, val in operatorOperands(self.value[1:]):
            if op == '+':
                result += val.eval()
            elif op == '*':
                result *= val.eval()
        return result


integer = ppc.integer
op = oneOf("+ *")

integer.setParseAction(EvalConstant)
expr = infixNotation(
    integer,
    [
        (op, 2, opAssoc.LEFT, EvalOp),
    ]
)

EXAMPLES = [
    '1 + 2 * 3 + 4 * 5 + 6',
    '1 + (2 * 3) + (4 * (5 + 6))',
    '2 * 3 + (4 * 5)',
    '5 + (8 * 3 + 9 + 3 * 4 * 3)',
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
]

for e in EXAMPLES:
    print(e)
    ret = expr.parseString(e)[0]
    print(ret)
    print(ret.eval())
    print()
