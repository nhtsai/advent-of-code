from pathlib import PurePath
from heapq import heappush, heappop
import pytest

def part1(l: list[list[int]]) -> int:
    # dijkstra's
    n = len(l)
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0
    minheap = []

    # starting node weight is never used
    heappush(minheap, (l[0][0], (0, 0)))

    while minheap:
        (_, curr) = heappop(minheap)
        (r, c) = curr

        if visited[r][c]:
            continue

        visited[r][c] = True

        # check valid neighbors
        for (dr, dc) in deltas:
            nr, nc = r + dr, c + dc
            if  0 <= nr < n and \
                0 <= nc < n and \
                (nr, nc) not in visited:
                # if we find a better distance, update that node's best distance
                dist[nr][nc] = min(dist[nr][nc], dist[r][c] + l[nr][nc])
                heappush(minheap, (dist[nr][nc], (nr, nc)))

    return dist[n - 1][n - 1]

def part2(l: list[list[int]]) -> int:
    n = len(l)
    cave = [[0 for _ in range(5 * n)] for _ in range(5 * n)]

    '''
    x0 x1 x2 x3 x4
    x1 x2 x3 x4 x5
    x2 x3 x4 x5 x6
    x3 x4 x5 x6 x7
    x4 x5 x6 x7 x8
    '''

    # copy first cell
    for i in range(n):
        for j in range(n):
            cave[i][j] = l[i][j]

    # write first row
    for i in range(n):
        for j in range(n, 5 * n):
            cave[i][j] = cave[i][j - n] + 1 if cave[i][j - n] < 9 else 1

    # write subsequent rows
    for i in range(n, 5 * n):
        for j in range(5 * n):
            cave[i][j] = cave[i - n][j] + 1 if cave[i - n][j] < 9 else 1

    return part1(cave)

@pytest.fixture
def example1() -> list[list[int]]:
    return [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
    ]

def test(example1) -> None:
    assert part1(example1) == 40
    assert part2(example1) == 315

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = [[int(i) for i in line] for line in f.read().splitlines()]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))