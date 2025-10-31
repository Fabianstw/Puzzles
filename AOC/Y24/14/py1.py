mapW = 101
mapH = 103


def readInput():
	robs = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			split = line.split('p=')[1].split(' v=')
			pos = split[0].split(',')
			vel = split[1].split(',')
			robs.append([int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])])
	return robs


def countQuadrants(pos):
	quad = [0, 0, 0, 0]
	for x, y in pos:
		if x == (mapW - 1) // 2 or y == (mapH - 1) // 2:
			continue
		if x < (mapW - 1) // 2:
			if y < (mapH - 1) // 2:
				quad[0] += 1
			else:
				quad[1] += 1
		else:
			if y < (mapH - 1) // 2:
				quad[2] += 1
			else:
				quad[3] += 1
	return quad[0] * quad[1] * quad[2] * quad[3]


def simulate(x, y, vx, vy):
	for i in range(100):
		x = (x + vx) % mapW
		y = (y + vy) % mapH
	return [x, y]


def simulateRobs(robs):
	newPos = []
	for x, y, vx, vy in robs:
		newPos.append(simulate(x, y, vx, vy))
	print(newPos)
	return countQuadrants(newPos)


if __name__ == '__main__':
	r = readInput()
	print(simulateRobs(r))
