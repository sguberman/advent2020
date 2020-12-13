from itertools import count
from typing import List, Tuple

from utils import elapsed_time, print_results


def parse_input(filename: str) -> Tuple[int, List[int]]:
    with open(filename) as f:
        earliest_departure = int(f.readline())
        buses_in_service = [int(x)
                            for x in f.readline().split(',') if x != 'x']
    return earliest_departure, buses_in_service


def next_bus(departure_time: int,
             buses_in_service: List[int]) -> Tuple[int, int]:
    for time in count(departure_time):
        for bus in buses_in_service:
            if not time % bus:
                return time, bus


def part1(filename: str) -> int:
    earliest_departure, buses_in_service = parse_input(filename)
    departure_time, bus = next_bus(earliest_departure, buses_in_service)
    return bus * (departure_time - earliest_departure)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day13.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
