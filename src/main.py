# Sudoku board -> sboard
sboard = list[list[int]]
sgroup = sboard
my_board = [[0]*9 for _ in range(9)]
for i in range(9):
	for j in range(9):
		my_board[i][j] = j

class InvalidCell(Exception): pass
class InvalidVector(Exception): pass
class InvalidIndex(Exception): pass
		
def check_cell (num: int):
	if num is None: return
	if num < 0 or num > 8:
		raise InvalidCell("Value out of range 0-8") 

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
def is_vector_valid (vector: list) -> bool:
	if len(vector) != 9: raise InvalidVector("Length of vector != 9")
	count = [0]*9
	for num in vector:
		if num is None: return False
		check_cell(num)
		if count[num] != 1:
			count[num] += 1
		else:
			return False
	return True

# num is zero-indexed 
def get_group (board: sboard, index: int) -> sgroup:
	check_index(index)
	col = (index % 3) * 3
	row = (index // 3) * 3 
	group = [[None]*3 for _ in range(3)]
	x = y = 0
	for i in range(row, row+3):
		for j in range(col, col+3):
			group[x][y] = board[i][j]
			y = (y + 1) % 3 # Increment but loop at 3
		x += 1
	return group

def is_group_valid (group: sgroup) -> bool:
	# group is technically just a long row/col when flattened
	return is_vector_valid(flatten(group))

def check_board (board: sboard) -> list[list[bool]]:
	pass
	# cols = [[board[j][i] for j in range(9)] for i in range(9)]
	# rows = [board[i] for i in range(9)]
	# groups = [get_group(board, i) for i in range(9)]
	# is_cols_valid = [is_vector_valid(col) for col in cols]
	# is_rows_valid = [is_vector_valid(row) for row in rows]
	# is_groups_valid = [is_group_valid(group) for group in groups]
	# # print(is_groups_valid)

# print(check_board(my_board))
# print(is_group_valid(get_group(my_board, 0)))

# print(is_vector_valid([0,1,2,3,1000]))
 
if __name__ == "__main__":
	check_board(my_board)
