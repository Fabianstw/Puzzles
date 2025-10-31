def readInput():
	start, end = (-1, -1), (-1, -1)
	track = set()
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for i in range(len(data)):
			data[i] = data[i].strip().replace('\n', '')
			for j in range(len(data[i])):
				if data[i][j] != '#':
					track.add((i, j))
				if data[i][j] == 'S':
					start = (i, j)
				if data[i][j] == 'E':
					end = (i, j)
	return start, end, track


distances = {}
shorties = {}

def findPath(start, end, track, shortcuts = False):
	queue = [(start, 0)]
	visited = set()
	visited.add(start)
	while queue:
		coord, dist = queue.pop(0)
		distances[coord] = dist
		visited.add(coord)
		if coord == end:
			return dist
		for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			newCoord = (coord[0] + x, coord[1] + y)
			if newCoord in track and newCoord not in visited:
				queue.append((newCoord, dist + 1))
		if shortcuts:
			for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				newCoord = (coord[0] + x, coord[1] + y)
				if newCoord in track:
					continue
				newCoord = (coord[0] + x * 2, coord[1] + y * 2)
				if newCoord in track:
					shortDistance = distances[newCoord] - distances[coord] - 2
					if shortDistance > 0:
						if shortDistance not in shorties:
							shorties[shortDistance] = [coord]
						else:
							shorties[shortDistance].append(coord)
	return -1


if __name__ == '__main__':
	s, e, t = readInput()
	findPath(s, e, t)
	findPath(s, e, t, True)
	res = 0
	for s in shorties:
		if s >= 100:
			res += len(shorties[s])
	print(res)
	# print(len(shorties[64]))