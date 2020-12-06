def read_groups(filename):
    with open(filename) as f:
        group = []
        for line in f:
            if line == '\n':
                yield group
                group = []
            else:
                group.append(line.strip())
        yield group


def group_answers(group):
    answers = set()
    for individual_answers in group:
        answers.update(individual_answers)
    return answers


def part1(filename):
    return sum(len(group_answers(group)) for group in read_groups(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day06.txt'
    print(part1(puzzle_input))
