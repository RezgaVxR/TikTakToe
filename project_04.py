"""Projecto de tic tac toe o tablero"""


def print_board(board):
    """Funcion que nos permite visualizar el tablero"""
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row)-1:
                row_str += " | "

        print(row_str)
        if i != len(board)-1:
            print("-----------")


def valid_input(promt):
    """Funcion para verificar que la entrada sea valida"""
    while True:
        value = input(promt)
        if not value.strip():
            print("You can't enter a empty value")
        else:
            try:
                return int(value)
            except ValueError:
                print("Please type a valid number")


def get_move(turn, board):
    """Funcion que nos permite identificar/realizar un movimiento"""
    while True:
        row = valid_input("Row: ")
        print()
        col = valid_input("Col: ")
        print()
        if row < 1 or row > len(board):
            print("Invalid row, try again!")
        elif col < 1 or col > len(board[row-1]):
            print("Invalid col, try again!")
        elif board[row-1][col-1] != " ":
            print("Already taken, please try again!")
        else:
            break
    board[row-1][col-1] = turn


def check_winner(board, turn):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break

        if win:
            return True

    return False


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
    print()
    print("It is the", turn, "players turn. Please select your move.")
    get_move(turn, board)
    print_board(board)
    winner = check_winner(board, turn)
    if winner:
        break

    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1

if turn_number == 9:
    print("Tied game")
else:
    print("The winner was", turn)
