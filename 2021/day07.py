from pathlib import PurePath

def part1(l: list[int]) -> int:
    counts = {}
    lowest, highest = float('inf'), float('-inf')
    for num in l:
        counts[num] = counts.get(num, 0) + 1
        lowest = min(lowest, num)
        highest = max(highest, num)
    best = -1
    best_cost = float('inf')
    for pos in range(lowest, highest + 1):
        # calculate cost given position
        cost = sum(abs(k - pos) * v for k,v in counts.items())
        if cost < best_cost:
            best_cost = cost
            best = pos
    return sum(abs(k - best) * v for k,v in counts.items())


def part2(l: list[int]) -> int:
    counts = {}
    lowest, highest = float('inf'), float('-inf')
    for num in l:
        counts[num] = counts.get(num, 0) + 1
        lowest = min(lowest, num)
        highest = max(highest, num)
    best = -1
    best_cost = float('inf')
    cache = {}
    for pos in range(lowest, highest + 1):
        # calculate cost given position
        cost = 0
        for k,v in counts.items():
            diff = abs(k - pos)
            if diff in cache:
                single_cost = cache[diff]
            else:
                single_cost = sum(range(diff + 1))
                cache[diff] = single_cost
            cost += single_cost * v

        if cost < best_cost:
            best_cost = cost
            best = pos

    return best_cost


def test() -> None:
    l = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert part1(l) == 37
    assert part2(l) == 168

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = list(map(int, f.read().split(',')))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
