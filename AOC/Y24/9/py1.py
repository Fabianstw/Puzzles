

def readInput():
	with open('inp.txt', 'r') as file:
		data = file.readlines()
	return data[0]


def createBlockString(line):
	toggleFile = True
	block = []
	currID = 0
	for i in range(len(line)):
		value = int(line[i])
		if toggleFile:
			block.append([str(currID)] * value)
			currID += 1
			toggleFile = False
		else:
			block.append(["."] * value)
			toggleFile = True
	return block


def swapFreeWithID(block):
	i = 0
	j = len(block) - 1
	while i < j:
		if block[i] == ".":
			while block[j] == ".":
				j -= 1
			block[i], block[j] = block[j], block[i]
		i += 1
	return block


def calcChecksum(block):
	i = 0
	check = 0
	while block[i] != ".":
		check += i * int(block[i])
		i += 1
	return check
		

if __name__ == '__main__':
	line = readInput()
	block = createBlockString(line)
	# filter empty arrays from block
	block = list(filter(lambda x: x != [], block))
	# flatten the block
	block = [item for sublist in block for item in sublist]
	block = swapFreeWithID(block)
	print(calcChecksum(block))
	