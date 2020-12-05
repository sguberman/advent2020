def read_seats(filename):
    return open(filename).read().splitlines()


def seat_id(seat):
    return row(seat) * 8 + column(seat)


def row(seat):
    parts = seat[:7]
    first, last = 0, 127
    for part in parts:
        half = first + (last - first) // 2
        if part == 'F':
            last = half
        elif part == 'B':
            first = half + 1
    return first


def column(seat):
    parts = seat[7:]
    first, last = 0, 7
    for part in parts:
        half = first + (last - first) // 2
        if part == 'L':
            last = half
        elif part == 'R':
            first = half + 1
    return first


def part1(filename):
    return seat_id(max(read_seats(filename), key=seat_id))


def part2(filename):
    ids = [seat_id(seat) for seat in read_seats(filename)]
    missing = [id for id in range(min(ids), max(ids) + 1) if id not in ids]
    return missing


if __name__ == '__main__':
    print(part1('input_day05.txt'))
    print(part2('input_day05.txt'))
