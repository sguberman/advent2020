import pytest

from day05 import part1, part2, seat_id

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
                         zip(EXAMPLES, (357, 567, 119, 820)))
def test_seat_id(boarding_pass, expected):
    assert seat_id(boarding_pass) == expected
