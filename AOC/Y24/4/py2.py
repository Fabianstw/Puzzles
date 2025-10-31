from aocd import get_data
lines = []
res = 0

data = get_data(day=3, year=2024).split("\n")
for line in data:
	lines.append(list(line.rstrip()))
		
		
for i in range(1, len(lines) - 1):
	for j in range(1, len(lines[0]) - 1):
		if lines[i][j] == "A":
			if lines[i-1][j-1] == lines[i-1][j+1] == "M":
				if lines[i+1][j-1] == lines[i+1][j+1] == "S":
					res += 1
			elif lines[i-1][j-1] == lines[i-1][j+1] == "S":
				if lines[i+1][j-1] == lines[i+1][j+1] == "M":
					res += 1
			elif lines[i-1][j-1] == lines[i+1][j-1] == "M":
				if lines[i-1][j+1] == lines[i+1][j+1] == "S":
					res += 1
			elif lines[i-1][j-1] == lines[i+1][j-1] == "S":
				if lines[i-1][j+1] == lines[i+1][j+1] == "M":
					res += 1
			
print(res)
