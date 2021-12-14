from pathlib import PurePath
import pytest

def print_matrix(points: set[tuple[int]]) -> None:
    rows = max(r for r,_ in points)
    cols = max(c for _,c in points)
    matrix = [['.' for _ in range(cols + 1)] for _ in range(rows + 1)]
    for (r, c) in points:
        matrix[r][c] = '#'

    for r in range(rows + 1):
        print(f'{r}:', end=' ')
        for c in range(cols + 1):
            print(matrix[r][c], end='')
        print()
    print()

def part1(l: list[str]) -> int:
    points = set()
    for entry in l:
        if entry == '':
            continue
        elif entry.startswith('fold'):
            axis, fold = entry.lstrip('fold along ').split('=')
            fold = int(fold)
            new_points = set()
            while points:
                (r,c) = points.pop()
                if axis == 'y':
                    if r > fold:
                        new_r = fold - (r - fold)
                        if new_r >= 0:
                            new_points.add((new_r, c))
                    else:
                        new_points.add((r, c))
                elif axis == 'x':
                    if c > fold:
                        new_c = fold - (c - fold)
                        if new_c >= 0:
                            new_points.add((r, new_c))
                    else:
                        new_points.add((r, c))
            return len(new_points)
        else:
            c, r = entry.split(',')
            r, c = int(r), int(c)
            points.add((r, c))
    return 0

def part2(l: list[str]) -> int:
    points = set()
    for entry in l:
        if entry == '':
            continue
        elif entry.startswith('fold'):
            axis, fold = entry.lstrip('fold along ').split('=')
            fold = int(fold)
            new_points = set()
            while points:
                (r,c) = points.pop()
                if axis == 'y':
                    if r > fold:
                        new_r = fold - (r - fold)
                        if new_r >= 0:
                            new_points.add((new_r, c))
                    else:
                        new_points.add((r, c))
                elif axis == 'x':
                    if c > fold:
                        new_c = fold - (c - fold)
                        if new_c >= 0:
                            new_points.add((r, new_c))
                    else:
                        new_points.add((r, c))
            points = new_points
        else:
            c, r = entry.split(',')
            r, c = int(r), int(c)
            points.add((r, c))
    print_matrix(points)
    return 1

@pytest.fixture
def example1() -> list[str]:
    return [
        '6,10',
        '0,14',
        '9,10',
        '0,3',
        '10,4',
        '4,11',
        '6,0',
        '6,12',
        '4,1',
        '0,13',
        '10,12',
        '3,4',
        '3,0',
        '8,4',
        '1,10',
        '2,14',
        '8,10',
        '9,0',
        '',
        'fold along y=7',
        'fold along x=5',
    ]

def test(example1) -> None:
    assert part1(example1) == 17
    assert part2(example1) == 1

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
