def readInput():
	coords = set()
	newCoords = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		count = 0
		for line in data:
			sp = line.strip().split(',')
			count += 1
			if count > 1024:
				newCoords.append((int(sp[0]), int(sp[1])))
			else:
				coords.add((int(sp[0]), int(sp[1])))
	return coords, newCoords


def simulate(start, end, coords):
	queue = [(start, 0)]
	while queue:
		coord, dist = queue.pop(0)
		if coord == end:
			return dist
		for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			new_coord = (coord[0] + x, coord[1] + y)
			if new_coord not in coords and 0 <= new_coord[0] <= end[0] and 0 <= new_coord[1] <= end[0]:
				queue.append((new_coord, dist + 1))
				coords.add(new_coord)
	return -1


"""
Could be improve with Binary Search, but this works
"""
def findFirstBlock(start, end, coords, newCoords):
	for coord in newCoords:
		coords.add(coord)
		if simulate(start, end, coords.copy()) == -1:
			return coord


if __name__ == "__main__":
	c, nc = readInput()
	print(findFirstBlock((0, 0), (70, 70), c, nc))
