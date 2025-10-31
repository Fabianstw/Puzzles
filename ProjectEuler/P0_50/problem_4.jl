function biggest_palindrome(digits)
  current_best = 0
  for i in 10^(digits-1):(10^digits - 1)
    for j in 10^(digits-1):(10^digits - 1)
      product = i * j
      if product > current_best
        # check if i * j is a palindrome
        value = string(product)
        if value == reverse(value)
          current_best = product
        end
      end
    end
  end
  return current_best
end


println(biggest_palindrome(2)) # expect 9009
println(biggest_palindrome(3))