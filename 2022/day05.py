import io
import re
from pathlib import PurePath


def parse_crate_diagram(lines: list[str], div: int) -> list[list[str]]:
    crate_stacks = list(zip(*lines[div - 2 :: -1]))[1::4]  # O(I + C)
    crates = [
        [item for item in crate if item != " "]  # O(I)
        for crate in crate_stacks  # O(C)
    ]
    return crates


def part1(lines: list[str]) -> str:
    """
    Time: O(I + I + C + (I * C) + (N * (S + M)) + C)
        - index of split
        - reverse diagram slice
        - crate stack slice
        - crates list comprehension
        - iterate moves: regex match, move crates
        - join top crates string
    Space: O(N + C + (I * C) + C)
        - reverse diagram slice
        - crate stack slice
        - crates list
        - top crates string
    Where:
        I = number of items per starting crate,
        C = number of crate stacks,
        N = number of move operations,
        S = length of move operation string,
        M = number of crates moved per operation,
    """
    div = lines.index("")  # O(I)
    crates = parse_crate_diagram(lines, div)  # O(I + C + I * C)
    move_regex = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    for i in range(div + 1, len(lines)):  # O(N)
        if matched := move_regex.match(lines[i]):  # O(S)
            m, start, end = map(int, matched.group(1, 2, 3))
        for _ in range(m):  # O(M)
            crates[end - 1].append(crates[start - 1].pop())

    return "".join(crate[-1] for crate in crates)  # O(C)


def part2(lines: list[str]) -> str:
    """
    Time: O(I + I + C + (I * C) + (N * (S + 2M)) + C)
        - index of split
        - reverse diagram slice
        - crate stack slice
        - crates list comprehension
        - iterate moves: regex match, move crates to temp stack, empty temp stack
        - join top crates string
    Space: O(N + C + (I * C) + M + C)
        - reverse diagram slice
        - crate stack slice
        - crates list
        - temp stack list
        - top crates string
    Where:
        I = number of items per starting crate,
        C = number of crate stacks,
        N = number of move operations,
        S = length of move operation string,
        M = number of crates moved per operation,
    """
    div = lines.index("")  # O(I)
    crates = parse_crate_diagram(lines, div)  # O(I + C + I * C)
    move_regex = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    temp_stack: list[str] = []
    for i in range(div + 1, len(lines)):  # O(N)
        if matched := move_regex.match(lines[i]):  # O(S)
            m, start, end = map(int, matched.group(1, 2, 3))
        for _ in range(m):  # O(M)
            temp_stack.append(crates[start - 1].pop())
        while temp_stack:  # O(M)
            crates[end - 1].append(temp_stack.pop())

    return "".join(crate[-1] for crate in crates)  # O(C)


def test() -> None:
    test_input = (
        "    [D]    \n"
        "[N] [C]    \n"
        "[Z] [M] [P]\n"
        " 1   2   3 \n"
        "\n"
        "move 1 from 2 to 1\n"
        "move 3 from 1 to 3\n"
        "move 2 from 2 to 1\n"
        "move 1 from 1 to 2"
    )
    with io.StringIO(test_input) as fp:
        lines = fp.read().splitlines()
    assert "CMZ" == part1(lines)
    assert "MCD" == part2(lines)


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
