# Inicializamos las listas
columna1 = []
columna2 = []

# Procesamos los datos línea por línea
with open('input.txt', 'r') as file:
	for linea in file:
		value1, value2 = map(int, linea.split())	# Convertimos los valores a enteros
		columna1.append(value1)
		columna2.append(value2)

# Ordenamos las listas
sorted_list1 = sorted(columna1)
sorted_list2 = sorted(columna2)

total = 0
for i in range(len(columna1)):
	total += abs(sorted_list1[i] - sorted_list2[i])

print(total)
