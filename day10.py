from collections import Counter
from itertools import combinations
from typing import Iterable, List

from utils import elapsed_time, print_results


def connected_adapters(filename: str) -> List[int]:
    return sorted(int(line) for line in open(filename))


def joltage_differences(joltages: List[int]) -> Iterable[int]:
    return (b - a for a, b in zip(joltages, joltages[1:]))


def is_valid(arrangement: List[int]) -> bool:
    return all(difference <= 3
               for difference in joltage_differences(arrangement))


def all_arrangements(adapters: List[int]) -> Iterable[List[int]]:
    outlet = 0
    device = max(adapters) + 3
    min_len = (device - outlet) // 3
    for r in range(min_len, len(adapters)):
        for arrangement in combinations(adapters, r):
            yield [outlet] + list(arrangement) + [device]


def part1(filename: str) -> int:
    adapters = connected_adapters(filename)
    outlet = 0
    device = max(adapters) + 3
    joltages = [outlet] + adapters + [device]
    differences = Counter(joltage_differences(joltages))
    return differences[1] * differences[3]


def part2(filename: str) -> int:
    adapters = connected_adapters(filename)
    return sum(is_valid(arrangement)
               for arrangement in all_arrangements(adapters))


if __name__ == '__main__':
    puzzle_input = 'input_day10.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
