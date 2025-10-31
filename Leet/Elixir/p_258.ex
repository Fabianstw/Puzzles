defmodule Solution do
  @spec add_digits(num :: integer) :: integer
  def add_digits(num) when num < 10, do: num

  def add_digits(num) do
    num
    |> Integer.digits()
    |> Enum.sum()
    |> add_digits()
  end
end

IO.inspect(Solution.add_digits(38)) # Expected output: 2
IO.inspect(Solution.add_digits(0)) # Expected output: 0
