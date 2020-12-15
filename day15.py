from utils import elapsed_time, print_results


def part1(puzzle_input: str, nth_spoken: int = 2020) -> int:
    *starting_numbers, current_number = [int(x)
                                         for x in puzzle_input.split(',')]
    last_spoken_on_turn = {number: turn
                           for turn, number in enumerate(starting_numbers,
                                                         start=1)}
    for current_turn in range(len(starting_numbers) + 1, nth_spoken + 1):
        if current_number in last_spoken_on_turn:
            next_number = current_turn - last_spoken_on_turn[current_number]
        else:
            next_number = 0
        last_spoken_on_turn[current_number] = current_turn
        previous_number = current_number
        current_number = next_number
    return previous_number


def part2(puzzle_input: str) -> int:
    return part1(puzzle_input, 30000000)


if __name__ == '__main__':
    puzzle_input = '1,0,16,5,17,4'
    print_results(elapsed_time(part1, puzzle_input),  # 1294
                  elapsed_time(part2, puzzle_input))  # 573522
