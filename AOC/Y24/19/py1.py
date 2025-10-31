def readInput():
	patterns = []
	towels = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		pat = True
		for line in data:
			if line == '\n':
				pat = False
				continue
			if pat:
				patterns = line.replace("\n", "").split(", ")
			else:
				towels.append(line.strip())
	
	return patterns, towels


def checkTowel(patterns, towel):
	towels = set()
	towels.add(towel)
	while towels:
		tow = towels.pop()
		if tow == "":
			return 1
		for pattern in patterns:
			if tow.startswith(pattern):
				towels.add(tow[len(pattern):])
	return 0


cache = {}


def checkTowel(patterns, towel):
	if towel in cache:
		return cache[towel]
	if towel == "":
		return 1
	ans = 0
	for pattern in patterns:
		if towel.startswith(pattern):
			ans = max(ans, checkTowel(patterns, towel[len(pattern):]))
	cache[towel] = ans
	return ans


def checkAllTowels(patterns, towels):
	res = 0
	for i, towel in enumerate(towels):
		print(i)
		res += checkTowel(patterns, towel)
	return res


if __name__ == "__main__":
	p, t = readInput()
	print(checkAllTowels(p, t))


# too low
# 252
