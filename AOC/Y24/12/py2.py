def readInput():
	mat = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			mat.append(list(line.strip()))
	return mat


seen = set()


def findRegion(mat, i, j):
	region = [(i, j)]
	queue = [(i, j)]
	seen.add((i, j))
	while queue:
		x, y = queue.pop(0)
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nx, ny = x + dx, y + dy
			if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and (nx, ny) not in seen:
				if mat[nx][ny] == mat[i][j]:
					queue.append((nx, ny))
					region.append((nx, ny))
					seen.add((nx, ny))
	return region


def computeNumberOfSides(region):
	total = 0
	min_y = min(y for y, _ in region)
	max_y = max(y for y, _ in region)
	min_x = min(x for _, x in region)
	max_x = max(x for _, x in region)
	
	edges = {}
	for y in range(min_y, max_y + 1):
		prevIn = False
		nextEdges = {}
		for x in range(min_x, max_x + 2):
			if ((y, x) in region) != prevIn:
				prevIn = not prevIn
				nextEdges[x] = prevIn
				if edges.get(x) != prevIn:
					total += 1
		edges = nextEdges
	
	return total*2
	

def findEachRegion(mat):
	res = 0
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if (i, j) not in seen:
				newRegion = findRegion(mat, i, j)
				res += len(newRegion) * computeNumberOfSides(newRegion)
	return res


if __name__ == '__main__':
	m = readInput()
	print(findEachRegion(m))
