from typing import List, Mapping, Tuple, Union

from utils import elapsed_time, print_results

RuleDict = Mapping[int, List[Union[List[int], str]]]


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


def parse_rules(rule_strs: List[str]) -> RuleDict:
    rules: RuleDict = {}
    for rule_str in rule_strs:
        rule_num, rule_txt = rule_str.split(': ')
        try:
            sublists = rule_txt.split(' | ')
            rule = [[int(subrule) for subrule in sublist.split()]
                    for sublist in sublists]
        except ValueError:
            rule = [rule_txt.strip('"')]
        rules[int(rule_num)] = rule
    return rules


def count_matches(rule: List[str], messages: List[str]) -> int:
    return sum(message in rule for message in messages)


def process_rule_dict(rules: RuleDict) -> Mapping[int, List[str]]:
    pass


def resolve_rule(rules: RuleDict, n: int) -> List:
    rule = rules[n]
    while any(isinstance(elem, int) for option in rule for elem in option):
        new_rule = []
        for option in rule:
            new_option = []
            for elem in option:
                if isinstance(elem, int):
                    new_option.append(rules[elem])
                else:
                    new_option.append(elem)
            new_rule.append(new_option)
        rule = new_rule
    return rule


def resolve_rule(rules: RuleDict, n: int) -> List:
    if item := rules[n][0] in 'ab':
        return item
    else:
        return [[resolve_rule(rules, x) for x in option] for option in rules[n]]


def part1(filename: str) -> int:
    rule_strs, messages = read_input(filename)
    rules = process_rule_dict(parse_rules(rule_strs))
    return count_matches(rules[0], messages)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'test_input_day19.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
