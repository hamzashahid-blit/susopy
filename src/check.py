# Sudoku board -> sboard
sboard = [[int]]
sgroup = sboard
my_board = [[0]*9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        my_board[i][j] = j

class InvalidCell(Exception): pass
class InvalidVector(Exception): pass
class InvalidIndex(Exception): pass

def check_cell (num: int):
    if num == 0: return
    if num < 1 or num > 9:
        raise InvalidCell("Value out of range 0-9 (1-9 and 0 for empty)") 

def check_index (index: int):
        if type(index) != int or index < 0 or index > 8:
                raise InvalidIndex("Index out of range 0-8")

collection = (list, tuple, range, set)
def flatten(iterable: collection) -> list:
    def generator(something):
        for elem in something:
            if isinstance(elem, collection):
                yield from flatten(elem)
            else:
                yield elem
    return list(generator(iterable))

# vector = row or column
def is_vector_valid (vector: list, allow_empty: bool = False) -> bool:
    "A vector can be a row, column or flattened group"
    if len(vector) != 9: raise InvalidVector("Length of vector != 9")
    count = [0]*9
    for num in vector:
        if num == 0: # Empty cell
            if allow_empty: continue # Ignore it
            else: return False # Throw a tantrum
        check_cell(num)
        if count[num-1] != 1:
            count[num-1] += 1
        else:
            return False
    return True

def is_group_valid (group: sgroup, allow_empty: bool = False) -> bool:
    # group is technically just a long row/col when flattened
    return is_vector_valid(flatten(group), allow_empty)

# num is zero-indexed 
def get_group (board: sboard, index: int) -> sgroup:
    check_index(index)
    col = (index % 3) * 3
    row = (index // 3) * 3 
    group = [[0]*3 for _ in range(3)]
    x = y = 0
    for i in range(row, row+3):
        for j in range(col, col+3):
            group[x][y] = board[i][j]
            y = (y + 1) % 3 # Increment but loop at 3
        x += 1
    return group

def get_cols(board: sboard) -> [[int]]:
    return [[board[j][i] for j in range(9)] for i in range(9)]

def get_rows(board: sboard) -> [[int]]:
    return [board[i] for i in range(9)]

def get_groups(board: sboard) -> [sgroup]:
    return [get_group(board, i) for i in range(9)]

def check_board (board: sboard, allow_empty: bool = False) -> [[bool]]:
    is_cols_valid = all([is_vector_valid(col, allow_empty) for col in get_cols(board)])
    is_rows_valid = all([is_vector_valid(row, allow_empty) for row in get_rows(board)])
    is_groups_valid = all([is_group_valid(group, allow_empty) for group in get_groups(board)])
    return is_cols_valid and is_rows_valid and is_groups_valid

if __name__ == "__main__":
    check_board(my_board)
