#!/usr/bin/env python3

with open('../measurements.txt', 'r') as f:
    measurements = f.read().splitlines()

depthIncreases = 0

for i in range(1, len(measurements)):
    if measurements[i] > measurements[i-1]:
        depthIncreases += 1

print(depthIncreases)