from pathlib import PurePath

def part1(l: list[str]) -> int:
    horiz, depth = 0, 0
    for step in l:
        d, n = step.split()
        n = int(n)
        match d:
            case 'forward':
                horiz += n
            case 'down':
                depth += n
            case 'up':
                depth -= n
    return horiz * depth

def part2(l: list[int]) -> int:
    horiz, depth, aim = 0, 0, 0
    for step in l:
        d, n = step.split()
        n = int(n)
        match d:
            case 'forward':
                horiz += n
                depth += aim * n
            case 'down':
                aim += n
            case 'up':
                aim -= n
    return horiz * depth

def test() -> None:
    l = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    assert part1(l) == 150
    assert part2(l) == 900

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
