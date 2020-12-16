import pytest

from day16 import invalid_values, parse_input, part1, part2

PUZZLE_INPUT = 'input_day16.txt'
TEST_INPUT = 'test_input_day16.txt'

EXAMPLE_RULES = {
    'class': [range(1, 4), range(5, 8)],
    'row': [range(6, 12), range(33, 45)],
    'seat': [range(13, 41), range(45, 51)],
}

EXAMPLE_TICKET = [7, 1, 14]

EXAMPLE_NEARBY = [
    [7, 3, 47],
    [40, 4, 50],
    [55, 2, 20],
    [38, 6, 12],
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 71),
    (PUZZLE_INPUT, 29759),
])
def test_part1(puzzle_input, answer):
    rules, _, nearby = parse_input(puzzle_input)
    assert part1(rules, nearby) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 0),
    (PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_parse_input():
    expected = (EXAMPLE_RULES, EXAMPLE_TICKET, EXAMPLE_NEARBY)
    assert parse_input(TEST_INPUT) == expected


def test_invalid_values():
    assert list(invalid_values(EXAMPLE_RULES, EXAMPLE_NEARBY)) == [4, 55, 12]
