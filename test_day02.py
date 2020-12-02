from day02 import is_valid_positions, is_valid_times, parse_line, part1, part2

PUZZLE_INPUT = 'input_day02.txt'
TEST_INPUT = 'test_input_day02.txt'


def test_parse_line():
    assert parse_line('1-3 a: abcde') == ((1, 3), 'a', 'abcde')
    assert parse_line('1-3 b: cdefg') == ((1, 3), 'b', 'cdefg')
    assert parse_line('2-9 c: ccccccccc') == ((2, 9), 'c', 'ccccccccc')


def test_is_valid_times():
    assert is_valid_times((1, 3), 'a', 'abcde') == True
    assert is_valid_times((1, 3), 'b', 'cdefg') == False
    assert is_valid_times((2, 9), 'c', 'ccccccccc') == True


def test_is_valid_positions():
    assert is_valid_positions((1, 3), 'a', 'abcde') == True
    assert is_valid_positions((1, 3), 'b', 'cdefg') == False
    assert is_valid_positions((2, 9), 'c', 'ccccccccc') == False


def test_part1():
    assert part1(TEST_INPUT) == 2
    assert part1(PUZZLE_INPUT) == 454


def test_part2():
    assert part2(TEST_INPUT) == 1
    assert part2(PUZZLE_INPUT) == 649
