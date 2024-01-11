# Santiago DaSilva 1.2.5

import turtle as trtl

# draw tictactoe board


spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def drawBoard():
    print(str(board[0:3]) + '\n')
    print(str(board[3:6]) + '\n')
    print(str(board[6:9]) + '\n')


gameOver = False
turns = 1
drawBoard()

while (turns<10):
    turns += 1
    move1 = int(input("Make a move, pick any of the numbers 1-9"))
    board[move1-1]="X"
    spaces.remove(move1-1)
    drawBoard()
    gameOver = False
turns = 2
drawBoard()
while (turns<10):
    turns += 2
    move1=int(input("My turn"))
    board[move1 - 2] = "O"
    spaces.remove(move1 - 1)
    drawBoard()
