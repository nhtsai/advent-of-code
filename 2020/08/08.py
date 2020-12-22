def part1(l):
    visited = set()
    acc = 0
    i = 0
    while i < len(l):
        if i in visited:
            return (acc, False)
        visited.add(i)

        op = l[i][:3]
        value = int(l[i][4:])
        if op == 'acc':
            acc += value
        elif op == 'jmp':
            i += value
            continue
        i += 1
    return (acc, True)


def part2(l):
    for i, line in enumerate(l):
        op = line[:3]
        value = int(line[4:])
        if op == 'nop' or op == 'jmp':
            new_op = 'jmp' if op == 'nop' else 'nop'
            new_line = "{} {}".format(new_op, str(value))
            new_l = l[:i] + [new_line] + l[i+1:]
            acc, valid = part1(new_l)
            if valid:
                return acc
    return 0

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(f.readlines())
    print("Part 1:", part1(l)[0])
    print("Part 2:", part2(l))
