using Primes

function prime_numbers(n)
  count = 0
  num = 1
  while count < n
    num += 1
    if isprime(num)
      count += 1
    end
  end
  return num
end

values = [6, 10001]
for v in values
    println("The ", v, "th prime number is ", prime_numbers(v))
end