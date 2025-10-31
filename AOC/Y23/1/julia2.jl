function readInput()
  lines = []
  open("/Users/fabianstiewe/Desktop/AOC/23/1/inp.txt", "r") do file
    for line in eachline(file)
      push!(lines, line)
    end
  end
  return lines
end

numNames = Dict("zero" => 0, "one" => 1, "two" => 2, "three" => 3, "four" => 4, "five" => 5, "six" => 6, "seven" => 7, "eight" => 8, "nine" => 9)

function getNumbers(line)
  firstValue = -1
  lastValue = -1
  foundFirst = false

  for i in eachindex(line)  
    if isdigit(line[i])  
      num = parse(Int, line[i])  
      if !foundFirst
        firstValue = num
        foundFirst = true
      else
        lastValue = num
      end
    end
    for (name, num) in numNames
      if startswith(line[i:end], name)
        if !foundFirst
          firstValue = num
          foundFirst = true
        else
          lastValue = num
        end
      end
    end
  end

  return firstValue, lastValue
end

function getAllNumbers(lines)
  res = 0
  for line in lines
      firstValue, lastValue = getNumbers(line)
      if firstValue != -1
        if lastValue == -1
          lastValue = firstValue
        end
          concatenated = parse(Int, string(firstValue, lastValue))
          res += concatenated
      end
  end
  return res
end

function main()
  lines = readInput()
  res = getAllNumbers(lines)
  println(res)
end
main()