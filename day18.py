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


class EvalAddOp:
    def __init__(self, tokens):
        self.value = tokens[0]

    def eval(self):
        result = self.value[0].eval()
        for op, val in operatorOperands(self.value[1:]):
            result += val.eval()
        return result


class EvalMulOp:
    def __init__(self, tokens):
        self.value = tokens[0]

    def eval(self):
        result = self.value[0].eval()
        for op, val in operatorOperands(self.value[1:]):
            result *= val.eval()
        return result


def stream_input(filename: str) -> Iterator[str]:
    with open(filename) as f:
        for line in f:
            yield line.strip()


def evaluate(expression: str, parser: ParserElement) -> int:
    return parser.parseString(expression)[0].eval()


def part1_parser() -> ParserElement:
    integer = ppc.integer
    integer.setParseAction(EvalConstant)
    op = oneOf("+ *")
    expr = infixNotation(
        integer,
        [
            (op, 2, opAssoc.LEFT, EvalOp),  # equal precedence
        ]
    )
    return expr


def part2_parser() -> ParserElement:
    integer = ppc.integer
    integer.setParseAction(EvalConstant)
    add_op = "+"
    mul_op = "*"
    expr = infixNotation(
        integer,
        [
            (add_op, 2, opAssoc.LEFT, EvalAddOp),  # + takes precedence over *
            (mul_op, 2, opAssoc.LEFT, EvalMulOp),
        ]
    )
    return expr


def part1(filename: str) -> int:
    parser = part1_parser()
    return sum(evaluate(expression, parser)
               for expression in stream_input(filename))


def part2(filename: str) -> int:
    parser = part2_parser()
    return sum(evaluate(expression, parser)
               for expression in stream_input(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day18.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
