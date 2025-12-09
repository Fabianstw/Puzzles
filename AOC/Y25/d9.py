import itertools as it

coords = []
with open("d9.txt","r") as f:
  for line in f.readlines():
    parts = line.strip().split(",")
    coords.append([int(parts[0]), int(parts[1])])

f = lambda l: [(min(a,c), min(b,d), max(a,c),
                max(b,d)) for (a,b),(c,d) in l]
    
def solve_part_1():
  global coords
  best = 0
  for x,y,u,v in f(it.combinations(coords, 2)):
    best = max(best, (u - x + 1) * (v - y + 1))
        
  return best
  
  
def solve_part_2():
  global coords
  green = f(it.pairwise(coords))
  
  best = 0
  for x,y,u,v in f(it.combinations(coords, 2)):
    size = (u - x + 1) * (v - y + 1)
    if size > best:
      failure = False
      for p,q,r,s in green:
        # Check if the rectangles overlap, they should not
        # https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
        if x<r and y<s and u>p and v>q:
          failure = True
          break
      if not failure:
        best = size
  return best
  
  
print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())
