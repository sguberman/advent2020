def read_tree_map(filename):
    return [line.strip() for line in open(filename)]


def count_trees_in_path(tree_map, dx, dy):
    width = len(tree_map[0])
    height = len(tree_map)
    x, y = 0, 0
    count = 0
    while True:
        x = (x + dx) % width
        y += dy
        if y >= height:
            break
        if tree_map[y][x] == '#':
            count += 1
    return count


def part1(puzzle_input):
    tree_map = read_tree_map(puzzle_input)
    return count_trees_in_path(tree_map, 3, 1)


def part2(puzzle_input):
    tree_map = read_tree_map(puzzle_input)
    result = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for dx, dy in slopes:
        result *= count_trees_in_path(tree_map, dx, dy)
    return result


if __name__ == '__main__':
    puzzle_input = 'input_day03.txt'
    print(part1(puzzle_input))
    print(part2(puzzle_input))
