from collections import deque
from typing import Deque, TextIO, Tuple

from utils import elapsed_time, print_results

Hand = Deque[int]


def read_hand(file_handle: TextIO) -> Hand:
    player_name = file_handle.readline().strip(': ')
    hand: Hand = deque()
    for line in file_handle:
        if line == '\n':
            break
        hand.append(int(line))
    return hand


def get_hands(filename: str) -> Tuple[Hand, Hand]:
    with open(filename) as f:
        hand1 = read_hand(f)
        hand2 = read_hand(f)
    return hand1, hand2


def play_round(hand1: Hand, hand2: Hand) -> Tuple[Hand, Hand]:
    hand1, hand2 = hand1.copy(), hand2.copy()
    card1, card2 = hand1.popleft(), hand2.popleft()
    if card1 > card2:
        hand1.extend([card1, card2])
    else:
        hand2.extend([card2, card1])
    return hand1, hand2


def play_game(hand1: Hand, hand2: Hand) -> Tuple[Hand, Hand]:
    while True:
        try:
            hand1, hand2 = play_round(hand1, hand2)
        except IndexError:
            return hand1, hand2


def score_hand(hand: Hand) -> int:
    return sum(mul * card for mul, card in enumerate(reversed(hand), start=1))


def part1(filename: str) -> int:
    hand1, hand2 = get_hands(filename)
    return max(map(score_hand, play_game(hand1, hand2)))


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'test_input_day22.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 31314
                  elapsed_time(part2, puzzle_input))
