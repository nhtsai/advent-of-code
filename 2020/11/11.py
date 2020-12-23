def part1(l):
    def seat(l, x, y):
        adjacents = [(x,y) for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0)]
        positions = [(x+a[0], y+a[1]) for a in adjacents if 0 <= x+a[0] < len(l) and 0<= y+a[1] < len(l[0])]
        current = l[x][y]
        adj_seats = [l[x][y] for (x,y) in positions]
        if current == 'L' and adj_seats.count('#') == 0:
            return '#'
        elif current == '#' and adj_seats.count('#') >= 4:
            return 'L'
        return current

    old_occupied = 0
    while True:
        count = 0
        new = []
        for x in range(len(l)):
            row = ""
            for y in range(len(l[0])):
                s = seat(l, x, y)
                if s == '#':
                    count += 1
                row += s
            new.append(row)
        if old_occupied != count:
            old_occupied = count
            l = new
        else:
            break
    return old_occupied


def part2(l):
    def seat(l, x, y):
        adjacents = [(x,y) for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0)]
        visible = []
        for a in adjacents:
            new_x = x + a[0]
            new_y = y + a[1]
            while True: 
                if not (0 <= new_x < len(l) and 0 <= new_y < len(l[0])):
                    break
                adj_tile = l[new_x][new_y]
                if adj_tile == '.':
                    new_x += a[0]
                    new_y += a[1]
                else:
                    visible.append(adj_tile)
                    break
        current = l[x][y]
        if current == 'L' and visible.count('#') == 0:
            return '#'
        elif current == '#' and visible.count('#') >= 5:
            return 'L'
        return current

    old_occupied = 0
    while True:
        count = 0
        new = []
        for x in range(len(l)):
            row = ""
            for y in range(len(l[0])):
                s = seat(l, x, y)
                if s == '#':
                    count += 1
                row += s
            new.append(row)
        if old_occupied != count:
            old_occupied = count
            l = new
        else:
            break
    return old_occupied

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = [x.strip() for x in f.readlines()]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
