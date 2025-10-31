function readInput()
  lines = []
  open("/Users/fabianstiewe/Desktop/AOC/23/2/inp.txt", "r") do file
    for line in eachline(file)
      newLine = []
      bags = split(line, ": ")[2]
      eachBag = split(bags, "; ")
      for bag in eachBag
        balls = split(bag, ", ")
        bagDict = Dict()
        for ball in balls
          ba = split(ball, " ")
          bagDict[ba[2]] = parse(Int64, ba[1])
        end
        push!(newLine, bagDict)
      end
      push!(lines, newLine)
    end
  end
  return lines
end

function findMinimumValues(games)
  res = 0
  for game in games 
    minRed = 0
    minGreen = 0
    minBlue = 0
    for bag in game
      if haskey(bag, "red")
        minRed = max(minRed, bag["red"])
      end
      if haskey(bag, "green")
        minGreen = max(minGreen, bag["green"])
      end
      if haskey(bag, "blue")
        minBlue = max(minBlue, bag["blue"])
      end
    end
    res += minRed * minGreen * minBlue
  end
  return res
end

function main()
  lines = readInput()
  println(findMinimumValues(lines))
end
main()