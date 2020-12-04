from functools import reduce
from operator import mul

def part1(l):
    c = 0
    t = 0
    r = 0
    while r < (len(l) - 1):
        c = (c + 3) % len(l[r])
        r += 1
        if l[r][c] == '#':
            t += 1
    return t

def part2(l):

    def trees(right, down):
        c = 0
        t = 0
        r = 0
        while r < (len(l) - down):
            c = (c + right) % len(l[r])
            r += down
            if l[r][c] == '#':
                t += 1
        return t

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ans = [trees(*x) for x in slopes]
    return reduce(mul, ans)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(map(str.strip, f.readlines()))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))


