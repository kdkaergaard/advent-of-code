#!/usr/bin/env python3

def add(paramOne, paramTwo):
    return paramOne + paramTwo

def multiply(paramOne, paramTwo):
    return paramOne * paramTwo

class Intcode(object):
    instructions = {
        1: add,
        2: multiply
    }
    def __init__(self, intcode):
        self.memory = intcode[:]
        self.snapshot = intcode[:]
        self.instructionPointer = 0
    def step(self):
        instruction = self.instructions.get(self.memory[self.instructionPointer], lambda: 99)
        paramOne = self.memory[self.memory[self.instructionPointer+1]]
        paramTwo = self.memory[self.memory[self.instructionPointer+2]]
        self.memory[self.memory[self.instructionPointer + 3]] = instruction(paramOne, paramTwo)
    def iterate(self):
        while not self.memory[self.instructionPointer] == 99:
            self.step()
            self.instructionPointer += 4
    def run(self):
        self.iterate()
    def getAddress(self, address):
        return self.memory[address]
    def setAddress(self, address, value):
        self.memory[address] = value
    def dump(self):
        return self.memory
    def reset(self):
        self.memory = self.snapshot[:]
        self.instructionPointer = 0

if __name__ == "__main__":
    with open('../intcode.txt', 'r') as f:
        intcodeString = f.read()
    intcode = list(map(int, intcodeString.rstrip().split(',')))
    program = Intcode(intcode)
    for i in range(100):
        for x in range(100):
            program.setAddress(1, i)
            program.setAddress(2, x)
            program.run()
            if program.getAddress(0) == 19690720:
                print("%02d%02d" % (program.getAddress(1), program.getAddress(2)))
                quit()
            program.reset()
    