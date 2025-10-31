use std::cmp::{max, min};
use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> Vec<(i32, i32, i32, i32)> {
  let file = match File::open("src/d5/inp5.txt") {
    Ok(file) => file,
    Err(_) => return Vec::new(),
  };

  let reader = io::BufReader::new(file);

  let mut coordinate_lines: Vec<(i32, i32, i32, i32)> = Vec::new();

  for line in reader.lines() {
    let line = line.unwrap();
    let mut line = line.split(" -> ");
    let first_coords = line.next().unwrap().split(",");
    let second_coords = line.next().unwrap().split(",");
    let first_coords: Vec<i32> = first_coords.map(|x| x.parse().unwrap()).collect();
    let second_coords: Vec<i32> = second_coords.map(|x| x.parse().unwrap()).collect();
    coordinate_lines.push((first_coords[0], first_coords[1], second_coords[0], second_coords[1]));
  }

  coordinate_lines
}

fn get_max_coords(coordinate_lines: &Vec<(i32, i32, i32, i32)>) -> (i32, i32) {
  let mut max_x = 0;
  let mut max_y = 0;
  for line in coordinate_lines.iter() {
    if line.0 > max_x {
      max_x = line.0;
    }
    if line.1 > max_y {
      max_y = line.1;
    }
    if line.2 > max_x {
      max_x = line.2;
    }
    if line.3 > max_y {
      max_y = line.3;
    }
  }
  (max_x, max_y)
}

fn count_higher(grid: Vec<Vec<i32>>, value: i32) -> i32 {
  let mut count = 0;
  for row in grid.iter() {
    for cell in row.iter() {
      if *cell > value {
        count += 1;
      }
    }
  }
  count
}

fn draw_lines(coordinate_lines: Vec<(i32, i32, i32, i32)>) -> i32 {
  let (max_x, max_y) = get_max_coords(&coordinate_lines);
  let mut grid = vec![vec![0; max_x as usize + 1]; max_y as usize + 1];
  for line in coordinate_lines.iter() {
    if line.0 == line.2 {
      for y in min(line.1, line.3)..max(line.1, line.3) + 1 {
        grid[y as usize][line.0 as usize] += 1;
      }
    }
    if line.1 == line.3 {
      for x in min(line.0, line.2)..max(line.0, line.2) + 1 {
        grid[line.1 as usize][x as usize] += 1;
      }
    }
  }
  count_higher(grid, 1)
}

pub fn solve() {
  let coordinate_lines = read_file();
  let res = draw_lines(coordinate_lines);
  println!("Part one --> {res}")
}
