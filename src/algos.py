import copy
from src.check import *

def backtrack_recursive (board: sboard) -> sboard:
    x = 0
    while x < 9:
        y = 0
        while y < 9:
            cell = board[x][y]
            if cell == 0:
                for i in range(1, 10):
                    board[x][y] = i
                    if check_board(board):
                        board[x][y] = n
                        backtrack_recursive(board)
                        board[x][y] = 0
                return
    print_board(board)
                        

def backtrack (board: sboard) -> sboard:
    new_board = copy.deepcopy(board)
    fixed_cells = get_fixed_cells(board)
    is_backtracking = False
    i = -1
    while i < 9:
        i += 1
        j = -1
        while j < 9:
            j += 1
            cell = new_board[i][j]
            if (i, j) in fixed_cells:
                if is_backtracking:
                    if i == 0 and j == 0: # No solution...
                        return None
                    elif j == 0:
                        i -= 1
                        j = 9
                    else:
                        j -= 1
            else: #elif cell == 0 or is_backtracking:
                is_cell_valid = False
                if is_backtracking:
                    print("\nBACKTRACKED (i, j):", i, j)
                    if new_board[i][j] == 9: # Actually backtrack
                        print("\nBACKTRACKING (i, j):", i, j)
                        is_backtracking = True
                        new_board[i][j] = 0
                        if i == 0 and j == 0: # No solution...
                            return None
                        elif j == 0:
                            i -= 1
                            j = 9
                        else:
                            j -= 1
                        continue
                    else:
                        new_board[i][j] += 1
                    print("\nDONE SOMESHI (i, j):", i, j)
                    is_backtracking = False
                    is_cell_valid = check_board(new_board, True)
                while not is_cell_valid:
                    if new_board[i][j] == 9: # Actually backtrack
                        print("\nBACKTRACKING (i, j):", i, j)
                        is_backtracking = True
                        new_board[i][j] = 0
                        if i == 0 and j == 0: # No solution...
                            return None
                        elif j == 0:
                            i -= 1
                            j = 9
                        else:
                            j -= 1
                        break
                    new_board[i][j] += 1
                    is_cell_valid = check_board(new_board, True)
            print()
            print_board(new_board)
            print()
    return new_board

def get_fixed_cells (board: sboard) -> [(int, int)]:
    indexes = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                indexes.append((i, j))
    return indexes

def print_board (board: sboard):
    for row in board:
        for cell in row:
            if cell == 0:
                print(' ', end=' ')
            else:
                print(cell, end=' ')
        print()
