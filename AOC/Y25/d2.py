ranges = []
with open("d2.txt","r") as f:
  for line in f.readlines():
    # only one line
    for r in line.split(","):
      parts = r.split("-")
      ranges.append([int(parts[0]), int(parts[1])])
      
      
def solve_part_1():
  global ranges
  ids = []
  
  for r in ranges:
    ids.extend(invalid_ids(r[0], r[1]))
  
  return sum(ids)


def invalid_ids(start, end):
  ids = []
  for i in range(start, end + 1):
    str_i = str(i)
    if str_i[:len(str_i)//2] == str_i[len(str_i)//2:]:
      ids.append(i)
      
  return ids


def solve_part_2():
  global ranges
  ids = []
  
  for r in ranges:
    ids.extend(invalid_ids_2(r[0], r[1]))
  
  return sum(ids)


def invalid_ids_2(start, end):
  # Now invalid if a repeated pattern
  ids = []
  
  for i in range(start, end + 1):
    str_i = str(i)
    for step_size in range(1, len(str_i) // 2 + 1):
      pattern = str_i[:step_size]
      pattern_match = True
      # check if the pattern reoccurs at every stepsize
      for j in range(step_size, len(str_i), step_size):
        if str_i[j:j+step_size] != pattern:
          pattern_match = False
          break
      if pattern_match:
        ids.append(i)
        break
        
  return ids
  


print("Part 1:", solve_part_1())
print("Part 2:", solve_part_2())
