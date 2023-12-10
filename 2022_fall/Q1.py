# A.
board = [['-'] * 3] * 3
board[1][2] = 'X'
print(f'A: {board}')

# B.
board = [['-'] * 3 for row in range(3)]
board[1][2] = 'X'
print(f'B: {board}')

# C.
row = ['-'] * 3
board = []
for _ in range(3):
    board.append(row)
board[1][2] = 'X'
print(f'C: {board}')

# D.
board = []
for _ in range(3):
    row = ['-'] * 3
    board.append(row)
board[1][2] = 'X'
print(f'D: {board}')

# E. All of these code snippets will create that specific data structure stored in board, Chris
# F. None of these snippets will create that specific data structure stored in board, Chris.
