from pathlib import PurePath
import pytest

def part1(l: list[int]) -> int:
    pass

def part2(l: list[int]) -> int:
    pass

def test() -> None:
    assert 1 == 1

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
