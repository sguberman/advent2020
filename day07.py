from typing import Dict, List, Tuple

from utils import elapsed_time, print_results

RuleDict = Dict[str, List[str]]

CONTAINS_CACHE: Dict[Tuple[str, str], bool] = {}


def read_rules(filename: str) -> RuleDict:
    rule_dict: RuleDict = {}
    with open(filename) as f:
        for line in f:
            lhs, rhs = line.strip().split(' contain ')
            outer = ' '.join(lhs.split()[:2])
            if rhs.startswith('no'):
                rule_dict[outer] = []
                continue
            inners = []
            for inner in rhs.split(', '):
                num, adj, color, _ = inner.split()
                inners.extend(int(num) * [f"{adj} {color}"])
            rule_dict[outer] = inners
    return rule_dict


def contains(rules: RuleDict, outer: str, inner: str) -> bool:
    if (outer, inner) in CONTAINS_CACHE:
        return CONTAINS_CACHE[(outer, inner)]
    else:
        children = rules[outer]
        if inner in children:
            CONTAINS_CACHE[(outer, inner)] = True
            return True
        else:
            for child in children:
                if contains(rules, child, inner):
                    CONTAINS_CACHE[(outer, inner)] = True
                    return True
            CONTAINS_CACHE[(outer, inner)] = False
            return False


def part1(filename: str) -> int:
    rules = read_rules(filename)
    return sum(contains(rules, bag, 'shiny gold') for bag in rules)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day07.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
