from collections import defaultdict, deque
from itertools import product
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


def count_neighbors(coordinate: Coordinate, tiles: Tiles) -> int:
    x, y, z = coordinate
    count = 0
    for dx, dy, dz in DELTAS.values():
        if tiles[(x + dx, y + dy, z + dz)]:
            count += 1
    return count


def next_state(coordinate: Coordinate, tiles: Tiles) -> bool:
    current_state = tiles[coordinate]  # False = white, True = black
    neighbors = count_neighbors(coordinate, tiles)
    if current_state and (neighbors == 0 or neighbors > 2):  # black tile
        return not current_state
    elif not current_state and neighbors == 2:  # white tile
        return not current_state
    else:
        return current_state


def next_day(tiles: Tiles) -> Tiles:
    next_tiles = defaultdict(bool)
    current_coordinates = list(tiles.keys())
    for coordinate in current_coordinates:
        next_tiles[coordinate] = next_state(coordinate, tiles)
    return next_tiles


def empty_grid(size: int) -> Tiles:
    grid = defaultdict(bool)
    xs = range(-size, size + 1)
    ys = range(-size, size + 1)
    zs = range(-size, size + 1)
    for coordinate in product(xs, ys, zs):
        grid[coordinate] = False
    return grid


def size(tiles: Tiles) -> int:
    maxx = max(abs(x) for x, y, z in tiles)
    maxy = max(abs(y) for x, y, z in tiles)
    maxz = max(abs(z) for x, y, z in tiles)
    return max(maxx, maxy, maxz)


def part1(filename: str) -> int:
    tiles = flip_tiles(filename)
    return sum(tiles.values())


def part2(filename: str) -> int:
    tiles = flip_tiles(filename)
    grid_size = size(tiles) + 1
    grid = empty_grid(grid_size)
    grid.update(tiles)
    for i in range(1, 101):
        next_grid = next_day(grid)
        if not i % 10:
            print(i, sum(next_grid.values()))
        grid_size += 1
        grid = empty_grid(grid_size)
        grid.update(next_grid)
    return sum(grid.values())


if __name__ == '__main__':
    puzzle_input = 'input_day24.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 293
                  elapsed_time(part2, puzzle_input))  # 3967
