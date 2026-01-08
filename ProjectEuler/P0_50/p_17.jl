lookup_table = Dict(
  1 => "one",
  2 => "two",
  3 => "three",
  4 => "four",
  5 => "five",
  6 => "six",
  7 => "seven",
  8 => "eight",
  9 => "nine",
  10 => "ten",
  11 => "eleven",
  12 => "twelve",
  13 => "thirteen",
  14 => "fourteen",
  15 => "fifteen",
  16 => "sixteen",
  17 => "seventeen",
  18 => "eighteen",
  19 => "nineteen",
  20 => "twenty",
  30 => "thirty",
  40 => "forty",
  50 => "fifty",
  60 => "sixty",
  70 => "seventy",
  80 => "eighty",
  90 => "ninety",
  1000 => "onethousand"
)

function number_word(n::Int)
  s = get(lookup_table, n, "")
  if s != ""
    return s
  elseif n < 100
    tens = div(n, 10) * 10
    units = n % 10
    return get(lookup_table, tens, "") * (units != 0 ? get(lookup_table, units, "") : "")
  elseif n < 1000
    hundreds = div(n, 100)
    remainder = n % 100
    return get(lookup_table, hundreds, "") * "hundred" * (remainder != 0 ? "and" * number_word(remainder) : "")
  else
    error("number_word only supports 1..1000")
  end
end

function letter_counts(n::Int)
  count = 0
  for i in 1:n
    word = number_word(i)
    count += length(word)
  end
  return count
end

function parse_values()
  if length(ARGS) == 0
    return [1000]
  else
    vals = Int[]
    for a in ARGS
      try
        push!(vals, parse(Int, a))
      catch
        @warn "ignored non-integer argument" arg=a
      end
    end
    return isempty(vals) ? [1000] : vals
  end
end

for v in parse_values()
  println("Letter counts for n=$v: ", letter_counts(v))
end