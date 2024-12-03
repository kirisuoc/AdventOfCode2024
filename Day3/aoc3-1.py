import re

# Expresión regular para buscar la operación 'mul(a, b)'
patron = r"mul\((\d+),(\d+)\)"

total = 0
with open('input.txt', 'r') as file:
	cadena = file.read()

	# Buscar todas las coincidencias
	coincidencias = re.findall(patron, cadena)

for a, b in coincidencias:
	total += int(a) * int(b)

print(total)
