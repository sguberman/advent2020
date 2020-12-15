import pytest

from day15 import part1, part2

PUZZLE_INPUT = '1,0,16,5,17,4'

PART1_EXAMPLES = [
    ('1,3,2', 1),
    ('2,1,3', 10),
    ('1,2,3', 27),
    ('2,3,1', 78),
    ('3,2,1', 438),
    ('3,1,2', 1836),
]

PART2_EXAMPLES = [
    ('0,3,6', 175594),
    ('1,3,2', 2578),
    ('2,1,3', 3544142),
    ('1,2,3', 261214),
    ('2,3,1', 6895259),
    ('3,2,1', 18),
    ('3,1,2', 362),
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (PUZZLE_INPUT, 1294),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (PUZZLE_INPUT, 573522),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


@pytest.mark.parametrize('example, expected', PART1_EXAMPLES)
def test_part1_examples(example, expected):
    assert part1(example) == expected


@pytest.mark.parametrize('example, expected', PART2_EXAMPLES)
def test_part2_examples(example, expected):
    assert part2(example) == expected
