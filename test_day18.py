import pytest

from day18 import (evaluate, part1, part1_parser, part2, part2_parser,
                   stream_input)

PUZZLE_INPUT = 'input_day18.txt'
TEST_INPUT = 'test_input_day18.txt'
EXAMPLES_1 = [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
]
EXAMPLES_2 = [
    ('1 + 2 * 3 + 4 * 5 + 6', 231),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 46),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 26457),
    (PUZZLE_INPUT, 464478013511),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 694173),
    (PUZZLE_INPUT, 85660197232452),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


@pytest.mark.parametrize('example, expected', EXAMPLES_1)
def test_evaluate_part1(example, expected):
    assert evaluate(example, part1_parser()) == expected


@pytest.mark.parametrize('example, expected', EXAMPLES_2)
def test_evaluate_part2(example, expected):
    assert evaluate(example, part2_parser()) == expected


def test_stream_input():
    assert list(stream_input(TEST_INPUT)) == [example[0]
                                              for example in EXAMPLES_1]
