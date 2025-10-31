use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<i8> {
  let file = match File::open("src/d6/inp6.txt") {
    Ok(file) => file,
    Err(_) => return Vec::new(),
  };

  let reader = io::BufReader::new(file);
  let mut fishes: Vec<i8> = Vec::new();

  let line = reader.lines().next().unwrap().unwrap();
  let line = line.split(",");
  for num in line {
    fishes.push(num.parse().unwrap());
  }
  fishes
}

fn simulate_fish(fish: i8, days_left: i16, cache: &mut HashMap<(i8, i16), usize>) -> usize {
  if days_left == 0 {
    return 1;
  }
  if let Some(&amount) = cache.get(&(fish, days_left)) {
    amount
  } else {
    if fish == 0 {
      let amount = simulate_fish(6, days_left - 1, cache) + simulate_fish(8, days_left - 1, cache);
      cache.insert((fish, days_left), amount);
      amount
    } else {
      let amount = simulate_fish(fish - 1, days_left - 1, cache);
      cache.insert((fish, days_left), amount);
      amount
    }
  }
}

fn simulate_fishes(fishes: Vec<i8>, days: i16) -> usize {
  let mut amount = 0;
  let mut cache: HashMap<(i8, i16), usize> = HashMap::new();
  for fish in fishes {
    amount += simulate_fish(fish, days, &mut cache);
  }
  amount
}

pub fn solve() {
  let fishes = read_file();
  let result_part1 = simulate_fishes(fishes.clone(), 80);
  println!("Part one --> {result_part1}");
  let result_part2 = simulate_fishes(fishes.clone(), 256);
  println!("Part two --> {result_part2}");
}
