with open("inputtest.txt") as file:
	map = [list(line) for line in file.read().splitlines()]

patrol_position = []

def get_patrol_position(array):
	for i in range(len(array)):
		for j in range(len(array[0])):
			if array[i][j] in ('<', '>', '^', 'v'):
				print(i, j)
				return i, j

init_pos = get_patrol_position(map)
pos_row, pos_col = init_pos
visited_pos = 0


def check_outside(row, col, map):
	# Verifica si las coordenadas (x, y) están fuera de los límites del mapa
	if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]):
		return True  # El movimiento está fuera del mapa
	return False  # El movimiento está dentro del mapa


def moveleft(map):
	global pos_row, pos_col, visited_pos
	print('left')
	pos_col -= 1
	visited_pos += 1
	map[pos_row][pos_col] = '<'

def moveright(map):
	global pos_row, pos_col, visited_pos
	print('right')
	pos_col += 1
	visited_pos += 1
	map[pos_row][pos_col] = '>'

def moveup(map):
	global pos_row, pos_col, visited_pos
	print('up')
	pos_row -= 1
	visited_pos += 1
	map[pos_row][pos_col] = '^'

def movedown(map):
	global pos_row, pos_col, visited_pos
	print('down')
	pos_row += 1
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


# Ejemplo de ejecución
while True:
	if not move_patrol(map):  # Mueve el patrullero y detiene el ciclo si sale del mapa
		print(visited_pos)
		break
"""
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
for row in map:
	print(''.join(row))
print(pos_row, pos_col)
move_patrol(map)
 """
