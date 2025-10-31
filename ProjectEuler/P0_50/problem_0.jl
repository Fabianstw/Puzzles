function sum_odd_squares_first_N(N::Integer)
  sumso = 0
  for i in 1:N
    square_value = i^2
    if isodd(square_value)
      sumso += square_value
    end
  end
  return sumso
end

# Example: first 5 squares -> odd squares: 1^2 + 3^2 + 5^2 = 35
println(sum_odd_squares_first_N(5))       # prints 35

# Example: your main problem
println(sum_odd_squares_first_N(627_000)) # sum of odd squares among first 412000 squares

# Print first milion
println(sum_odd_squares_first_N(1000000))
