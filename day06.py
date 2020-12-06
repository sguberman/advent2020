from time import time
from typing import Iterator, List


def groups(filename: str) -> Iterator[List[str]]:
    with open(filename) as f:
        group: List[str] = []
        for line in f:
            if line == '\n':
                yield group
                group = []
            else:
                group.append(line.strip())
        yield group  # last group at end of file has no extra newline


def anyone_answers(group: List[str]) -> set:
    return set.union(*[set(x) for x in group])


def everyone_answers(group: List[str]) -> set:
    return set.intersection(*[set(x) for x in group])


def part1(filename):
    return sum(len(anyone_answers(group)) for group in groups(filename))


def part2(filename):
    return sum(len(everyone_answers(group)) for group in groups(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day06.txt'

    part1_start = time()
    part1_answer = part1(puzzle_input)  # 6630
    part1_time = time() - part1_start
    print(part1_answer, f"{part1_time:.6f}s")

    part2_start = time()
    part2_answer = part2(puzzle_input)  # 3437
    part2_time = time() - part2_start
    print(part2_answer, f"{part2_time:.6f}s")
