from typing import Iterator

from utils import elapsed_time, print_results


def boarding_passes(filename: str) -> Iterator[str]:
    return (line.strip() for line in open(filename))


def seat_id(boarding_pass: str) -> int:
    binary_boarding_pass = boarding_pass.\
        replace('B', '1').\
        replace('F', '0').\
        replace('R', '1').\
        replace('L', '0')
    return int(binary_boarding_pass, 2)


def part1(filename: str) -> int:
    return max(seat_id(bp) for bp in boarding_passes(filename))


def part2(filename: str) -> int:
    ids = set(seat_id(bp) for bp in boarding_passes(filename))
    return next(id for id in range(min(ids), max(ids) + 1) if id not in ids)


if __name__ == '__main__':
    puzzle_input = 'input_day05.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
