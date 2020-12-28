from collections import deque

import pytest

from day22 import get_hands, part1, part2, play_game, play_round, score_hand

PUZZLE_INPUT = 'input_day22.txt'
TEST_INPUT = 'test_input_day22.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 306),
    (PUZZLE_INPUT, 31314),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 0),
    (PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_play_round():
    HAND_1_BEFORE = deque([9, 2, 6, 3, 1])
    HAND_2_BEFORE = deque([5, 8, 4, 7, 10])
    HAND_1_AFTER = deque([2, 6, 3, 1, 9, 5])
    HAND_2_AFTER = deque([8, 4, 7, 10])
    assert play_round(HAND_1_BEFORE, HAND_2_BEFORE) == (HAND_1_AFTER,
                                                        HAND_2_AFTER)


def test_play_game():
    HAND_1_BEFORE = deque([9, 2, 6, 3, 1])
    HAND_2_BEFORE = deque([5, 8, 4, 7, 10])
    WINNING_HAND = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    assert play_game(HAND_1_BEFORE, HAND_2_BEFORE) == (deque(), WINNING_HAND)


def test_score_hand():
    WINNING_HAND = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    assert score_hand(WINNING_HAND) == 306


def test_get_hands():
    HAND_1_BEFORE = deque([9, 2, 6, 3, 1])
    HAND_2_BEFORE = deque([5, 8, 4, 7, 10])
    assert get_hands(TEST_INPUT) == (HAND_1_BEFORE, HAND_2_BEFORE)
