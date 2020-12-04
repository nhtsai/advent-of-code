def part1(l):
    for a in l:
        b = 2020 - a
        if b in l and a != b:
            return a * b

def part2(l):
    for a in l:
        for b in l:
            c = 2020 - a - b
            if c in l and a != b and a != c and b != c:
                return a * b * c

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(map(int, f.readlines()))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
