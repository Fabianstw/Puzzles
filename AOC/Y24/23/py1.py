def readFile():
	mapping = {}
	with open('inp.txt', 'r') as f:
		data = f.readlines()
		for line in data:
			split = line.strip().split("-")
			if split[0] in mapping:
				mapping[split[0]].append(split[1])
			else:
				mapping[split[0]] = [split[1]]
			if split[1] in mapping:
				mapping[split[1]].append(split[0])
			else:
				mapping[split[1]] = [split[0]]
	return mapping

	
def findThreeTuples(mapping):
	tup = set()
	for key1 in mapping:
		for key2 in mapping[key1]:
			for key3 in mapping[key2]:
				if key3 in mapping[key1]:
					new_tup = tuple(sorted([key1, key2, key3]))
					tup.add(new_tup)
	return tup
	

def count_tuple_with_t(tups):
	tuple_t = set()
	for tup in tups:
		if tup[0].startswith('t') or tup[1].startswith('t') or tup[2].startswith('t'):
			tuple_t.add(tup)
	return tuple_t
	
	
if __name__ == '__main__':
	m = readFile()
	t = findThreeTuples(m)
	tt = count_tuple_with_t(t)
	print("Part 1: ", len(tt))
	