#!/usr/bin/env python3

with open('../intcode.txt', 'r') as f:
    opcodeString = f.read()

opcodes = list(map(int, opcodeString.rstrip().split(',')))

opcodes[1] = 12
opcodes[2] = 2

cursor = 0

while not opcodes[cursor] == 99:
    if opcodes[cursor] == 1:
        opcodes[opcodes[cursor+3]] = opcodes[opcodes[cursor+1]] + opcodes[opcodes[cursor+2]]
    elif opcodes[cursor] == 2:
        opcodes[opcodes[cursor+3]] = opcodes[opcodes[cursor+1]] * opcodes[opcodes[cursor+2]]
    cursor += 4

print(opcodes[0])
