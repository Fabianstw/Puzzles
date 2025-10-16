from aocd import get_data

left = []
right = []


data = get_data(day=1, year=2024)
for line in data:
    sp = line.rstrip().split("  ")
    left.append(int(sp[0]))
    right.append(int(sp[1]))

leftS = set(left)
dist = 0
for l in leftS:
    dist += l * right.count(l)

print(dist)
