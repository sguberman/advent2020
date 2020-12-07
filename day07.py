from typing import Dict, List, Tuple

from utils import elapsed_time, print_results

RuleDict = Dict[str, List[str]]
ContainsCache = Dict[Tuple[str, str, str], bool]


def read_rules(filename: str) -> RuleDict:
    rules: RuleDict = {}
    with open(filename) as f:
        for line in f:
            lhs, rhs = line.strip().split(' contain ')
            adj, color, _ = lhs.split()
            outer_bag = f"{adj} {color}"
            if rhs.startswith('no'):
                rules[outer_bag] = []
            else:
                inner_bags = []
                for inner_bag in rhs.split(', '):
                    num, adj, color, _ = inner_bag.split()
                    inner_bags.extend(int(num) * [f"{adj} {color}"])
                rules[outer_bag] = inner_bags
    return rules


def does_contain(outer_bag: str,
                 target_bag: str,
                 filename: str,
                 rules: RuleDict,
                 cache: ContainsCache = {}) -> bool:
    if (filename, outer_bag, target_bag) in cache:
        return cache[(filename, outer_bag, target_bag)]
    else:
        inner_bags = rules[outer_bag]
        if target_bag in inner_bags:
            cache[(filename, outer_bag, target_bag)] = True
            return True
        else:
            for inner_bag in inner_bags:
                if does_contain(inner_bag, target_bag, filename, rules, cache):
                    cache[(filename, outer_bag, target_bag)] = True
                    return True
            cache[(filename, outer_bag, target_bag)] = False
            return False


def number_contained(rules: RuleDict, bag: str) -> int:
    children = rules[bag]
    return (len(children) +
            sum(number_contained(rules, child) for child in children))


def part1(filename: str) -> int:
    rules = read_rules(filename)
    return sum(does_contain(bag, 'shiny gold', filename, rules) for bag in rules)


def part2(filename: str) -> int:
    rules = read_rules(filename)
    return number_contained(rules, 'shiny gold')


if __name__ == '__main__':
    puzzle_input = 'input_day07.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 126
                  elapsed_time(part2, puzzle_input))  # 220149
