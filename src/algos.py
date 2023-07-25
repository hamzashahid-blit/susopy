import copy
from src.check import *

def backtrack (board: sboard) -> sboard:
    new_board = copy.deepcopy(board)
    fixed_cells = get_fixed_cells(board)
    is_backtracking = False
    print()
    print_board(new_board)
    print()
    print("Solving...")
    print()
    y = 0
    while y < 9:
        x = 0
        while x < 9:
            if (y, x) not in fixed_cells:
                while True:
                    if new_board[y][x] < 9: 
                        # Try cell till 9
                        is_backtracking = False
                        new_board[y][x] += 1
                    else: 
                        # Backtrack 
                        is_backtracking = True
                        new_board[y][x] = 0
                        while True:
                            if y == 0 and x == 0: # No solution (Trying to backtrack 1st row, 1st col)
                                return None
                            elif x == 0: # First col
                                y -= 1
                                x = 8
                            else: # Normal case
                                x -= 1
                            if (y, x) not in fixed_cells: break
                    if check_board(new_board, True) or is_backtracking: break
            if not is_backtracking: x += 1
        if not is_backtracking: y += 1
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
