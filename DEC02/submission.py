from functools import reduce
import re


def readLinesAsList(filename = "./input"):
    lines = None
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines


maxCount = {"red": 12, "green": 13, "blue": 14}


validGameSum = 0


for game in readLinesAsList():

    gameNumber = int(re.search("(?<=Game )[0-9]+", game).group())
    totalFound = {k:re.findall("[0-9]+(?= " + k + ")", game) for k in maxCount.keys()}
    validGameSum += gameNumber if all([max([int(vv) for vv in v])<=maxCount[k] for k,v in totalFound.items()]) else 0


print("Part 1:" + str(validGameSum))

totalPower = 0
for game in readLinesAsList():

    totalFound = {k:re.findall("[0-9]+(?= " + k + ")", game) for k in maxCount.keys()}
    totalPower += reduce(lambda a,b: a*b, [max([int(vv) for vv in v]) for k,v in totalFound.items()])

print("Part 2:" + str(totalPower))