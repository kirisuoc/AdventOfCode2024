def is_sorted(lst):
		return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def are_differences_valid(lst):
		return all(1 <= abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))

with open("input.txt", "r") as file:
	data = file.read()

	lista = [list(map(int, line.split())) for line in data.strip().split("\n")]


total_valid_list = 0
for inner_list in lista:
	if is_sorted(inner_list) and are_differences_valid(inner_list):
		total_valid_list += 1

print(total_valid_list)
