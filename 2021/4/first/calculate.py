#!/usr/bin/env python3

with open("../game.txt") as fp:
    lines = fp.read().splitlines()

numbers = lines[0].split(",")

class Board:
    def __init__(self, board = None):
        self.board = []
        self.lists = []
        for i, row in enumerate(board):
            self.board += row.split()
            self.lists.append(row.split()) # row
            self.lists.append([row.split()[i] for row in board]) # column
        self.stamped = []
    def __stamp(self, number):
        self.stamped.append(number)
    def addNumber(self, number):
        if any(number in row for row in self.lists):
            self.__stamp(number)
            return True
        return False
    def hasBingo(self):
        for list in self.lists:
            if set(list).issubset(set(self.stamped)):
                return True
        return False
    def score(self, lastNumber):
        score = sum([int(n) for n in self.board if n not in self.stamped]) * lastNumber
        return score

boardCount = lines.count("")
boards = [] * boardCount

for i in range(0, boardCount):
    board = Board(lines[2+i+5*i:2+i+5*i+5])
    boards.append(board)

def play(boards):
    for number in numbers:
        for board in boards:
            board.addNumber(number)
            if board.hasBingo():
                return (board, int(number))

result = play(boards)
print(result[0].score(result[1]))
