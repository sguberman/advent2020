def part1(puzzle_input, dx, dy):
    tree_map = [line.strip() for line in open(puzzle_input)]
    width = len(tree_map[0])
    height = len(tree_map)
    x, y = 0, 0
    tree_count = 0
    while y < height:
        x = (x + dx) % width
        y += dy
        if y >= height:
            break
        if tree_map[y][x] == '#':
            tree_count += 1
    return tree_count


def part2(puzzle_input):
    result = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for dx, dy in slopes:
        result *= part1(puzzle_input, dx, dy)
    return result


if __name__ == '__main__':
    puzzle_input = 'input_day03.txt'
    print(part1(puzzle_input, 3, 1))
    print(part2(puzzle_input))
