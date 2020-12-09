import pytest

from day09 import (all_sums, first_invalid, is_valid, is_valid2, part1, part2,
                   update_sums)

PUZZLE_INPUT = 'input_day09.txt'
TEST_INPUT = 'test_input_day09.txt'
EXAMPLE1 = [20] + list(range(1, 20)) + list(range(21, 26))
EXAMPLE2 = EXAMPLE1[1:] + [45]
EXAMPLE3 = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 0),
    (PUZZLE_INPUT, 0),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 0),
    (PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


@pytest.mark.parametrize('number, preamble, expected', [
    (26, EXAMPLE1, True),
    (49, EXAMPLE1, True),
    (100, EXAMPLE1, False),
    (50, EXAMPLE1, False),
    (26, EXAMPLE2, True),
    (65, EXAMPLE2, False),
    (64, EXAMPLE2, True),
    (66, EXAMPLE2, True),
])
def test_is_valid(number, preamble, expected):
    assert is_valid(number, preamble) == expected


def test_first_invalid():
    assert first_invalid(EXAMPLE3, 5) == 127


PREAMBLE = [1, 2, 3, 4]
PREAMBLE_SUMS = {
    1: {3, 4, 5},
    2: {5, 6},
    3: {7, },
    4: set(),
}
UPDATED_SUMS = {
    2: {5, 6, 7},
    3: {7, 8},
    4: {9, },
    5: set(),
}


def test_all_sums():
    assert all_sums(PREAMBLE) == PREAMBLE_SUMS


def test_update_sums():
    assert update_sums(PREAMBLE_SUMS, 5) == UPDATED_SUMS


@pytest.mark.parametrize('number, sums, expected', [
    (5, PREAMBLE_SUMS, True),
    (10, PREAMBLE_SUMS, False),
    (2, PREAMBLE_SUMS, False),
    (8, PREAMBLE_SUMS, False),
])
def test_is_valid2(number, sums, expected):
    assert is_valid2(number, sums) == expected
