from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def init_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def get_diagonal(board):
    return [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]


def get_columns(board):
    columns = []
    for i in range(3):
        columns.append([row[i] for row in board])

    return columns
