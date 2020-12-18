from collections import defaultdict

import pytest

from day17 import (count_active_cubes, count_active_neighbors,
                   expand_initial_grid, initialize_grid, neighboring_points,
                   next_cube_state, part1, part2, print_grid, simulate_cycle)

PUZZLE_INPUT = 'input_day17.txt'
TEST_INPUT = 'test_input_day17.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 112),
    (PUZZLE_INPUT, 286),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.skip()
@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT, 0),
    #(PUZZLE_INPUT, 0),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_initialize_grid():
    grid = initialize_grid(TEST_INPUT)
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
    neighbors = list(neighboring_points((0, 0, 0)))
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
    grid = initialize_grid(TEST_INPUT)
    assert count_active_cubes(grid) == 5


def test_simulate_cycle():
    grid_0 = initialize_grid(TEST_INPUT)
    grid_0 = expand_initial_grid(grid_0)
    #print("Before any cycles:\n")
    #print(print_grid(grid_0, 0))
    grid_1 = simulate_cycle(grid_0)
    #print("\nAfter 1 cycle:\n")
    #print(print_grid(grid_1, -1))
    #print(print_grid(grid_1, 0))
    #print(print_grid(grid_1, 1))
    assert count_active_cubes(grid_1) == 11
    grid_2 = simulate_cycle(grid_1)
    assert count_active_cubes(grid_2) == 21
    grid_3 = simulate_cycle(grid_2)
    assert count_active_cubes(grid_3) == 38


def test_count_active_neighbors():
    grid = initialize_grid(TEST_INPUT)
    assert count_active_neighbors(grid, (0, 0, 0)) == 1
    assert count_active_neighbors(grid, (1, 0, 0)) == 1
    assert count_active_neighbors(grid, (2, 0, 0)) == 2
    assert count_active_neighbors(grid, (0, 1, 0)) == 3
    assert count_active_neighbors(grid, (1, 1, 0)) == 5
    assert count_active_neighbors(grid, (2, 1, 0)) == 3
    assert count_active_neighbors(grid, (0, 2, 0)) == 1
    assert count_active_neighbors(grid, (1, 2, 0)) == 3
    assert count_active_neighbors(grid, (2, 2, 0)) == 2


EXAMPLE_1_n1 = initialize_grid('test_input_day17_1_n1.txt', -1)
EXAMPLE_1_0 = initialize_grid('test_input_day17_1_0.txt', 0)
EXAMPLE_1_1 = initialize_grid('test_input_day17_1_1.txt', 1)

EXAMPLE_1 = EXAMPLE_1_n1 | EXAMPLE_1_0 | EXAMPLE_1_1


def test_example():
    for z in (-1, 0, 1):
        print(print_grid(EXAMPLE_1, z))
        print()
    assert count_active_cubes(EXAMPLE_1) == 11

    assert count_active_neighbors(EXAMPLE_1, (1, 1, 0)) == 10
    assert next_cube_state(EXAMPLE_1, (1, 1, 0)) == '.'

    assert count_active_neighbors(EXAMPLE_1, (0, 0, -1)) == 2
    assert next_cube_state(EXAMPLE_1, (0, 0, -1)) == '#'

    assert count_active_neighbors(EXAMPLE_1, (0, 2, -1)) == 3
    assert next_cube_state(EXAMPLE_1, (0, 2, -1)) == '#'
