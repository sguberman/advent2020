from functools import partial
from itertools import chain, filterfalse
from typing import Dict, Iterable, List, TextIO, Tuple

from utils import elapsed_time, print_results

Rules = Dict[str, List[range]]
Ticket = List[int]


def parse_input(filename: str) -> Tuple[Rules, Ticket, List[Ticket]]:
    with open(filename) as f:
        rules = read_rules(f)
        ticket = read_ticket(f)
        nearby = read_nearby(f)
    return rules, ticket, nearby


def read_rules(file_handle: TextIO) -> Rules:
    rules = {}
    while line := file_handle.readline().strip():
        field, ranges = parse_rule(line)
        rules[field] = ranges
    return rules


def parse_rule(line: str) -> Tuple[str, List[range]]:
    field, rhs = line.split(': ')
    ranges = [parse_range(r) for r in rhs.split(' or ')]
    return field, ranges


def parse_range(range_str: str) -> range:
    start, stop = map(int, range_str.split('-'))
    return range(start, stop + 1)


def read_ticket(file_handle: TextIO) -> Ticket:
    _ = file_handle.readline()
    return parse_ticket(file_handle.readline())


def parse_ticket(line: str) -> Ticket:
    return [int(x) for x in line.split(',')]


def read_nearby(file_handle: TextIO) -> List[Ticket]:
    _ = file_handle.readline()
    _ = file_handle.readline()
    return [parse_ticket(line) for line in file_handle]


def invalid_values(rules: Rules, tickets: List[Ticket]) -> Iterable[int]:
    _is_valid = partial(is_valid, rules)
    return filterfalse(_is_valid, chain.from_iterable(tickets))


def is_valid(rules: Rules, value: int) -> bool:
    all_ranges = chain.from_iterable(rules.values())
    return any(value in r for r in all_ranges)


def part1(rules: Rules, nearby: List[Ticket]) -> int:
    return sum(invalid_values(rules, nearby))


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day16.txt'
    rules, ticket, nearby = parse_input(puzzle_input)
    print_results(elapsed_time(part1, rules, nearby),  # 29759
                  elapsed_time(part2, puzzle_input))
