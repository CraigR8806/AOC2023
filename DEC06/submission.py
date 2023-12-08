import re
import math
from functools import reduce


def readLinesAsList(filename="./input"):
    lines = None
    with open(filename, "r") as file:
        lines = [line.rstrip() for line in file.readlines()]

    return lines



times=[]
distances=[]

records={}

for line in readLinesAsList():
    timesTmp=re.findall("(?<=^Time:).+", line)
    distsTmp=re.findall("(?<=^Distance:).+", line)
    if len(timesTmp):
        times=[int(t.strip()) for t in timesTmp[0].strip().split(" ") if t != '']

    if len(distsTmp):
        distances=[int(t.strip()) for t in distsTmp[0].strip().split(" ") if t != '']

mappings = {times[i]:distances[i] for i in range(len(times))}

findings=[]
for t,d in mappings.items():
    finding=0
    left = math.floor(t/2)
    right = math.ceil(t/2)
    while((left-finding)*(right+finding) > d):
        finding+=1


    findings.append(((left-finding) - (right+finding) + 1) * -1)

print("Part 1: " + str(reduce(lambda a,b:a*b, findings)))


for line in readLinesAsList():
    timesTmp=re.findall("(?<=^Time:).+", line)
    distsTmp=re.findall("(?<=^Distance:).+", line)
    if len(timesTmp):
        times=[int(t.strip()) for t in [timesTmp[0].strip().replace(" ", "")] if t != '']

    if len(distsTmp):
        distances=[int(t.strip()) for t in [distsTmp[0].strip().replace(" ", "")] if t != '']

mappings = {times[i]:distances[i] for i in range(len(times))}




findings=[]
for t,d in mappings.items():
    finding=0
    left = math.floor(t/2)
    right = math.ceil(t/2)
    while((left-finding)*(right+finding) > d):
        finding+=1


    findings.append(((left-finding) - (right+finding) + 1) * -1)

print("Part 2: " + str(findings[0]))