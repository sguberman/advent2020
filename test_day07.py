import pytest

from day07 import part1, part2

PUZZLE_INPUT = 'input_day07.txt'
TEST_INPUT = 'test_input_day07.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 4),
    (PUZZLE_INPUT, 126),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 32),
    (PUZZLE_INPUT, 220149),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer
