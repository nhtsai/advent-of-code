from pathlib import PurePath
import pytest

def part1(l: str) -> int:
    # parse hex string into bit string
    readNibble = lambda c: bin(int(c, 16))[2:].zfill(4)
    buf = ''.join([readNibble(c) for c in l])
    vers = []
    debug = False

    def read_packet(buf: str, ptr: int, ignore_padding: bool = False) -> int:
        """Reads a packet at the given index of pointer in buffer.
        Recursively reads subpackets if packet is operator type.
        Returns new pointer index.
        """
        nonlocal vers
        nonlocal debug

        if debug and ptr == 0:
            print(f'Packet: {buf}')

        # read version (3 bits)
        ver = int(buf[ptr:ptr + 3], 2)
        ptr += 3
        vers.append(ver)
        if debug: print(f'\tVersion: {ver}')

        # read packet type (3 bits)
        pkt_type = int(buf[ptr:ptr + 3], 2)
        ptr += 3
        if debug: print(f'\tPacket Type: {pkt_type}')

        # literal packet
        if pkt_type == 4:
            pkt_nums = []
            # while next bit is 1:
            while buf[ptr] == '1':
                ptr += 1
                # read 4 bits to build a num int str
                # num = int(buf[ptr:ptr + 4], 2)
                num = buf[ptr:ptr + 4]
                ptr += 4
                pkt_nums.append(num)

            # next bit is 0, consume it
            ptr += 1

            # read 4 bits to get last number
            # num = int(buf[ptr:ptr + 4], 2)
            num = buf[ptr:ptr + 4]
            ptr += 4

            pkt_nums.append(num)

            # skip padding bits
            if not ignore_padding:
                ptr += (4 - (ptr % 4))

            combined_num = int(''.join(pkt_nums), 2)

            if debug: print(f'\tLiteral Packet: {pkt_nums} -> {combined_num}')

        # operator packet
        else:
            # read length type ID (1 bit)
            len_type = int(buf[ptr], 2)
            ptr += 1

            if debug: print(f'\tOperator Packet with length type {len_type}')

            if len_type == 0:
                # read total bit length (15 bits)
                total_len = int(buf[ptr:ptr + 15], 2)
                ptr += 15

                if debug: print(f'\t\tThere are {total_len} subpacket bits.')

                # read subpackets
                start_bits = ptr
                ptr = read_packet(buf, ptr, ignore_padding=True) # do
                while (ptr - start_bits) < total_len: # while
                    ptr = read_packet(buf, ptr, ignore_padding=True)


            elif len_type == 1:
                # read num subpackets (11 bits)
                num_subpkts = int(buf[ptr:ptr + 11], 2)
                ptr += 11

                if debug: print(f'\t\tThere are {num_subpkts} subpackets.')

                # read subpackets
                for _ in range(num_subpkts):
                    ptr = read_packet(buf, ptr, ignore_padding=True)
        return ptr

    ptr = read_packet(buf, 0)
    if debug: print(f'{ptr} of {len(buf)} bits read')
    return sum(vers)

def part2(l: str) -> int:
    # parse hex string into bit string
    readNibble = lambda c: bin(int(c, 16))[2:].zfill(4)
    buf = ''.join([readNibble(c) for c in l])
    ptr = 0
    vers = []
    debug = False

    def read_packet(ignore_padding: bool = False) -> int:
        """Reads a packet at the given index of pointer in buffer.
        Recursively reads subpackets if packet is operator type.
        Returns new pointer index.
        """
        nonlocal vers
        nonlocal debug
        nonlocal ptr
        nonlocal buf

        if debug and ptr == 0:
            print(f'Packet: {buf}')

        # read version (3 bits)
        ver = int(buf[ptr:ptr + 3], 2)
        ptr += 3
        vers.append(ver)
        if debug: print(f'\tVersion: {ver}')

        # read packet type (3 bits)
        pkt_type = int(buf[ptr:ptr + 3], 2)
        ptr += 3
        if debug: print(f'\tPacket Type: {pkt_type}')

        # literal packet
        if pkt_type == 4:
            pkt_nums = []
            # while next bit is 1:
            while buf[ptr] == '1':
                ptr += 1
                # read 4 bits to build a num int str
                # num = int(buf[ptr:ptr + 4], 2)
                num = buf[ptr:ptr + 4]
                ptr += 4
                pkt_nums.append(num)

            # next bit is 0, consume it
            ptr += 1

            # read 4 bits to get last number
            # num = int(buf[ptr:ptr + 4], 2)
            num = buf[ptr:ptr + 4]
            ptr += 4

            pkt_nums.append(num)

            # skip padding bits
            if not ignore_padding:
                ptr += (4 - (ptr % 4))

            combined_num = int(''.join(pkt_nums), 2)

            if debug: print(f'\tLiteral Packet: {pkt_nums} -> {combined_num}')

            return combined_num

        # operator packet
        else:
            # read length type ID (1 bit)
            len_type = int(buf[ptr], 2)
            ptr += 1

            if debug: print(f'\tOperator Packet with length type {len_type}')

            values = []

            if len_type == 0:
                # read total bit length (15 bits)
                total_len =  int(buf[ptr:ptr + 15], 2)
                ptr += 15

                if debug: print(f'\t\tThere are {total_len} subpacket bits.')

                # read subpackets
                start_bits = ptr
                num = read_packet(ignore_padding=True) # do
                values.append(num)
                while (ptr - start_bits) < total_len: # while
                    num = read_packet(ignore_padding=True)
                    values.append(num)

            elif len_type == 1:
                # read num subpackets (11 bits)
                num_subpkts = int(buf[ptr:ptr + 11], 2)
                ptr += 11

                if debug: print(f'\t\tThere are {num_subpkts} subpackets.')

                # read subpackets
                for _ in range(num_subpkts):
                    num = read_packet(ignore_padding=True)
                    values.append(num)

            match pkt_type:
                # sum
                case 0:
                    return sum(values)
                # product
                case 1:
                    prod = 1
                    for v in values:
                        prod *= v
                    return prod
                # min
                case 2:
                    return min(values)
                # max
                case 3:
                    return max(values)
                # greater than
                case 5:
                    return int(values[0] > values[1])
                # less than
                case 6:
                    return int(values[0] < values[1])
                # equal
                case 7:
                    return int(values[0] == values[1])

    result = read_packet()
    if debug:
        print(f'Result: {result}')
        print(f'{ptr} of {len(buf)} bits read')
    return result

"""
Addition: C200B40A82
1100 0010 0000 0000 1011 0100 0000 1010 1000 0010
110 000 1 00000000010 110 100 0 0001 010 100 0 0010
ver typ l num_sub = 2 ver typ   num  ver typ   num



Less than: D8005AC2A8F0
5 < 15

0101    1111
1101 1000 0000 0000 0101 1010 1100 0010 1010 1000 1111 0000
110 110 0 000000000010110 101 100 0 0101 010 100 0 1111 0000
ver typ l bit_len = 22    ver typ   num  ver typ   num
"""


@pytest.fixture
def literal1() -> str:
    return 'D2FE28'

@pytest.fixture
def operator1() -> str:
    return '38006F45291200'

@pytest.fixture
def operator2() -> str:
    return 'EE00D40C823060'

@pytest.fixture
def example1() -> str:
    return '8A004A801A8002F478'

@pytest.fixture
def example2() -> str:
    return '620080001611562C8802118E34'

@pytest.fixture
def example3() -> str:
    return 'C0015000016115A2E0802F182340'

@pytest.fixture
def example4() -> str:
    return 'A0016C880162017C3686B18A3D4780'

def test_part1_literal(literal1) -> None:
    assert part1(literal1) == 6

def test_part1_operator(operator1, operator2) -> None:
    assert part1(operator1) == 1 + 6 + 2
    assert part1(operator2) == 7 + 2 + 4 + 1

def test_part1(example1, example2, example3, example4) -> None:
    assert part1(example1) == 16
    assert part1(example2) == 12
    assert part1(example3) == 23
    assert part1(example4) == 31

def test_part2_sum() -> None:
    assert part2('C200B40A82') == 3

def test_part2_product() -> None:
    assert part2('04005AC33890') == 54

def test_part2_minimum() -> None:
    assert part2('880086C3E88112') == 7

def test_part2_maximum() -> None:
    assert part2('CE00C43D881120') == 9

def test_part2_less_than() -> None:
    assert part2('D8005AC2A8F0') == 1

def test_part2_greater_than() -> None:
    assert part2('F600BC2D8F') == 0

def test_part2_equal() -> None:
    assert part2('9C005AC2F8F0') == 0

def test_part2() -> None:
    assert part2('9C0141080250320F1802104A08') == 1

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().rstrip()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
