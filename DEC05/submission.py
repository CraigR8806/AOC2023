import re


def readLinesAsList(filename="./input"):
    lines = None
    with open(filename, "r") as file:
        lines = [line.rstrip() for line in file.readlines()]

    return lines


headers = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

headersRegex = "^(" + "|".join(headers) + ")"

seeds = []
mappings = {}
currentHeader = ""
for line in readLinesAsList():
    seedsTmp = re.findall("(?<=^seeds: ).+", line)
    if len(seedsTmp):
        seeds = [int(seed) for seed in seedsTmp[0].split(" ")]

    headersTmp = re.findall(headersRegex + "(?= map:)", line)
    if len(headersTmp):
        currentHeader = headersTmp[0]


    mappingEntryTmp = [int(num.strip()) for num in re.findall("(?<!^seeds: )[0-9]+", line)]
    if len(mappingEntryTmp) and currentHeader != "":
        headerMappings = mappings.get(currentHeader, [])
        delta = mappingEntryTmp[0]-mappingEntryTmp[1]
        mappingEntryTmp.append(delta)
        mappingEntryTmp.append(delta*-1)
        mappingEntryTmp.append(mappingEntryTmp[0] + mappingEntryTmp[2])
        headerMappings.append(mappingEntryTmp)
        mappings[currentHeader] = headerMappings


for header in headers:
    headerMappings = mappings[header]
    for i in range(len(seeds)):
        seedTmp = seeds[i]
        for headerMapping in headerMappings:
            delta = 0
            if seeds[i] in range(headerMapping[1], headerMapping[1] + headerMapping[2]):
                delta = headerMapping[3]

            seedTmp+=delta
        seeds[i] = seedTmp

minimum = min(seeds)
print("Part 1: " + str(minimum))
        

seeds = []
for line in readLinesAsList():
    seedsTmp = re.findall("(?<=^seeds: ).+", line)
    if len(seedsTmp):
        seedInfo = [int(seed) for seed in seedsTmp[0].split(" ")]
        for i in range(0, len(seedInfo), 2):
            seeds.append((seedInfo[i], seedInfo[i] + seedInfo[i+1]))
print(seeds)



lowest = 99999999
for i in range(minimum):
    print(i)
    itmp = i
    for j in range(len(headers) - 1, -1, -1):
        headerMappings = mappings[headers[j]]
        itmptmp = itmp
        for headerMapping in headerMappings:
            delta = 0
            if itmp in range(headerMapping[0], headerMapping[5]):
                delta = headerMapping[4]

            itmptmp+=delta
        itmp = itmptmp
    if any([itmp in range(seed[0], seed[1]) for seed in seeds]):
        lowest = i
        break
        


print("Part 2: " + str(lowest))

