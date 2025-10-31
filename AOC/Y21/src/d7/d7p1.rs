use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<i16> {
  let file = match File::open("src/d7/inp7.txt") {
    Ok(file) => file,
    Err(_) => return Vec::new(),
  };

  let reader = io::BufReader::new(file);
  let mut crabs: Vec<i16> = Vec::new();

  let line = reader.lines().next().unwrap().unwrap();
  let line = line.split(",");
  for num in line {
    crabs.push(num.parse().unwrap());
  }
  crabs
}

fn min_amount_movement(crabs: Vec<i16>, part1: bool) -> usize {
  let mut best = usize::MAX;

  for i in *crabs.iter().min().unwrap()..=*crabs.iter().max().unwrap() {
    let mut moves = 0;
    for crab in &crabs {
      if part1 {
        moves += (crab - i).abs() as usize;
      } else {
        let distance = (crab - i).abs() as usize;
        if let Some(triangle_number) = distance.checked_mul(distance + 1)
                                               .and_then(|val| val.checked_div(2))
        {
          moves += triangle_number;
        } else {
          // Overflow occurred
          moves = usize::MAX;
          break;
        }
      }
    }
    best = best.min(moves);
  }

  best
}

pub fn solve() {
  let crabs = read_file();
  let fuel = min_amount_movement(crabs.clone(), true);
  println!("Part one --> {}", fuel);
  let fuel = min_amount_movement(crabs.clone(), false);
  println!("Part two --> {}", fuel);
}
