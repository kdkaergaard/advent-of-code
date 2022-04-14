#!/usr/bin/env python3

with open("../positions.txt") as fp:
    lines = fp.read()

positions = lines.split(",")
positions = list(map(int, positions))

costOptions = []

for p in range(min(positions), max(positions)+1):
    distances = [abs(distance - p) for distance in positions]
    costOption = sum([int(cost*(cost+1)/2) for cost in distances])
    costOptions.append(costOption)

print(min(costOptions))