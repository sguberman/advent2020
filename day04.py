def read_passports(filename):
    passport_entries = open(filename).read().split('\n\n')
    passports = []
    for passport_entry in passport_entries:
        passport = {}
        for field in passport_entry.split():
            key, value = field.split(':')
            passport[key] = value
        passports.append(passport)
    return passports


def is_valid(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport.keys() for field in fields)


def part1(filename: str) -> int:
    return sum(is_valid(passport) for passport in read_passports(filename))


def part2(filename: str) -> int:
    raise NotImplementedError


if __name__ == '__main__':
    puzzle_input = 'input_day04.txt'
    print(part1(puzzle_input))
    # print(part2(puzzle_input))
