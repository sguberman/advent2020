from collections import defaultdict
from functools import partial
from itertools import chain, filterfalse
from math import prod
from typing import Dict, Iterable, List, Optional, TextIO, Tuple

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
    _is_valid_value = partial(is_valid_value, rules)
    return filterfalse(_is_valid_value, chain.from_iterable(tickets))


def is_valid_value(rules: Rules, value: int) -> bool:
    all_ranges = chain.from_iterable(rules.values())
    return any(value in r for r in all_ranges)


def valid_tickets(rules: Rules, tickets: List[Ticket]) -> List[Ticket]:
    _is_valid_ticket = partial(is_valid_ticket, rules)
    return list(filter(_is_valid_ticket, tickets))


def is_valid_ticket(rules: Rules, ticket: Ticket) -> bool:
    _is_valid_value = partial(is_valid_value, rules)
    return all(_is_valid_value(value) for value in ticket)


def ticket_columns(tickets: List[Ticket]) -> List[List[int]]:
    return [[ticket[i] for ticket in tickets] for i in range(len(tickets[0]))]


def match_fields(rules: Rules,
                 tickets: List[Ticket]) -> Dict[str, List[int]]:
    columns = ticket_columns(tickets)
    matches = defaultdict(list)
    for field in rules.keys():
        for i, column in enumerate(columns):
            if all(value in chain.from_iterable(rules[field]) for value in column):
                matches[field].append(i)
    return matches


def eliminate_matches(matches: Dict[str, List[int]],
                      todo: Optional[List[str]] = None) -> Dict[str, List[int]]:
    if not todo:
        todo = list(matches.keys())
    else:
        todo = todo.copy()

    solved_fields = set()
    while todo:
        # Find a field that only matches one column
        solved_field = next(field
                            for field, matching_columns in matches.items()
                            if field not in solved_fields
                            and len(matching_columns) == 1)
        if not solved_field:
            break

        # Remove that column from the other fields
        matching_column = matches[solved_field][0]
        for field in matches:
            if field == solved_field:
                continue
            try:
                matches[field].remove(matching_column)
            except ValueError:
                pass

        # Track progress
        solved_fields.add(solved_field)
        try:
            todo.remove(solved_field)
        except ValueError:
            pass

    return matches


def part1(rules: Rules, nearby: List[Ticket]) -> int:
    return sum(invalid_values(rules, nearby))


def part2(rules: Rules, ticket: Ticket, nearby: List[Ticket]) -> int:
    tickets = valid_tickets(rules, nearby)
    todo = [field for field in rules if field.startswith('departure')]
    matched_fields = eliminate_matches(match_fields(rules, tickets), todo)
    return prod(ticket[columns[0]]
                for field, columns in matched_fields.items()
                if field in todo)


if __name__ == '__main__':
    puzzle_input = 'input_day16.txt'
    rules, ticket, nearby = parse_input(puzzle_input)
    print_results(elapsed_time(part1, rules, nearby),  # 29759
                  elapsed_time(part2, rules, ticket, nearby))  # 1307550234719
