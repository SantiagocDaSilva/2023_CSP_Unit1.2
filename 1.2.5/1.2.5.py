# Santiago DaSilva 1.2.5

import turtle as trtl
colors = ["black", "sky blue", "salmon", "orchid", "pale green"]
font_setup = ("Arial", 20, "normal")
t_size = 2
t_color = 'pink'
t_shape = "turtle"

# draw tictactoe board
painter = trtl.Turtle()

spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def drawBoard():
    print(str(board[0:3]) + '\n')
    print(str(board[3:6]) + '\n')
    print(str(board[6:9]) + '\n')


gameOver = False
turns = 1
drawBoard()

while (turns < 10) and not gameOver:
    turns += 1
    move1 = int(input("Make a move, pick any of the numbers 1-9"))
    board[move1 - 1] = "X"
    spaces.remove(move1 - 1)
    drawBoard()
    gameOver = False
turns = 2
while (turns < 10) and not gameOver:
    turns += 2
    move2 = int(input("My turn"))
    board[move2 - 2] = "O"
    spaces.remove(move2 - 2)
    drawBoard()
turns = 3
while (turns < 10) and not gameOver:
    turns += 3
    move3 = int(input("Make a move, pick any of the numbers 1-9"))
    board[move3 - 3] = "X"
    spaces.remove(move3 - 3)
    drawBoard()
    gameOver = False




def drawScoreboard():
    painter.pendown()
    painter.forward(50)
