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
				newBut.append([int(split[0].split('=')[1].replace('\n', '')) + 10000000000000, int(split[1].split('=')[1].replace('\n', '')) + 10000000000000])
			i += 1
		return but


cache = {}


def determ(mat):
	det = (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])
	if det == 0:
		return 0
	return det


def getMinDistance(A, B, dist):
	det = determ([[A[0], B[0]], [A[1], B[1]]])
	if det == 0:
		return 0
	Da = dist[0] * B[1] - dist[1] * B[0]
	Db = dist[1] * A[0] - dist[0] * A[1]
	a = Da / det
	b = Db / det
	
	if a < 0 or b < 0 or not a.is_integer() or not b.is_integer():
		return 0
	return int(3 * a + b)
	

if __name__ == '__main__':
	b = readInput()
	res = 0
	for A, B, dist in b:
		a = getMinDistance(A, B, dist)
		res += a
	print(res)
