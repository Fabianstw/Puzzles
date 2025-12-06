"""
Only works with the final input.
The indices for testing input don't work.
"""


def solve_part_1():
  data = []
  with open("d6.txt","r") as f:
    for line in f.readlines():
      parts = line.strip().split(" ")
      d = []
      for part in parts:
        if part != "":
          d.append(part)
      data.append(d)
      
  total = 0
  for i in range(len(data[0])):
    sign = data[4][i]
    if sign == "+":
      start = 0
    else:
      start = 1
    for j in range(len(data) - 1):
      if sign == "+":
        start += int(data[j][i])
      else:
        start *= int(data[j][i])
    total += start
  
  return total

def solve_part_2():
  data = []
  with open("d6.txt","r") as f:
    for line in f.readlines():
      data.append(line.replace("\n",""))
  data[4] += "    "
  
  total = 0
  prev = len(data[0])
  for i in range(len(data[0]), -1, -1):
    if data[4][i] == "+" or data[4][i] == "*":
      sign = data[4][i]
      values = []
      for j in range(i, prev):
        number = ""
        for k in range(0, 4):
          number += data[k][j]
        values.append(int(number))
      if sign == "+":
        total += sum(values)
      elif sign == "*":
        start = 1
        for value in values:
          start *= value
        total += start
      prev = i - 1
    else:
      pass

  return total

print("Part 1:", solve_part_1())
print("Part 2:", solve_part_2())
