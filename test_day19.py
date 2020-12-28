import pytest

from day19 import (count_matches, parse_rules, part1, part2, process_rule_dict,
                   read_input)

PUZZLE_INPUT = 'input_day19.txt'
TEST_INPUT = 'test_input_day19.txt'
RULES = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"',
]
MESSAGES = [
    'ababbb',
    'bababa',
    'abbbab',
    'aaabbb',
    'aaaabbb',
]
INITIAL_RULE_DICT = {
    0: [[4, 1, 5]],
    1: [[2, 3], [3, 2]],
    2: [[4, 4], [5, 5]],
    3: [[4, 5], [5, 4]],
    4: ['a'],
    5: ['b'],
}
FINAL_RULE_DICT = {
    0: ['aaaabb', 'aaabab', 'abbabb', 'abbbab',
        'aabaab', 'aabbbb', 'abaaab', 'ababbb'],
    1: ['aaab', 'aaba', 'bbab', 'bbba',
        'abaa', 'abbb', 'baaa', 'babb'],
    2: ['aa', 'bb'],
    3: ['ab', 'ba'],
    4: ['a'],
    5: ['b'],
}


@pytest.mark.skip()
@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 2),
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


def test_read_input():
    assert read_input(TEST_INPUT) == (RULES, MESSAGES)


def test_parse_rules():
    assert parse_rules(RULES) == INITIAL_RULE_DICT


def test_count_matches():
    assert count_matches(FINAL_RULE_DICT[0], MESSAGES) == 2


def test_process_rule_dict():
    assert process_rule_dict(INITIAL_RULE_DICT) == FINAL_RULE_DICT
