from aocd import get_data

dmap = []
currPos = (-1, -1)

data = get_data(day=3, year=2024).split("\n")
for i in range(len(data)):
	newLine = []
	for j in range(len(data[i])):
		if data[i][j] != "\n":
			newLine.append(data[i][j])
		if data[i][j] == "^":
			currPos = (i, j)
	dmap.append(newLine)


def moving(d_map, pos):
	directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
	d_order = ["N", "E", "S", "W"]
	d = "N"
	
	while True:
		dx, dy = directions[d]
		new_pos = (pos[0] + dx, pos[1] + dy)
		
		if not (0 <= new_pos[0] < len(d_map) and 0 <= new_pos[1] < len(d_map[0])):
			break
		
		if d_map[new_pos[0]][new_pos[1]] == "#":
			d = d_order[(d_order.index(d) + 1) % 4]
		else:
			pos = new_pos
			d_map[pos[0]][pos[1]] = "X"
	
	for row in d_map:
		print(row)
	
	return sum(row.count("X") for row in d_map)


print(moving(dmap, currPos))