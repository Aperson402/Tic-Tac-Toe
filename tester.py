import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None


board = [[X,X ,O ],
            [X,X,O],
            [X, O,X]]
#print(ttt.player(board))
print(ttt.winner(board))
print(ttt.utility(board))