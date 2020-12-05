def boarding_passes(filename):
    return (line.strip() for line in open(filename))


def seat_id(boarding_pass):
    return row(boarding_pass) * 8 + column(boarding_pass)


def partition(minn, maxx, halves):
    for half in halves:
        mid = minn + (maxx - minn) // 2
        if half in 'FL':
            maxx = mid
        else:
            minn = mid + 1
    return minn


def row(boarding_pass):
    halves = boarding_pass[:7]
    minn, maxx = 0, 127
    return partition(minn, maxx, halves)


def column(boarding_pass):
    halves = boarding_pass[-3:]
    minn, maxx = 0, 7
    return partition(minn, maxx, halves)


def part1(filename):
    return max(seat_id(bp) for bp in boarding_passes(filename))


def part2(filename):
    ids = [seat_id(bp) for bp in boarding_passes(filename)]
    return next(id for id in range(min(ids), max(ids) + 1) if id not in ids)


if __name__ == '__main__':
    puzzle_input = 'input_day05.txt'
    print(part1(puzzle_input))  # 994
    print(part2(puzzle_input))  # 741
