from day01 import find_n_numbers_totaling, part1, part2


PUZZLE_INPUT = 'input_day01.txt'
TEST_INPUT = 'test_input_day01.txt'
EXAMPLE = [1721, 979, 366, 299, 675, 1456]

def test_part1():
    assert part1(PUZZLE_INPUT) == 1016131


def test_part2():
    assert part2(PUZZLE_INPUT) == 276432018


def test_part1_example():
    assert part1(TEST_INPUT) == 514579


def test_part2_example():
    assert part2(TEST_INPUT) == 241861950


def test_find_2_numbers_totaling():
    assert find_n_numbers_totaling(2, 2020, EXAMPLE) == (1721, 299)


def test_find_3_numbers_totaling():
    assert find_n_numbers_totaling(3, 2020, EXAMPLE) == (979, 366, 675)
