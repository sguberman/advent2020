import pytest

from day04 import (check_ecl, check_fields, check_hcl, check_hgt, check_pid,
                   check_yr, is_valid, part1, part2, read_passports)

PUZZLE_INPUT = 'input_day04.txt'
TEST_INPUT = 'test_input_day04.txt'
EXAMPLE1 = [
    dict(ecl="gry", pid="860033327", eyr="2020", hcl="#fffffd", byr="1937",
         iyr="2017", cid="147", hgt="183cm"),
    dict(iyr="2013", ecl="amb", cid="350", eyr="2023", pid="028048884",
         hcl="#cfa07d", byr="1929"),
    dict(hcl="#ae17e1", iyr="2013", eyr="2024", ecl="brn", pid="760753108",
         byr="1931", hgt="179cm"),
    dict(hcl="#cfa07d", eyr="2025", pid="166559648", iyr="2011", ecl="brn",
         hgt="59in")
]
INVALID_PASSPORTS = 'test_input_day04_invalid.txt'
VALID_PASSPORTS = 'test_input_day04_valid.txt'


@pytest.mark.parametrize('puzzle_input, answer', [
    (PUZZLE_INPUT, 242),
    (TEST_INPUT, 2),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


def test_read_passports():
    assert list(read_passports(TEST_INPUT)) == EXAMPLE1


@pytest.mark.parametrize('passport, expected',
                         zip(EXAMPLE1, (True, False, True, False)))
def test_check_fields(passport, expected):
    assert check_fields(passport) == expected


@pytest.mark.parametrize('puzzle_input, answer', [
    (PUZZLE_INPUT, 186),
    (INVALID_PASSPORTS, 0),
    (VALID_PASSPORTS, 3),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


@pytest.mark.parametrize('passport, expected', [
    ({'byr': '2002'}, True),
    ({'byr': '2003'}, False),
    ({'byr': 'blah'}, False),
])
def test_check_yr(passport, expected):
    assert check_yr(passport, 'byr', 1920, 2002) == expected


@pytest.mark.parametrize('passport, expected', [
    ({'hgt': '60in'}, True),
    ({'hgt': '190cm'}, True),
    ({'hgt': '190in'}, False),
    ({'hgt': '190'}, False),
])
def test_check_hgt(passport, expected):
    assert check_hgt(passport) == expected


@pytest.mark.parametrize('passport, expected', [
    ({'hcl': '#123abc'}, True),
    ({'hcl': '#123abz'}, False),
    ({'hcl': '123abc'}, False),
])
def test_check_hcl(passport, expected):
    assert check_hcl(passport) == expected


@pytest.mark.parametrize('passport, expected', [
    ({'ecl': 'brn'}, True),
    ({'ecl': 'wat'}, False),
])
def test_check_ecl(passport, expected):
    assert check_ecl(passport) == expected


@pytest.mark.parametrize('passport, expected', [
    ({'pid': '000000001'}, True),
    ({'pid': '0123456789'}, False),
])
def test_check_pid(passport, expected):
    assert check_pid(passport) == expected
