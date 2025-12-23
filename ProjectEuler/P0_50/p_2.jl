function sum_even_fibonacci(n)
  sumsef = 0

  pos1 = 0
  pos2 = 1
  while pos2 < n
    tmp = pos1 + pos2
    if tmp % 2 == 0
      sumsef += tmp
    end
    pos1 = pos2
    pos2 = tmp
  end
  return sumsef
end

println(sum_even_fibonacci(9)) # expect 10
println(sum_even_fibonacci(4000000))