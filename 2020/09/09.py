def part1(l):
    window = 25
    current = l[:window]
    for i in l[window:]:
        found = False
        # twosum
        for j in range(len(current)):
            complement = i - current[j]
            if complement in current:
                found = True
                break
        if not found:
            return i
        current = current[1:] + [i]

def part2(l):
    n = part1(l)
    # starting from 0, make a continuous range
    start = 0
    end = start + 2
    while True:
        r = l[start:end]
        # if the list is smaller, then continue adding 
        if sum(r) < n:
            end += 1
        # if the list is larger, then move up the window and restart
        elif sum(r) > n:
            start += 1
            end = start + 2
        # if the list is equal, then return min + max
        else:
            return min(r) + max(r)
    return -1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(map(int, f.readlines()))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
