#!/usr/bin/env python3

with open('../diagnostics.txt', 'r') as f:
    diagnostics = f.read().splitlines()

gammaRate = ""
epsilonRate = ""
occurrence = [[0]*2 for _ in diagnostics[0]]

for row in diagnostics:
    #print(row)
    for column, value in enumerate(row):
        #print(column)
        occurrence[column][int(value)] += 1

for bitColumn in occurrence:
    if bitColumn[0] > bitColumn[1]:
        gammaRate += "0"
        epsilonRate += "1"
    else:
        gammaRate += "1"
        epsilonRate += "0"

print(gammaRate, epsilonRate)

powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)

print(powerConsumption)