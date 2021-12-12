from pathlib import PurePath
from collections import defaultdict

def part1(l: list[str]) -> int:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    illegals = defaultdict(int)

    for line in l:
        stack = []
        is_corrupt = False
        for c in line:
            if c in pairs.keys():
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    illegals[c] += 1
                    is_corrupt = True
            else:
                stack.append(c)
            if is_corrupt: break
    return sum(points[c] * illegals[c] for c in illegals.keys())

def part2(l: list[str]) -> int:
    closers = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    openers = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []

    for line in l:
        stack = []
        for c in line:
            if c in closers.keys():
                if stack and closers[c] == stack[-1]:
                    stack.pop()
                else:
                    # break when corrupt
                    break
            else:
                stack.append(c)
        else:
            # inner loop did not break, line is incomplete
            # get missing closers
            missing = [openers[i] for i in reversed(stack)]

            # calculate total_score
            total_score = 0
            for i in missing:
                total_score *= 5
                total_score += points[i]
            scores.append(total_score)

    # return middle score
    scores.sort()
    return scores[len(scores) // 2]

def test() -> None:
    l = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]',
    ]
    assert part1(l) == 26397
    assert part2(l) == 288957

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
