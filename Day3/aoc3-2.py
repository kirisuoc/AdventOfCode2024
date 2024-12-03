import re

# Expresión regular para buscar la operación 'mul(a, b)'
patron = r"mul\((\d+),(\d+)\)"

enable = True

total = 0
pos = 0

with open("input.txt", "r") as file:
	cadena = file.read()

while (pos < len(cadena)):
	# Buscamos las operaciones
	if cadena[pos:pos + 4] == "do()":
		enable = True
		pos += 4
	elif cadena[pos:pos + 7] == "don't()":
		enable = False
		pos += 7
	elif re.match(patron, cadena[pos:]):
		if enable:
			match = re.match(patron, cadena[pos:])
			a, b = int(match.group(1)), int(match.group(2))
			total += a * b
		# Avanzamos hasta el final de la operación mul(a, b)
		pos += cadena[pos:].find(')') + 1
	else:
		pos += 1

print(total)
