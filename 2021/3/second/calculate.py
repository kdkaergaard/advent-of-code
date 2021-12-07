#!/usr/bin/env python3

with open('../diagnostics.txt', 'r') as f:
    diagnostics = f.read().splitlines()

bytes = [[0]*2 for _ in diagnostics[0]]
rows = len(diagnostics)
cols = len(diagnostics[0])

print("oxygenGeneratorRating")
oxygenGeneratorDiagnostics = diagnostics
oxygenGeneratorRating = 0
print(oxygenGeneratorDiagnostics)
for col in range(0, cols):
    sumCol = 0
    rowsLeft = len(oxygenGeneratorDiagnostics)
    for row in range(0, rowsLeft):
        sumCol = sumCol + int(oxygenGeneratorDiagnostics[row][col])
    #print("Col{}: {} of {}".format(str(col+1), str(sumCol), rows))
    keepBit = 1 if sumCol >= rowsLeft / 2 else 0
    #print(keepBit)
    oxygenGeneratorDiagnostics = [row for row in oxygenGeneratorDiagnostics if row[col] == str(keepBit)]
    print(oxygenGeneratorDiagnostics)
    oxygenGeneratorRating = oxygenGeneratorDiagnostics[0]
    if len(oxygenGeneratorDiagnostics) == 1:
        break

print("co2ScrubberRating")
co2ScrubberDiagnostics = diagnostics
co2ScrubberRating = 0
for col in range(0, cols):
    sumCol = 0
    rowsLeft = len(co2ScrubberDiagnostics)
    for row in range(0, rowsLeft):
        sumCol = sumCol + (1 if co2ScrubberDiagnostics[row][col] == "0" else 0)
    #print("Col{}: {} of {}".format(str(col+1), str(sumCol), rows))
    keepBit = 0 if sumCol <= rowsLeft / 2 else 1
    #print(keepBit)
    co2ScrubberDiagnostics = [row for row in co2ScrubberDiagnostics if row[col] == str(keepBit)]
    print(co2ScrubberDiagnostics)
    co2ScrubberRating = co2ScrubberDiagnostics[0]
    if len(co2ScrubberDiagnostics) == 1:
        break

lifeSupportRating = int(oxygenGeneratorRating, 2) * int(co2ScrubberRating, 2)
print(lifeSupportRating)