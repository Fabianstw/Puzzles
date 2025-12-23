function power_digit_sum(n)
  ds = digits(BigInt(2)^n)
  return sum(ds)
end

values = [15, 1000]
for v in values
  println("Power digit sum for 2^$v: ", power_digit_sum(v))
end
