from collections import deque

import pytest

from day23 import from_labels, labels_after_1, move, part1, part2

PUZZLE_INPUT = '653427918'
TEST_INPUT = '389125467'
EXAMPLE_START = deque([3, 8, 9, 1, 2, 5, 4, 6, 7])
EXAMPLE_AFTER_1 = deque([2, 8, 9, 1, 5, 4, 6, 7, 3])
EXAMPLE_AFTER_10 = deque([8, 3, 7, 4, 1, 9, 2, 6, 5])


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 67384529),
    (PUZZLE_INPUT, 76952348),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    #(TEST_INPUT, 149245887792),
    #(PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_labels_after_1():
    assert labels_after_1(EXAMPLE_AFTER_10) == 92658374


def test_1_move():
    cups = from_labels(TEST_INPUT)
    assert cups == EXAMPLE_START
    cups = move(cups, times=1)
    assert cups == EXAMPLE_AFTER_1


def test_10_moves():
    assert move(EXAMPLE_START, times=10) == EXAMPLE_AFTER_10


def test_up_to():
    assert from_labels('54321', up_to=9) == deque([5, 4, 3, 2, 1, 6, 7, 8, 9])
