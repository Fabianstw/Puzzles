function smallest_multiple(n)
  value = 1
  while !evenly_divisible(value, n)
    value += 1
  end
  value
end

function evenly_divisible(value, n)
  for i in 1:n
    if value % i != 0
      return false
    end
  end
  return true
end

values = [10, 20]
for n in values
  println(n, ": ", string(smallest_multiple(n)))
end