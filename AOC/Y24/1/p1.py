from aocd import get_data

left = []
right = []


data = get_data(day=1, year=2024)
for line in data.split("\n"):
    sp = line.rstrip().split("  ")
    left.append(int(sp[0]))
    right.append(int(sp[1]))

left.sort()
right.sort()

dist = 0

for i in range(0, len(left)):
    dist += abs(right[i] - left[i])

print(dist)
