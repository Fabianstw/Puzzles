def readInput():
	values = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			values.append(int(line.strip()))
	return values


def getPseudoRandoms(values):
	res = []
	for value in values:
		res.append(simulate(value, 2000))
	return res

def simulate(value, rounds):
	# print(value)
	for i in range(rounds):
		newValue = value * 64
		value = (value ^ newValue) % 16777216
		newValue = value // 32
		value = (value ^ newValue) % 16777216
		newValue = value * 2048
		value = (value ^ newValue) % 16777216
	return value

		
if __name__ == '__main__':
	v = readInput()
	p = getPseudoRandoms(v)
	print(f"Part 1: {sum(p)}")