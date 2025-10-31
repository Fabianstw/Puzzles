use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<String> {
  let file = File::open("src/d3/inp3.txt");
  let file = match file {
    Ok(file) => file,
    Err(_) => return Vec::new(), // Return an empty vector if file can't be opened
  };

  let reader = io::BufReader::new(file);

  let mut binary_lines: Vec<String> = Vec::new();

  for line in reader.lines() {
    let line = line.unwrap();
    binary_lines.push(line);
  }

  binary_lines
}

fn get_bit_numbers(binary_lines: Vec<String>) -> i64 {
  let line_length = binary_lines[0].len();
  let mut most_bit = String::new();
  let mut least_bit = String::new();

  for bit_index in 0..line_length {
    let mut count_zero = 0;
    let mut count_one = 0;

    for line in &binary_lines {
      match line.chars().nth(bit_index) {
        Some('0') => count_zero += 1,
        Some('1') => count_one += 1,
        _ => panic!("Invalid character in input: only '0' or '1' are allowed."),
      }
    }

    if count_one >= count_zero {
      most_bit.push('1');
      least_bit.push('0');
    } else {
      most_bit.push('0');
      least_bit.push('1');
    }
  }

  let most_bit_value = i64::from_str_radix(&most_bit, 2).expect("Invalid binary string");
  let least_bit_value = i64::from_str_radix(&least_bit, 2).expect("Invalid binary string");

  most_bit_value * least_bit_value
}

pub fn solve() {
  let binary_lines = read_file();
  let res = get_bit_numbers(binary_lines);
  println!("Part one --> {res}");
}
