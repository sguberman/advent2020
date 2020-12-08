from itertools import chain
from typing import Callable, Iterator, List, Optional, Tuple

from utils import elapsed_time, print_results

State = Tuple[int, int]
Op = Callable[[int, int, int], State]
Instruction = Tuple[Op, int]
Program = List[Instruction]
ExitState = Tuple[int, int, int]


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


def run_program_until_loop(program: Program) -> ExitState:
    step, acc = 0, 0
    visited = set()
    while step not in visited:
        visited.add(step)
        try:
            instruction = program[step]
        except IndexError:
            return step, acc, 0  # exit at end of program
        step, acc = execute_instruction(instruction, step, acc)
    return step, acc, -1  # halt at loop


def swap_ops(program: Program, orig_op: Op, new_op: Op) -> Iterator[Program]:
    for step, instruction in enumerate(program):
        op, arg = instruction
        if op == orig_op:
            new_instruction = (new_op, arg)
            new_program = program.copy()
            new_program[step] = new_instruction
            yield new_program


def part1(filename: str) -> int:
    _, acc, _ = run_program_until_loop(read_program(filename))
    return acc


def part2(filename: str) -> Optional[int]:
    orig_program = read_program(filename)
    alternate_programs = chain(swap_ops(orig_program, nop, jmp),
                               swap_ops(orig_program, jmp, nop))
    for program in alternate_programs:
        _, acc, exit_code = run_program_until_loop(program)
        if exit_code == 0:  # ran to completion without looping
            return acc
    return None


if __name__ == '__main__':
    puzzle_input = 'input_day08.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 1782
                  elapsed_time(part2, puzzle_input))  # 797
