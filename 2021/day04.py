from pathlib import PurePath

def part1(l: list[str]) -> int:
    # parse draws and boards
    boards = []
    curr = []
    for i in range(len(l)):
        if i == 0:
            draws = [int(j) for j in l[i].split(',')]
        elif l[i] == '':
            if curr:
                boards.append(curr)
            curr = []
        else:
            row = [int(k) for k in l[i].split()]
            curr.append(row)
    boards.append(curr)

    # play bingo
    drawn = set()
    n = len(boards[0])
    for draw in draws:
        drawn.add(draw)
        # start checking for bingo
        if len(drawn) > n:
            for board in boards:
                matches = [0 for _ in range(2 * n)]
                board_sum = 0
                # check the board
                for r in range(n):
                    for c in range(n):
                        if board[r][c] in drawn:
                            # record row match
                            matches[r] += 1
                            # record col match
                            matches[c + n] += 1
                        else:
                            board_sum += board[r][c]
                # return if bingo
                if any(i == n for i in matches):
                    return draw * board_sum
    return -1

def part2(l: list[str]) -> int:
    # parse draws and boards
    boards = []
    curr = []
    for i in range(len(l)):
        if i == 0:
            draws = [int(j) for j in l[i].split(',')]
        elif l[i] == '':
            if curr:
                boards.append(curr)
            curr = []
        else:
            row = [int(k) for k in l[i].split()]
            curr.append(row)
    boards.append(curr)

    # play bingo
    drawn = set()
    n = len(boards[0])
    won_boards = set()
    for draw in draws:
        drawn.add(draw)
        # start checking for bingo
        if len(drawn) > n:
            for idx,board in enumerate(boards):
                if idx in won_boards:
                    continue
                matches = [0 for _ in range(2 * n)]
                board_sum = 0
                # check the board
                for r in range(n):
                    for c in range(n):
                        if board[r][c] in drawn:
                            # record row match
                            matches[r] += 1
                            # record col match
                            matches[c + n] += 1
                        else:
                            board_sum += board[r][c]
                # board has bingo
                if any(i == n for i in matches):
                    # mark board won if not yet
                    won_boards.add(idx)
                    if len(won_boards) == len(boards):
                        return draw * board_sum
    return -1

def test() -> None:
    l = [
            '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
                          '',
            '22 13 17 11  0',
            ' 8  2 23  4 24',
            '21  9 14 16  7',
            ' 6 10  3 18  5',
            ' 1 12 20 15 19',
                          '',
            ' 3 15  0  2 22',
            ' 9 18 13 17  5',
            '19  8  7 25 23',
            '20 11 10 24  4',
            '14 21 16 12  6',
                          '',
            '14 21 17 24  4',
            '10 16 15  9 19',
            '18  8 23 26 20',
            '22 11 13  6  5',
            ' 2  0 12  3  7',
    ]
    assert part1(l) == 4512
    assert part2(l) == 1924

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
