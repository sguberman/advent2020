from itertools import count
from math import prod
from typing import List

from utils import elapsed_time, print_results


def read_tree_map(filename: str) -> List[str]:
    return [line.strip() for line in open(filename)]


def count_trees_in_path(tree_map: List[str], dx: int, dy: int) -> int:
    width = len(tree_map[0])
    height = len(tree_map)
    xs = (x % width for x in count(0, dx))
    ys = range(0, height, dy)
    return sum(tree_map[y][x] == '#' for x, y in zip(xs, ys))


def part1(filename: str) -> int:
    tree_map = read_tree_map(filename)
    return count_trees_in_path(tree_map, 3, 1)


def part2(filename: str) -> int:
    tree_map = read_tree_map(filename)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(count_trees_in_path(tree_map, dx, dy) for dx, dy in slopes)


if __name__ == '__main__':
    puzzle_input = 'input_day03.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
