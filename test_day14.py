import pytest

from day14 import part1, part2

pytestmark = pytest.mark.skip()


PUZZLE_INPUT = 'input_day14.txt'
TEST_INPUT = 'test_input_day14.txt'
EXAMPLE = [
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
