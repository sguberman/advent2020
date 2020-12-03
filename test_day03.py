import pytest

from day03 import count_trees_in_path, part1, part2, read_tree_map

PUZZLE_INPUT = 'input_day03.txt'
TEST_INPUT = 'test_input_day03.txt'
EXAMPLE = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (PUZZLE_INPUT, 181),
    (TEST_INPUT, 7),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (PUZZLE_INPUT, 1260601650),
    (TEST_INPUT, 336),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_read_tree_map():
    assert read_tree_map(TEST_INPUT) == EXAMPLE


@pytest.mark.parametrize('dx, dy, expected', [
    (3, 1, 7),
    (1, 1, 2),
    (5, 1, 3),
    (7, 1, 4),
    (1, 2, 2),
])
def test_count_trees_in_path(dx, dy, expected):
    assert count_trees_in_path(EXAMPLE, dx, dy) == expected
