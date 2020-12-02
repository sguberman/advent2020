import pytest

from day01 import find_n_numbers_totaling, part1, part2

PUZZLE_INPUT = 'input_day01.txt'
TEST_INPUT = 'test_input_day01.txt'
EXAMPLE = [1721, 979, 366, 299, 675, 1456]


@pytest.mark.parametrize('puzzle_input, expected', [
    (TEST_INPUT, 514579),
    (PUZZLE_INPUT, 1016131),
])
def test_part1(puzzle_input, expected):
    assert part1(puzzle_input) == expected


@pytest.mark.parametrize('puzzle_input, expected', [
    (TEST_INPUT, 241861950),
    (PUZZLE_INPUT, 276432018),
])
def test_part2(puzzle_input, expected):
    assert part2(puzzle_input) == expected


@pytest.mark.parametrize('n, total, numbers, expected', [
    (2, 2020, EXAMPLE, (1721, 299)),
    (3, 2020, EXAMPLE, (979, 366, 675)),
])
def test_find_n_numbers_totaling(n, total, numbers, expected):
    assert find_n_numbers_totaling(n, total, numbers) == expected
