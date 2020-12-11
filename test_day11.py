import pytest

from day11 import (count_neighbors, count_occupied_seats, next_seat, part1,
                   part2, simulate_one_round, simulate_to_end)

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
ROUND1 = [
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
ROUND2 = [
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
ROUND3 = [
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
ROUND4 = [
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
ROUND5 = [
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


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 37),
    (PUZZLE_INPUT, 2441),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    #(TEST_INPUT, 0),
    #(PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_count_occupied_seats():
    assert count_occupied_seats(ROUND5) == 37


@pytest.mark.parametrize('state, next_state', [
    (EXAMPLE, ROUND1),
    (ROUND1, ROUND2),
    (ROUND2, ROUND3),
    (ROUND3, ROUND4),
    (ROUND4, ROUND5),
    (ROUND5, ROUND5),
])
def test_simulate_one_round(state, next_state):
    before, after = simulate_one_round(state)
    assert before == state
    assert after == next_state


@pytest.mark.parametrize('i, j, state, expected', [
    (0, 0, EXAMPLE, 0),
    (0, 0, ROUND1, 2),
    (0, 0, ROUND2, 1),
    (0, 0, ROUND3, 1),
    (0, 0, ROUND4, 1),
    (0, 0, ROUND5, 1),
    (1, 4, EXAMPLE, 0),
    (1, 4, ROUND1, 5),
    (1, 4, ROUND2, 0),
    (1, 4, ROUND3, 3),
    (1, 4, ROUND4, 0),
    (1, 4, ROUND5, 0),
    (9, 9, EXAMPLE, 0),
    (9, 9, ROUND1, 2),
    (9, 9, ROUND2, 1),
    (9, 9, ROUND3, 1),
    (9, 9, ROUND4, 1),
    (9, 9, ROUND5, 1),
])
def test_count_neighbors(i, j, state, expected):
    assert count_neighbors(i, j, state) == expected
