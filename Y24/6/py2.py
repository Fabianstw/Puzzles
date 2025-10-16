import copy
from aocd import get_data

# too high 2140

dmap = []
initPos = (-1, -1)

data = get_data(day=3, year=2024).split("\n")
for i in range(len(data)):
	newLine = []
	for j in range(len(data[i])):
		if data[i][j] != "\n":
			newLine.append(data[i][j])
		if data[i][j] == "^":
			initPos = (i, j)
	dmap.append(newLine)


directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
d_order = ["N", "E", "S", "W"]


def doesLoop(d_map, pos, dir):
	visited = set()
	
	while True:
		if (pos, dir) in visited:
			return 1
		visited.add((pos, dir))
		
		dx, dy = directions[dir]
		new_pos = (pos[0] + dx, pos[1] + dy)
		
		if not (0 <= new_pos[0] < len(d_map) and 0 <= new_pos[1] < len(d_map[0])):
			return 0
		if d_map[new_pos[0]][new_pos[1]] == "#":
			dir = d_order[(d_order.index(dir) + 1) % 4]
		else:
			pos = new_pos


usedPos = set()

def moving(d_map, pos):
	d = "N"
	loop_res = 0
	
	while True:
		dx, dy = directions[d]
		new_pos = (pos[0] + dx, pos[1] + dy)
		
		if not (0 <= new_pos[0] < len(d_map) and 0 <= new_pos[1] < len(d_map[0])):
			break
		
		if d_map[new_pos[0]][new_pos[1]] == "#":
			d_map[pos[0]][pos[1]] = "+"
			d = d_order[(d_order.index(d) + 1) % 4]
		else:
			# create a deepcopy of d_map
			if new_pos != initPos and new_pos not in usedPos:
				usedPos.add(new_pos)
				d_map_copy = copy.deepcopy(d_map)
				d_map_copy[new_pos[0]][new_pos[1]] = "#"
				loop_res += doesLoop(d_map_copy, pos, d_order[(d_order.index(d) + 1) % 4])
			pos = new_pos
			if d == "N" or d == "S":
				d_map[pos[0]][pos[1]] = "|"
			else:
				d_map[pos[0]][pos[1]] = "-"
				
	for row in d_map:
		print(row)
	
	return loop_res


print(moving(dmap, initPos))