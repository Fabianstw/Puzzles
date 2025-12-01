turns = []
with open("d1.txt","r") as f:
  for line in f.readlines():
    # line = letternumber
    dir = line[0]
    value = int(line[1:])
    turns.append([dir, value])
    

def solve_part_1(moves):
  count = 0
  dial = 50
  for move in moves:
    if move[0] == "L":
      dial = (dial - move[1]) % 100
    else:
      dial = (dial + move[1]) % 100
    
    if dial == 0:
      count += 1
    
  return count


def solve_part_2(moves):
  count = 0
  dial = 50
  prev_dial = 50
  for move in moves:
    if move[0] == "L":
      dial = dial - move[1]
      if prev_dial == 0:
        dial += 100
      while dial <= 0:
        dial += 100
        count += 1
    else:
      dial = dial + move[1]
      while dial >= 100:
        count += 1
        dial -= 100
    dial %= 100
    prev_dial = dial
    
  return count
  
  
print("Part 1: ", solve_part_1(turns))
print("Part 2: ", solve_part_2(turns))
