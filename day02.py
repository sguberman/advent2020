from collections import Counter
from time import time
from typing import Callable, Tuple


def parse_line(line: str) -> Tuple[Tuple[int, int], str, str]:
    """
    Parse a line from input and return a tuple containing the range, letter,
    and password.
    """
    policy, password = line.split(':')
    password = password.strip()
    times, letter = policy.split(' ')
    at_least, at_most = map(int, times.split('-'))
    return ((at_least, at_most), letter, password)


def is_valid_times(times: Tuple[int, int],
                   letter: str,
                   password: str) -> bool:
    """
    Return True if password is valid according to policy: letter appears
    correct number of times.
    """
    at_least, at_most = times
    return Counter(password)[letter] in range(at_least, at_most + 1)


def is_valid_positions(positions: Tuple[int, int],
                       letter: str,
                       password: str) -> bool:
    """
    Return True if password is valid according to policy: letter appears
    at the correct location.
    """
    i, j = positions
    i -= 1
    j -= 1
    return ((password[i] == letter and password[j] != letter) or
            (password[i] != letter and password[j] == letter))


def count_valid_passwords(filename: str, validation_fn: Callable) -> int:
    return sum(validation_fn(*parse_line(line)) for line in open(filename))


def part1(filename: str) -> int:
    return count_valid_passwords(filename, is_valid_times)


def part2(filename: str) -> int:
    return count_valid_passwords(filename, is_valid_positions)


if __name__ == '__main__':
    puzzle_input = 'input_day02.txt'
    part1_start = time()
    print(part1(puzzle_input), f"{time() - part1_start:.3f}s")  # 454
    part2_start = time()
    print(part2(puzzle_input), f"{time() - part2_start:.3f}s")  # 649
