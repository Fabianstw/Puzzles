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


def find_biggest_tuple(mapping):
	biggest_tuple = {}
	seen = set()
	count = 0
	for key in mapping:
		print(count)
		tups = set()
		tups.add(tuple([key]))
		while True:
			new_tups = set()
			for tup in tups:
				btf = biggest_tuple_for(mapping, tup)
				for bt in btf:
					if bt not in seen:
						seen.add(bt)
						new_tups.add(bt)
			if len(new_tups) == 0:
				break
			tups = new_tups
		biggest_tuple[key] = tups
		count += 1
	
	biggest = 0
	big_tup = None
	for key in biggest_tuple:
		for tup in biggest_tuple[key]:
			if len(tup) > biggest:
				biggest = len(tup)
				big_tup = tup
	return biggest, big_tup
	

def biggest_tuple_for(mapping, values):
	tups = set()
	for key in mapping:
		all_in = True
		for value in values:
			if value not in mapping[key]:
				all_in = False
				break
		if all_in:
			tups.add(tuple(sorted(list(values) + [key])))
	return tups

if __name__ == '__main__':
	m = readFile()
	_, bt = find_biggest_tuple(m)
	print("Part 2: ", ",".join(sorted(bt)))
