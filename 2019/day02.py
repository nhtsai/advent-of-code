from pathlib import PurePath

def part1(l: list[int]) -> int:
    l = l.copy()
    i = 0
    while i < len(l):
        match l[i]:
            case 1:
                l[l[i + 3]] = l[l[i + 1]] + l[l[i + 2]]
                i += 3
            case 2:
                l[l[i + 3]] = l[l[i + 1]] * l[l[i + 2]]
                i += 3
            case 99:
                break
        i += 1
    return l[0]

def part2(l: list[int]) -> int:
    ans = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            curr = l.copy()
            curr[1] = noun
            curr[2] = verb
            try:
                result = part1(curr)
            except IndexError:
                continue
            else:
                # ++noun -> result + 345600
                # ++verb -> result + 1
                if ans - result > 99:
                    break
                if result == ans:
                    return 100 * noun + verb
    return -1

def test() -> None:
    assert part1([1,9,10,3,2,3,11,0,99,30,40,50]) == 3500

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = list(map(int, f.read().split(',')))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
