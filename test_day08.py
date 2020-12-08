import pytest

from day08 import (acc, execute_instruction, jmp, nop, parse_line, part1,
                   part2, read_program, run_program_until_loop, swap_ops)

PUZZLE_INPUT = 'input_day08.txt'
TEST_INPUT_LOOPS = 'test_input_day08_loops.txt'
TEST_INPUT_TERMINATES = 'test_input_day08_terminates.txt'
EXAMPLE_LOOPS = [
    (nop, 0),
    (acc, 1),
    (jmp, 4),
    (acc, 3),
    (jmp, -3),
    (acc, -99),
    (acc, 1),
    (jmp, -4),
    (acc, 6),
]

EXAMPLE_TERMINATES = [
    (nop, 0),
    (acc, 1),
    (jmp, 4),
    (acc, 3),
    (jmp, -3),
    (acc, -99),
    (acc, 1),
    (nop, -4),
    (acc, 6),
]


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT_LOOPS, 5),
    (PUZZLE_INPUT, 1782),
])
def test_part1(puzzle_input, answer):
    assert part1(puzzle_input) == answer


@pytest.mark.parametrize('puzzle_input, answer', [
    (TEST_INPUT_LOOPS, 8),
    (PUZZLE_INPUT, 797),
])
def test_part2(puzzle_input, answer):
    assert part2(puzzle_input) == answer


def test_part2_no_solution(monkeypatch):
    def mock_swap_ops(program, orig_op, new_op):
        return [program]

    monkeypatch.setattr('day08.swap_ops', mock_swap_ops)
    assert part2(TEST_INPUT_LOOPS) == None


def test_read_program():
    assert read_program(TEST_INPUT_LOOPS) == EXAMPLE_LOOPS


@pytest.mark.parametrize('line, expected', [
    ('nop +0', (nop, 0)),
    ('acc +1', (acc, 1)),
    ('jmp +4', (jmp, 4)),
    ('acc +3', (acc, 3)),
    ('jmp -3', (jmp, -3)),
    ('acc -99', (acc, -99)),
    ('acc +1', (acc, 1)),
    ('jmp -4', (jmp, -4)),
    ('acc +6', (acc, 6)),
])
def test_parse_line(line, expected):
    assert parse_line(line) == expected


@pytest.mark.parametrize('instruction, expected', zip(
    EXAMPLE_LOOPS, (
        (1, 0),  # (step, acc) after calling instruction
        (1, 1),
        (4, 0),
        (1, 3),
        (-3, 0),
        (1, -99),
        (1, 1),
        (-4, 0),
        (1, 6),
    )
))
def test_execute_instruction(instruction, expected):
    step, acc = 0, 0  # all cases use the same starting state (0, 0)
    assert execute_instruction(instruction, step, acc) == expected


@pytest.mark.parametrize('program, expected', [
    (EXAMPLE_LOOPS, (1, 5, -1)),        # halting step, acc, and exit code
    (EXAMPLE_TERMINATES, (9, 8, 0)),
])
def test_run_program_until_loop(program, expected):
    assert run_program_until_loop(program) == expected


def test_swap_ops():
    assert EXAMPLE_TERMINATES in swap_ops(EXAMPLE_LOOPS, jmp, nop)
