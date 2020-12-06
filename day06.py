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
    print(part1(puzzle_input))  # 6630
    print(part2(puzzle_input))  # 3437
