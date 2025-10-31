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

function checkValues(games)
  res = 0
  for (index, game) in enumerate(games)
    trueGame = true
    for bag in game
      if haskey(bag, "blue") && bag["blue"] > 14
        trueGame = false
        break
      end
      if haskey(bag, "green") &&  bag["green"] > 13
        trueGame = false
        break
      end
      if haskey(bag, "red") &&  bag["red"] > 12
        trueGame = false
        break
      end
    end
    if trueGame
      res += index
    end
  end
  return res
end

function main()
  lines = readInput()
  println(checkValues(lines))
end
main()