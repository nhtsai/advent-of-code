def part1(l):
    valid = 0
    for p in l:
        a, b = p.split(': ')
        char = a[-1]
        a = list(map(int, a[:-1].split('-')))
        low, hi = a[0], a[1]
        if char not in b: 
            continue
        count = 0
        for c in b:
            if char == c:
                count += 1
        if count >= low and count <= hi:
            valid += 1
    return valid

def part2(l):
    valid = 0
    for p in l:
        a, b = p.split(': ')
        char = a[-1]
        a = list(map(int, a[:-1].split('-')))
        c1 = b[a[0] - 1]
        c2 = b[a[1] - 1]
        if (c1 == char) ^ (c2 == char):
            valid += 1
    return valid

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(f.readlines())
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
