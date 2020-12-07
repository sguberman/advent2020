from typing import Dict, List, Tuple

from utils import elapsed_time, print_results

Rule = Tuple[str, List[str]]
RuleDict = Dict[str, List[str]]
ContainsCache = Dict[Tuple[str, str, str], bool]


def parse_rule(line: str) -> Rule:
    lhs, rhs = line.strip().split(' contain ')
    adj, color, _ = lhs.split()
    outer_bag = f"{adj} {color}"
    inner_bags = []
    if not rhs.startswith('no'):
        for inner_bag in rhs.split(', '):
            num, adj, color, _ = inner_bag.split()
            inner_bags.extend(int(num) * [f"{adj} {color}"])
    return outer_bag, inner_bags


def read_rules(filename: str) -> RuleDict:
    return dict(parse_rule(line) for line in open(filename))


def does_contain(target_bag: str,
                 outer_bag: str,
                 filename: str,
                 rules: RuleDict,
                 cache: ContainsCache = {}) -> bool:
    if (filename, outer_bag, target_bag) in cache:
        return cache[(filename, outer_bag, target_bag)]
    else:
        for inner_bag in rules[outer_bag]:
            if inner_bag == target_bag:
                cache[(filename, outer_bag, target_bag)] = True
                return True
            elif does_contain(target_bag, inner_bag, filename, rules, cache):
                cache[(filename, outer_bag, target_bag)] = True
                return True
        cache[(filename, outer_bag, target_bag)] = False
        return False


def number_contained(bag: str, rules: RuleDict) -> int:
    children = rules[bag]
    return (len(children) +
            sum(number_contained(child, rules) for child in children))


def part1(filename: str) -> int:
    rules = read_rules(filename)
    return sum(does_contain('shiny gold', bag, filename, rules) for bag in rules)


def part2(filename: str) -> int:
    rules = read_rules(filename)
    return number_contained('shiny gold', rules)


if __name__ == '__main__':
    puzzle_input = 'input_day07.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 126
                  elapsed_time(part2, puzzle_input))  # 220149
