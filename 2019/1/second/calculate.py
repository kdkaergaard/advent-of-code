#!/usr/bin/env python3

import math

with open('../modules.txt', 'r') as f:
    modules = f.readlines()

requiredFuel = 0

for mass in modules:
    itrMass = int(mass)
    fuelRequirement = 0
    while itrMass >= 0:
        itrMass = itrMass // 3 - 2
        if itrMass >= 0:
            requiredFuel += itrMass

print(requiredFuel, 'required to launch all modules.')
