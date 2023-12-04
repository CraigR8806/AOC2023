import re
import math

def readLinesAsList(filename = "./input"):
    lines = None
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines

totalWorth = 0

for line in readLinesAsList():
    line = line.split(":")[1]
    a = line.rstrip().split("|")[0].split(" ")
    b = line.rstrip().split("|")[1].split(" ")
    cardWorth = 0.5
    for found in [2 for n in a if n != "" and n in b]:
        cardWorth *= found

    cardWorth = math.floor(cardWorth)
    totalWorth += cardWorth

print("Part 1:" + str(totalWorth))

cards = {int(card) + 1:1 for card in range(int(re.search("[0-9]+",readLinesAsList()[-1].split(":")[0]).group()))}

cardsProcessed = 0
for line in readLinesAsList():
    card = int(re.search("[0-9]+",line.split(":")[0]).group())
    line = line.split(":")[1]
    a = line.rstrip().split("|")[0].split(" ")
    b = line.rstrip().split("|")[1].split(" ")
    numWon = len([1 for n in a if n != "" and n in b])
    for i in range(1, numWon + 1):
        cards[card + i] += cards[card]

    cardsProcessed += cards[card]

print("Part 2:" + str(cardsProcessed))