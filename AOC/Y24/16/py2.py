import heapq

def readInput():
	mat = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			mat.append(list(line.strip()))
	return mat


def simulate(mat, start, end, face="E"):
	directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
	rows, cols = len(mat), len(mat[0])
	dist = [[float('inf')] * cols for _ in range(rows)]
	dist[start[0]][start[1]] = 0
	visited = set()
	minHeap = [(0, start, face)]
	
	while minHeap:
		d, (x, y), face = heapq.heappop(minHeap)
		if (x, y, face) in visited:
			continue
		visited.add((x, y, face))
		
		for direction, (dx, dy) in directions.items():
			nx, ny = x + dx, y + dy
			if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] != "#":
				cost = d + (1 if face == direction else 1001)
				if dist[nx][ny] > cost:
					dist[nx][ny] = cost
				heapq.heappush(minHeap, (cost, (nx, ny), direction))
	
	# for row in dist:
	# 	print(' '.join(f'{d:5}' for d in row))
	return dist[end[0]][end[1]]


def countTiles(mat, start, end, dist):
	directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
	rows, cols = len(mat), len(mat[0])
	visited = set()
	uniques = {(start[0], start[1])}
	stack = [(0, start, "E")]
	
	while stack:
		d, (x, y), face= stack.pop()
		if (x, y, face) in visited:
			continue
		visited.add((x, y, face))
		for direction, (dx, dy) in directions.items():
			nx, ny = x + dx, y + dy
			if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] != "#":
				newCost = d + (1 if face == direction else 1001)
				if simulate(mat, (nx, ny), end, direction) + newCost == dist:
					uniques.add((nx, ny))
					stack.append((newCost, (nx, ny), direction))
	return len(uniques)


if __name__ == '__main__':
	m = readInput()
	s = [len(m) - 2, 1]
	e = [1, len(m[0]) - 2]
	cacheDist = simulate(m, s, e)
	print(countTiles(m, s, e, cacheDist))
# 143564
