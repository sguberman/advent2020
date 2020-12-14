from collections import defaultdict
from typing import Dict, Iterable, Optional, Tuple

from utils import elapsed_time, print_results

Instruction = Tuple[Optional[str], Optional[int], Optional[int]]
Memory = Dict[int, int]


def parse_line(line: str) -> Instruction:
    lhs, rhs = line.strip().split(' = ')
    if lhs == 'mask':
        return rhs, None, None
    else:  # mem
        value = int(rhs)
        address = int(lhs.split('[')[1][:-1])
        return None, address, value


def stream_program(filename: str) -> Iterable[Instruction]:
    return (parse_line(line) for line in open(filename))


def apply_mask(mask: str, value: int) -> int:
    set_mask = int(mask.replace('X', '0'), base=2)
    unset_mask = int(mask.replace('X', '1'), base=2) ^ 68719476735  # all 1's
    value = value | set_mask
    value = value & ~unset_mask
    return value


def update_memory(mask: str, address: int, value: int,
                  memory: Memory) -> Memory:
    memory[address] = apply_mask(mask, value)
    return memory


def part1(filename: str) -> int:
    memory: Memory = defaultdict(int)
    for new_mask, address, value in stream_program(filename):
        if new_mask:
            mask = new_mask
        else:
            memory = update_memory(mask, address, value, memory)
    return sum(memory.values())


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day14.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
