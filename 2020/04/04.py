import re

def part1(l):
    matches = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    return sum([all(m in p for m in matches) for p in l])

def part2(l):
    # pattern = r"""(?=.*byr:(19[2-9][0-9]|200[0-2]))(?=.*iyr:(201[0-9]|2020))(?=.*eyr:(202[0-9]|2030))(?=.*hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))(?=.*hcl:(#[0-9a-f]{6}))(?=.*ecl:([a-z]{3}))(?=.*pid:([0-9]{9}))"""
    # valid = 0
    # for p in l:
    #     s = re.search(pattern, p)
    #     if s is not None:
    #         byr, iyr, eyr, whole, inch, cm, hcl, ecl, pid = [x for x in s.groups()]
    #         print(whole, inch, cm, hcl)
    #         byr, iyr, eyr = int(byr), int(iyr), int(eyr)
    #         hgt = int(inch) if inch else int(cm)

    #         if valid == 3: break
    # return valid

    checks = {
        'byr': re.compile("byr:(19[2-9][0-9]|200[0-2])"),
        'iyr': re.compile("iyr:(201[0-9]|2020)"),
        'eyr': re.compile("eyr:(202[0-9]|2030)"),
        'hgt': re.compile("hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)"),
        'hcl': re.compile("hcl:(#[0-9a-f]{6})"),
        'ecl': re.compile("ecl:(amb|blu|brn|gry|grn|hzl|oth)"),
        'pid': re.compile("pid:([0-9]{9})\\b")
    }
    return sum([all([v.search(p) for v in checks.values()]) for p in l])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = [x.replace("\n", " ") for x in f.read().split('\n\n')]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
