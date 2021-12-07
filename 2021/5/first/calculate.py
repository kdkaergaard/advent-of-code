#!/usr/bin/env python3

with open("../coordinates.txt") as fp:
    lines = fp.read().splitlines()

# split coordinate sets '0,9 -> 8,9' into ['0,9','8,9']
coordinates = [line.split(" -> ") for line in lines]

# split parts of coordinates '0,9' into ['0','9']
coordinates = [[coord.split(",") for coord in set] for set in coordinates]

# convert all values into integers
coordinates = [[[int(num) for num in item] for item in set] for set in coordinates]

#print(coordinates)

mapSize = max([x[0][1] for x in coordinates]) + 1

map = [[0] * mapSize for _ in range(mapSize)]
# single dimension mapping
#map = [0] * pow(mapSize, 2)

# generate coordinates between all sets
for c, coordinate in enumerate(coordinates):
    #if (coordinate[0][0] != coordinate[1][0]) and (coordinate[0][1] != coordinate[1][1]):
    #    continue
    #print("coord {}".format(c))
    x = coordinate[1][0]
    y = coordinate[1][1]
    dx = coordinate[0][0] - coordinate[1][0]
    dy = coordinate[0][1] - coordinate[1][1]
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    #print(coordinate)
    #print(dx, dy, steps)
    Xincrement = dx / steps
    Yincrement = dy / steps
    #print(round(x), round(y))
    for step in range(steps+1):
        #map[int(x * mapSize + y)]
        map[round(x)][round(y)] = map[round(x)][round(y)] + 1
        #print(round(x), round(y))
        x = x + Xincrement
        y = y + Yincrement

flatMap = [j for row in map for j in row]
meh = [value for value in flatMap if value >= 2]
print(len(meh))

#index = indexX * arrayWidth + indexY;