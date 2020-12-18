import pytest

from day18 import evaluate, part1, part2, stream_input

PUZZLE_INPUT = 'input_day18.txt'
TEST_INPUT = 'test_input_day18.txt'
EXAMPLES = [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 26457),
    (PUZZLE_INPUT, 0),
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


@pytest.mark.parametrize('example, expected', EXAMPLES)
def test_evaluate(example, expected):
    assert evaluate(example) == expected


def test_stream_input():
    assert list(stream_input(TEST_INPUT)) == [example[0]
                                              for example in EXAMPLES]
