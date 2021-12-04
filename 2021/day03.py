from pathlib import PurePath

def part1(l: list[str]) -> int:
    gamma = []
    for t in zip(*l):
        num_ones = t.count('1')
        num_zeros = len(t) - num_ones
        if num_ones > num_zeros:
            gamma.append('1')
        else:
            gamma.append('0')
    epsilon = ['0' if b == '1' else '1' for b in gamma]
    gamma = int('0b' + ''.join(gamma), 2)
    epsilon = int('0b' + ''.join(epsilon), 2)
    return gamma * epsilon

def part2(l: list[str]) -> int:
    oxy_valid = set(range(len(l)))
    co_valid = set(range(len(l)))
    for t in zip(*l):
        # calculate most common of valid oxy nums
        oxy_num_ones = sum(t[i] == '1' for i in oxy_valid)
        oxy_num_zeros = len(oxy_valid) - oxy_num_ones
        most_common = '1' if oxy_num_ones >= oxy_num_zeros else '0'

        # calculate least common of valid co nums
        co_num_ones = sum(t[i] == '1' for i in co_valid)
        co_num_zeros = len(co_valid) - co_num_ones
        least_common = '0' if co_num_zeros <= co_num_ones else '1'

        # print(f'OXY: {oxy_num_ones} ones + {oxy_num_zeros} zeros => {most_common}')
        # print(f'CO: {co_num_ones} ones + {co_num_zeros} zeros => {least_common}')

        # filter both oxy and co
        for i,b in enumerate(t):
            # if the bit is not most common, discard from oxy
            if b != most_common:
                if len(oxy_valid) > 1:
                    oxy_valid.discard(i)
            # if the bit is not least common, discard from co
            if b != least_common:
                if len(co_valid) > 1:
                    co_valid.discard(i)

        # print(f'OXY: {oxy_valid}')
        # print(f'CO: {co_valid}')

        if len(oxy_valid) == 1 and len(co_valid) == 1:
            break

    # convert valid bin string to decimal
    oxy_rating = int('0b' + l[oxy_valid.pop()], 2)
    co_rating = int('0b' + l[co_valid.pop()], 2)
    # print(oxy_rating, co_rating)
    return oxy_rating * co_rating

def test() -> None:
    l = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    assert part1(l) == 198
    assert part2(l) == 230

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
