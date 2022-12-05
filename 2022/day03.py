import io
from pathlib import PurePath


def calculate_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


def part1(lines: list[str]) -> int:
    """
    Time: O(N * K, K=line length)
    Space: O(K/2, K=line length)
    """
    item_sum = 0
    for line in lines:
        mid = len(line) // 2
        first = set()
        for i, item in enumerate(line):
            if i < mid:
                first.add(item)
            else:
                if item in first:
                    item_sum += calculate_priority(item)
                    break
    return item_sum


def part2(lines: list[str]) -> int:
    """
    Time: O(N * K, K=line_length)
    Space: O(K)
    """
    badge_sum = 0
    group: set[str] = set()
    for i, line in enumerate(lines):
        if i % 3 == 0:
            group = set(line)
        else:
            group.intersection_update(line)

        if i % 3 == 2:
            badge = group.pop()
            badge_sum += calculate_priority(badge)
    return badge_sum


def test() -> None:
    test_input = (
        "vJrwpWtwJgWrhcsFMMfFFhFp\n"
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n"
        "PmmdzqPrVvPwwTWBwg\n"
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n"
        "ttgJtRGJQctTZtZT\n"
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    )
    with io.StringIO(test_input) as fp:
        lines = fp.read().splitlines()
    assert 157 == part1(lines)
    assert 70 == part2(lines)


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
