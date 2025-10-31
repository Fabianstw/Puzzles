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


def simulate(x, y, vx, vy):
	x = (x + vx) % mapW
	y = (y + vy) % mapH
	return [x, y, vx, vy]


def createMap(pos):
	ma = [[0 for _ in range(mapW)] for _ in range(mapH)]
	for p in pos:
		ma[p[1]][p[0]] = 1
	return ma


def simulateRobs(robs):
	for i in range(1, 8010):
		newPos = []
		for x, y, vx, vy in robs:
			newPos.append(simulate(x, y, vx, vy))
		robs = newPos
		ma = createMap(newPos)
		# print(sum(sum(x) for x in ma))
		if sum(sum(x) for x in ma) == 500:
			with open(f'img/test3.txt', 'a') as f:
				f.write(f"\n\nTest: {i}\n")
				for a in ma:
					for l in a:
						if l == 0:
							f.write(" ")
						else:
							f.write(str(l))
					f.write("\n")


if __name__ == '__main__':
	r = readInput()
	print(simulateRobs(r))

