from pathlib import PurePath

def part1(l: list[str]) -> int:
    m = [[int(i) for i in row] for row in l]
    a, b = len(m), len(m[0])
    result = 0
    for i in range(a):
        for j in range(b):
            is_low = True
            # up
            if i > 0:
                is_low = is_low and m[i][j] < m[i-1][j]
            # down
            if i < a - 1:
                is_low = is_low and m[i][j] < m[i+1][j]
            # left
            if j > 0:
                is_low = is_low and m[i][j] < m[i][j-1]
            # right
            if j < b - 1:
                is_low = is_low and m[i][j] < m[i][j+1]

            if is_low:
                # print(f'{m[i][j]} at ({i}, {j})')
                result += m[i][j] + 1
    return result

def part2(l: list[str]) -> int:
    m = [[int(i) for i in row] for row in l]
    a, b = len(m), len(m[0])

    # size of islands
    def dfs(r: int, c: int) -> int:
        if r < 0 or c < 0 or \
           r >= a or c >= b or \
           m[r][c] == 9:
            return 0

        # visit
        m[r][c] = 9

        # dfs
        return 1 + dfs(r + 1, c) + \
               dfs(r - 1, c) + \
               dfs(r, c + 1) + \
               dfs(r, c - 1)

    basins = []
    for i in range(a):
        for j in range(b):
            if m[i][j] != 9:
                basin_size = dfs(i, j)
                basins.append(basin_size)

    result = 1
    for i in sorted(basins, reverse=True)[:3]:
        result *= i
    return result


def test() -> None:
    l = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678',
    ]
    assert part1(l) == 15
    assert part2(l) == 1134

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
