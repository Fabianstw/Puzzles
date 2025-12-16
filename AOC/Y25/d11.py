graph = {}
with open("d11.txt","r") as f:
  for line in f.readlines():
    parts = line.strip().split(": ")
    outputs = parts[1].split(" ")
    graph[parts[0]] = outputs
    
    
def solve_part_1():
  global graph
  paths = set()
  
  stack = [("you", "")]
  visited = set()
  visited.add(("you", ""))
  while stack:
    current = stack.pop()
    
    if current[0] == "out":
      paths.add(current[1])
      continue
    
    for output in graph[current[0]]:
      if output not in visited:
        stack.append((output, current[1] + output))
        visited.add((output, current[1] + output))
        
        
  return len(paths)


def solve_part_2():
  global graph
  memo = {}
  
  def dfs(node, seen_fft, seen_dac):
    seen_fft = seen_fft or (node == "fft")
    seen_dac = seen_dac or (node == "dac")
    
    if node == "out":
      return 1 if seen_fft and seen_dac else 0
    
    key = (node, seen_fft, seen_dac)
    if key in memo:
      return memo[key]
    
    count = 0
    for nxt in graph.get(node, []):
      count += dfs(nxt, seen_fft, seen_dac)
    
    memo[key] = count
    return count
  
  return dfs("svr", False, False)


print("Part 1: ", solve_part_1())
print("Part 2: ", solve_part_2())