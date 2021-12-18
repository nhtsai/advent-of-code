from pathlib import PurePath
import pytest

def part1(l):
    pass

def part2(l):
    pass

if __name__ == '__main__':
    with open(f'input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = list(f.readlines())
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
