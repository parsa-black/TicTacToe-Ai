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


def terminal(row):
    return True if row.conunt(row[0]) == 3 else False


# return player who has the next turn
def turn(board):
    count_X = 0
    count_O = 0

    for i in board:
        for j in i:
            if j == "X":
                count_X += 1  # count = count + 1
            if j == "O":
                count_O += 1  # count = count + 1
    if count_X > count_O:
        return O
    else:
        return X
