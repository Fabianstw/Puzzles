use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<(Vec<String>, Vec<String>)> {
  let file = match File::open("src/d8/inp8.txt") {
    Ok(file) => file,
    Err(_) => return Vec::new(),
  };

  let reader = io::BufReader::new(file);
  let mut lines: Vec<(Vec<String>, Vec<String>)> = Vec::new();

  for line in reader.lines() {
    let line = line.unwrap();
    let mut parts = line.split(" | ");
    let left_vec: Vec<String> = parts.next()
                                     .unwrap()
                                     .split_whitespace()
                                     .map(String::from)
                                     .collect();
    let right_vec: Vec<String> = parts.next()
                                      .unwrap()
                                      .split_whitespace()
                                      .map(String::from)
                                      .collect();

    lines.push((left_vec, right_vec));
  }
  lines
}

fn count_uniques(lines: &Vec<(Vec<String>, Vec<String>)>) -> i32 {
  let mut uniques: i32 = 0;
  for line in lines {
    for output_value in &line.1 {
      match output_value.len() {
        2 | 3 | 4 | 7 => uniques += 1,
        _ => (),
      }
    }
  }
  uniques
}

pub fn solve() {
  let lines = read_file();
  let uniques = count_uniques(&lines);
  println!("Part one --> {uniques}");
}
