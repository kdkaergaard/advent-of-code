#!/usr/bin/env python3

with open("../test.txt") as fp:
    lines = fp.read().splitlines()

numbers = lines[0].split(",")

class Board:
    def __init__(self, board = None):
        self.board = []
        self.sets = []
        for i, row in enumerate(board):
            self.board += row.split()
            self.sets.append(row.split()) # row
            self.sets.append([row.split()[i] for row in board]) # column
        self.stamped = []
        # for row in rows:
        #     self.sets.append([])
        #     self.sets.append([])
    def stamp(self, number):
        self.stamped.append(number)
    #def score(self):
        #for row in self.sets

boardCount = lines.count("")
boards = [] * boardCount

for i in range(0, boardCount):
    board = Board(lines[2+i+5*i:2+i+5*i+5])
    boards.append(board)

for number in numbers:
    for board in boards:
        board.stamp(number)

for board in boards:
    print("board")
    print(board.sets)

# print(boards[0].score())
