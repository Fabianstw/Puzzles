def two_sum(nums, target)
  seen = {}
  nums.each_with_index do |num, i|
    complement = target - num
    return [seen[complement], i] if seen.key?(complement)
    seen[num] = i
  end
  []
end

puts two_sum([2,7,11,15], 9)
puts two_sum([3,2,4], 6)
puts two_sum([3,3], 6)
