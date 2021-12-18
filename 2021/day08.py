from pathlib import PurePath

def part1(l: list[str]) -> int:
    # 1: 2
    # 4: 4
    # 7: 3
    # 8: 7

    result = 0
    for entry in l:
        output = entry.split(' | ')[1]
        for num in output.split():
            if len(num) in (2, 4, 3, 7):
                result += 1
    return result


def part2(l: list[str]) -> int:
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    segments = {
        0: {'a', 'b', 'c', 'e', 'f', 'g'},
        1: {'c', 'f'}
    }

    for entry in l:
        signals, output = entry.split(' | ')
        for s in signals:
            pass

        for o in output:
            pass
    """
    * each pattern maps to a set of numbers to cross off
    * each fake segment maps to a set of real segments to cross off
    * go through 10 patterns
    * identify the easy ones: 1, 4, 7, 8


    fake segments to numbers
        eliminate using lengths
    numbers to real segments
        eliminate using set diff?
    fake segments to real segments by elimination

    acedgfb     abcdefg     8
    cdfbe       bcdef
    gcdfa       acdfg
    fbcad       abcdf
    dab         abd         7
    cefabd      abcdef
    cdfgeb      bcdefg
    eafb        abef        4
    cagedb      abcdeg
    ab          ab          1

    first pass: easy numbers 1, 4, 7, 8

    0: abcefg
    1: cf
    2: acdeg
    3: acdfg
    4: bcdf
    5: abdfg
    6: abdefg
    7: acf
    8: abcdefg
    9: abcdfg

    for each fake seg, match up to real seg
    a: cf, bcdf, acf
    b: cf, bcdf, acf
    c:
    d: acf
    e: bcdf
    f: bcdf
    g:

    """





def test() -> None:
    l = [
        'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
        'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
        'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
        'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
        'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
        'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
        'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
        'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
        'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
        'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
    ]
    assert part1(l) == 26


if __name__ == '__main__':
    with open(f'./data/input-{PurePath(__file__).stem}.txt', 'r') as f:
        l = f.read().splitlines()
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
