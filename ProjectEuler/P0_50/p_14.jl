function longest_collatz_sequence(limit::Int)
  max_length = 0
  starting_number = 0

  cache = Dict{Int, Int}(1 => 1)
  for i in 1:limit-1
    n = i
    chain_len = 0
    while !haskey(cache, n)
      if iseven(n)
        n = n ÷ 2
      else
        n = 3 * n + 1
      end
      chain_len += 1
    end
    cache[i] = chain_len + cache[n]
    if cache[i] > max_length
      max_length = cache[i]
      starting_number = i
    end
  end

  return starting_number
end

values = [100, 1000000]
for v in values
  res = longest_collatz_sequence(v)
  println("The starting number under $v that produces the longest Collatz sequence is $res.")
end

