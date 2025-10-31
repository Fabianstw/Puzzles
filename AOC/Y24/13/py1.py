def readInput():
	but = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		i = 0
		newBut = []
		for line in data:
			if line == '\n':
				but.append(newBut)
				newBut = []
				i = 0
				continue
			split = line.split(': ')[1].split(', ')
			if i == 0 or i == 1:
				newBut.append([int(split[0].split('+')[1].replace('\n', '')), int(split[1].split('+')[1].replace('\n', ''))])
			else:
				newBut.append([int(split[0].split('=')[1].replace('\n', '')), int(split[1].split('=')[1].replace('\n', ''))])
			i += 1
		return but


cache = {}


def getMinDistance(A, B, dist):
	if (A[0], A[1], B[0], B[1], dist[0], dist[1]) in cache:
		return cache[(A[0], A[1], B[0], B[1], dist[0], dist[1])]
	if dist[0] < 0 or dist[1] < 0:
		return None
	if dist[0] == 0 and dist[1] == 0:
		return 0
	ra = getMinDistance(A, B, [dist[0] - A[0], dist[1] - A[1]])
	rb = getMinDistance(A, B, [dist[0] - B[0], dist[1] - B[1]])
	if ra is None and rb is None:
		cache[(A[0], A[1], B[0], B[1], dist[0], dist[1])] = None
		return None
	if ra is None:
		cache[(A[0], A[1], B[0], B[1], dist[0], dist[1])] = 1 + rb
		return 1 + rb
	if rb is None:
		cache[(A[0], A[1], B[0], B[1], dist[0], dist[1])] = 3 + ra
		return 3 + ra
	cache[(A[0], A[1], B[0], B[1], dist[0], dist[1])] = min(3 + ra, 1 + rb)
	return min(3 + ra, 1 + rb)


if __name__ == '__main__':
	b = readInput()
	res = 0
	for A, B, dist in b:
		a = getMinDistance(A, B, dist)
		if a:
			res += a
	print(res)
