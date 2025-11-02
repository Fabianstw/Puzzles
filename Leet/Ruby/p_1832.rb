require 'set'

def check_if_pangram(sentence)
  # store all letters in a set
  letters = Set.new
  sentence.each_char do |char|
    letters.add(char)
    if letters.size == 26
      return true
    end
  end

  false
end

values = %w[thequickbrownfoxjumpsoverthelazydog leetcode]
for val in values
  puts check_if_pangram(val)
end