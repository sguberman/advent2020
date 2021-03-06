from typing import Tuple

from utils import elapsed_time, print_results


def part1(filename: str) -> int:
    x, y, facing = 0, 0, 0
    instructions = (line.strip() for line in open(filename))
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            facing = (facing + value) % 360
        elif action == 'R':
            facing = (facing - value) % 360
        else:  # forward
            if facing == 0:
                x += value
            elif facing == 90:
                y += value
            elif facing == 180:
                x -= value
            else:  # 270
                y -= value
    return abs(x) + abs(y)


def rotate(dx: int, dy: int, angle: int) -> Tuple[int, int]:
    if angle == 90 or angle == -270:
        return -dy, dx
    elif angle == 180 or angle == -180:
        return -dx, -dy
    elif angle == 270 or angle == -90:
        return dy, -dx


def part2(filename: str) -> int:
    x, y, dx, dy = 0, 0, 10, 1
    instructions = (line.strip() for line in open(filename))
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action == 'N':
            dy += value
        elif action == 'S':
            dy -= value
        elif action == 'E':
            dx += value
        elif action == 'W':
            dx -= value
        elif action == 'L':
            dx, dy = rotate(dx, dy, value)
        elif action == 'R':
            dx, dy = rotate(dx, dy, -value)
        else:  # forward
            x += value * dx
            y += value * dy
    return abs(x) + abs(y)


if __name__ == '__main__':
    puzzle_input = 'input_day12.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 882
                  elapsed_time(part2, puzzle_input))  # 28885
