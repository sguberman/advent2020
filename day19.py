import re
from typing import Dict, List, Tuple

from utils import elapsed_time, print_results

RuleDict = Dict[str, str]


def read_input(filename: str) -> Tuple[List[str], List[str]]:
    rules: List[str] = []
    messages: List[str] = []
    with open(filename) as f:
        section = rules
        for line in f:
            if line == '\n':
                section = messages
                continue
            section.append(line.strip())
    return rules, messages


def parse_rule(rule: str) -> Tuple[str, str]:
    lhs, rhs = rule.split(': ')
    return lhs, rhs.strip('"')


def parse_rules(rules: List[str]) -> RuleDict:
    return dict(parse_rule(rule) for rule in rules)


def replace_rules(rules: RuleDict) -> RuleDict:
    to_replace = set(key for key, value in rules.items() if value in 'ab')
    solved = set(key for key in to_replace)
    while to_replace:
        replacing = to_replace.pop()
        replacing_re = re.compile(r"\b" + replacing + r"\b")
        replace_with = f"({rules[replacing]})"
        for key, value in rules.items():
            if key not in solved:
                new_value = replacing_re.sub(replace_with, value)
                rules[key] = new_value
                if all(x not in '0123456789' for x in new_value):
                    to_replace.add(key)
                    solved.add(key)
    return rules


def part1(filename: str) -> int:
    rule_strs, messages = read_input(filename)
    replaced_rules = replace_rules(parse_rules(rule_strs))
    rule_0 = re.compile(replaced_rules['0'].replace(' ', ''))
    return sum(bool(rule_0.fullmatch(m)) for m in messages)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day19.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 102
                  elapsed_time(part2, puzzle_input))
