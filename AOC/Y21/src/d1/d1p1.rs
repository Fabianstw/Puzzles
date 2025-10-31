use std::fs::File;
use std::io::{self, BufRead, Error};

fn read_file() -> Result<Vec<i32>, Error> {
  let file = File::open("inp1.txt")?;
  let reader = io::BufReader::new(file);

  let mut lines: Vec<i32> = Vec::new();

  for line in reader.lines() {
    let line = line?;
    match line.parse::<i32>() {
      Ok(num) => lines.push(num),
      Err(_) => eprintln!("Warning: Could not parse line '{}' as i32", line),
    }
  }

  Ok(lines)
}

fn get_increasings(lines: Vec<i32>) -> i32 {
  let mut res = 0;
  for i in 1..lines.len() {
    if lines[i] > lines[i - 1] {
      res += 1;
    }
  }
  res
}

pub fn solve() {
  let lines: Result<Vec<i32>, Error> = read_file();
  match lines {
    Ok(lines) => {
      let result: i32 = get_increasings(lines);
      println!("Part one --> {result}");
    }
    Err(e) => {
      println!("{}", e);
    }
  }
}
