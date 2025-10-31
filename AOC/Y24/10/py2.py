def readInput():
	mat = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			newLine = list(map(int, line.strip()))
			mat.append(newLine)
	return mat


def findZeros(mat):
	zeroes = []
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == 0:
				zeroes.append((i, j))
	return zeroes


def runBFS(mat, start):
	queue = [(start[0], start[1], 0)]
	highPoints = 0
	while queue:
		x, y, r = queue.pop(0)
		if r == 9:
			highPoints += 1
			continue
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Four possible directions
			nx, ny = x + dx, y + dy
			if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and (nx, ny, r+1):
				if mat[nx][ny] == r + 1:
					queue.append((nx, ny, r+1))
	return highPoints


if __name__ == '__main__':
	mat = readInput()
	zeroes = findZeros(mat)
	res = 0
	for zero in zeroes:
		c = runBFS(mat, zero)
		res += c
	print(res)
	
	