#!/usr/bin/env python3

with open('../commands.txt', 'r') as f:
    commands = f.read().splitlines()

horizontalPos = 0
depthPos = 0
aim = 0

for command in commands:
    parts = command.split(" ")
    parts[1] = int(parts[1])
    print(parts)
    if parts[0] == "forward":
        horizontalPos += parts[1]
        depthPos += aim * parts[1]
    if parts[0] == "down":
        aim += parts[1]
    if parts[0] == "up":    
        aim -= parts[1]

print(horizontalPos, depthPos, aim)
print(horizontalPos * depthPos)

# depthIncreases = 0

# print(measurements[0:3])

# for i in range(2, len(measurements)):
#     if sum(measurements[i-2:i+1]) > sum(measurements[i-3:i]):
#         depthIncreases += 1

# print(depthIncreases)