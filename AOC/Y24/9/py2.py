

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


def getBlockFront(block, j):
	i = j
	while block[i] == block[j] and i <= len(block) - 1:
		i += 1
	return [j, i - 1]


def getBlockBack(block, j):
	i = j
	while block[i] == block[j] and i >= 0:
		i -= 1
	return [i + 1, j]


def swapBlocks(block):
	j = len(block) - 1
	while j >= 0:
		bj = getBlockBack(block, j)
		for i in range(0, bj[0] - 1):
			if block[i] != ".":
				continue
			bi = getBlockFront(block, i)
			if bj[1] - bj[0] <= bi[1] - bi[0]:
				for k in range(bj[0], bj[1] + 1):
					block[bi[0] + k - bj[0]], block[bj[0] + k - bj[0]] = block[bj[0] + k - bj[0]], block[bi[0] + k - bj[0]]
				break
				
		j = bj[0] - 1
	
	return block


def calcChecksum(block):
	
	check = 0
	for i in range(len(block)):
		if block[i] != ".":
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
	block = swapBlocks(block)
	print(calcChecksum(block))
	