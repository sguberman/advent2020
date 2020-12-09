from copy import deepcopy

import pytest

from day09 import all_sums, first_invalid, is_valid, part1, part2, update_sums

PUZZLE_INPUT = 'input_day09.txt'
TEST_INPUT = 'test_input_day09.txt'
EXAMPLE = [
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


@pytest.mark.parametrize('puzzle_input, preamble_len, answer', [
    (TEST_INPUT, 5, 127),
    (PUZZLE_INPUT, 25, 542529149),
])
def test_part1(puzzle_input, preamble_len, answer):
    assert part1(puzzle_input, preamble_len) == answer


@pytest.mark.parametrize('puzzle_input, preamble_len, answer', [
    (TEST_INPUT, 5, 0),
    (PUZZLE_INPUT, 25, 0),
])
def test_part2(puzzle_input, preamble_len, answer):
    assert part2(puzzle_input, preamble_len) == answer


@pytest.mark.parametrize('numbers, expected', [
    ((x for x in EXAMPLE), 127),
    ((x for x in EXAMPLE[:14]), None),
])
def test_first_invalid(numbers, expected):
    assert first_invalid(numbers, 5) == expected


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
    sums = deepcopy(PREAMBLE_SUMS)  # avoid changes to PREAMBLE_SUMS
    assert update_sums(sums, 5) == UPDATED_SUMS


@pytest.mark.parametrize('number, sums, expected', [
    (4, PREAMBLE_SUMS, True),
    (5, PREAMBLE_SUMS, True),
    (10, PREAMBLE_SUMS, False),
    (2, PREAMBLE_SUMS, False),
    (8, PREAMBLE_SUMS, False),
])
def test_is_valid(number, sums, expected):
    assert is_valid(number, sums) == expected
