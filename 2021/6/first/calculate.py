#!/usr/bin/env python3

with open("../school.txt") as fp:
    lines = fp.read()

school = lines.split(",")
school = list(map(int, school))

print(school)

for day in range(80):
    for f in range(len(school)):
        if school[f] == 0:
            school[f] = 6
            school.append(8)
            continue
        school[f] -= 1
    

#print(school)
print(len(school))