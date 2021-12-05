from pathlib import PurePath

def part1(l: list[int]) -> int:
    covered = {}
    for vent in l:
        x1, y1, x2, y2 = [int(i) for i in vent.replace(' -> ', ',').split(',')]

        # horizontal
        if x1 == x2:
            r = range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1)
            for y in r:
                covered[(x1, y)] = covered.get((x1, y), 0) + 1

        # vertical
        elif y1 == y2:
            r = range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1)
            for x in r:
                covered[(x, y1)] = covered.get((x, y1), 0) + 1

    return sum(1 for c in covered.values() if c > 1)

def part2(l: list[int]) -> int:
    covered = {}
    for vent in l:
        x1, y1, x2, y2 = [int(i) for i in vent.replace(' -> ', ',').split(',')]
        # horizontal
        if x1 == x2:
            r = range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1)
            for y in r:
                covered[(x1, y)] = covered.get((x1, y), 0) + 1

        # vertical
        elif y1 == y2:
            r = range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1)
            for x in r:
                covered[(x, y1)] = covered.get((x, y1), 0) + 1

        # diagonal
        else:
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            x, y = x1, y1
            for _ in range(abs(x1 - x2) + 1):
                covered[(x, y)] = covered.get((x, y), 0) + 1
                x += dx
                y += dy
    return sum(1 for c in covered.values() if c > 1)

def test() -> None:
    l = [
        '0,9 -> 5,9', # horiz right
        '8,0 -> 0,8', # diagonal up left
        '9,4 -> 3,4', # horiz left
        '2,2 -> 2,1', # vert down
        '7,0 -> 7,4', # vert up
        '6,4 -> 2,0', # diagonal down left
        '0,9 -> 2,9', # horiz right
        '3,4 -> 1,4', # horiz left
        '0,0 -> 8,8', # diagonal up right
        '5,5 -> 8,2', # diagonal down right
    ]
    assert part1(l) == 5
    assert part2(l) == 12

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
