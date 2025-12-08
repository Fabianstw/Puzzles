class UnionFind:
  def __init__(self):
    self.parent = {}
    self.rank = {}
    self.size = {}   # size of each root
  
  def find(self, x):
    if x not in self.parent:
      # initialize new element
      self.parent[x] = x
      self.rank[x] = 0
      self.size[x] = 1
      return x
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])  # path compression
    return self.parent[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    
    if root_x == root_y:
      return False
    
    # union by rank
    if self.rank[root_x] < self.rank[root_y]:
      root_x, root_y = root_y, root_x  # ensure root_x is bigger
    
    self.parent[root_y] = root_x
    self.size[root_x] += self.size[root_y]
    
    if self.rank[root_x] == self.rank[root_y]:
      self.rank[root_x] += 1
    return True
  
  def largest_components(self, k=3):
    """Return sizes of the k largest connected components."""
    if len(self.parent) < k:
      return [0] * k
    
    # ensure all parents are compressed
    for x in list(self.parent.keys()):
      self.find(x)
    
    # collect sizes of roots only
    component_sizes = [self.size[x] for x in self.size if self.parent[x] == x]
    component_sizes.sort(reverse=True)
    
    return component_sizes[:k]


boxes = []
with open("d8.txt","r") as f:
  for line in f.readlines():
    parts = line.strip().split(",")
    boxes.append([int(parts[0]), int(parts[1]), int(parts[2])])
    

def solve_part_1():
  global boxes
  distances = []
  for i in range(len(boxes) - 1):
    id_i = boxes[i][0] * boxes[i][1] * boxes[i][2]
    for j in range(i + 1, len(boxes)):
      id_j = boxes[j][0] * boxes[j][1] * boxes[j][2]
      if id_i != id_j:
        distance = (boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2
        distances.append([distance, id_i, id_j])
    
  sorted_distances = sorted(distances, key=lambda x: x[0])
  union_find = UnionFind()
  for i in range(1000):
    curr = sorted_distances[i]
    id_1 = curr[1]
    id_2 = curr[2]
    union_find.union(id_1, id_2)
    
    
  sizes = union_find.largest_components()
  return sizes[0] * sizes[1] * sizes[2]


def solve_part_2():
  global boxes
  distances = []
  for i in range(len(boxes) - 1):
    id_i = boxes[i][0] * boxes[i][1] * boxes[i][2]
    for j in range(i + 1, len(boxes)):
      id_j = boxes[j][0] * boxes[j][1] * boxes[j][2]
      if id_i != id_j:
        distance = (boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2
        distances.append([distance, id_i, id_j, boxes[i][0], boxes[j][0]])
  
  sorted_distances = sorted(distances, key=lambda x: x[0])
  union_find = UnionFind()
  mult_x = 0
  i = 0
  while union_find.largest_components(1)[0] < len(boxes):
    curr = sorted_distances[i]
    id_1 = curr[1]
    id_2 = curr[2]
    union_find.union(id_1, id_2)
    i += 1
    mult_x = curr[3] * curr[4]
  
  return mult_x
    
  
# print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())