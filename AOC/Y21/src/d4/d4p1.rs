use std::fs::File;
use std::io::{self, BufRead};

fn read_file() -> (Vec<i16>, Vec<Vec<Vec<i16>>>) {
  let file = match File::open("src/d4/inp4.txt") {
    Ok(file) => file,
    Err(_) => return (Vec::new(), Vec::new()),
  };

  let reader = io::BufReader::new(file);

  let mut lines = reader.lines().filter_map(Result::ok);
  let values = lines.next()
                    .map(|line| {
                      line.split(',')
                          .filter_map(|x| x.parse::<i16>().ok())
                          .collect()
                    })
                    .unwrap_or_default();

  let mut boards = Vec::new();
  let mut current_board = Vec::new();

  for line in lines {
    if line.is_empty() {
      if !current_board.is_empty() {
        boards.push(current_board);
        current_board = Vec::new();
      }
    } else {
      let row = line.split_whitespace()
                    .filter_map(|x| x.parse::<i16>().ok())
                    .collect();
      current_board.push(row);
    }
  }

  if !current_board.is_empty() {
    boards.push(current_board);
  }

  (values, boards)
}

fn x_value(value: i16, boards: &mut Vec<Vec<Vec<i16>>>) {
  for board in boards.iter_mut() {
    for i in 0..board.len() {
      for j in 0..board[i].len() {
        // Fixed index typo
        if board[i][j] == value {
          board[i][j] = -1;
        }
      }
    }
  }
}

fn check_bingo(board: &Vec<Vec<i16>>) -> bool {
  let mut bingo = true;
  for i in 0..board.len() {
    let mut row_bingo = true;
    let mut col_bingo = true;
    for j in 0..board[i].len() {
      if board[i][j] != -1 {
        row_bingo = false;
      }
      if board[j][i] != -1 {
        col_bingo = false;
      }
    }
    if row_bingo || col_bingo {
      return true;
    }
    if board[i][i] != -1 {
      bingo = false;
    }
  }
  bingo
}

fn get_free_values(board: &Vec<Vec<i16>>) -> Vec<i16> {
  let mut free_values = Vec::new();
  for row in board.iter() {
    for value in row.iter() {
      if *value != -1 {
        free_values.push(*value);
      }
    }
  }
  free_values
}

fn simulate_bingo(values: Vec<i16>, mut boards: Vec<Vec<Vec<i16>>>) -> i64 {
  for value in values {
    x_value(value, &mut boards);
    for board in boards.iter() {
      if check_bingo(board) {
        return get_free_values(board).iter().sum::<i16>() as i64 * value as i64;
      }
    }
  }
  -1
}

pub fn solve() {
  let (values, boards) = read_file();
  let res = simulate_bingo(values, boards);
  println!("Part one --> {res}")
}
