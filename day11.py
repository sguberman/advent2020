import time
from functools import partial
from typing import Callable, Iterator, List, Tuple

from utils import elapsed_time, print_results

State = List[List[str]]
CountFn = Callable[[int, int, State], int]

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = [
    (-1, -1), (-1,  0), (-1,  1),
    (0,  -1),           (0,   1),
    (1,  -1), (1,   0), (1,   1),
]


def read_seats(filename: str) -> State:
    return [[x for x in line.strip()] for line in open(filename)]


def in_bounds(row: int, col: int, state: State) -> bool:
    return (0 <= row < len(state)) and (0 <= col < len(state[0]))


def look(i: int,
         j: int,
         state: State,
         direction: Tuple[int, int]) -> Iterator[str]:
    ns, ew = direction
    row, col = i + ns, j + ew
    while in_bounds(row, col, state):
        spot = state[row][col]
        yield spot
        if spot in (EMPTY, OCCUPIED):  # can't see past first seat
            break
        row += ns
        col += ew


def count_adjacent_neighbors(i: int, j: int, state: State) -> int:
    return sum(next(look(i, j, state, direction), None) == OCCUPIED
               for direction in DIRECTIONS)


def count_visible_neighbors(i: int, j: int, state: State) -> int:
    return sum(OCCUPIED in look(i, j, state, direction)
               for direction in DIRECTIONS)


def new_seat(i: int,
             j: int,
             state: State,
             max_neighbors: int,
             count_fn: CountFn) -> str:
    seat = state[i][j]
    if seat == FLOOR:
        return FLOOR
    elif (seat == EMPTY) and (count_fn(i, j, state) == 0):
        return OCCUPIED
    elif (seat == OCCUPIED) and (count_fn(i, j, state) >= max_neighbors):
        return EMPTY
    else:
        return seat


def simulate_one_round(state: State,
                       max_neighbors: int,
                       count_fn: CountFn) -> Tuple[State, State]:
    _new_seat = partial(new_seat, state=state,
                        max_neighbors=max_neighbors, count_fn=count_fn)
    rows = range(len(state))
    cols = range(len(state[0]))
    new_state = [[_new_seat(i, j) for j in cols] for i in rows]
    return state, new_state


def simulate_to_end(state: State,
                    max_neighbors: int,
                    count_fn: CountFn) -> State:
    before, after = simulate_one_round(state, max_neighbors, count_fn)
    while before != after:
        start = time.perf_counter()
        before, after = simulate_one_round(after, max_neighbors, count_fn)
        end = time.perf_counter()
        print(f"{end - start:.6f}")
    return after


def count_occupied_seats(state: State) -> int:
    return sum(sum(seat == OCCUPIED for seat in row) for row in state)


def part1(filename: str) -> int:
    initial_state = read_seats(filename)
    final_state = simulate_to_end(initial_state, 4, count_adjacent_neighbors)
    return count_occupied_seats(final_state)


def part2(filename: str) -> int:
    initial_state = read_seats(filename)
    final_state = simulate_to_end(initial_state, 5, count_visible_neighbors)
    return count_occupied_seats(final_state)


if __name__ == '__main__':
    puzzle_input = 'input_day11.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 2441
                  elapsed_time(part2, puzzle_input))  # 2190
