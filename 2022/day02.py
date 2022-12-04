import io
from pathlib import PurePath


def part1(lines: list[str]) -> int:
    """
    To find the score for one round:
    - Add the value of your hand (1, 2, 3)
    - Add the value of the outcome (0, 3, 6)
        - The difference between opp (1, 2, 3) and you (1, 2, 3)
          determines the index of the outcome
        - The outcomes list handles the win/loss wrapping
            - If the difference is -2, you lose, add 0
            - If the difference is -1, you win, add 6
            - If the difference is 0, draw, add 3
            - If the difference is 1, you lose, add 0
            - If the difference is 2, you win, add 6

    Time: O(N)
    Space: O(1)
    """
    outcomes: tuple[int, int, int] = (3, 0, 6)
    score = 0
    for line in lines:
        opp, you = line.split(" ")
        opp_val = ord(opp) - ord("A") + 1
        you_val = ord(you) - ord("X") + 1
        # add value of your hand
        score += you_val
        # add value of outcome
        score += outcomes[opp_val - you_val]
    return score


def part2(lines: list[str]) -> int:
    """
    To find the score for one round:
    - Add the value of your hand (1, 2, 3)
        - The outcome_val - 1 is the change (-1, 0, 1) to apply
          to the opp value to get the your needed hand value
        - The % 3 handles the wrapping of the your hand values
          - If rock + lose, then ((0 - 1) % 3) + 1 = 3, pick scissors
          - If paper + win, then ((2 + 1) % 3) + 1 = 1, pick rock
    - Add the value of the needed outcome (0, 3, 6)

    Time: O(N)
    Space: O(1)
    """
    score = 0
    for line in lines:
        opp, outcome = line.split(" ")
        opp_val = ord(opp) - ord("A")
        outcome_val = ord(outcome) - ord("X")
        # add value of your hand
        score += ((opp_val + (outcome_val - 1)) % 3) + 1
        # add value of outcome
        score += outcome_val * 3
    return score


def test() -> None:
    test_input = "A Y\nB X\nC Z"
    with io.StringIO(test_input) as fp:
        lines = fp.read().splitlines()
    assert 15 == part1(lines)
    assert 12 == part2(lines)


if __name__ == "__main__":
    with open(f"./data/input-{PurePath(__file__).stem}.txt", "r") as f:
        lines = f.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
