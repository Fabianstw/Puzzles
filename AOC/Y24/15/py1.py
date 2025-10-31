def readInput():
	mat = []
	moves = []
	init = []
	matStill = True
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for j, line in enumerate(data):
			if line == '\n':
				matStill = False
				continue
			if matStill:
				extendMat = []
				for i in range(len(line)):
					if line[i] == '\n':
						continue
					extendMat.append(line[i])
					if line[i] == '@':
						init = [j, i]
				mat.append(extendMat)
			else:
				moves.append(line.strip())
	return mat, moves, init


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def checkBehind(mat, pos, x, y):
	while mat[pos[0] + x][pos[1] + y] == 'O':
		pos = [pos[0] + x, pos[1] + y]
		if mat[pos[0] + x][pos[1] + y] == '.':
			return True, [pos[0] + x, pos[1] + y]
	return False, []


def simulateRobot(mat, moves, init):
	pos = init
	for move in moves:
		for i in range(len(move)):
			x, y = directions[move[i]]
			if mat[pos[0] + x][pos[1] + y] == '.':
				mat[pos[0]][pos[1]] = '.'
				pos = [pos[0] + x, pos[1] + y]
				mat[pos[0]][pos[1]] = '@'
				continue
			if mat[pos[0] + x][pos[1] + y] == '#':
				continue
			if mat[pos[0] + x][pos[1] + y] == 'O':
				valid, newPos = checkBehind(mat, pos, x, y)
				if valid:
					mat[newPos[0]][newPos[1]] = 'O'
					mat[pos[0]][pos[1]] = '.'
					pos = [pos[0] + x, pos[1] + y]
					mat[pos[0]][pos[1]] = '@'
	return mat


def calcGPS(mat):
	res = 0
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if mat[i][j] == 'O':
				res += 100 * i + j
	return res


if __name__ == '__main__':
	m, mo, ini = readInput()
	m = simulateRobot(m, mo, ini)
	print(calcGPS(m))
	