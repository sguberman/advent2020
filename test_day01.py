from day01 import find_n_numbers_totaling, part1, part2


def test_part1():
    assert part1('input_day01.txt') == 1016131


def test_part2():
    assert part2('input_day01.txt') == 276432018


def test_part1_example():
    assert part1('test_input_day01.txt') == 514579


def test_part2_example():
    assert part2('test_input_day01.txt') == 241861950


def test_find_2_numbers_totaling():
    example_list = [1721, 979, 366, 299, 675, 1456]
    assert find_n_numbers_totaling(2, 2020, example_list) == (1721, 299)


def test_find_3_numbers_totaling():
    example_list = [1721, 979, 366, 299, 675, 1456]
    assert find_n_numbers_totaling(3, 2020, example_list) == (979, 366, 675)
