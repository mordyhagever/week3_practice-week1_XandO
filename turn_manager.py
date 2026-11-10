from validations import *

from XOdatabase import board, WINNING_LINES

def print_board():
    print(f"""
[1]{board[0]}  |  [2]{board[1]}  |  [3]{board[2]}
------+-------+----
[4]{board[3]}  |  [5]{board[4]}  |  [6]{board[5]}
------+-------+----
[7]{board[6]}  |  [8]{board[7]}   | [9]{board[8]}
    """)

def game_finished(user):
    for pattern in WINNING_LINES:
        if board[pattern[0]] == user and board[pattern[1]] == user and board[pattern[2]] == user:
            return True
    return False

def is_table_full():
    count = 0
    for square in board:
        if square == "X" or square == "Y":
            count += 1
    if count == 9:
        return True
    return False

def add_turn(last_move):
    print_board()
    this_turn = None
    if last_move == "X":
        this_turn = "O"
    elif last_move == "O":
        this_turn = "X"
    print(f"{this_turn} it's your turn, choose a square")
    square = input()
    while not check_square(square):
        square = input("square doesn't exist: ")
    square = int(square)
    while board[square - 1] == "X" or board[square - 1] == "O":
        square = input("square isn't available: ")
        while not check_square(square):
            square = input("square doesn't exist: ")
        square = int(square)
    board[square-1] = this_turn

    if game_finished(this_turn):
        print_board()
        return this_turn

    elif is_table_full():
        print_board()
        return "noone"
    return "game is on"

def game_manager():
    count = 1
    turn = add_turn("O")
    this_turn = None
    while turn == "game is on":
        count += 1
        if count % 2 == 0:
            this_turn = "X"
        else:
            this_turn = "O"
        turn = add_turn(this_turn)
    if turn == "X":
        return "X has one the game"
    elif turn == "O":
        return "O has one the game"
    return "The game has finished with a tie"





