from typing import Iterator

from pyparsing import *

from utils import elapsed_time, print_results

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


def stream_input(filename: str) -> Iterator[str]:
    with open(filename) as f:
        for line in f:
            yield line.strip()


def evaluate(expression: str) -> int:
    return expr.parseString(expression)[0].eval()


def part1(filename: str) -> int:
    return sum(evaluate(expression) for expression in stream_input(filename))


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day18.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
