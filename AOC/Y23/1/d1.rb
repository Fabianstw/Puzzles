# frozen_string_literal: true

lines = IO.readlines("1/inp.txt")

def part1(lines)
  value = 0
  lines.each { |line|
    first_number = -1
    last_number = -1
    line.each_char { |char|
      if char.match(/[0-9]/)
        if first_number == -1
          first_number = char.to_i
        else
          last_number = char.to_i
        end
      end
    }
    if last_number == - 1
      value += first_number * 10 + first_number
    else
      value += first_number * 10 + last_number
    end

  }
  value
end

def part2(lines)
  numbers = {
    "zero" => 0,
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "four" => 4,
    "five" => 5,
    "six" => 6,
    "seven" => 7,
    "eight" => 8,
    "nine" => 9
  }
  value = 0
  lines.each { |line|
    first_number = -1
    last_number = -1
    line.each_char { |char|
      if char.match(/[0-9]/)
        if first_number == -1
          first_number = char.to_i
        else
          last_number = char.to_i
        end
      else
        for number_word, number_value in numbers
          # TODO
        end
      end
    }
  }
end

puts part1(lines)