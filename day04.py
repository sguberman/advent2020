from typing import Iterator

from utils import elapsed_time, print_results


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


def check_byr(passport: dict) -> bool:
    return check_yr(passport, 'byr', 1920, 2002)


def check_iyr(passport: dict) -> bool:
    return check_yr(passport, 'iyr', 2010, 2020)


def check_eyr(passport: dict) -> bool:
    return check_yr(passport, 'eyr', 2020, 2030)


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
    return len(pid) == 9 and pid.isdigit()


def is_valid(passport: dict) -> bool:
    checks = [check_fields, check_byr, check_iyr, check_eyr, check_hgt,
              check_hcl, check_ecl, check_pid]
    return all(check(passport) for check in checks)


def part1(filename: str) -> int:
    return sum(check_fields(passport) for passport in read_passports(filename))


def part2(filename: str) -> int:
    return sum(is_valid(passport) for passport in read_passports(filename))


if __name__ == '__main__':
    puzzle_input = 'input_day04.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
