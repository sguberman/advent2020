import pytest

from day14 import apply_mask_to_address, apply_mask_to_value, part1, part2

PUZZLE_INPUT = 'input_day14.txt'
TEST_INPUT_1 = 'test_input_day14_1.txt'
TEST_INPUT_2 = 'test_input_day14_2.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT_1, 165),
    (PUZZLE_INPUT, 6386593869035),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT_2, 208),
    (PUZZLE_INPUT, 4288986482164),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


@pytest.mark.parametrize('mask, value, expected', [
    ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11, 73),
    ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101, 101),
    ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0, 64),
])
def test_apply_mask_to_value(mask, value, expected):
    assert apply_mask_to_value(mask, value) == expected


@pytest.mark.parametrize('mask, address, expected', [
    ('000000000000000000000000000000X1001X', 42,
     [26, 27, 58, 59]),
    ('00000000000000000000000000000000X0XX', 26,
     [16, 17, 18, 19, 24, 25, 26, 27]),
])
def test_apply_mask_to_address(mask, address, expected):
    assert apply_mask_to_address(mask, address) == expected
