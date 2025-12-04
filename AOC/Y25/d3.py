banks = []
with open("d3.txt","r") as f:
  for line in f.readlines():
    bank = []
    for char in line.strip():
      bank.append(char)
    banks.append(bank)
  
  
def solve_part_1():
  global banks
  joltages = []
  
  for bank in banks:
    current_max = 0
    for i in range(len(bank)-1):
      for j in range(i+1,len(bank)):
        combine = int(bank[i] + bank[j])
        if combine > current_max:
          current_max = combine
    joltages.append(current_max)
    
  return sum(joltages)


def solve_part_2():
  global banks
  joltages = []
  
  for bank in banks:
    result = []
    for i, x in enumerate(bank):
      remaining = len(bank)-i-1
      
      while result and result[-1] < x and (len(result) + remaining) >= 12:
        result.pop()
      result.append(x)
    
    joltages.append(int("".join(result)[:12]))
  
  return sum(joltages)


print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())