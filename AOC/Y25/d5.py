ranges = []
ids = []
empty_line = False
with open("d5.txt","r") as f:
  for line in f.readlines():
    if line.strip() =="":
      empty_line = True
      continue
    if not empty_line:
      parts = line.split("-")
      ranges.append((int(parts[0]),int(parts[1])))
    else:
      ids.append(int(line))
      
      
def solve_part_1():
  global ids
  global ranges
  count = 0
  for id in ids:
    for r in ranges:
      if r[0] <= id <= r[1]:
        count += 1
        break
    
  return count

def solve_part_2():
  global ranges
  # sort ranges by first element
  ranges = sorted(ranges, key=lambda x: x[0])
  current = ranges[0][1]
  total = ranges[0][1] - ranges[0][0] + 1
  for r in ranges[1:]:
    if r[0] > current:
      total += r[1] - r[0] + 1
      current = r[1]
      continue
    if r[0] == current:
      total += r[1] - r[0]
      current = r[1]
      continue
    if r[0] < current:
      if r[1] > current:
        total += r[1] - current
        current = r[1]
        continue
      if r[1] == current:
        continue
      if r[1] < current:
        continue
        
  return total


print("Part 1:", solve_part_1())
print("Part 2:", solve_part_2())