from collections import defaultdict

def part1(l):
    s = sorted(l)
    s = [0] + s + [s[-1] + 3]
    diffs = defaultdict(int)
    for i, j in zip(s[:-1], s[1:]):
        diffs[j - i] += 1
    return diffs[1] * diffs[3]


def part2(l):
    s = sorted(l)
    s = [0] + s + [s[-1] + 3]
    counts = defaultdict(int, {0: 1})
    for i in s[1:]:
        # number of ways to get to adapter i =
        # all the ways to get to adapters (i - 3), (i - 2), (i - 1) then to adapter i
        counts[i] = counts[i - 3] + counts[i - 2] + counts[i - 1]
    return counts[s[-1]]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(map(int, f.readlines()))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
