def part1(l):
    # get start time
    start = int(l[0])
    # get running bus numbers
    buses = [int(x) for x in l[1].replace(',x', '').split(',')]
    # get waittimes for each bus
    waittimes = [x - (start % x) for x in buses]
    m = min(waittimes)
    # return the wait time * next bus number
    return m * buses[waittimes.index(m)]

def part2(l):
    # get all bus numbers, replacing x with 0
    all_buses = [int(x) if x != 'x' else 0 for x in l[1].split(',')]
    # get running bus numbers
    buses = [x for x in all_buses if x != 0]
    # get target arrival intervals for each bus
    targets = [all_buses.index(x) for x in buses]
    t, step = 0, 1
    for bus, target in zip(buses, targets):
        # keep stepping while t is invalid for current bus
        while ((t + target) % bus) != 0:
            t += step
        # increase step size by the bus number
        step *= bus
    return t


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(x.strip() for x in f.readlines())
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
