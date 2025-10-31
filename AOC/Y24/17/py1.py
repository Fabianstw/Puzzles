def readInput():
	register = {}
	program = []
	with open('inp.txt', 'r') as file:
		data = file.readlines()
		for i, line in enumerate(data):
			if i == 0:
				register["A"] = int(line.split(": ")[1])
			if i == 1:
				register["B"] = int(line.split(": ")[1])
			if i == 2:
				register["C"] = int(line.split(": ")[1])
			if i == 4:
				program = list(map(int, line.split(": ")[1].split(",")))
	return register, program


def getOperandValue(register, literal):
	if 0 <= literal <= 3:
		return literal
	if literal == 4:
		return register["A"]
	if literal == 5:
		return register["B"]
	if literal == 6:
		return register["C"]


def runProgram(register, program):
	i = 0
	res = ""
	while i < len(program) - 1:
		instruction = program[i]
		literal = program[i+1]
		if instruction == 0:
			register["A"] = register["A"] // (2 ** getOperandValue(register, literal))
		if instruction == 1:
			register["B"] = register["B"] ^ literal
		if instruction == 2:
			register["B"] = getOperandValue(register, literal) % 8
		if instruction == 3:
			if register["A"] != 0:
				i = literal
				continue
		if instruction == 4:
			register["B"] = register["B"] ^ register["C"]
		if instruction == 5:
			out = getOperandValue(register, literal) % 8
			res += str(out) + ","
		if instruction == 6:
			register["B"] = register["A"] // (2 ** getOperandValue(register, literal))
		if instruction == 7:
			register["C"] = register["A"] // (2 ** getOperandValue(register, literal))
		i += 2
	
	return res[:-1]
	
	
if __name__ == "__main__":
	r, p = readInput()
	print(runProgram(r, p))
	