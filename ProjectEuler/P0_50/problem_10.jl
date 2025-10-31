using Primes

function sum_primes(n)
  total = 2
  count = 3
  while count < n
    if isprime(count)
      total += count
    end
    count += 2
  end
  total
end

values = [10, 2000000]

for v in values
  res = sum_primes(v)
  println("Until the value of $v the sum of all primes is: $res")
end