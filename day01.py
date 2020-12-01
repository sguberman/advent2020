from itertools import combinations
from typing import Iterable, Tuple


def find_n_numbers_totaling(n: int,
                            total: int,
                            numbers: Iterable[int]) -> Tuple[int, ...]:
    return next(group for group in combinations(numbers, n)
                if sum(group) == total)


def part1(filename: str) -> int:
    entries = (int(entry) for entry in open(filename))
    first, second = find_n_numbers_totaling(2, 2020, entries)
    return first * second


def part2(filename: str) -> int:
    entries = (int(entry) for entry in open(filename))
    first, second, third = find_n_numbers_totaling(3, 2020, entries)
    return first * second * third


if __name__ == '__main__':
    puzzle_input = 'input_day01.txt'
    print(part1(puzzle_input))  # 1016131
    print(part2(puzzle_input))  # 276432018
