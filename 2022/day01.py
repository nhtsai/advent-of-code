import heapq
import io
from pathlib import PurePath
from typing import Final


def part1(lines: list[str]) -> int:
    """
    Time: O(N)
    Space: O(1)
    """
    max_elf = -1
    curr_elf = 0
    for line in lines:
        if line:
            curr_elf += int(line)
        else:
            max_elf = max(max_elf, curr_elf)
            curr_elf = 0
    return max_elf


def part2(lines: list[str]) -> int:
    """
    Time: O(N*KlogK), K=3 => O(N)
    Space: O(K), K=3 => O(1)
    """
    K: Final[int] = 3
    minheap: list[int] = []
    curr_elf = 0
    for line in lines:
        if line:
            curr_elf += int(line)
        else:
            if len(minheap) < K:
                heapq.heappush(minheap, curr_elf)
            elif curr_elf > minheap[0]:
                heapq.heappushpop(minheap, curr_elf)
            curr_elf = 0
    return sum(minheap)


def test() -> None:
    test_input = "1000\n2000\n3000\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    with io.StringIO(test_input) as fp:
        lines = fp.read().splitlines()
    assert 24000 == part1(lines)
    assert 45000 == part2(lines)


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
