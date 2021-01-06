from collections import defaultdict, deque
from typing import Dict, Iterator, Tuple

from utils import elapsed_time, print_results

Coordinate = Tuple[int, int, int]
Tiles = Dict[Coordinate, bool]

DELTAS = {  # hexagonal grid directions in cube coordinates
    'e':  (+1, -1, 0),
    'se': (0, -1, +1),
    'sw': (-1, 0, +1),
    'w':  (-1, +1, 0),
    'nw': (0, +1, -1),
    'ne': (+1, 0, -1),
}


def tiles_to_flip(filename: str) -> Iterator[str]:
    with open(filename) as f:
        for line in f:
            yield line.strip()


def parse_steps(line: str) -> Iterator[str]:
    steps = deque(line)
    while steps:
        next_step = steps.popleft()
        if next_step in 'ns':
            next_step += steps.popleft()
        yield next_step


def walk_steps(line: str, start: Coordinate = (0, 0, 0)) -> Coordinate:
    x, y, z = start
    for step in parse_steps(line):
        dx, dy, dz = DELTAS[step]
        x += dx
        y += dy
        z += dz
    return (x, y, z)


def flip_tiles(filename: str) -> Tiles:
    tiles: Tiles = defaultdict(bool)  # white = False, black = True
    for line in tiles_to_flip(filename):
        coordinate_to_flip = walk_steps(line)
        tiles[coordinate_to_flip] = not tiles[coordinate_to_flip]
    return tiles


def part1(filename: str) -> int:
    tiles = flip_tiles(filename)
    return sum(tiles.values())


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day24.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 293
                  elapsed_time(part2, puzzle_input))
