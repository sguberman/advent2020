from time import time
from typing import Iterator


def boarding_passes(filename: str) -> Iterator[str]:
    return (line.strip() for line in open(filename))


def seat_id(boarding_pass: str) -> int:
    return row(boarding_pass) * 8 + column(boarding_pass)


def partition(minn: int, maxx: int, halves: str) -> int:
    for half in halves:
        mid = minn + (maxx - minn) // 2
        if half in 'FL':
            maxx = mid
        else:
            minn = mid + 1
    return minn


def row(boarding_pass: str) -> int:
    halves = boarding_pass[:7]
    minn, maxx = 0, 127
    return partition(minn, maxx, halves)


def column(boarding_pass: str) -> int:
    halves = boarding_pass[-3:]
    minn, maxx = 0, 7
    return partition(minn, maxx, halves)


def part1(filename: str) -> int:
    return max(seat_id(bp) for bp in boarding_passes(filename))


def part2(filename: str) -> int:
    ids = [seat_id(bp) for bp in boarding_passes(filename)]
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
