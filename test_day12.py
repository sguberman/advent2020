import pytest

from day12 import part1, part2

PUZZLE_INPUT = 'input_day12.txt'
TEST_INPUT = 'test_input_day12.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 25),
    (PUZZLE_INPUT, 882),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 286),
    (PUZZLE_INPUT, 28885),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer
