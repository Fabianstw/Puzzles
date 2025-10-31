def readInput():
	arr = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for line in data:
			arr = list(map(int, line.strip().split(' ')))
	return arr


def blink(arr):
	for i in range(75):
		print(i, len(arr))
		newArr = []
		for j in range(len(arr)):
			if arr[j] == 0:
				newArr.append(1)
			elif len(str(arr[j])) % 2 == 0:
				newArr.append(int(str(arr[j])[:len(str(arr[j]))//2]))
				newArr.append(int(str(arr[j])[len(str(arr[j]))//2:]))
			else:
				newArr.append(arr[j] * 2024)
		arr = newArr
	return arr

			
if __name__ == '__main__':
	values = readInput()
	values = blink(values)
	print(len(values))
	