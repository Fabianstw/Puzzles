def number_game(nums)
  new_nums = []
  nums = nums.dup

  while nums.any?
    nums.sort!
    smallest_1 = nums.shift
    smallest_2 = nums.shift

    if smallest_2
      new_nums.push(smallest_2)
      new_nums.push(smallest_1)
    end
  end

  new_nums
end

puts number_game([5,4,2,3]).join(',') # -> [3,2,5,4]
puts number_game([2,5]).join(',') # -> [5,2]