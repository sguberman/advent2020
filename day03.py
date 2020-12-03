def part1(puzzle_input):
    tree_map = [line.strip() for line in open(puzzle_input)]
    width = len(tree_map[0])
    height = len(tree_map)
    x, y = 0, 0
    dx, dy = 3, 1
    tree_count = 0
    while y < height:
        x = (x + dx) % width
        y += dy
        if y >= height:
            break
        if tree_map[y][x] == '#':
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    puzzle_input = 'input_day03.txt'
    print(part1(puzzle_input))
