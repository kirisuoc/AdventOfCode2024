with open("input.txt") as file:
	data = file.read()

	lista = data.splitlines()

# Función para comprobar si el patrón "MAS" o "SAM" forma una "X"
def count_x_pattern(data):
	total_x = 0
	rows = len(data)
	cols = len(data[0])

	# Recorremos todos los posibles centros de un bloque 3x3
	for i in range(1, rows - 1):  # Empezamos desde la fila 1 hasta la fila -1
		for j in range(1, cols - 1):  # Empezamos desde la columna 1 hasta la columna -1
			# Comprobamos la diagonal principal (arriba-izquierda a abajo-derecha)
			diagonal_principal = (data[i-1][j-1] in ['S', 'M'] and  # Diagonal principal (arriba-izquierda)
								data[i][j] == 'A' and
								# Si la primera letra es 'S', la tercera debe ser 'M'
								((data[i+1][j+1] == 'M' if data[i-1][j-1] == 'S' else False) or
								# Si la primera letra es 'M', la tercera debe ser 'S'
								(data[i+1][j+1] == 'S' if data[i-1][j-1] == 'M' else False)))

			# Comprobamos la diagonal secundaria (arriba-derecha a abajo-izquierda)
			diagonal_secundaria = (data[i-1][j+1] in ['S', 'M'] and  # Diagonal secundaria (arriba-derecha)
									data[i+1][j-1] in ['M', 'S'] and  # Diagonal secundaria (abajo-izquierda)
									data[i][j] == 'A' and
									# Si la primera letra es 'S', la tercera debe ser 'M'
									((data[i+1][j-1] == 'M' if data[i-1][j+1] == 'S' else False) or
									# Si la primera letra es 'M', la tercera debe ser 'S'
									(data[i+1][j-1] == 'S' if data[i-1][j+1] == 'M' else False)))

			# Si ambas diagonales cumplen la condición, incrementamos el contador
			if diagonal_principal and diagonal_secundaria:
				total_x += 1

	return total_x

# Contamos las "X" formadas por 'MAS' o 'SAM'
total_x = count_x_pattern(lista)
print(total_x)
