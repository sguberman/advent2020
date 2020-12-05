import pytest

from day05 import column, part1, part2, partition, row, seat_id

PUZZLE_INPUT = 'input_day05.txt'
EXAMPLES = [
    'FBFBBFFRLR',
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL',
]


def test_part1():
    assert part1(PUZZLE_INPUT) == 994


def test_part2():
    assert part2(PUZZLE_INPUT) == 741


@pytest.mark.parametrize('boarding_pass, expected',
                         zip(EXAMPLES, (44, 70, 14, 102)))
def test_row(boarding_pass, expected):
    assert row(boarding_pass) == expected


@pytest.mark.parametrize('boarding_pass, expected',
                         zip(EXAMPLES, (5, 7, 7, 4)))
def test_column(boarding_pass, expected):
    assert column(boarding_pass) == expected


@pytest.mark.parametrize('boarding_pass, expected',
                         zip(EXAMPLES, (357, 567, 119, 820)))
def test_seat_id(boarding_pass, expected):
    assert seat_id(boarding_pass) == expected


@pytest.mark.parametrize('minn, maxx, halves, expected', [
    (0, 127, 'FBFBBFF', 44),
    (0, 7, 'RLR', 5),
])
def test_partition(minn, maxx, halves, expected):
    assert partition(minn, maxx, halves) == expected
