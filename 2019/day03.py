from pathlib import PurePath

def manhattan_dist(p1: tuple[int], p2: tuple[int]) -> int:
    return sum(abs(a-b) for a,b in zip(p1, p2))

def part1(l):
    l = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
    wire1 = l[0].split(',')
    wire2 = l[1].split(',')
    curr_x = 0
    curr_y = 0
    for step in wire1:
        print(curr_x, curr_y)
        d = step[0]
        n = int(step[1:])
        match d:
            case 'R':
                curr_x += n
            case 'L':
                curr_x -= n
            case 'U':
                curr_y += n
            case 'D':
                curr_y -= n
        print(d, n)

def part2(l):
    pass

def test():
    assert manhattan_dist((0, 0), (3, 3)) == 6

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
