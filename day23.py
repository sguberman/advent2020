from collections import deque
from typing import Deque, Optional, Tuple

from utils import elapsed_time, print_results

Cups = Deque[int]


def from_labels(cup_labels: str, up_to: Optional[int] = None) -> Cups:
    cups = deque(int(label) for label in cup_labels)
    if up_to:
        cups.extend(range(max(cups) + 1, up_to + 1))
    return cups


def move(cups: Cups, times: int) -> Cups:
    max_cup = max(cups)
    for i in range(1, times + 1):
        if not i % 1000:
            print(f"Working on move {i}...")
        current = cups.popleft()
        pick_up = deque(cups.popleft() for _ in range(3))
        destination = current - 1
        while destination in pick_up or destination < 1 or destination == current:
            if destination < 1:
                destination = max_cup
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


def first_two_after_1(cups: Cups) -> Tuple[int, int]:
    idx = cups.index(1)
    return cups[idx + 1], cups[idx + 2]


def part1(cup_labels: str) -> int:
    cups = from_labels(cup_labels)
    cups = move(cups, times=100)
    return labels_after_1(cups)


def part2(cup_labels: str) -> int:
    cups = from_labels(cup_labels, up_to=1_000_000)
    cups = move(cups, times=10_000_000)
    cup1, cup2 = first_two_after_1(cups)
    return cup1 * cup2


if __name__ == '__main__':
    puzzle_input = '653427918'
    print_results(elapsed_time(part1, puzzle_input),  # 76952348
                  elapsed_time(part2, puzzle_input))
