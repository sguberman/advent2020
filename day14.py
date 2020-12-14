from collections import defaultdict
from itertools import product
from typing import Dict, Iterable, List, Optional, Tuple

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


def apply_mask_to_value(mask: str, value: int) -> int:
    set_mask = int(mask.replace('X', '0'), base=2)
    unset_mask = int(mask.replace('X', '1'), base=2) ^ 68719476735  # all 1's
    value = value | set_mask
    value = value & ~unset_mask
    return value


def update_memory_v1(mask: str, address: int, value: int,
                     memory: Memory) -> Memory:
    memory[address] = apply_mask_to_value(mask, value)
    return memory


def apply_mask_to_address(mask: str, address: int) -> List[int]:
    set_mask = int(mask.replace('X', '0'), base=2)
    address = address | set_mask
    addresses = []
    floating_indices = [i for i, bit in enumerate(mask) if bit == 'X']
    for combo in product('01', repeat=len(floating_indices)):
        temp_address = list(f"{address:0>36b}")
        for i, bit in zip(floating_indices, combo):
            temp_address[i] = bit
        new_address = int(''.join(temp_address), base=2)
        addresses.append(new_address)
    return addresses


def update_memory_v2(mask: str, address: int, value: int,
                     memory: Memory) -> Memory:
    for masked_address in apply_mask_to_address(mask, address):
        memory[masked_address] = value
    return memory


def run_program(filename: str, version: int) -> Memory:
    update_memory = update_memory_v1 if version == 1 else update_memory_v2
    memory: Memory = defaultdict(int)
    for new_mask, address, value in stream_program(filename):
        if new_mask:
            mask = new_mask
        else:
            memory = update_memory(mask, address, value, memory)
    return memory


def part1(filename: str) -> int:
    memory = run_program(filename, version=1)
    return sum(memory.values())


def part2(filename: str) -> int:
    memory = run_program(filename, version=2)
    return sum(memory.values())


if __name__ == '__main__':
    puzzle_input = 'input_day14.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 6386593869035
                  elapsed_time(part2, puzzle_input))  # 4288986482164
