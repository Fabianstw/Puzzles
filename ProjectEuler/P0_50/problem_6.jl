using Printf 

function sum_square_difference(n)
  return (n*(n+1)/2)^2 - ((n*(n+1)*(2n+1))/6)
end

values = [10, 100]
for v in values
    @printf("For n = %d, the sum square difference is %.0f\n", v, sum_square_difference(v))
end