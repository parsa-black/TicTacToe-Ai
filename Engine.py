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


# Win position
def terminal_win(row):
    return True if row.count(row[0]) == 3 else False


# return player who has the next turn
def player(board):

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


# possible actions in the board
def actions(board):
    action = set()
    for i, row in enumerate(board):
        for j, worth in enumerate(row):
            if worth == EMPTY:
                action.add((i, j))
    return action


# result of actions in the board
def result(board, action):
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid Move")
    next_move = player(board)
    deep_board = deepcopy(board)
    deep_board[i][j] = next_move
    return deep_board


# Return Winner
def winner(board):

    rows = board + get_diagonal(board) + get_columns(board)
    for row in rows:
        current_player = row[0]
        if current_player is not None and terminal_win(row):
            return current_player
    return None


# End Position
def terminal(board):
    winner_player = winner(board)
    if winner_player is not None:
        return True
    if all(all(j != EMPTY for j in i) for i in board):
        return True
    return False


def value(board):
    winner_player = winner(board)
    if winner_player == X:
        return 1
    if winner_player == O:
        return -1
    else:
        return 0


# Max alpha-beta Pruning
def max_pruning(board, alpha, beta):
    if terminal(board):
        return value(board), None
    worth = float("-inf")
    best = None
    for action in actions(board):
        min_worth = min_pruning(result(board, action), alpha, beta)[0]
        if min_worth > worth:
            best = action
            worth = min_worth
        alpha = max(alpha, worth)
        if beta <= alpha:
            break
    return worth, best


# Min alpha-beta Pruning
def min_pruning(board, alpha, beta):
    if terminal(board):
        return value(board), None
    worth = float("inf")
    best = None
    for action in actions(board):
        max_worth = max_pruning(result(board, action), alpha, beta)[0]
        if max_worth < worth:
            best = action
            worth = max_worth
        beta = min(beta, worth)
        if beta <= alpha:
            break
    return worth, best


# MiniMax
def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        return max_pruning(board, float("-inf"), float("inf"))[1]
    elif player(board) == O:
        return min_pruning(board, float("-inf"), float("inf"))[1]
    else:
        raise Exception("Error in Calculation Optimal Move")
