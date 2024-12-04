with open("input.txt") as file:
	data = file.read()

	lista = data.splitlines()

total = 0

# Función para contar las ocurrencias en una lista de strings
def count_word_occurrences(data, word):
	count = 0
	word_len = len(word)

	# Horizontal (líneas)
	for line in data:
		for i in range(len(line) - word_len + 1):
			if line[i:i+word_len] == word:
				count += 1

	# Vertical (columnas)
	num_rows = len(data)
	num_cols = len(data[0])
	for col in range(num_cols):
		for row in range(num_rows - word_len + 1):
			vertical_word = ''.join([data[row + i][col] for i in range(word_len)])
			if vertical_word == word:
				count += 1

	# Diagonal (de arriba a la izquierda hacia abajo a la derecha)
	for row in range(num_rows - word_len + 1):
		for col in range(num_cols - word_len + 1):
			diagonal_word = ''.join([data[row + i][col + i] for i in range(word_len)])
			if diagonal_word == word:
				count += 1

	# Diagonal secundaria (de arriba a la derecha hacia abajo a la izquierda)
	for row in range(num_rows - word_len + 1):
		for col in range(word_len - 1, num_cols):
			diagonal_word = ''.join([data[row + i][col - i] for i in range(word_len)])
			if diagonal_word == word:
				count += 1

	return count

# Contamos las ocurrencias de "XMAS" y "SAMX"
total += count_word_occurrences(lista, "XMAS")
total += count_word_occurrences(lista, "SAMX")
print(total)
