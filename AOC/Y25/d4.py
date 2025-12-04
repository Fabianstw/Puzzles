grid = []
with open("d4.txt","r") as f:
  for line in f.readlines():
    g = []
    for char in line.strip():
      g.append(char)
    grid.append(g)
    
    
def solve_part_1():
  global grid
  forklifts = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "@":
        adjacent_positions = [
          [i - 1, j - 1],
          [i - 1, j],
          [i - 1, j + 1],
          [i, j - 1],
          [i, j + 1],
          [i + 1, j - 1],
          [i + 1, j],
          [i + 1, j + 1],
        ]
        count = 0
        for position in adjacent_positions:
          if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
            if grid[position[0]][position[1]] == "@":
              count += 1
        if count < 4:
          forklifts += 1
  
  return forklifts


def solve_part_2():
  global grid
  papers = 0
  change = True
  while change:
    change = False
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "@":
          adjacent_positions = [
            [i - 1, j - 1],
            [i - 1, j],
            [i - 1, j + 1],
            [i, j - 1],
            [i, j + 1],
            [i + 1, j - 1],
            [i + 1, j],
            [i + 1, j + 1],
          ]
          count = 0
          for position in adjacent_positions:
            if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
              if grid[position[0]][position[1]] == "@":
                count += 1
          if count < 4:
            grid[i][j] = "."
            papers += 1
            change = True
  
  return papers

  
print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())