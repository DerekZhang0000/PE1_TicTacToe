import random

board = [1, 2, 3, 4, "X", 6, 7, 8, 9]
def display_board(board):
    print("+", "+", "+", "+", sep="-" * 7)
    print("|", "|", "|", "|", sep="       ")
    print("|   ", board[0], "   |   ", board[1], "   |   ", board[2], "   |", sep="")
    print("|", "|", "|", "|", sep="       ")
    print("+", "+", "+", "+", sep="-" * 7)
    print("|", "|", "|", "|", sep="       ")
    print("|   ", board[3], "   |   ", board[4], "   |   ", board[5], "   |", sep="")
    print("|", "|", "|", "|", sep="       ")
    print("+", "+", "+", "+", sep="-" * 7)
    print("|", "|", "|", "|", sep="       ")
    print("|   ", board[6], "   |   ", board[7], "   |   ", board[8], "   |", sep="")
    print("|", "|", "|", "|", sep="       ")
    print("+", "+", "+", "+", sep="-" * 7)

def enter_move(board):
    try:
        user_move = int(input("Enter a number: "))
        while user_move not in make_list_of_free_fields(board):
            print("Please enter a valid space.")
            user_move = int(input("Enter a number: "))
        board[user_move - 1] = "O"
        display_board(board)
        victory_for(board, "O")
    except:
        print("Please enter a valid input.")

def make_list_of_free_fields(board):
    returnBoard = []
    for i in board:
        if type(i) == int:
            returnBoard.append(i)
    # print(returnBoard)
    return returnBoard

def victory_for(board, sign):
    winner = "none"
    global game_over
    if board[0] == board [1] == board[2] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[3] == board [4] == board[5] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[6] == board [7] == board[8] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[0] == board [3] == board[6] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[1] == board [4] == board[7] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[2] == board [5] == board[8] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[0] == board [4] == board[8] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    elif board[2] == board [4] == board[6] == sign:
        if sign == "O":
            winner = "user"
        else:
            winner = "computer"
    if winner == "user":
        print("User wins!")
        game_over = True
    elif winner == "computer":
        print("Computer wins!")
        game_over = True
    elif len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        game_over = True

def draw_move(board):
    computer_move = random.randint(1,9)
    while computer_move not in make_list_of_free_fields(board):
        computer_move = random.randint(1,9)
    board[computer_move - 1] = "X"
    display_board(board)
    victory_for(board, "X")

game_over = False
display_board(board)
while True:
    enter_move(board)
    if game_over:
        break
    draw_move(board)
    if game_over:
        break