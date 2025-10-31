def first_uniq_char(s)
  char_count = Hash.new(0)

  for char in s.chars
    char_count[char] += 1
  end

  for i in 0...s.length
    return i if char_count[s[i]] == 1
  end

  -1
end

puts first_uniq_char("leetcode") # => 0
puts first_uniq_char("loveleetcode") # => 2
puts first_uniq_char("aabb") # => -1