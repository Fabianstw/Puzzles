from aocd import get_data

def readInput():
	connections = {}
	dmap = []
	data = get_data(day=3, year=2024).split("\n")
	for i in range(len(data)):
		splitted = list(data[i])[0:len(data[i]) - 1]
		dmap.append(splitted)
		for j in range(len(splitted)):
			if splitted[j] == "." or splitted[j] == "\n":
				continue
			if splitted[j] in connections:
				connections[splitted[j]].append((i, j))
			else:
				connections[splitted[j]] = [(i, j)]
	
	return connections, dmap

res = set()
def antinode(pr1, pr2, dmap):
	x1, y1 = pr1
	x2, y2 = pr2
	newx = x2 + (x2 - x1)
	newy = y2 + (y2 - y1)
	if 0 <= newx < len(dmap[0]) and 0 <= newy < len(dmap):
		res.add((newx,newy))
		

def placeNodes(connections, dmap):
	for key in connections:
		for i in range(len(connections[key])):
			for j in range(i + 1, len(connections[key])):
				antinode(connections[key][i], connections[key][j], dmap)
				antinode(connections[key][j], connections[key][i], dmap)


if __name__ == "__main__":
	connections, dmap = readInput()
	placeNodes(connections, dmap)
	print(len(res))


# to high:
# 257

# too low:
# 245
# 234