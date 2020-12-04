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


def check_byr(passport):
    try:
        byr = int(passport['byr'])
        return 1920 <= byr <= 2002
    except:
        return False


def check_iyr(passport):
    try:
        iyr = int(passport['iyr'])
        return 2010 <= iyr <= 2020
    except:
        return False


def check_eyr(passport):
    try:
        eyr = int(passport['eyr'])
        return 2020 <= eyr <= 2030
    except:
        return False


def check_hgt(passport):
    hgt = passport['hgt']
    h, unit = hgt[:-2], hgt[-2:]
    if unit == 'cm':
        try:
            h = int(h)
            return 150 <= h <= 193
        except:
            return False
    elif unit == 'in':
        try:
            h = int(h)
            return 59 <= h <= 76
        except:
            return False
    else:
        return False


def check_hcl(passport):
    hcl = passport['hcl']
    first, rest = hcl[0], hcl[1:]
    if first == '#':
        return all(c in '0123456789abcdef' for c in rest)
    else:
        return False


def check_ecl(passport):
    ecl = passport['ecl']
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def check_pid(passport):
    pid = passport['pid']
    if len(pid) == 9:
        try:
            pid = int(pid)
            return True
        except:
            return False
    else:
        return False


def is_valid2(passport):
    if not is_valid(passport):
        return False
    else:
        byr = check_byr(passport)
        iyr = check_iyr(passport)
        eyr = check_eyr(passport)
        hgt = check_hgt(passport)
        hcl = check_hcl(passport)
        ecl = check_ecl(passport)
        pid = check_pid(passport)
        return byr and iyr and eyr and hgt and hcl and ecl and pid


def part1(filename: str) -> int:
    return sum(is_valid(passport) for passport in read_passports(filename))


def part2(filename: str) -> int:
    return sum(is_valid2(passport) for passport in read_passports(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day04.txt'
    print(part1(puzzle_input))
    print(part2(puzzle_input))
