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


def anyone_answers(group):
    answers = set()
    for individual_answers in group:
        answers.update(individual_answers)
    return answers


def everyone_answers(group):
    individual_answers = [set(x) for x in group]
    return individual_answers[0].intersection(*individual_answers[1:])


def part1(filename):
    return sum(len(anyone_answers(group)) for group in read_groups(filename))


def part2(filename):
    return sum(len(everyone_answers(group)) for group in read_groups(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day06.txt'
    print(part1(puzzle_input))
    print(part2(puzzle_input))
