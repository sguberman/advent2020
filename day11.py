from typing import List, Tuple

from utils import elapsed_time, print_results

State = List[str]

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = [
    (-1, -1), (-1,  0), (-1,  1),
    (0,  -1),           (0,   1),
    (1,  -1), (1,   0), (1,   1),
]


def read_seats(filename: str) -> State:
    return open(filename).read().splitlines()


def count_neighbors(i: int, j: int, state: State) -> int:
    count = 0
    for (ns, ew) in DIRECTIONS:
        row, col = i + ns, j + ew
        if (0 <= row < len(state)) and (0 <= col < len(state[0])):
            neighbor = state[i + ns][j + ew]
            if neighbor == OCCUPIED:
                count += 1
    return count


def next_seat(seat: str, i: int, j: int, state: State) -> str:
    if seat == FLOOR:
        return FLOOR
    elif (seat == EMPTY) and (count_neighbors(i, j, state) == 0):
        return OCCUPIED
    elif (seat == OCCUPIED) and (count_neighbors(i, j, state) >= 4):
        return EMPTY
    else:
        return seat


def simulate_one_round(state: State) -> Tuple[State, State]:
    next_state: State = []
    for i, row in enumerate(state):
        next_row = ''
        for j, seat in enumerate(row):
            next_row += next_seat(seat, i, j, state)
        next_state.append(next_row)
    return state, next_state


def simulate_to_end(state: State) -> State:
    before, after = simulate_one_round(state)
    while before != after:
        before, after = simulate_one_round(after)
    return after


def count_occupied_seats(state: State) -> int:
    return sum(sum(seat == OCCUPIED for seat in row) for row in state)


def part1(filename: str) -> int:
    initial_state = read_seats(filename)
    final_state = simulate_to_end(initial_state)
    return count_occupied_seats(final_state)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day11.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 2441
                  elapsed_time(part2, puzzle_input))
