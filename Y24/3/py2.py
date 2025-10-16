import re
from aocd import get_data

pattern = r"mul\(\d{1,3},\d{1,3}\)"

longLine = ""

res = 0

data = get_data(day=3, year=2024).split("\n")
for line in data:
	longLine += line
split = longLine.rstrip().split("do()")
for i in range(len(split)):
	secondSplit = split[i].split("don't()")
	for match in re.finditer(pattern, secondSplit[0]):
		x, y = map(int, match.group()[4:-1].split(","))
		res += x * y

print(res)