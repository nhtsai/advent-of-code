def part1(l):
    return sum([len(set([x for x in p.replace("\n", "")])) for p in l])

def part2(l):
    # yes = 0
    # for p in l:
    #     ppl = p.strip().count("\n") + 1
    #     for s in set(list(p.replace("\n", ""))):
    #         if p.count(s) == ppl:
    #             yes += 1
    # return yes
    return sum([sum([p.count(s) == p.strip().count("\n") + 1 for s in set(list(p.replace("\n", "")))]) for p in l])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = f.read().split("\n\n")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
