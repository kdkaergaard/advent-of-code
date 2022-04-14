#!/usr/bin/env python3

from statistics import median

with open("../positions.txt") as fp:
    lines = fp.read()

positions = lines.split(",")
positions = list(map(int, positions))

optimalPosition = int(median(positions))

print(sum([abs(distance - optimalPosition) for distance in positions]))