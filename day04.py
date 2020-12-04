from typing import Iterator


def read_passports(filename: str) -> Iterator[dict]:
    for passport_text in open(filename).read().split('\n\n'):
        passport = {}
        for field in passport_text.split():
            key, value = field.split(':')
            passport[key] = value
        yield passport


def check_fields(passport: dict) -> bool:
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport.keys() for field in fields)


def check_yr(passport: dict, key: str, minn: int, maxx: int) -> bool:
    try:
        yr = int(passport[key])
        return minn <= yr <= maxx
    except:
        return False


def check_hgt(passport: dict) -> bool:
    hgt = passport['hgt']
    h, unit = hgt[:-2], hgt[-2:]
    try:
        h = int(h)
        if unit == 'cm':
            return 150 <= h <= 193
        elif unit == 'in':
            return 59 <= h <= 76
        else:
            return False
    except:
        return False


def check_hcl(passport: dict) -> bool:
    hcl = passport['hcl']
    first, rest = hcl[0], hcl[1:]
    return first == '#' and all(c in '0123456789abcdef' for c in rest)


def check_ecl(passport: dict) -> bool:
    ecl = passport['ecl']
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def check_pid(passport: dict) -> bool:
    pid = passport['pid']
    return len(pid) == 9 and pid.isnumeric()


def is_valid(passport: dict) -> bool:
    if not check_fields(passport):
        return False
    else:
        byr = check_yr(passport, 'byr', 1920, 2002)
        iyr = check_yr(passport, 'iyr', 2010, 2020)
        eyr = check_yr(passport, 'eyr', 2020, 2030)
        hgt = check_hgt(passport)
        hcl = check_hcl(passport)
        ecl = check_ecl(passport)
        pid = check_pid(passport)
        return byr and iyr and eyr and hgt and hcl and ecl and pid


def part1(filename: str) -> int:
    return sum(check_fields(passport) for passport in read_passports(filename))


def part2(filename: str) -> int:
    return sum(is_valid(passport) for passport in read_passports(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day04.txt'
    print(part1(puzzle_input))  # 242
    print(part2(puzzle_input))  # 186
