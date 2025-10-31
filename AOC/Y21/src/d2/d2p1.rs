use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<(String, String)> {
  let file = File::open("src/d2/inp2.txt");
  let file = match file {
    Ok(file) => file,
    Err(_) => return Vec::new(), // Return an empty vector if file can't be opened
  };

  let reader = io::BufReader::new(file);

  let mut instructions: Vec<(String, String)> = Vec::new();

  for line in reader.lines() {
    let line = match line {
      Ok(line) => line,
      Err(_) => continue, // Skip lines that can't be read
    };

    // Split line by space and check for exactly two parts
    let instruction: Vec<&str> = line.split(" ").collect();
    if instruction.len() == 2 {
      instructions.push((instruction[0].to_string(), instruction[1].to_string()));
    }
  }

  instructions
}

fn move_submarine(instructions: Vec<(String, String)>) -> i32 {
  let mut start = (0, 0);
  for (direction, distance) in instructions {
    let distance = distance.parse::<i32>().unwrap();
    match direction.as_str() {
      "forward" => start.0 += distance,
      "up" => start.1 -= distance,
      "down" => start.1 += distance,
      _ => eprintln!("Warning: Unknown direction '{}'", direction),
    }
  }
  start.0 * start.1
}

pub fn solve() {
  let instructions: Vec<(String, String)> = read_file();
  let result: i32 = move_submarine(instructions);
  println!("Part one --> {result}");
}
