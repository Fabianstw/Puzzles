from aocd import get_data

lines = []
search = ['X', "M", "A", "S"]
res = 0

data = get_data(day=3, year=2024).split("\n")
for line in data:
	lines.append(list(line.rstrip()))
		

for i in range(len(lines)):
	for j in range(len(lines[0])):
		if j >= 3:
			if lines[i][j-4:j][::-1] == search:
				res += 1
		if j <= len(lines[0]) - 4:
			if lines[i][j:j+4] == search:
				res += 1

for j in range(len(lines[0])):
	for i in range(len(lines)):
		if i <= len(lines) - 4:
			vertical = [lines[i+k][j] for k in range(4)]
			if vertical == search:
				res += 1
			if vertical[::-1] == search:
				res += 1

for i in range(len(lines) - 3):
	for j in range(len(lines[0]) - 3):
		diagonal_down = [lines[i+k][j+k] for k in range(4)]
		if diagonal_down == search:
			res += 1
		if diagonal_down[::-1] == search:
			res += 1

for i in range(len(lines) - 3):
	for j in range(3, len(lines[0])):
		diagonal_up = [lines[i+k][j-k] for k in range(4)]
		if diagonal_up == search:
			res += 1
		if diagonal_up[::-1] == search:
			res += 1
				
print(res)
