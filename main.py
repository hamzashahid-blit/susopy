# TODO: Implement tests

# Sudoku board -> sboard
sboard = list[list[int]]
sgroup = sboard
my_board = [[0]*9 for _ in range(9)]
for i in range(9):
	for j in range(9):
		my_board[i][j] = j

# num is zero-indexed 
def get_group (board: sboard, num: int) -> sgroup:
	if num < 0 or num > 8:
		raise Exception("Group num should be in the range 0-8")
	col = (num % 3) * 3
	row = num // 3
	group = [[None]*3 for _ in range(3)]
	x = y = 0
	for i in range(row, row+3):
		for j in range(col, col+3):
			group[x][y] = board[i][j]
			y = (y + 1) % 3 # Increment but loop at 3
		x += 1
	return group

def is_group_valid (group: sgroup) -> bool:
	count = [0]*9
	for i in range(9):
		for j in range(9):
			num = group[i][j]
			check_num(num)
			if count[num] != 1:
				count[num] += 1
			else: return False
	return True

# vector = row or column
def is_vector_valid (vector: list) -> bool:
	count = [0]*9
	for num in vector:
		check_num(num)
		if count[num] != 1:
			count[num] += 1
		else:
			return False
	return True

def check_num (num: int):
	if num < 0 or num > 9:
		raise Exception("Value out of range 0-9") 

def check_board (board: sboard) -> list[list[bool]]:
	# TODO: Finish this method
	cols = [[board[j][i] for j in range(9)] for i in range(9)]
	rows = [board[i] for i in range(9)]
	groups = [get_group(board, i) for i in range(9)]
	is_cols_valid = [is_vector_valid(col) for col in cols]
	is_rows_valid = [is_vector_valid(row) for row in rows]
	is_groups_valid = [is_group_valid(group) for group in groups]
	print(is_groups_valid)

# print(check_board(my_board))
print(is_group_valid(get_group(my_board, 0)))

# print(is_vector_valid([0,1,2,3,1000]))
