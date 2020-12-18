from collections import defaultdict

import pytest

from day17 import (count_active_cubes, count_active_neighbors,
                   initialize_nd_grid, make_directions, neighboring_points,
                   next_cube_state, part1, part2, simulate_cycle)

PUZZLE_INPUT = 'input_day17.txt'
TEST_INPUT = 'test_input_day17.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 112),
    (PUZZLE_INPUT, 286),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 848),
    (PUZZLE_INPUT, 960),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_initialize_nd_grid():
    grid, _ = initialize_nd_grid(TEST_INPUT)
    assert grid[(0, 0, 0)] == '.'
    assert grid[(1, 0, 0)] == '#'
    assert grid[(2, 0, 0)] == '.'
    assert grid[(0, 1, 0)] == '.'
    assert grid[(1, 1, 0)] == '.'
    assert grid[(2, 1, 0)] == '#'
    assert grid[(0, 2, 0)] == '#'
    assert grid[(1, 2, 0)] == '#'
    assert grid[(2, 2, 0)] == '#'
    assert grid[(-1, -1, -1)] == '.'


def test_neighboring_points():
    directions = make_directions(3)
    neighbors = list(neighboring_points(directions, (0, 0, 0)))
    assert len(neighbors) == 26
    assert (0, 0, 0) not in neighbors
    assert (1, 1, 1) in neighbors
    assert (-1, -1, -1) in neighbors
    assert (2, 0, 0) not in neighbors
    assert sum(x == 1 for x, y, z in neighbors) == 9
    assert sum(y == 1 for x, y, z in neighbors) == 9
    assert sum(z == 1 for x, y, z in neighbors) == 9
    assert sum(x == -1 for x, y, z in neighbors) == 9
    assert sum(y == -1 for x, y, z in neighbors) == 9
    assert sum(z == -1 for x, y, z in neighbors) == 9
    assert sum(x == 0 for x, y, z in neighbors) == 8
    assert sum(y == 0 for x, y, z in neighbors) == 8
    assert sum(z == 0 for x, y, z in neighbors) == 8


def test_count_active_cubes():
    grid, _ = initialize_nd_grid(TEST_INPUT)
    assert count_active_cubes(grid) == 5


def test_simulate_cycle():
    grid_0, directions = initialize_nd_grid(TEST_INPUT)
    #print("Before any cycles:\n")
    #print(print_grid(grid_0, 0))
    grid_1 = simulate_cycle(grid_0, directions)
    #print("\nAfter 1 cycle:\n")
    #print(print_grid(grid_1, -1))
    #print(print_grid(grid_1, 0))
    #print(print_grid(grid_1, 1))
    assert count_active_cubes(grid_1) == 11
    grid_2 = simulate_cycle(grid_1, directions)
    assert count_active_cubes(grid_2) == 21
    grid_3 = simulate_cycle(grid_2, directions)
    assert count_active_cubes(grid_3) == 38


def test_count_active_neighbors():
    grid, directions = initialize_nd_grid(TEST_INPUT)
    assert count_active_neighbors(grid, directions, (0, 0, 0)) == 1
    assert count_active_neighbors(grid, directions, (1, 0, 0)) == 1
    assert count_active_neighbors(grid, directions, (2, 0, 0)) == 2
    assert count_active_neighbors(grid, directions, (0, 1, 0)) == 3
    assert count_active_neighbors(grid, directions, (1, 1, 0)) == 5
    assert count_active_neighbors(grid, directions, (2, 1, 0)) == 3
    assert count_active_neighbors(grid, directions, (0, 2, 0)) == 1
    assert count_active_neighbors(grid, directions, (1, 2, 0)) == 3
    assert count_active_neighbors(grid, directions, (2, 2, 0)) == 2
