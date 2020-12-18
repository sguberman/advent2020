from collections import defaultdict
from typing import Dict, Iterable, List, Tuple

from utils import elapsed_time, print_results

Point = Tuple[int, int, int]
Grid = Dict[Point, str]

ACTIVE = '#'
INACTIVE = '.'
DIRECTIONS = [
    (-1, -1,  1), (0, -1,  1), (1, -1,  1),
    (-1,  0,  1), (0,  0,  1), (1,  0,  1),
    (-1,  1,  1), (0,  1,  1), (1,  1,  1),

    (-1, -1,  0), (0, -1,  0), (1, -1,  0),
    (-1,  0,  0),              (1,  0,  0),
    (-1,  1,  0), (0,  1,  0), (1,  1,  0),

    (-1, -1, -1), (0, -1, -1), (1, -1, -1),
    (-1,  0, -1), (0,  0, -1), (1,  0, -1),
    (-1,  1, -1), (0,  1, -1), (1,  1, -1),
]


def initialize_grid(filename: str, at_z: int = 0) -> Grid:
    grid = defaultdict(lambda: INACTIVE)
    z = at_z
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, cube_state in enumerate(line.strip()):
                grid[(x, y, z)] = cube_state
    return grid


def neighboring_points(point: Point) -> Iterable[Point]:
    for direction in DIRECTIONS:
        yield tuple(sum(pair) for pair in zip(point, direction))


def count_active_neighbors(grid: Grid, point: Point) -> int:
    # Grid will expand to include neighbors as they get checked
    return sum(grid[point] == ACTIVE for point in neighboring_points(point))


def expand_initial_grid(grid: Grid) -> Grid:
    initial_points = list(grid.keys())
    for point in initial_points:
        # visit neighbors to expand the grid
        neighbor_states = list(grid[n] for n in neighboring_points(point))
    return grid


def next_cube_state(grid: Grid, point: Point) -> str:
    active_neighbors = count_active_neighbors(grid, point)
    cube_state = grid[point]
    if active_neighbors == 3:
        return ACTIVE
    elif active_neighbors == 2 and cube_state == ACTIVE:
        return ACTIVE
    else:
        return INACTIVE


def simulate_cycle(grid: Grid) -> Grid:
    points = list(grid.keys())
    next_grid = {point: next_cube_state(grid, point) for point in points}
    grid.update(next_grid)
    return grid


def count_active_cubes(grid: Grid) -> int:
    return sum(cube_state == ACTIVE for cube_state in grid.values())


def print_grid(grid: Grid, at_z: int) -> str:
    plane = [(x, y, z) for x, y, z in grid if z == at_z]
    min_x = min(plane, key=lambda p: p[0])[0]
    max_x = max(plane, key=lambda p: p[0])[0]
    min_y = min(plane, key=lambda p: p[1])[1]
    max_y = max(plane, key=lambda p: p[1])[1]
    lines = [[grid[(x, y, at_z)] for x in range(min_x, max_x + 1)]
             for y in range(min_y, max_y + 1)]
    header = f'z={at_z}'
    return '\n'.join([header] +
                     [''.join(line) for line in lines])


def part1(filename: str) -> int:
    grid = initialize_grid(filename)
    grid = expand_initial_grid(grid)
    for _ in range(6):
        grid = simulate_cycle(grid)
    return count_active_cubes(grid)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day17.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 286
                  elapsed_time(part2, puzzle_input))
