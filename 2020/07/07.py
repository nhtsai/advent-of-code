import re
from collections import defaultdict

def part1(l, query="shiny gold"):

    def build_dict(l):
        get_outer = re.compile(r"([\w ]+)(?:bag|bags) contain")
        get_inner = re.compile(r" [\d ]+([\w ]+)(?:bag|bags)")
        contained = defaultdict(list)
        for p in l:
            outer = [x.strip() for x in get_outer.findall(p)][0]
            inner = [x.strip() for x in get_inner.findall(p)]
            for b in inner:
                contained[b].append(outer)
        return contained

    def get_containers(query, contained):
        ans = set()
        stack = contained[query]
        while stack:
            current = stack.pop()
            ans.add(current)
            stack = stack + contained[current]
        return ans

    contained = build_dict(l)
    bags = get_containers(query, contained)
    return len(bags)


def part2(l, query="shiny gold"):

    def build_dict(l):
        get_outer = re.compile(r"([\w ]+)(?:bag|bags) contain")
        get_inner = re.compile(r" ([\d ]+)([\w ]+)(?:bag|bags)")
        contains = defaultdict(list)
        for p in l:
            outer = [x.strip() for x in get_outer.findall(p)][0]
            inner = [(y.strip(), int(x.strip())) for (x,y) in get_inner.findall(p)]
            for b in inner:
                contains[outer].append(b)
        return contains

    def get_contained(query, contains):
        q = contains[query]
        if not q:
            return 0
        total = 0
        for (k,v) in q:
            total += v + v*get_contained(k, contains)
        return total
    
    contains = build_dict(l)
    return get_contained(query, contains)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(f.readlines())
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
