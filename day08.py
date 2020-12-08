from typing import Callable, List, Tuple

from utils import elapsed_time, print_results

State = Tuple[int, int]
Op = Callable[[int, int, int], State]
Instruction = Tuple[Op, int]
Program = List[Instruction]


def acc(arg: int, step: int, acc: int) -> State:
    return step + 1, acc + arg


def jmp(arg: int, step: int, acc: int) -> State:
    return step + arg, acc


def nop(arg: int, step: int, acc: int) -> State:
    return step + 1, acc


OPS = {
    'acc': acc,
    'jmp': jmp,
    'nop': nop,
}


def read_program(filename: str) -> Program:
    return [parse_line(line) for line in open(filename)]


def parse_line(line: str) -> Instruction:
    operation, argument = line.strip().split()
    return OPS[operation], int(argument)


def execute_instruction(instruction: Instruction,
                        step: int,
                        acc: int) -> Tuple[int, int]:
    op, arg = instruction
    return op(arg, step, acc)


def run_program_until_loop(program: Program) -> State:
    step, acc = 0, 0
    visited = set()
    while step not in visited:
        visited.add(step)
        step, acc = execute_instruction(program[step], step, acc)
    return step, acc


def part1(filename: str) -> int:
    _, acc = run_program_until_loop(read_program(filename))
    return acc


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day08.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
