function readInput()
  grid = []
  open(joinpath(@__DIR__, "inp.txt"), "r") do file
    for line in eachline(file)
      push!(grid, collect(line))
    end
  end
  grid
end

function part_1()
  grid = readInput()

  rows = length(grid)
  cols = length(grid[1])

  valid_numbers = Int[]

  for i in 1:rows
    row = grid[i]
    j = 1
    while j ≤ cols
      if isdigit(row[j])
        # find full number span
        start = j
        while j ≤ cols && isdigit(row[j])
          j += 1
        end
        stop = j - 1
        number = parse(Int, String(row[start:stop]))

        # check adjacency for ANY digit in the number
        has_symbol_neighbor = false
        for c in start:stop
          for di in -1:1
            for dj in -1:1
              ni = i + di
              nj = c + dj
              if 1 ≤ ni ≤ rows && 1 ≤ nj ≤ cols && !(di == 0 && dj == 0)
                ch = grid[ni][nj]
                if !(isdigit(ch) || ch == '.')
                  has_symbol_neighbor = true
                end
              end
            end
          end
        end

        if has_symbol_neighbor
          push!(valid_numbers, number)
        end
      else
        j += 1
      end
    end
  end
  sum(valid_numbers)
end

function part_2()
  grid = readInput()
  rows = length(grid)
  cols = length(grid[1])

  numbers = []
  for i in 1:rows
    row = grid[i]
    j = 1
    while j ≤ cols
      if isdigit(row[j])
        start = j
        while j ≤ cols && isdigit(row[j])
          j += 1
        end
        stop = j - 1
        val = parse(Int, String(row[start:stop]))
        push!(numbers, (val, i, start, stop))
      else
        j += 1
      end
    end
  end

  total_ratio = 0
  for r in 1:rows
    for c in 1:cols
      if grid[r][c] == '*'
        adj = []
        for (val, nr, ns, ne) in numbers
          if abs(nr - r) ≤ 1 && ns ≤ c + 1 && c - 1 ≤ ne
            push!(adj, val)
          end
        end
        if length(adj) == 2
          total_ratio += adj[1] * adj[2]
        end
      end
    end
  end
  total_ratio
end

println("Part 1: ", part_1())
println("Part 2: ", part_2())
