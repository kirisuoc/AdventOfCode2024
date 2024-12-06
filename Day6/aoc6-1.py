with open("input.txt") as file:
	map = [list(line) for line in file.read().splitlines()]

patrol_position = []

def get_patrol_position(array):
	for i in range(len(array)):
		for j in range(len(array[0])):
			if array[i][j] in ('<', '>', '^', 'v'):
				return i, j

init_pos = get_patrol_position(map)
pos_row, pos_col = init_pos
visited_pos = 1

def check_outside(row, col, map):
	if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]):
		return True
	return False


def moveleft(map):
	global pos_row, pos_col, visited_pos
	#print('left')
	pos_col -= 1
	if map[pos_row][pos_col] == '.':
		visited_pos += 1
	map[pos_row][pos_col] = '<'

def moveright(map):
	global pos_row, pos_col, visited_pos
	#print('right')
	pos_col += 1
	if map[pos_row][pos_col] == '.':
		visited_pos += 1
	map[pos_row][pos_col] = '>'

def moveup(map):
	global pos_row, pos_col, visited_pos
	#print('up')
	pos_row -= 1
	if map[pos_row][pos_col] == '.':
		visited_pos += 1
	map[pos_row][pos_col] = '^'

def movedown(map):
	global pos_row, pos_col, visited_pos
	#print('down')
	pos_row += 1
	if map[pos_row][pos_col] == '.':
		visited_pos += 1
	map[pos_row][pos_col] = 'v'


def move_patrol(map):
	global pos_row, pos_col, visited_pos
	ppos_row, ppos_col = pos_row, pos_col

	if map[pos_row][pos_col] == '<':
		if check_outside(pos_row, pos_col - 1, map):
			return False
		elif map[pos_row][pos_col - 1] == '#':
			moveup(map)
		else:
			moveleft(map)
	elif map[pos_row][pos_col] == '>':
		if check_outside(pos_row, pos_col + 1, map):
			return False
		elif map[pos_row][pos_col + 1] == '#':
			movedown(map)
		else:
			moveright(map)
	elif map[pos_row][pos_col] == '^':
		if check_outside(pos_row - 1, pos_col, map):
			return False
		elif map[pos_row - 1][pos_col] == '#':
			moveright(map)
		else:
			moveup(map)
	elif map[pos_row][pos_col] == 'v':
		if check_outside(pos_row + 1, pos_col, map):
			return False
		elif map[pos_row + 1][pos_col] == '#':
			moveleft(map)
		else:
			movedown(map)
	map[ppos_row][ppos_col] = 'X'
	return True

while True:
	if not move_patrol(map):
		print(visited_pos)
		break
