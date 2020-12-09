from collections import defaultdict
from itertools import combinations, islice
from typing import Dict, Iterable, Optional

from utils import elapsed_time, print_results


def stream_numbers(filename: str) -> Iterable[int]:
    return (int(line) for line in open(filename))


def all_sums(preamble: Iterable[int]) -> Dict[int, set]:
    sums = defaultdict(set)
    for first, second in combinations(preamble, 2):
        sums[first].add(first + second)
    sums[second] = set()
    return sums


def update_sums(sums: Dict[int, set], new_number: int) -> Dict[int, set]:
    del(sums[list(sums.keys())[0]])  # remove the first (oldest) key
    for key in sums:
        sums[key].add(key + new_number)
    sums[new_number] = set()
    return sums


def is_valid(number: int, sums: Dict[int, set]) -> bool:
    return any(number in value for value in sums.values())


def first_invalid(numbers: Iterable[int],
                  preamble_len: int = 25) -> Optional[int]:
    preamble = islice(numbers, preamble_len)
    sums = all_sums(preamble)
    for new_number in numbers:
        if not is_valid(new_number, sums):
            return new_number
        else:
            sums = update_sums(sums, new_number)
    return None


def part1(filename: str, preamble_len: int = 25) -> Optional[int]:
    numbers = stream_numbers(filename)
    return first_invalid(numbers, preamble_len)


def part2(filename: str, preamble_len: int = 25) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day09.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
