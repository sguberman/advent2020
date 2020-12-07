import pytest

from day07 import does_contain, number_contained, part1, part2, read_rules

PUZZLE_INPUT = 'input_day07.txt'
TEST_INPUT = 'test_input_day07.txt'
EXAMPLE = {
    'light red': [
        'bright white',
        'muted yellow', 'muted yellow'
    ],
    'dark orange': [
        'bright white', 'bright white', 'bright white',
        'muted yellow', 'muted yellow', 'muted yellow', 'muted yellow'
    ],
    'bright white': [
        'shiny gold'
    ],
    'muted yellow': [
        'shiny gold', 'shiny gold',
        'faded blue', 'faded blue', 'faded blue',
        'faded blue', 'faded blue', 'faded blue',
        'faded blue', 'faded blue', 'faded blue'
    ],
    'shiny gold': [
        'dark olive',
        'vibrant plum', 'vibrant plum'
    ],
    'dark olive': [
        'faded blue', 'faded blue', 'faded blue',
        'dotted black', 'dotted black', 'dotted black', 'dotted black'
    ],
    'vibrant plum': [
        'faded blue', 'faded blue', 'faded blue', 'faded blue', 'faded blue',
        'dotted black', 'dotted black', 'dotted black',
        'dotted black', 'dotted black', 'dotted black'
    ],
    'faded blue': [],
    'dotted black': []
}


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


def test_read_rules():
    assert read_rules(TEST_INPUT) == EXAMPLE


@pytest.mark.parametrize('outer_bag, expected', [
    ('bright white', True),
    ('muted yellow', True),
    ('dark orange', True),
    ('light red', True),
    ('shiny gold', False),
    ('dark olive', False),
    ('vibrant plum', False),
    ('faded blue', False),
    ('dotted black', False),
])
def test_does_contain(outer_bag, expected):
    filename = TEST_INPUT
    rules = EXAMPLE
    target_bag = 'shiny gold'
    assert does_contain(target_bag, outer_bag, filename, rules) == expected


@pytest.mark.parametrize('bag, expected', [
    ('faded blue', 0),
    ('dotted black', 0),
    ('vibrant plum', 11),
    ('dark olive', 7),
    ('shiny gold', 32),
])
def test_number_contained(bag, expected):
    rules = EXAMPLE
    assert number_contained(bag, rules) == expected
