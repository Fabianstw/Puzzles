from copy import deepcopy

_grid = []
start = []
with open("d7.txt","r") as f:
  i = 0
  for line in f.readlines():
    row = []
    j = 0
    for p in line.strip():
      if p == "S":
        start = [i, j]
      row.append(p)
      j += 1
    _grid.append(row)
    i += 1
    

def solve_part_1():
  global _grid
  global start
  grid = deepcopy(_grid)
  grid[start[0]][start[1]] = "|"
  total = 0
  for i in range(1, len(grid)):
    for j in range(len(grid[i])):
      if grid[i-1][j] == "|":
        if grid[i][j] == ".":
          grid[i][j] = "|"
        elif grid[i][j] == "^":
          total += 1
          grid[i][j-1] = "|"
          grid[i][j+1] = "|"
          
  return total


def replace_dot(g):
  for i in range(len(g)):
    for j in range(len(g[i])):
      if g[i][j] == ".":
        g[i][j] = 0
  return g


def solve_part_2():
  global _grid
  global start
  grid = deepcopy(_grid)
  grid = replace_dot(grid)
  grid[start[0]][start[1]] = 1
  for i in range(1, len(grid)):
    for j in range(len(grid[i])):
      if grid[i-1][j] == "^":
        continue
      if grid[i-1][j] > 0:
        if grid[i][j] == "^":
          grid[i][j-1] += grid[i-1][j]
          grid[i][j+1] += grid[i-1][j]
        else:
          grid[i][j] += grid[i-1][j]
          
  return sum(grid[len(grid)-1])
          

    
print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())