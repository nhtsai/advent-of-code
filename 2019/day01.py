from pathlib import PurePath

def part1(l):
    return sum((m // 3) - 2 for m in l)

def part2(l):
    total = 0
    for m in l:
        while m > 5:
            m = (m // 3) - 2
            total += m
    return total

def test():
    l = [12, 14, 1969, 100756]
    assert part1(l) == sum([2, 2, 654, 33583])
    assert part2(l) == sum([2, 2, 966, 50346])

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = list(map(int, f.read().splitlines()))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
