from pathlib import PurePath
import pytest

def print_compact(l: list[list[int]]) -> None:
    n = len(l)
    for i in range(n):
        for j in range(n):
            print(l[i][j], end='')
        print()

# conway's game of life
def part1(l: list[list[int]]) -> int:
    debug = False
    if debug:
        print('Before any steps:')
        print_compact(l)

    n = len(l)
    steps = 100
    flashed = set() # popped empty after every step
    total_flashes = 0
    for step in range(steps):
        # increment every energy level
        for i in range(n):
            for j in range(n):
                l[i][j] += 1

        # flash every octopus > 9, increment every neighbor
        more_to_flash = True
        while more_to_flash:
            more_to_flash = False
            for i in range(n):
                for j in range(n):
                    if l[i][j] > 9 and (i, j) not in flashed:
                        flashed.add((i, j))
                        # increment neighbors
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                # skip self-increment
                                if di == dj == 0:
                                    continue
                                curr_i, curr_j = i + di, j + dj
                                if 0 <= curr_i < n and 0 <= curr_j < n:
                                    l[curr_i][curr_j] += 1

                                    # see if neighbors need to flash
                                    if not more_to_flash and l[curr_i][curr_j] > 9 and (curr_i, curr_j) not in flashed:
                                        more_to_flash = True

        if debug:
            print(f'After step {step + 1}:')
            print_compact(l)
            print(f'There were {len(flashed)} flashes.')
            print()

        total_flashes += len(flashed)
        # reset flashed
        while flashed:
            (i, j) = flashed.pop()
            l[i][j] = 0

    if debug:
        print(f'{total_flashes} total flashes in {steps} steps')
    return total_flashes

def part2(l: list[list[int]]) -> int:
    debug = False
    if debug:
        print('Before any steps:')
        print_compact(l)

    n = len(l)
    step = 0
    flashed = set() # popped empty after every step
    num_flashed = 0
    while num_flashed != n*n:
        step += 1
        # increment every energy level
        for i in range(n):
            for j in range(n):
                l[i][j] += 1

        # flash every octopus > 9, increment every neighbor
        more_to_flash = True
        while more_to_flash:
            more_to_flash = False
            for i in range(n):
                for j in range(n):
                    if l[i][j] > 9 and (i, j) not in flashed:
                        flashed.add((i, j))
                        if len(flashed) == n*n:
                            return step
                        # increment neighbors
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                # skip self-increment
                                if di == dj == 0:
                                    continue
                                curr_i, curr_j = i + di, j + dj
                                if 0 <= curr_i < n and 0 <= curr_j < n:
                                    l[curr_i][curr_j] += 1

                                    # see if neighbors need to flash
                                    if not more_to_flash and l[curr_i][curr_j] > 9 and (curr_i, curr_j) not in flashed:
                                        more_to_flash = True

        if debug:
            print(f'After step {step + 1}:')
            print_compact(l)
            print(f'There were {len(flashed)} flashes.')
            print()

        num_flashed = len(flashed)
        # reset flashed
        while flashed:
            (i, j) = flashed.pop()
            l[i][j] = 0

    return step

@pytest.fixture
def fixture() -> list[list[int]]:
    l = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]
    return l

def test_part1(fixture) -> None:
    assert part1(fixture) == 1656

def test_part2(fixture) -> None:
    assert part2(fixture) == 195

# def test():
#     l = [
#         [1, 1, 1, 1, 1],
#         [1, 9, 9, 9, 1],
#         [1, 9, 1, 9, 1],
#         [1, 9, 9, 9, 1],
#         [1, 1, 1, 1, 1],
#     ]
#     assert part1(l) == 0

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
    i    l = [[int(i) for i in list(j)] for j in f.read().splitlines()]
    l2 = [row[:] for row in l]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l2))
