from time import time
from typing import Iterator


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

    part1_start = time()
    part1_answer = part1(puzzle_input)  # 994
    part1_time = time() - part1_start
    print(part1_answer, f"{part1_time:.6f}s")

    part2_start = time()
    part2_answer = part2(puzzle_input)  # 741
    part2_time = time() - part2_start
    print(part2_answer, f"{part2_time:.6f}s")
