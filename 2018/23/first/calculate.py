#!/usr/bin/env python3

# A little bit of VSCode shortcuts, and the serialized information from day 23 turned into a JSON.

import json, operator
from scipy.spatial import distance

with open('../nanobots.json', 'r') as f:
    nanobots = json.load(f)

# find strongest nanobot
originID = 0
for nanobotID, nanobot in enumerate(nanobots):
    if nanobot['range'] > nanobots[originID]['range']:
        originID = nanobotID

# count contacts
contacts = 0
for target in nanobots:
    if distance.cityblock(nanobots[originID]['pos'], target['pos']) <= nanobots[originID]['range']:
        contacts += 1

print("nanobot", originID, "has", contacts, "contacts.")
