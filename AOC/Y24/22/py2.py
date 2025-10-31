def readInput():
	values = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			values.append(int(line.strip()))
	return values


def get_bananas(values):
	res_values = []
	res_diffs = []
	for value in values:
		res_values.append(simulate(value, 2000))
		res_diffs.append(getDifferences(res_values[-1]))
	combinations = getAllCombinations(res_diffs, res_values)
	return getBestCombination(combinations)


def getBestCombination(combinations):
	high = -1
	for key in combinations:
		if sum(combinations[key]) > high:
			high = sum(combinations[key])
	return high


def getDifferences(values):
	differences = []
	for i in range(1, len(values)):
		differences.append(values[i] - values[i-1])
	return differences


def getAllCombinations(diffs, values):
	combinations = {}
	for j, diff in enumerate(diffs):
		newCombs = {}
		for i in range(len(diff) - 3):
			key = tuple(diff[i:i+4])
			if key not in newCombs:
				newCombs[key] = values[j][i+4]
		for key in newCombs:
			if key not in combinations:
				combinations[key] = [newCombs[key]]
			else:
				combinations[key].append(newCombs[key])
	return combinations


def simulate(value, rounds):
	last_digits = []
	for i in range(rounds):
		last_digits.append(value % 10)
		newValue = value * 64
		value = (value ^ newValue) % 16777216
		newValue = value // 32
		value = (value ^ newValue) % 16777216
		newValue = value * 2048
		value = (value ^ newValue) % 16777216
	return last_digits


if __name__ == '__main__':
	v = readInput()
	p = get_bananas(v)
	print(f"Part 2: {p}")
	
# too high
# 1500
	