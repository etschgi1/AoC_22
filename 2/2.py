data = []
with open("2/inp.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

test = ["A Y", "B X", "C Z"]
WINNER = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0,
          "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
PART_TWO = True
WINNER_PART_TWO = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1,
                   "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}


def getPoints(str):
    my_shape = str[2]
    if PART_TWO:
        return WINNER_PART_TWO[str]
    return ord(my_shape)-87 + WINNER[str]


def solve(data):
    total = 0
    for d in data:
        total += getPoints(d)
    return total


print(solve(data))
