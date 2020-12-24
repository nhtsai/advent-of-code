from math import sin, cos, radians

def part1(l):
    current = [0., 0.]
    facing = 0.
    for (op, value) in l:
        if op == 'N':
            current[1] += value
        elif op == 'S':
            current[1] -= value
        elif op == 'E':
            current[0] += value
        elif op == 'W':
            current[0] -= value
        elif op == 'L':
            facing += value
        elif op == 'R':
            facing -= value
        elif op == 'F':
            current[0] += round(value * cos(radians(facing)), 4)
            current[1] += round(value * sin(radians(facing)), 4)

    return round(abs(current[0]) + abs(current[1]))


def part2(l):
    current = [0., 0.]
    waypoint = [10., 1.]
    for (op, value) in l:
        if op == 'N':
            waypoint[1] += value
        elif op == 'S':
            waypoint[1] -= value
        elif op == 'E':
            waypoint[0] += value
        elif op == 'W':
            waypoint[0] -= value
        elif op == 'L':
            waypoint = [cos(radians(value))*waypoint[0] - sin(radians(value))*waypoint[1],
                        sin(radians(value))*waypoint[0] + cos(radians(value))*waypoint[1]]
        elif op == 'R':
            waypoint = [cos(radians(-value))*waypoint[0] - sin(radians(-value))*waypoint[1],
                        sin(radians(-value))*waypoint[0] + cos(radians(-value))*waypoint[1]]
        elif op == 'F':
            current = [a + value*b for a,b in zip(current, waypoint)]

    return round(abs(current[0]) + abs(current[1]))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = [(x[0], int(x[1:])) for x in f.read().splitlines()]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
