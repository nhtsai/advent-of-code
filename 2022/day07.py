# mypy: disable-error-code=valid-type
import io
from dataclasses import dataclass, field
from pathlib import PurePath
from typing import Final, Self


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Self | None = None
    children: dict[str, Self | File] = field(default_factory=dict)
    size: int = 0

    def __str__(self) -> str:
        return f"Directory({self.name=}, {self.size=})"


def parse_tree(lines: list[str]) -> Directory:
    """
    Time: O(N)
    Space: O(N)
    """
    base_dir = Directory(name="base")
    curr_dir = base_dir
    for line in lines:
        match line.split():
            case ["$", "cd", ".."]:
                if curr_dir.parent:
                    curr_dir = curr_dir.parent
            case ["$", "cd", next_dir_nm]:
                if next_dir_nm not in curr_dir.children:
                    curr_dir.children[next_dir_nm] = Directory(
                        name=next_dir_nm, parent=curr_dir
                    )
                next_dir = curr_dir.children.get(next_dir_nm)
                if isinstance(next_dir, Directory):
                    curr_dir = next_dir
            case ["$", "ls"]:
                continue
            case ["dir", dir_nm]:
                if dir_nm not in curr_dir.children:
                    curr_dir.children[dir_nm] = Directory(name=dir_nm, parent=curr_dir)
            case [file_size, file_nm]:
                curr_dir.children[file_nm] = File(name=file_nm, size=int(file_size))
                temp_dir = curr_dir
                while temp_dir != base_dir:
                    temp_dir.size += int(file_size)
                    if temp_dir.parent:
                        temp_dir = temp_dir.parent
    return base_dir


def print_tree(base: Directory | File, indent_level: int = 0) -> None:
    print(" " * 4 * indent_level + str(base))
    if isinstance(base, Directory):
        for child in base.children.values():
            print_tree(child, indent_level + 1)


def sum_dirs_under_maximum(base: Directory | File, max_size: int) -> int:
    """
    Time: O(N)
    Space: O(logN)
    """
    total_sum: int = 0
    if isinstance(base, Directory):
        for child in base.children.values():
            total_sum += sum_dirs_under_maximum(child, max_size)
        if base.size < max_size:
            total_sum += base.size
    return total_sum


def get_smallest_dir_over_minimum(
    base: Directory | File, curr: Directory, min_size: int
) -> Directory:
    """
    Time: O(N)
    Space: O(logN)
    """
    if isinstance(base, Directory):
        min_dir = min(base, curr, key=lambda d: d.size)
        for child in base.children.values():
            if isinstance(child, File) or child.size < min_size:
                continue
            min_child = get_smallest_dir_over_minimum(child, curr, min_size)
            min_dir = min(min_dir, min_child, key=lambda d: d.size)
        return min_dir
    else:
        return curr


def part1(lines: list[str]) -> int:
    """
    Time: O()
    Space: O()
    """
    base_dir = parse_tree(lines)
    # print_tree(base_dir, 0)
    return sum_dirs_under_maximum(base_dir, 100_000)


def part2(lines: list[str]) -> int:
    """
    Time: O()
    Space: O()
    """
    TOTAL_DISK_SPACE: Final[int] = 70_000_000
    UPDATE_DISK_SPACE: Final[int] = 30_000_000
    base_dir = parse_tree(lines)
    root_dir = base_dir.children.get("/")
    if isinstance(root_dir, Directory):
        DISK_SPACE_USED: Final[int] = root_dir.size
        DISK_SPACE_FREE: Final[int] = TOTAL_DISK_SPACE - DISK_SPACE_USED
        DISK_SPACE_NEEDED: Final[int] = UPDATE_DISK_SPACE - DISK_SPACE_FREE

        delete_dir = get_smallest_dir_over_minimum(
            root_dir, curr=root_dir, min_size=DISK_SPACE_NEEDED
        )
        return delete_dir.size
    return base_dir.size


def test() -> None:
    test_input = "\n".join(
        [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]
    )
    with io.StringIO(test_input) as fp:
        lines = fp.read().splitlines()
    assert part1(lines) == 95_437
    assert part2(lines) == 24_933_642


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
