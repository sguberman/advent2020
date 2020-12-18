from collections import defaultdict
from itertools import product
from typing import Dict, Iterable, List, Tuple

from utils import elapsed_time, print_results

Point = Tuple[int, ...]
Direction = Tuple[int, ...]
Grid = Dict[Point, str]

ACTIVE = '#'
INACTIVE = '.'


def initialize_nd_grid(filename: str,
                       num_dimensions: int = 3) -> Tuple[Grid, List[Direction]]:
    grid = defaultdict(lambda: INACTIVE)
    extra_dimensions = (num_dimensions - 2) * (0,)
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, cube_state in enumerate(line.strip()):
                grid[(x, y) + extra_dimensions] = cube_state
    directions = make_directions(num_dimensions)
    expanded_grid = expand_initial_grid(grid, directions)
    return expanded_grid, directions


def make_directions(num_dimensions: int = 3) -> List[Point]:
    directions = list(product(*[(-1, 0, 1) for _ in range(num_dimensions)]))
    directions.remove(num_dimensions * (0,))
    return directions


def expand_initial_grid(grid: Grid, directions: List[Direction]) -> Grid:
    initial_points = list(grid.keys())
    for point in initial_points:
        # visit neighbors to expand the grid
        neighbor_states = list(grid[n]
                               for n in neighboring_points(directions, point))
    return grid


def neighboring_points(directions: List[Direction],
                       point: Point) -> Iterable[Point]:
    for direction in directions:
        yield tuple(sum(pair) for pair in zip(point, direction))


def count_active_neighbors(grid: Grid,
                           directions: List[Direction],
                           point: Point) -> int:
    # Grid will expand to include neighbors as they get checked
    return sum(grid[point] == ACTIVE
               for point in neighboring_points(directions, point))


def next_cube_state(grid: Grid,
                    directions: List[Direction],
                    point: Point) -> str:
    active_neighbors = count_active_neighbors(grid, directions, point)
    cube_state = grid[point]
    if active_neighbors == 3:
        return ACTIVE
    elif active_neighbors == 2 and cube_state == ACTIVE:
        return ACTIVE
    else:
        return INACTIVE


def simulate_cycle(grid: Grid,
                   directions: List[Direction]) -> Grid:
    points = list(grid.keys())
    next_grid = {point: next_cube_state(grid, directions, point)
                 for point in points}
    grid.update(next_grid)
    return grid


def count_active_cubes(grid: Grid) -> int:
    return sum(cube_state == ACTIVE for cube_state in grid.values())


def simulate(filename: str, num_dimensions: int, num_cycles: int) -> Grid:
    grid, directions = initialize_nd_grid(filename, num_dimensions)
    for _ in range(num_cycles):
        grid = simulate_cycle(grid, directions)
    return grid


def part1(filename: str) -> int:
    grid = simulate(filename, 3, 6)
    return count_active_cubes(grid)


def part2(filename: str) -> int:
    grid = simulate(filename, 4, 6)
    return count_active_cubes(grid)


if __name__ == '__main__':
    puzzle_input = 'input_day17.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 286
                  elapsed_time(part2, puzzle_input))  # 960
