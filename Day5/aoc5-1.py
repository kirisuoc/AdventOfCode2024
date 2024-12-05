with open("input.txt") as file:
	text = file.read()

# Dividimos el texto en dos textos por la línea en blanco
partes = text.split("\n\n")

# Procesamos la primera parte
relations = [tuple(map(int, pair.split("|"))) for pair in partes[0].splitlines()]

# Procesamos la segunda parte
number_lists = [list(map(int, line.split(","))) for line in partes[1].splitlines()]

def parse_relations(relations):
	'''
	Convierte la lista de relaciones en un diccionario donde
	cada número apunta a los números que deben ir después de él.
	'''
	relation_dict = {}
	for a, b in relations:
		if a not in relation_dict:
			relation_dict[a] = set()
		relation_dict[a].add(b)
	return relation_dict

def is_valid_list(numbers, relation_dict):
	'''
	Verifica si la lista de números respeta las relaciones dadas.
	'''
	seen = set()
	for num in numbers:
		if num in relation_dict:
			if any(after in seen for after in relation_dict[num]):
				return False
		seen.add(num)
	return True

def sum_of_middles(relations, number_lists):
    """
    Calcula la suma de los números centrales de todas las listas válidas.
    """
    relation_dict = parse_relations(relations)
    middle_sum = 0

    for number_list in number_lists:
        if is_valid_list(number_list, relation_dict):
            # Encontrar el número en el medio de la lista
            mid_index = len(number_list) // 2  # Índice del número en el medio
            middle_sum += number_list[mid_index]  # Sumar el número en el medio

    return middle_sum

valid_count = sum_of_middles(relations, number_lists)
print(valid_count)
