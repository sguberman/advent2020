from copy import deepcopy

import pytest

from day09 import (first_group_with_sum, first_invalid, is_valid, part1, part2,
                   preamble_sums, update_sums)

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
    (TEST_INPUT, 5, 62),
    (PUZZLE_INPUT, 25, 75678618),
])
def test_part2(puzzle_input, preamble_len, answer):
    assert part2(puzzle_input, preamble_len) == answer


@pytest.mark.parametrize('numbers, expected', [
    (EXAMPLE, 127),
    (EXAMPLE[:14], None),
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


def test_preamble_sums():
    assert preamble_sums(PREAMBLE) == PREAMBLE_SUMS


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


def test_first_group_with_sum():
    assert first_group_with_sum(127, EXAMPLE) == (15, 25, 47, 40)
