import pytest

from day02 import is_valid_positions, is_valid_times, parse_line, part1, part2

PUZZLE_INPUT = 'input_day02.txt'
TEST_INPUT = 'test_input_day02.txt'


@pytest.mark.parametrize('line, expected', [
    ('1-3 a: abcde', ((1, 3), 'a', 'abcde')),
    ('1-3 b: cdefg', ((1, 3), 'b', 'cdefg')),
    ('2-9 c: ccccccccc', ((2, 9), 'c', 'ccccccccc')),
])
def test_parse_line(line, expected):
    assert parse_line(line) == expected


@pytest.mark.parametrize('times, letter, password, expected', [
    ((1, 3), 'a', 'abcde', True),
    ((1, 3), 'b', 'cdefg', False),
    ((2, 9), 'c', 'ccccccccc', True),
])
def test_is_valid_times(times, letter, password, expected):
    assert is_valid_times(times, letter, password) == expected


@pytest.mark.parametrize('positions, letter, password, expected', [
    ((1, 3), 'a', 'abcde', True),
    ((1, 3), 'b', 'cdefg', False),
    ((2, 9), 'c', 'ccccccccc', False),
])
def test_is_valid_positions(positions, letter, password, expected):
    assert is_valid_positions(positions, letter, password) == expected


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 2),
    (PUZZLE_INPUT, 454),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 1),
    (PUZZLE_INPUT, 649),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer
