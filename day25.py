from typing import List

from utils import elapsed_time, print_results


def read_public_keys(filename: str) -> List[int]:
    return [int(x) for x in open(filename).readlines()]


def transform(value: int, subject_number: int) -> int:
    value = value * subject_number
    value = value % 20201227
    return value


def find_loop_size(public_key: int, subject_number: int) -> int:
    value = 1
    loop_size = 0
    while value != public_key:
        value = transform(value, subject_number)
        loop_size += 1
    return loop_size


def find_encryption_key(card_key: int,
                        door_key: int,
                        subject_number: int) -> int:
    card_loop_size = find_loop_size(card_key, subject_number)
    print(card_loop_size)
    value = 1
    for _ in range(card_loop_size):
        value = transform(value, subject_number=door_key)
    return value


def part1(filename: str) -> int:
    card_key, door_key = read_public_keys(filename)
    subject_number = 7
    encryption_key = find_encryption_key(card_key, door_key, subject_number)
    return encryption_key


if __name__ == '__main__':
    puzzle_input = 'input_day25.txt'
    print_results(elapsed_time(part1, puzzle_input))  # 3015200
