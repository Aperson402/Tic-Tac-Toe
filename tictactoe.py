"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_of_empty=sum([row.count(EMPTY) for row in board])
    if count_of_empty % 2 == 0:
        return "O"
    else:
        return "X"
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    empty_cells_matrix = [map(lambda i: i == EMPTY, tile) for tile in board]
    for i, row in enumerate(empty_cells_matrix):
        for j, tile in enumerate(row):
            if tile is True:
                action = (i, j)
                possible_actions.add(action)
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        current_player = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = current_player
        # print(new_board)
        return new_board
    else:
        raise Exception("Action invalid!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_horizontal(board) != None:
        return check_horizontal(board)
    elif check_vertical(board) != None:
        return check_vertical(board)
    elif check_diagonal(board) != None:
        return check_diagonal(board)
    elif len(actions(board)) == 0:
        return None
    else:
        return None

def check_horizontal(board):
    for row in board:
        if row.count(X)==3:
            return X
        elif row.count(O)==3:
            return O
        
    return None

def check_vertical(board):
    for i in range(len(board)):
        col=[board[0][i],board[1][i],board[2][i]]
        if col.count(X)==3:
            return X
        elif col.count(O)==3:
            return O
        
    return None

def check_diagonal(board):
    diagonal_one = [board[0][0], board[1][1], board[2][2]]
    diagonal_two = [board[0][2], board[1][1], board[2][0]]

    if diagonal_one.count(X) == 3 or diagonal_two.count(X) == 3:
        return X
    elif diagonal_one.count(O) == 3 or diagonal_two.count(O) == 3:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_won, no_more_moves = winner(board) != None, len(actions(board)) == 0
    return True if game_won or no_more_moves else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = {
        X: 1,
        None: 0,
        O: -1
    }

    evaluator = winner(board)
    return utility.get(evaluator)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float('-inf')
    Min = float('inf')

    if player(board) is X:
        return max_value(board, Max, Min)[1]
    else:
        return min_value(board, Max, Min)[1]


def max_value(board, Max, Min):
    """
    Returns tuple with best move and value
    """
    if terminal(board):
        return [utility(board), None]

    best_move = None
    value = float('-inf')
    possible_actions = actions(board)
    for action in possible_actions:
        new_board_state = result(board, action)
        move_value = min_value(new_board_state, Max, Min)[0]
        Max = max(Max, move_value)
        if move_value > value:
            value, best_move = move_value, action
        if Max >= Min:
            break
    return tuple([value, best_move])

def min_value(board: list, Max: float, Min: float) -> tuple:
    """
    Returns the value and optimal action (v, a) that gives O (min) player minimum score.
    Starts with worst value of +infinity and wants a -1 for a win.
    """
    if terminal(board):
        return [utility(board), None]

    best_move = None
    value = float('inf')
    possible_actions = actions(board)
    for action in possible_actions:
        new_board_state = result(board, action)
        move_value = max_value(new_board_state, Max, Min)[0]
        Min = min(Min, move_value)
        if move_value < value:
            value, best_move = move_value, action
        if Max >= Min:
            break
    return tuple([value, best_move])