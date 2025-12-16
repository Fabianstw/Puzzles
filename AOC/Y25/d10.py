from collections import deque


lights = []
presses = []
joltages = []
with open("d10.txt","r") as f:
  for line in f.readlines():
    parts = line.strip().split(" ")
    press_parts = []
    for part in parts:
      if part[0] == "[":
        lights.append(str(part[1:len(part)-1]))
      elif part[0] == "(":
        press_parts.append([int(x) for x in part.strip("()").split(",") if x])
      else:
        joltages.append([int(x) for x in part.strip("{}").split(",") if x])
    presses.append(press_parts)


def solve_part_1():
  global lights
  global presses
  total = 0
  
  for i in range(len(lights)):
    print(i)
    light = lights[i]
    start = "." * len(light)
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while True:
      curr = queue.popleft()
      if curr[0] == light:
        total += curr[1]
        break
      
      for press in presses[i]:
        new_light = list(curr[0])
        for p in press:
          if new_light[p] == ".":
            new_light[p] = "#"
          else:
            new_light[p] = "."
        
        new_light = "".join(new_light)
        if new_light not in visited:
          queue.append((new_light, curr[1]+1))
          visited.add(new_light)
        
  return total


from pulp import (
  LpProblem,
  LpVariable,
  LpMinimize,
  LpInteger,
  GUROBI_CMD,
)

def solve_minimal_integer(A, b):
  n = len(A)      # number of rows (lights)
  m = len(A[0])   # number of columns (presses)
  
  # Create the ILP problem
  prob = LpProblem("Minimal_Presses", LpMinimize)
  
  # Define integer variables x[j] >= 0
  x = [LpVariable(f"x_{j}", lowBound=0, cat=LpInteger) for j in range(m)]
  
  # Add constraints A x = b
  for i in range(n):
    prob += sum(A[i][j] * x[j] for j in range(m)) == b[i]
  
  # Objective: minimize total presses
  prob += sum(x)
  
  # Solve using Gurobi
  prob.solve(GUROBI_CMD(msg=False))
  
  # Extract solution
  solution = [int(x[j].value()) for j in range(m)]
  return solution


def solve_part_2():
  global lights
  global presses
  total = 0
  
  for i in range(len(lights)):
    joltage = joltages[i]
    A = [[0 for _ in range(len(presses[i]))] for _ in range(len(joltage))]
    for j in range(len(presses[i])):
      for k in presses[i][j]:
        A[k][j] = 1
    b = joltage
    x = solve_minimal_integer(A, b)
    total += sum(x)
  return total


# print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())