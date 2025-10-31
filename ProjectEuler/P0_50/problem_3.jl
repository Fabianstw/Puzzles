function largest_prime_factor(value)
  count = 2
  prime_factor = 0
  while value != 1
    if value % count == 0
      prime_factor = count
      value /= count
    else
      count += 1
    end
  end
  return prime_factor
end

println(largest_prime_factor(13195)) # expect 29
println(largest_prime_factor(600851475143))