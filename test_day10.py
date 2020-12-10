import pytest

from day10 import (build_connection_graph, connected_adapters, count_paths,
                   joltage_differences, part1, part2)

PUZZLE_INPUT = 'input_day10.txt'
TEST_INPUT1 = 'test_input_day10_short.txt'
TEST_INPUT2 = 'test_input_day10_long.txt'

EXAMPLE1 = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

EXAMPLE2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT1, 35),
    (TEST_INPUT2, 220),
    (PUZZLE_INPUT, 1700),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT1, 8),
    (TEST_INPUT2, 19208),
    (PUZZLE_INPUT, 12401793332096),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


CONNECTED = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]


def test_connected_adapters():
    assert connected_adapters(TEST_INPUT1) == CONNECTED


JOLTAGES = [0] + CONNECTED + [22]
DIFFERENCES = [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]


def test_joltage_differences():
    assert list(joltage_differences(JOLTAGES)) == DIFFERENCES


NEIGHBORS = {
    0: [1],
    1: [4],
    4: [5, 6, 7],
    5: [6, 7],
    6: [7],
    7: [10],
    10: [11, 12],
    11: [12],
    12: [15],
    15: [16],
    16: [19],
    19: [22],
    22: [],
}


def test_build_connection_graph():
    assert build_connection_graph(JOLTAGES) == NEIGHBORS


NUM_PATHS = {
    0: 1,
    1: 1,
    4: 1,
    5: 1,
    6: 2,
    7: 4,
    10: 4,
    11: 4,
    12: 8,
    15: 8,
    16: 8,
    19: 8,
    22: 8,
}


def test_count_paths():
    assert count_paths(NEIGHBORS) == (NUM_PATHS)
