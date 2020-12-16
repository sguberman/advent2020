import pytest

from day16 import (invalid_values, match_fields, parse_input, part1, part2,
                   ticket_columns, valid_tickets)

PUZZLE_INPUT = 'input_day16.txt'
TEST_INPUT_1 = 'test_input_day16_1.txt'
TEST_INPUT_2 = 'test_input_day16_2.txt'

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
    (TEST_INPUT_1, 71),
    (PUZZLE_INPUT, 29759),
])
def test_part1(puzzle_input, answer):
    rules, _, nearby = parse_input(puzzle_input)
    assert part1(rules, nearby) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT_2, 0),
    (PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    rules, ticket, nearby = parse_input(puzzle_input)
    assert part2(rules, ticket, nearby) == answer


def test_parse_input():
    expected = (EXAMPLE_RULES, EXAMPLE_TICKET, EXAMPLE_NEARBY)
    assert parse_input(TEST_INPUT_1) == expected


def test_invalid_values():
    assert list(invalid_values(EXAMPLE_RULES, EXAMPLE_NEARBY)) == [4, 55, 12]


def test_valid_tickets():
    assert valid_tickets(EXAMPLE_RULES, EXAMPLE_NEARBY) == [[7, 3, 47]]


def test_ticket_columns():
    assert ticket_columns(EXAMPLE_NEARBY) == [
        [7, 40, 55, 38],
        [3, 4, 2, 6],
        [47, 50, 20, 12],
    ]


def test_match_fields():
    rules, _, nearby = parse_input(TEST_INPUT_2)
    tickets = valid_tickets(rules, nearby)
    expected = {'class': [1], 'row': [0], 'seat': [2]}
    assert match_fields(rules, tickets) == expected
