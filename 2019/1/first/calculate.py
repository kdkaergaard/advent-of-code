#!/usr/bin/env python3

import math

with open('../modules.txt', 'r') as f:
    modules = f.readlines()

requiredFuel = 0

for mass in modules:
    requiredFuel += math.floor(int(mass) / 3) - 2

print(requiredFuel, 'required to launch all modules.')
