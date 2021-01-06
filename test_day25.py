import pytest

from day25 import find_encryption_key, find_loop_size, part1, read_public_keys

PUZZLE_INPUT = 'input_day25.txt'
TEST_INPUT = 'test_input_day25.txt'
CARD_KEY = 5764801
DOOR_KEY = 17807724
SUBJECT_NUMBER = 7
CARD_LOOP_SIZE = 8
DOOR_LOOP_SIZE = 11
ENCRYPTION_KEY = 14897079


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 14897079),
    (PUZZLE_INPUT, 3015200),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


def test_read_public_keys():
    assert read_public_keys(TEST_INPUT) == [CARD_KEY, DOOR_KEY]


@pytest.mark.parametrize('public_key, expected', [
    (CARD_KEY, CARD_LOOP_SIZE),
    (DOOR_KEY, DOOR_LOOP_SIZE),
])
def test_find_loop_size(public_key, expected):
    assert find_loop_size(public_key, SUBJECT_NUMBER) == expected


@pytest.mark.parametrize('key1, key2, expected', [
    (CARD_KEY, DOOR_KEY, ENCRYPTION_KEY),
    (DOOR_KEY, CARD_KEY, ENCRYPTION_KEY),
])
def test_find_encryption_key(key1, key2, expected):
    assert find_encryption_key(key1, key2, SUBJECT_NUMBER) == expected
