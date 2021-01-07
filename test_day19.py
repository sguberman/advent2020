import pytest

from day19 import part1, part2, read_input

PUZZLE_INPUT = 'input_day19.txt'
TEST_INPUT = 'test_input_day19.txt'
RULES = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"',
]
MESSAGES = [
    'ababbb',
    'bababa',
    'abbbab',
    'aaabbb',
    'aaaabbb',
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 2),
    (PUZZLE_INPUT, 102),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.skip()
@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 0),
    (PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_read_input():
    assert read_input(TEST_INPUT) == (RULES, MESSAGES)
