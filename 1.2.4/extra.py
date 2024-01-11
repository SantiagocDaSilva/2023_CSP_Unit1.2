while (turns < 10) and not gameOver:
    turns += 1
    move1 = int(input("Where will you start, pick any of the numbers given"))
    board[move1 - 1] = "X"
    spaces.remove(move1 - 1)

    print_tic_tac_toe_board()

    gameOver = False
turns = 2
print_tic_tac_toe_board()
while (turns < 10) and not (gameOver):
    turns += 2
    move1 = int(input("My turn"))
    board[move1 - 2] = "O"
    spaces.remove(move1 - 1)

    print_tic_tac_toe_board()
