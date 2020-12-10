from collections import Counter
from itertools import combinations
from typing import Dict, Iterable, List

from utils import elapsed_time, print_results


def connected_adapters(filename: str) -> List[int]:
    return sorted(int(line) for line in open(filename))


def joltage_differences(joltages: List[int]) -> Iterable[int]:
    return (b - a for a, b in zip(joltages, joltages[1:]))


def build_connection_graph(adapters: List[int]) -> Dict[int, List[int]]:
    neighbors = {}
    for adapter in adapters:
        potential_neighbors = [adapter + x for x in (1, 2, 3)]
        neighbors[adapter] = [n for n in potential_neighbors if n in adapters]
    return neighbors


def count_paths(neighbors_graph: Dict[int, List[int]]) -> Dict[int, int]:
    paths = {0: 1}
    for adapter, neighbors in neighbors_graph.items():
        for neighbor in neighbors:
            if neighbor in paths:
                paths[neighbor] += paths[adapter]
            else:
                paths[neighbor] = paths[adapter]
    return paths


def part1(filename: str) -> int:
    adapters = connected_adapters(filename)
    outlet = 0
    device = max(adapters) + 3
    joltages = [outlet] + adapters + [device]
    differences = Counter(joltage_differences(joltages))
    return differences[1] * differences[3]


def part2(filename: str) -> int:
    adapters = connected_adapters(filename)
    outlet = 0
    device = max(adapters) + 3
    joltages = [outlet] + adapters + [device]
    neighbors = build_connection_graph(joltages)
    num_paths = count_paths(neighbors)
    return num_paths[device]


if __name__ == '__main__':
    puzzle_input = 'input_day10.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
