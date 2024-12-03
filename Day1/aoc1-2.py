# Inicializamos las listas
columna1 = []
columna2 = []

# Procesamos los datos línea por línea
with open('input.txt', 'r') as file:
	for linea in file:
		value1, value2 = map(int, linea.split())	# Convertimos los valores a enteros
		columna1.append(value1)
		columna2.append(value2)

total = 0
for value in columna1:
	total += columna2.count(value) * value

print(total)
