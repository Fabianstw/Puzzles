def readInput():
	coords = set()
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		count = 0
		for line in data:
			sp = line.strip().split(',')
			coords.add((int(sp[0]), int(sp[1])))
			count += 1
			if count == 1024:
				break
	return coords
	

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


if __name__ == "__main__":
	c = readInput()
	print(simulate((0, 0), (70, 70), c))
