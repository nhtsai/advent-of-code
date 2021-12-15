from pathlib import PurePath
from collections import Counter
from collections import defaultdict


def part1(l: list[str]) -> int:
    # naive method
    template = None
    rules = {}
    for i, rule in enumerate(l):
        if i == 0:
            template = rule
        elif i == 1:
            continue
        else:
            pair, insert = rule.split(' -> ')
            rules[pair] = insert

    steps = 10
    for step in range(steps):
        new_template = [template[0]]
        for i in range(1, len(template)):
            pair = template[i-1:i+1]
            if pair in rules:
                new_template.append(rules[pair])
            new_template.append(template[i])
        template = ''.join(new_template)
        # print(f'after step {step+1}: {template}')

    counts = Counter(template)
    mc = counts.most_common()
    return mc[0][1] - mc[-1][1]

def part2(l: list[str]) -> int:
    template = None
    rules = {}
    for i, rule in enumerate(l):
        if i == 0:
            template = rule
        elif i == 1:
            continue
        else:
            pair, ins = rule.split(' -> ')
            pair = tuple(pair)
            rules[pair] = ins

    # add initial pairs
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pair = (template[i], template[i+1])
        pairs[pair] += 1

    # apply polymer matching steps
    steps = 40
    for i in range(steps):
        new_pairs = defaultdict(int)
        for (a, b), cnt in pairs.items():
            ins = rules[(a, b)] # char to insert
            new_pairs[(a, ins)] += cnt
            new_pairs[(ins, b)] += cnt
        pairs = new_pairs

    # count individual polymers
    polymers = defaultdict(int)
    polymers[template[0]] = 1 # account for first polymer
    for (a,b), c in pairs.items():
        polymers[b] += c

    # get most common and least common polymers
    mc = max(polymers.keys(), key=lambda k: polymers[k])
    lc = min(polymers.keys(), key=lambda k: polymers[k])
    return polymers[mc] - polymers[lc]


def test() -> None:
    l = [
        'NNCB',
        '',
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C',
    ]
    assert part1(l) == 1588
    assert part2(l) == 2188189693529

if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
