import re

def part1(l):
    memory = {}
    i = 0
    while i < len(l):
        # process group
        if 'mask' in l[i]:
            # get mask
            mask = l[i][7:]
        elif 'mem' in l[i]:
            # process memory operation
            m = re.match(r"mem\[([0-9]+)\] = ([0-9]+)$", l[i])
            address = int(m.group(1))
            value = int(m.group(2))
            # get binary string of value
            binary_str = format(value, 'b').zfill(len(mask))
            # get masked result
            result = ("").join([j if i == 'X' else i for i,j in zip(mask, binary_str)])
            # write result into memory
            memory[address] = int(result, 2)
        i += 1
    # return sum of values in memory
    return sum(memory.values())


def part2(l):
    idx = 0
    memory = {}
    while idx < len(l):
        # process group
        if 'mask' in l[idx]:
            # get mask
            mask = l[idx][7:]
        elif 'mem' in l[idx]:
            # process memory operation
            m = re.match(r"mem\[([0-9]+)\] = ([0-9]+)$", l[idx])
            # convert address to floating address
            address = int(m.group(1))
            binary_address_str = format(address, 'b').zfill(len(mask))
            address_result = ("").join(['X' if i == 'X' else '1' if i == '1' else j for i,j in zip(mask, binary_address_str)])
            # get all addresses
            n = address_result.count('X')
            address_result = address_result.replace('X', '%s')
            addresses = []
            for c in range(2**n):
                # get floating bit combination
                floating = tuple(list(str(bin(c))[2:].zfill(n)))
                # fill in combination in address
                address_str = address_result % floating
                # add address to list as a decimal
                addresses.append(int(address_str, 2))
            # write value into all addresses
            value = int(m.group(2))
            for a in addresses:
                memory[a] = value
        idx += 1
    # return sum of values in memory
    return sum(memory.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = [x.rstrip() for x in f.readlines()]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
