import re
from aocd import get_data

pattern = r"mul\(\d{1,3},\d{1,3}\)"

lines = []

res = 0


data = get_data(day=3, year=2024).split("\n")
for line in data:
	for match in re.finditer(pattern, line.rstrip()):
		x, y = map(int, match.group()[4:-1].split(","))
		res += x * y
			
print(res)