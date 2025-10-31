def readInput():
	arr = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			arr = list(map(int, line.strip().split(' ')))
	return arr


seen = {}


def blink(value, depth):
	if depth == 75:
		return 1
	if str(value) + "-" + str(depth) in seen:
		return seen[str(value) + "-" + str(depth)]
	if value == 0:
		tmp = blink(1, depth + 1)
		seen["0-" + str(depth)] = tmp
		return tmp
	if len(str(value)) % 2 == 0:
		tmp1 = blink(int(str(value)[:len(str(value)) // 2]), depth + 1)
		tmp2 = blink(int(str(value)[len(str(value)) // 2:]), depth + 1)
		seen[str(value) + "-" + str(depth)] = tmp1 + tmp2
		return tmp1 + tmp2
	tmp = blink(value * 2024, depth + 1)
	seen[str(value) + "-" + str(depth)] = tmp
	return tmp


# if arr[j] == 0:


# 	newArr.append(1)
# elif len(str(arr[j])) % 2 == 0:
# 	newArr.append(int(str(arr[j])[:len(str(arr[j]))//2]))
# 	newArr.append(int(str(arr[j])[len(str(arr[j]))//2:]))
# else:
# 	newArr.append(arr[j] * 2024)


if __name__ == '__main__':
	values = readInput()
	res = 0
	for val in values:
		res += blink(val, 0)
	print(res)
