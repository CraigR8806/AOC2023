import re


def readLinesAsList(filename = "./input"):
    lines = None
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines



lines = readLinesAsList()

numbers = [[(i.start(), i.group()) for i in re.finditer("[0-9]+", line)] for line in lines ]
symbols = [[i.start() for i in re.finditer("(\*|\#|\+|\$|\@|\/|\-|\=|\%|\&)", line)] for line in lines ]

partNumbers = []

checkit = lambda finding, number_index, number: \
    (finding - 2 < number_index and finding + 2 > number_index) or \
    (finding - 1 < number_index + len(number) and finding + 3 > number_index + len(number))

for index in range(len(symbols)):
    for finding in symbols[index]:
        partNumbers.extend([int(number[1]) for number in numbers[index - 1] if checkit(finding, number[0], number[1])])
        partNumbers.extend([int(number[1]) for number in numbers[index] if checkit(finding, number[0], number[1])])
        partNumbers.extend([int(number[1]) for number in numbers[index + 1] if checkit(finding, number[0], number[1])])

print("Part 1: " + str(sum(partNumbers)))

symbols = [[i.start() for i in re.finditer("\*", line)] for line in lines ]

totalRatio = 0
for index in range(len(symbols)):
    for finding in symbols[index]:
        partNumbers = []
        partNumbers.extend([int(number[1]) for number in numbers[index - 1] if checkit(finding, number[0], number[1])])
        partNumbers.extend([int(number[1]) for number in numbers[index] if checkit(finding, number[0], number[1])])
        partNumbers.extend([int(number[1]) for number in numbers[index + 1] if checkit(finding, number[0], number[1])])
        if len(partNumbers) == 2:
            totalRatio += partNumbers[0] * partNumbers[1]

print("Part 2: " + str(totalRatio))

