function sum_multiple_3_5(n)
  sumsm = 0
  for i in 0:n-1
    if i % 3 == 0 || i % 5 == 0
      sumsm += i
    end
  end
  sumsm
end

println(sum_multiple_3_5(10))  # Expected output: 23
println(sum_multiple_3_5(1000))  