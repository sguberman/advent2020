from collections import Counter
from typing import Tuple


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


def is_valid(times: Tuple[int, int],
             letter: str,
             password: str) -> bool:
    """
    Return True if password is valid according to policy: letter appears
    correct number of times.
    """
    at_least, at_most = times
    return Counter(password)[letter] in range(at_least, at_most + 1)


def part1(filename: str) -> int:
    return sum(is_valid(*parse_line(line)) for line in open(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day02.txt'
    print(part1(puzzle_input))  # 454
