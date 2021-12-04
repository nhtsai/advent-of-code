from pathlib import PurePath

def part1(l):
    return sum(l[i-1] < l[i] for i in range(1, len(l)))

def part2(l):
    k = 3
    return sum(l[i-k] < l[i] for i in range(k, len(l)))

def test():
    l = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert part1(l) == 7
    assert part2(l) == 5


if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = list(map(int, f.read().splitlines()))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
