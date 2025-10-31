def readFile():
	with open('inp.txt', 'r') as f:
		values = {}
		gates = {}
		data = f.readlines()
		switch = True
		for line in data:
			line = line.strip()
			if line == "":
				switch = False
				continue
			if switch:
				split = line.split(": ")
				values[split[0]] = int(split[1])
			else:
				split = line.split(" -> ")
				start_gates = split[0].split(" ")
				if (start_gates[0], start_gates[2], start_gates[1]) in gates:
					gates[(start_gates[0], start_gates[2], start_gates[1])].append(split[1])
				else:
					gates[(start_gates[0], start_gates[2], start_gates[1])] = [split[1]]
	return values, gates
	
	
def simulate_circuit(values, gates):
	while len(gates) > 0:
		still_gates = {}
		for key in gates:
			if key[0] in values and key[1] in values:
				operations = { "AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "XOR": lambda a, b: a ^ b }
				result = operations[key[2]](values[key[0]], values[key[1]])
				for new_value in gates[key]:
					values[new_value] = result
			else:
				still_gates[key] = gates[key]
		gates = still_gates
	return values
	
	
def get_z_values(values):
	binary = ""
	for i in range(99, -1, -1):
		if "z" + str(i).zfill(2) in values:
			binary += str(values["z" + str(i).zfill(2)])
	return int(binary, 2)
	
	
if __name__ == '__main__':
	v, g = readFile()
	v = simulate_circuit(v, g)
	print(get_z_values(v))
	