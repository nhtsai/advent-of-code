import io
from pathlib import PurePath


def part1(lines: list[str]) -> int:
    """
    Time: O(N)
    Space: O(1)
    """
    count = 0
    for line in lines:
        a, b, c, d = map(int, line.replace(",", "-", 1).split("-"))
        if (a <= c and d <= b) or (c <= a and b <= d):
            count += 1
    return count


def part2(lines: list[str]) -> int:
    """
    Time: O(N)
    Space: O(1)
    """
    count = 0
    for line in lines:
        a, b, c, d = map(int, line.replace(",", "-", 1).split("-"))
        if a <= d and c <= b:
            count += 1
    return count


def test() -> None:
    test_input = "2-4,6-8\n" "2-3,4-5\n" "5-7,7-9\n" "2-8,3-7\n" "6-6,4-6\n" "2-6,4-8\n"
    with io.StringIO(test_input) as fp:
        lines = fp.read().splitlines()
    assert 2 == part1(lines)
    assert 4 == part2(lines)


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
