from math import prod
from time import time
from typing import List


def read_tree_map(filename: str) -> List[str]:
    return [line.strip() for line in open(filename)]


def count_trees_in_path(tree_map: List[str], dx: int, dy: int) -> int:
    width = len(tree_map[0])
    height = len(tree_map)
    x, y = 0, 0
    count = 0
    while True:
        x = (x + dx) % width
        y += dy
        if y >= height:
            break
        if tree_map[y][x] == '#':
            count += 1
    return count


def part1(filename: str) -> int:
    tree_map = read_tree_map(filename)
    return count_trees_in_path(tree_map, 3, 1)


def part2(filename: str) -> int:
    tree_map = read_tree_map(filename)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(count_trees_in_path(tree_map, dx, dy) for dx, dy in slopes)


if __name__ == '__main__':
    puzzle_input = 'input_day03.txt'

    part1_start = time()
    part1_answer = part1(puzzle_input)
    part1_time = time() - part1_start
    print(part1_answer, f"{part1_time:.6f}s")

    part2_start = time()
    part2_answer = part2(puzzle_input)
    part2_time = time() - part2_start
    print(part2_answer, f"{part2_time:.6f}s")
