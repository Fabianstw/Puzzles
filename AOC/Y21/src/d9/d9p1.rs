use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<Vec<i32>> {
  let file = match File::open("src/d9/inp9.txt") {
    Ok(file) => file,
    Err(_) => return Vec::new(),
  };

  let reader = io::BufReader::new(file);
  let mut map: Vec<Vec<i32>> = Vec::new();

  for line in reader.lines() {
    let line = line.unwrap();
    let mut row: Vec<i32> = Vec::new();
    for ch in line.chars() {
      row.push(ch.to_digit(10).unwrap() as i32);
    }
    map.push(row);
  }
  map
}

fn find_ground(map: Vec<Vec<i32>>) -> Vec<i32> {
  let mut ground: Vec<i32> = Vec::new();
  for i in 0..map.len() {
    for j in 0..map[i].len() {
      let mut all_lower = true;
      if (i > 0 && map[i - 1][j] <= map[i][j])
         || (i < map.len() - 1 && map[i + 1][j] <= map[i][j])
         || (j > 0 && map[i][j - 1] <= map[i][j])
         || (j < map[i].len() - 1 && map[i][j + 1] <= map[i][j])
      {
        all_lower = false;
      }
      if all_lower {
        ground.push(map[i][j]);
      }
    }
  }
  ground
}

fn compute_risk_level(map: Vec<Vec<i32>>) -> i32 {
  let ground = find_ground(map);
  let mut risk_level = 0;
  for i in 0..ground.len() {
    risk_level += ground[i];
  }
  risk_level + ground.len() as i32
}

pub fn solve() {
  
  for i in 0..(5_isize.pow(15)) {
    if i % 100000000 == 0 {
      println!("{}", i);
    }
  }
  
  let map = read_file();
  let res = compute_risk_level(map);
  println!("Part one --> {res}")
}
