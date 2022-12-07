from pathlib import PurePath

import pytest


def get_start_packet_index(line: str, marker_len: int) -> int:
    """
    Time: O(N)
    Space: O(M)
    Where:
        N = signal line length
        M = marker length
    """
    seen: dict[str, int] = {}
    for i, end in enumerate(line, start=1):
        seen[end] = seen.get(end, 0) + 1
        if i < marker_len:
            continue
        if len(seen) == marker_len:
            return i
        start = line[i - marker_len]
        seen[start] -= 1
        if seen[start] == 0:
            del seen[start]
    return 0


def part1(line: str) -> int:
    return get_start_packet_index(line, marker_len=4)


def part2(line: str) -> int:
    return get_start_packet_index(line, marker_len=14)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part1(test_input: str, expected: int) -> None:
    assert part1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_part2(test_input: str, expected: int) -> None:
    assert part2(test_input) == expected


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
