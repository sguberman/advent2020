import pytest

from day11 import (count_adjacent_neighbors, count_occupied_seats,
                   count_visible_neighbors, next_seat, part1, part2,
                   simulate_one_round, simulate_to_end)

PUZZLE_INPUT = 'input_day11.txt'
TEST_INPUT = 'test_input_day11.txt'
EXAMPLE = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL',
]
ROUND1_1 = [
    '#.##.##.##',
    '#######.##',
    '#.#.#..#..',
    '####.##.##',
    '#.##.##.##',
    '#.#####.##',
    '..#.#.....',
    '##########',
    '#.######.#',
    '#.#####.##',
]
ROUND2_1 = [
    '#.LL.L#.##',
    '#LLLLLL.L#',
    'L.L.L..L..',
    '#LLL.LL.L#',
    '#.LL.LL.LL',
    '#.LLLL#.##',
    '..L.L.....',
    '#LLLLLLLL#',
    '#.LLLLLL.L',
    '#.#LLLL.##',
]
ROUND3_1 = [
    '#.##.L#.##',
    '#L###LL.L#',
    'L.#.#..#..',
    '#L##.##.L#',
    '#.##.LL.LL',
    '#.###L#.##',
    '..#.#.....',
    '#L######L#',
    '#.LL###L.L',
    '#.#L###.##',
]
ROUND4_1 = [
    '#.#L.L#.##',
    '#LLL#LL.L#',
    'L.L.L..#..',
    '#LLL.##.L#',
    '#.LL.LL.LL',
    '#.LL#L#.##',
    '..L.L.....',
    '#L#LLLL#L#',
    '#.LLLLLL.L',
    '#.#L#L#.##',
]
ROUND5_1 = [
    '#.#L.L#.##',
    '#LLL#LL.L#',
    'L.#.L..#..',
    '#L##.##.L#',
    '#.#L.LL.LL',
    '#.#L#L#.##',
    '..L.L.....',
    '#L#L##L#L#',
    '#.LLLLLL.L',
    '#.#L#L#.##',
]
ROUND1_2 = [
    '#.##.##.##',
    '#######.##',
    '#.#.#..#..',
    '####.##.##',
    '#.##.##.##',
    '#.#####.##',
    '..#.#.....',
    '##########',
    '#.######.#',
    '#.#####.##',
]
ROUND2_2 = [
    '#.LL.LL.L#',
    '#LLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLL#',
    '#.LLLLLL.L',
    '#.LLLLL.L#',
]
ROUND3_2 = [
    '#.L#.##.L#',
    '#L#####.LL',
    'L.#.#..#..',
    '##L#.##.##',
    '#.##.#L.##',
    '#.#####.#L',
    '..#.#.....',
    'LLL####LL#',
    '#.L#####.L',
    '#.L####.L#',
]
ROUND4_2 = [
    '#.L#.L#.L#',
    '#LLLLLL.LL',
    'L.L.L..#..',
    '##LL.LL.L#',
    'L.LL.LL.L#',
    '#.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLL#',
    '#.LLLLL#.L',
    '#.L#LL#.L#',
]
ROUND5_2 = [
    '#.L#.L#.L#',
    '#LLLLLL.LL',
    'L.L.L..#..',
    '##L#.#L.L#',
    'L.L#.#L.L#',
    '#.L####.LL',
    '..#.#.....',
    'LLL###LLL#',
    '#.LLLLL#.L',
    '#.L#LL#.L#',
]
ROUND6_2 = [
    '#.L#.L#.L#',
    '#LLLLLL.LL',
    'L.L.L..#..',
    '##L#.#L.L#',
    'L.L#.LL.L#',
    '#.LLLL#.LL',
    '..#.L.....',
    'LLL###LLL#',
    '#.LLLLL#.L',
    '#.L#LL#.L#',
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 37),
    (PUZZLE_INPUT, 2441),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 26),
    #(PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


@pytest.mark.parametrize('state, expected', [
    (ROUND5_1, 37),
    (ROUND6_2, 26),
])
def test_count_occupied_seats(state, expected):
    assert count_occupied_seats(state) == expected


@pytest.mark.parametrize('state, max_neighbors, count_fn, next_state', [
    (EXAMPLE, 4, count_adjacent_neighbors, ROUND1_1),
    (ROUND1_1, 4, count_adjacent_neighbors, ROUND2_1),
    (ROUND2_1, 4, count_adjacent_neighbors, ROUND3_1),
    (ROUND3_1, 4, count_adjacent_neighbors, ROUND4_1),
    (ROUND4_1, 4, count_adjacent_neighbors, ROUND5_1),
    (ROUND5_1, 4, count_adjacent_neighbors, ROUND5_1),
    (EXAMPLE, 5, count_visible_neighbors, ROUND1_2),
    (ROUND1_2, 5, count_visible_neighbors, ROUND2_2),
    (ROUND2_2, 5, count_visible_neighbors, ROUND3_2),
    (ROUND3_2, 5, count_visible_neighbors, ROUND4_2),
    (ROUND4_2, 5, count_visible_neighbors, ROUND5_2),
    (ROUND5_2, 5, count_visible_neighbors, ROUND6_2),
    (ROUND6_2, 5, count_visible_neighbors, ROUND6_2),
])
def test_simulate_one_round(state, max_neighbors, count_fn, next_state):
    before, after = simulate_one_round(state, max_neighbors, count_fn)
    assert before == state
    assert after == next_state


@pytest.mark.parametrize('i, j, state, expected', [
    (0, 0, EXAMPLE, 0),
    (0, 0, ROUND1_1, 2),
    (0, 0, ROUND2_1, 1),
    (0, 0, ROUND3_1, 1),
    (0, 0, ROUND4_1, 1),
    (0, 0, ROUND5_1, 1),
    (1, 4, EXAMPLE, 0),
    (1, 4, ROUND1_1, 5),
    (1, 4, ROUND2_1, 0),
    (1, 4, ROUND3_1, 3),
    (1, 4, ROUND4_1, 0),
    (1, 4, ROUND5_1, 0),
    (9, 9, EXAMPLE, 0),
    (9, 9, ROUND1_1, 2),
    (9, 9, ROUND2_1, 1),
    (9, 9, ROUND3_1, 1),
    (9, 9, ROUND4_1, 1),
    (9, 9, ROUND5_1, 1),
])
def test_count_adjacent_neighbors(i, j, state, expected):
    assert count_adjacent_neighbors(i, j, state) == expected


SEES_8 = [
    '.......#.',
    '...#.....',
    '.#.......',
    '.........',
    '..#L....#',
    '....#....',
    '.........',
    '#........',
    '...#.....',
]
SEES_1 = [
    '.............',
    '.L.L.#.#.#.#.',
    '.............',
]
SEES_0 = [
    '.##.##.',
    '#.#.#.#',
    '##...##',
    '...L...',
    '##...##',
    '#.#.#.#',
    '.##.##.',
]


@pytest.mark.parametrize('i, j, state, expected', [
    (4, 3, SEES_8, 8),
    (1, 1, SEES_1, 1),
    (3, 3, SEES_0, 0),
])
def test_count_visible_neighbors(i, j, state, expected):
    assert count_visible_neighbors(i, j, state) == expected


@pytest.mark.parametrize('state, max_neighbors, count_fn, expected', [
    (EXAMPLE, 4, count_adjacent_neighbors, ROUND5_1),
    (EXAMPLE, 5, count_visible_neighbors, ROUND6_2),
])
def test_simulate_to_end(state, max_neighbors, count_fn, expected):
    assert simulate_to_end(state, max_neighbors, count_fn) == expected
