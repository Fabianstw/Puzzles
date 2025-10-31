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
					if line[i] == '@':
						init = [j, len(extendMat)]
						extendMat.append(line[i])
						extendMat.append(".")
					elif line[i] == 'O':
						extendMat.append("[")
						extendMat.append("]")
					else:
						extendMat.append(line[i])
						extendMat.append(line[i])
				mat.append(extendMat)
			else:
				moves.append(line.strip())
	return mat, moves, init


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def checkSides(mat, pos, x, y):
	while mat[pos[0] + x][pos[1] + y] == '[' or mat[pos[0] + x][pos[1] + y] == ']':
		pos = [pos[0] + x, pos[1] + y]
		if mat[pos[0] + x][pos[1] + y] == '.':
			return True
	return False


def flipSign(sign):
	if sign == "[":
		return "]"
	else:
		return "["


def updateSides(mat, pos, x, y):
	sign = flipSign(mat[pos[0] + x][pos[1] + y])
	mat[pos[0] + x][pos[1] + y] = "@"
	mat[pos[0]][pos[1]] = "."
	while mat[pos[0] + x][pos[1] + y] == '[' or mat[pos[0] + x][pos[1] + y] == ']' or mat[pos[0] + x][pos[1] + y] == '@':
		pos = [pos[0] + x, pos[1] + y]
		sign = flipSign(sign)
		if mat[pos[0] + x][pos[1] + y] == '.':
			mat[pos[0] + x][pos[1] + y] = sign
			return
		mat[pos[0] + x][pos[1] + y] = sign
	return


def checkVertical(mat, pos, x, y):
	if mat[pos[0] + x][pos[1] + y] == "[":
		level = [[pos[0] + x, pos[1] + y], [pos[0] + x, pos[1] + y + 1]]
	else:
		level = [[pos[0] + x, pos[1] + y], [pos[0] + x, pos[1] + y - 1]]
	while True:
		newLevel = []
		for i in range(len(level)):
			if mat[level[i][0] + x][level[i][1]] == "[":
				newLevel.append([level[i][0] + x, level[i][1]])
				newLevel.append([level[i][0] + x, level[i][1] + 1])
			if mat[level[i][0] + x][level[i][1]] == "]":
				newLevel.append([level[i][0] + x, level[i][1]])
				newLevel.append([level[i][0] + x, level[i][1] - 1])
			if mat[level[i][0] + x][level[i][1]] == "#":
				return False
		if len(newLevel) == 0:
			return True
		level = newLevel
	
	
def updateVertical(mat, pos, x, y):
	if mat[pos[0] + x][pos[1] + y] == "[":
		level = [[pos[0] + x, pos[1] + y, "["], [pos[0] + x, pos[1] + y + 1, "]"]]
		mat[pos[0] + x][pos[1] + y] = "."
		mat[pos[0] + x][pos[1] + y + 1] = "."
	else:
		level = [[pos[0] + x, pos[1] + y, "]"], [pos[0] + x, pos[1] + y - 1, "["]]
		mat[pos[0] + x][pos[1] + y] = "."
		mat[pos[0] + x][pos[1] + y - 1] = "."
	while len(level) > 0:
		newLevel = []
		for i in range(len(level)):
			if mat[level[i][0] + x][level[i][1]] == "[":
				newLevel.append([level[i][0] + x, level[i][1], "["])
				mat[level[i][0] + x][level[i][1]] = "."
				newLevel.append([level[i][0] + x, level[i][1] + 1, "]"])
				mat[level[i][0] + x][level[i][1] + 1] = "."
			if mat[level[i][0] + x][level[i][1]] == "]":
				newLevel.append([level[i][0] + x, level[i][1], "]"])
				mat[level[i][0] + x][level[i][1]] = "."
				newLevel.append([level[i][0] + x, level[i][1] - 1, "["])
				mat[level[i][0] + x][level[i][1] - 1] = "."
			if mat[level[i][0]][level[i][1]] == "#":
				return
		for i in range(len(level)):
			mat[level[i][0] + x][level[i][1]] = level[i][2]
		level = newLevel
		

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
			if mat[pos[0] + x][pos[1] + y] == '[' or mat[pos[0] + x][pos[1] + y] == ']':
				if move[i] == "<" or move[i] == ">":
					if checkSides(mat, pos, x, y):
						updateSides(mat, pos, x, y)
						pos = [pos[0] + x, pos[1] + y]
				else:
					if checkVertical(mat, pos, x, y):
						updateVertical(mat, pos, x, y)
						mat[pos[0]][pos[1]] = '.'
						pos = [pos[0] + x, pos[1] + y]
						mat[pos[0]][pos[1]] = '@'
	return mat


def calcGPS(mat):
	res = 0
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if mat[i][j] == '[':
				res += 100 * i + j
	return res


if __name__ == '__main__':
	m, mo, ini = readInput()
	m = simulateRobot(m, mo, ini)
	print(calcGPS(m))
	