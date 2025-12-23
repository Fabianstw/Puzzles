function lattice_paths(n)
  grid = fill(0, n+1, n+1)
  for i in 0:n
    for j in 0:n
      if i == 0 || j == 0
        grid[i+1, j+1] = 1
      else
        grid[i+1, j+1] = grid[i, j+1] + grid[i+1, j]
      end
    end
  end
  return grid[n+1, n+1]
end

values = [2, 20]
for v in values
  println("Lattice paths for n=$v: ", lattice_paths(v))
end