from pathlib import PurePath
from collections import defaultdict
import pytest

def part1(l: list[str]) -> int:
    # build graph
    graph = defaultdict(list)
    for i in l:
        (a, b) = i.split('-')
        graph[a].append(b)
        graph[b].append(a)

    def dfs(visited: set[str], all_paths: list[list[str]], curr_path: list[str], cave: str) -> None:

        # invalid case
        if cave.islower() and cave in visited:
            return

        # visit
        if cave.islower():
            visited.add(cave)
        curr_path.append(cave)

        # success case
        if cave == 'end':
            all_paths.append(curr_path.copy())
            curr_path.pop()
            visited.remove('end')
            return

        # dfs
        for n in graph[cave]:
            dfs(visited, all_paths, curr_path, n)

        # backtrack
        visited.discard(cave)
        curr_path.pop()

    visited = set()
    all_paths = []
    # dfs + backtracking
    dfs(visited, all_paths, [], 'start')
    return len(all_paths)


def part2(l: list[str]) -> int:
    # build graph
    graph = defaultdict(list)
    for i in l:
        (a, b) = i.split('-')
        graph[a].append(b)
        if b != 'end':
            graph[b].append(a)

    def dfs(visited: dict[str, int], all_paths: list[list[str]], curr_path: list[str], cave: str) -> None:

        # invalid cases:
        # - cave is 'start' and we already started
        # - a cave was already visited twice and we are trying
        #   to visit another cave twice or this is the cave
        #   we already visited twice
        if (cave == 'start' and curr_path) or \
           (2 in visited.values() and visited[cave] >= 1):
            return

        # success case: reached the end
        if cave == 'end':
            all_paths.append(curr_path + [cave])
            return

        # visit
        curr_path.append(cave)
        # record small cave visits
        if cave.islower():
            visited[cave] += 1

        for n in graph[cave]:
            # consider paths
            dfs(visited, all_paths, curr_path, n)

        # backtrack
        if cave.islower():
            visited[cave] -= 1
        curr_path.pop()

    visited = defaultdict(int)
    all_paths = []
    # dfs + backtracking
    dfs(visited, all_paths, [], 'start')
    return len(all_paths)

@pytest.fixture
def example1() -> list[str]:
    return [
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end',
    ]

@pytest.fixture
def example2() -> list[str]:
    return [
        'dc-end',
        'HN-start',
        'start-kj',
        'dc-start',
        'dc-HN',
        'LN-dc',
        'HN-end',
        'kj-sa',
        'kj-HN',
        'kj-dc',
    ]

@pytest.fixture
def example3() -> list[str]:
    return [
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW',
    ]

def test_part1(example1, example2, example3) -> None:
    assert part1(example1) == 10
    assert part1(example2) == 19
    assert part1(example3) == 226

def test_part2(example1, example2, example3) -> None:
    assert part2(example1) == 36
    assert part2(example2) == 103
    assert part2(example3) == 3509

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
