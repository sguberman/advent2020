import pytest

from day06 import anyone_answers, everyone_answers, groups, part1, part2

PUZZLE_INPUT = 'input_day06.txt'
TEST_INPUT = 'test_input_day06.txt'
EXAMPLE = [
    ['abc'],
    ['a', 'b', 'c'],
    ['ab', 'ac'],
    ['a', 'a', 'a', 'a'],
    ['b'],
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 11),
    (PUZZLE_INPUT, 6630),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 6),
    (PUZZLE_INPUT, 3437),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_groups():
    assert list(groups(TEST_INPUT)) == EXAMPLE


@pytest.mark.parametrize('group, expected', [
    (EXAMPLE[0], {'a', 'b', 'c'}),
    (EXAMPLE[1], {'a', 'b', 'c'}),
    (EXAMPLE[2], {'a', 'b', 'c'}),
    (EXAMPLE[3], {'a'}),
    (EXAMPLE[4], {'b'}),
])
def test_anyone_answers(group, expected):
    assert anyone_answers(group) == expected


@pytest.mark.parametrize('group, expected', [
    (EXAMPLE[0], {'a', 'b', 'c'}),
    (EXAMPLE[1], set()),
    (EXAMPLE[2], {'a'}),
    (EXAMPLE[3], {'a'}),
    (EXAMPLE[4], {'b'}),
])
def test_everyone_answers(group, expected):
    assert everyone_answers(group) == expected
