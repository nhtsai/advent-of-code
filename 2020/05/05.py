NUM_ROWS = 128
NUM_COLS = 8

"""
Cool solution:
    https://github.com/tymofij/advent-of-code-2020/blob/master/05/seats.py

Cool solution using str.translate:
    def seat_id(s, t=str.maketrans("FBLR", "0101")):
        return int(s.translate(t), 2)

    def max_seat_id(boarding_passes):
        return max(map(seat_id, boarding_passes))

    def missing_seat(boarding_passes, t=str.maketrans("FBLR", "0101")):
        return max(set(range(920)) - set(int(s.translate(t), 2) for s in boarding_passes))
"""


def part1(l):
    highest_id = -1
    for p in l:
        row = -1
        col = -1
        r_lo = c_lo = 0
        r_hi = NUM_ROWS - 1
        c_hi = NUM_COLS - 1

        for s in p:
            r_mid = r_lo + (r_hi - r_lo) // 2
            c_mid = c_lo + (c_hi - c_lo) // 2

            if s == 'F':
                r_hi = r_mid
            elif s == 'B':
                r_lo = r_mid + 1
            elif s == 'R':
                c_lo = c_mid + 1
            elif s == 'L':
                c_hi = c_mid
            else:
                return -1

        assert r_hi == r_lo
        assert c_hi == c_lo

        row, col = r_hi, c_hi
        seat_id = row * 8 + col
        if seat_id > highest_id:
            highest_id = seat_id
    return highest_id


def part2(l):
    seats = []
    for p in l:
        row = -1
        col = -1
        r_lo = c_lo = 0
        r_hi = NUM_ROWS - 1
        c_hi = NUM_COLS - 1

        for s in p:
            r_mid = r_lo + (r_hi - r_lo) // 2
            c_mid = c_lo + (c_hi - c_lo) // 2

            if s == 'F':
                r_hi = r_mid
            elif s == 'B':
                r_lo = r_mid + 1
            elif s == 'R':
                c_lo = c_mid + 1
            elif s == 'L':
                c_hi = c_mid
            else:
                return -1

        assert r_hi == r_lo
        assert c_hi == c_lo

        row, col = r_hi, c_hi
        seat_id = row * 8 + col
        seats.append(seat_id)

    # all_seats = [r * 8 + c for r in range(NUM_ROWS) for c in range(NUM_COLS)]
    # missing = [x for x in all_seats if x not in seats]
    # my_seat = [x for x in missing if x - 1 not in missing and x + 1 not in missing][0]
    my_seat = [s for s in range(min(seats), max(seats) + 1) if s not in seats][0]
    return my_seat


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = [x.strip().upper() for x in f]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
