use std::collections::HashSet;
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

fn find_ground(map: Vec<Vec<i32>>) -> Vec<(i32, i32)> {
  let mut ground: Vec<(i32, i32)> = Vec::new();
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
        ground.push((i as i32, j as i32));
      }
    }
  }
  ground
}

fn dfs_alternative(start: (i32, i32), map: Vec<Vec<i32>>) -> usize {
  let mut stack: Vec<(i32, i32)> = Vec::new();
  let mut seen: HashSet<(i32, i32)> = HashSet::new();
  stack.push(start);
  while stack.len() > 0 {
    let (x, y) = stack.pop().unwrap();
    seen.insert((x, y));
    for (dx, dy) in vec![(0, 1), (0, -1), (1, 0), (-1, 0)] {
      let new_x = x + dx;
      let new_y = y + dy;
      if new_x >= 0 && new_x < map.len() as i32 && new_y >= 0 && new_y < map[0].len() as i32 {
        if !seen.contains(&(new_x, new_y)) && map[new_x as usize][new_y as usize] >= map[x as usize][y as usize] && map[new_x as usize][new_y as usize] != 9 {
          stack.push((new_x, new_y));
        }
      }
    }
  }
  seen.len()
}

fn find_basins(map: Vec<Vec<i32>>) -> usize {
  let ground = find_ground(map.clone());
  let mut basins: Vec<usize> = Vec::new();
  for point in ground {
    basins.push(dfs_alternative(point, map.clone()));
  }
  basins.sort();
  basins.reverse();
  basins[0] * basins[1] * basins[2]
}

pub fn solve() {
  let map = read_file();
  let res = find_basins(map);
  println!("Part one --> {res}")
}
