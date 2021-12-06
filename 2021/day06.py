from pathlib import PurePath

def part1(l: list[int], days: int = 80) -> int:
    counts = [0 for _ in range(9)]
    for f in l:
        counts[f] += 1

    for day in range(days):
        temp = counts[0]
        # rotate array 1 left
        for i in range(len(counts) - 1):
            counts[i] = counts[i + 1]
        # reset existing to 6
        counts[6] += temp
        # add new to 8
        counts[8] = temp
    return sum(counts)


def part2(l: list[int]) -> int:
    return part1(l, 256)

def test() -> None:
    l = [3, 4, 3, 1, 2]
    assert part1(l, 18) == 26
    assert part1(l, 80) == 5934
    assert part2(l) == 26984457539

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = list(map(int, f.read().split(',')))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
