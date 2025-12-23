function special_pythagorean_triplet(goal_sum)
  for a in 1:goal_sum
    for b in 1:goal_sum
      for c in 1:goal_sum
        if a + b + c == goal_sum && a^2 + b^2 == c^2
          return (a, b, c)
        end
      end
    end
  end
  return nothing
end

values = [12, 1000]

for n in values
  println("Finding special Pythagorean triplet for sum = $n")
  triplet = special_pythagorean_triplet(n)
  println("Triplet: $triplet", " Their product: ", triplet[1] * triplet[2] * triplet[3])
end