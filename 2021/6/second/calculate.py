#!/usr/bin/env python3

with open("../school.txt") as fp:
    lines = fp.read()

school = lines.split(",")
school = list(map(int, school))

schoolCount = [0] * 9

# array with number of fish per value
for fish in school:
    schoolCount[fish] += 1

for day in range(256):
    schoolCount = schoolCount[1:] + schoolCount[:1]
    schoolCount[6] += schoolCount[8]

print(sum(schoolCount))