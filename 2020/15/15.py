import time

def solve(l, stop):
    spoken = {} # maps {number : turn last spoken}
    # add starting numbers to spoken list
    for i in range(len(l) - 1):
        spoken[l[i]] = i + 1

    said = l[-1] # next number to consider
    turn = len(l)
    while turn < stop:
        # consider last number spoken
        last_spoken = spoken.get(said)
        # if first spoken last turn, say 0
        if last_spoken is None:
            spoken[said] = turn
            said = 0
        else:
            # get calculated number and say it
            spoken[said] = turn
            said = turn - last_spoken
        turn += 1
    return said

if __name__ == '__main__':
    l = [1, 12, 0, 20, 8, 16]
    print("Part 1:", solve(l, 2020))
    print("Part 2:", solve(l, 30000000))
