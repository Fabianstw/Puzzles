function get_first_number_nth_divisor(n::Int)
  k = 1
  while true
    # triangular number T = k*(k+1)/2
    if iseven(k)
      a = k ÷ 2
      b = k + 1
    else
      a = k
      b = (k + 1) ÷ 2
    end
    d = get_number_divisors(a) * get_number_divisors(b)
    if d >= n
      return k * (k + 1) ÷ 2
    end
    k += 1
  end
end

function get_number_divisors(n::Int)
  if n == 1
    return 1
  end
  cnt = 0
  r = floor(Int, sqrt(n))
  for i in 1:r
    if n % i == 0
      cnt += 1
      if i != n ÷ i
        cnt += 1
      end
    end
  end
  return cnt
end

values = [5, 500]
for v in values
  res = get_first_number_nth_divisor(v)
  println("The first triangular number with at least $v divisors is $res")
end