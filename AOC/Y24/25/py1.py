def read_file():
	blocks = []
	with open("inp.txt", "r") as f:
		data = f.read().split("\n\n")
		for block in data:
			blocks.append(block.split("\n"))
	return blocks
		
	
def sort_key_lock(blocks):
	keys = []
	locks = []
	for block in blocks:
		if all(char == "#" for char in block[0]):
			locks.append(block)
		else:
			keys.append(block)
	return keys, locks
	

def get_key_heights(keys):
	heights = []
	for key in keys:
		key_heights = []
		for i in range(len(key[0])):
			h = -1
			for j in range(len(key) - 1, -1, -1):
				if key[j][i] == "#":
					h += 1
				else:
					break
			key_heights.append(h)
		heights.append(key_heights)
	return heights


def get_lock_heights(locks):
	heights = []
	for lock in locks:
		lock_heights = []
		for i in range(len(lock[0])):
			h = -1
			for j in range(len(lock)):
				if lock[j][i] == "#":
					h += 1
				else:
					break
			lock_heights.append(h)
		heights.append(lock_heights)
	return heights
	
	
def find_non_overlap(keys, locks):
	key_heights = get_key_heights(keys)
	lock_heights = get_lock_heights(locks)
	no_overlap_res = 0
	for i in range(len(keys)):
		for j in range(len(locks)):
			no_overlap = True
			for m in range(len(key_heights[i])):
				if key_heights[i][m] + lock_heights[j][m] >= 6:
					no_overlap = False
					break
			if no_overlap:
				no_overlap_res += 1
	return no_overlap_res
	
	
if __name__ == "__main__":
	b = read_file()
	k, l = sort_key_lock(b)
	res = find_non_overlap(k, l)
	print("Part one --> ", res)
	print("Part two --> Merry Christmas :-)", )
	