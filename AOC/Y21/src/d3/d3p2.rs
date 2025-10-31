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

fn rating(mut binary_lines: Vec<String>, is_oxygen: bool) -> i64 {
  let line_length = binary_lines[0].len();

  for bit_index in 0..line_length {
    let mut zero_lines: Vec<String> = Vec::new();
    let mut one_lines: Vec<String> = Vec::new();

    for line in &binary_lines {
      match line.chars().nth(bit_index) {
        Some('0') => zero_lines.push(line.clone()),
        Some('1') => one_lines.push(line.clone()),
        _ => panic!("Invalid char"),
      }
    }

    binary_lines = if is_oxygen {
      if one_lines.len() >= zero_lines.len() {
        one_lines
      } else {
        zero_lines
      }
    } else {
      if zero_lines.len() <= one_lines.len() {
        zero_lines
      } else {
        one_lines
      }
    };

    // Stop iterating if only one line remains
    if binary_lines.len() == 1 {
      break;
    }
  }

  i64::from_str_radix(&binary_lines[0], 2).unwrap()
}

pub fn solve() {
  let binary_lines = read_file();
  let oxygen = rating(binary_lines.clone(), true);
  let co2 = rating(binary_lines.clone(), false);
  let res = oxygen * co2;
  println!("Part two --> {res}");
}
