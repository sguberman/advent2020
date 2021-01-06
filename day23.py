from collections import deque
from typing import Deque

from utils import elapsed_time, print_results

Cups = Deque[int]


def from_labels(cup_labels: str) -> Cups:
    return deque(int(label) for label in cup_labels)


def move(cups: Cups, times: int) -> Cups:
    for _ in range(times):
        current = cups.popleft()
        pick_up = deque(cups.popleft() for _ in range(3))
        destination = current - 1
        while destination not in cups:
            if destination < 1:
                destination = max(cups)
            else:
                destination -= 1
        destination_idx = cups.index(destination) + 1
        while pick_up:
            cups.insert(destination_idx, pick_up.popleft())
            destination_idx += 1
        cups.append(current)
    return cups


def labels_after_1(cups: Cups) -> int:
    while cups[0] != 1:
        cups.rotate()
    cups.popleft()
    return int(''.join(str(label) for label in cups))


def part1(cup_labels: str) -> int:
    cups = from_labels(cup_labels)
    cups = move(cups, times=100)
    return labels_after_1(cups)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = '653427918'
    print_results(elapsed_time(part1, puzzle_input),  # 76952348
                  elapsed_time(part2, puzzle_input))
