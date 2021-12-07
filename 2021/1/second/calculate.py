#!/usr/bin/env python3

with open('../measurements.txt', 'r') as f:
    measurements = f.read().splitlines()

depthIncreases = 0

print(measurements[0:3])

for i in range(2, len(measurements)):
    if sum(measurements[i-2:i+1]) > sum(measurements[i-3:i]):
        depthIncreases += 1

print(depthIncreases)