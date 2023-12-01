import re

def readLinesAsList(filename = "./input"):
    lines = None
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines



numberMappings = {
    "one":"o1ne",
    "two":"t2wo",
    "three":"t3hree",
    "four":"f4our",
    "five":"f5ive",
    "six":"s6ix",
    "seven":"s7even",
    "eight":"e8ight",
    "nine":"n9ine",
    "zero":"z0ero"
}




inputLines = readLinesAsList()

modifiedInputLines = []
for line in inputLines:
    tmp = line
    for word,number in numberMappings.items():
        tmp = tmp.replace(word, number)
    modifiedInputLines.append(tmp)




digits = [int(str([c for c in line if c.isdigit()][0]) + str([c for c in line if c.isdigit()][-1])) for line in modifiedInputLines] 




print(sum(digits))
