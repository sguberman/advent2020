from itertools import combinations


def find_n_numbers_totaling(n, total, numbers):
    return next(group for group in combinations(numbers, n)
                if sum(group) == total)


def part1(inputfile):
    entries = (int(entry) for entry in open(inputfile))
    first, second = find_n_numbers_totaling(2, 2020, entries)
    return first * second


def part2(inputfile):
    entries = (int(entry) for entry in open(inputfile))
    first, second, third = find_n_numbers_totaling(3, 2020, entries)
    return first * second * third


if __name__ == '__main__':
    inputfile = 'input_day01.txt'
    print(part1(inputfile))  # 1016131
    print(part2(inputfile))  # 276432018
