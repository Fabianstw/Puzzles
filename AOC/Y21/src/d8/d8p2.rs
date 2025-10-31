use std::collections::{HashMap, HashSet};
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

fn find_uniques(line: Vec<String>) -> (String, String, String, String) {
  let mut one: String = String::new();
  let mut seven: String = String::new();
  let mut four: String = String::new();
  let mut eight: String = String::new();

  for output_value in line {
    match output_value.len() {
      2 => one = output_value.clone(),
      3 => seven = output_value.clone(),
      4 => four = output_value.clone(),
      7 => eight = output_value.clone(),
      _ => (),
    }
  }

  (one, seven, four, eight)
}

fn letter_diff(s1: &str, s2: &str) -> String {
  let set1: HashSet<char> = s1.chars().collect();
  let set2: HashSet<char> = s2.chars().collect();

  set1.difference(&set2).cloned().collect::<String>()
  + &*set2.difference(&set1).cloned().collect::<String>()
}

fn find_encoding(lines: &Vec<(Vec<String>, Vec<String>)>) -> i32 {
  let mut final_res: i32 = 0;
  for (left, right) in lines {
    let (one, seven, four, eight) = find_uniques(left.clone());
    let top: String = letter_diff(&seven, &one);

    let mut bottom: String = String::new();
    for value in left {
      let inter = letter_diff(&four, &value);
      if inter.len() == 2 && value.len() > 4 {
        bottom = letter_diff(&top, &inter);
        break;
      }
    }

    let mut middle: String = String::new();
    for value in left {
      let inter = letter_diff(&*(seven.clone() + &*bottom.clone()), &value);
      if inter.len() == 1 && value.len() == 5 {
        middle = inter;
        break;
      }
    }

    let top_left: String = letter_diff(&*(one.clone() + &*middle.clone()), &four);

    let mut bottom_right: String = String::new();
    for value in left {
      let inter =
        letter_diff(&*(top.clone() + &*middle.clone() + &*bottom.clone() + &*top_left.clone()),
                    &value);
      if inter.len() == 1 && value.len() == 5 {
        bottom_right = inter;
        break;
      }
    }

    let mut bottom_left: String = String::new();
    for value in left {
      let inter = letter_diff(&*(top.clone()
                                 + &*middle.clone()
                                 + &*bottom.clone()
                                 + &*top_left.clone()
                                 + &*bottom_right.clone()),
                              &value);
      if inter.len() == 1 && value.len() == 6 && !one.contains(&inter) {
        bottom_left = inter;
        break;
      }
    }

    let top_right: String = letter_diff(&*(top.clone()
                                           + &*middle.clone()
                                           + &*bottom.clone()
                                           + &*top_left.clone()
                                           + &*bottom_right.clone()
                                           + &*bottom_left.clone()),
                                        &eight);
    let number_map = build_numbers(&top,
                                   &middle,
                                   &bottom,
                                   &top_left,
                                   &bottom_right,
                                   &bottom_left,
                                   &top_right);

    let mut res: String = String::new();
    for value in right {
      // iterate though the dict
      for (key, number) in &number_map {
        if letter_diff(&value, &key).len() == 0 {
          res += number;
          break;
        }
      }
    }
    final_res += res.parse::<i32>().unwrap();
  }
  final_res
}

fn build_numbers(top: &str,
                 middle: &str,
                 bottom: &str,
                 top_left: &str,
                 bottom_right: &str,
                 bottom_left: &str,
                 top_right: &str)
                 -> HashMap<String, String> {
  let number_map: HashMap<String, String> = [(top_right.to_owned() + bottom_right, "1"),
                                             (top.to_owned()
                                              + middle
                                              + bottom
                                              + top_right
                                              + bottom_left,
                                              "2"),
                                             (top.to_owned()
                                              + middle
                                              + bottom
                                              + top_right
                                              + bottom_right,
                                              "3"),
                                             (top_left.to_owned()
                                              + top_right
                                              + middle
                                              + bottom_right,
                                              "4"),
                                             (top.to_owned()
                                              + middle
                                              + bottom
                                              + top_left
                                              + bottom_right,
                                              "5"),
                                             (top.to_owned()
                                              + middle
                                              + bottom
                                              + top_left
                                              + bottom_left
                                              + bottom_right,
                                              "6"),
                                             (top.to_owned() + top_right + bottom_right, "7"),
                                             (top.to_owned()
                                              + middle
                                              + bottom
                                              + top_left
                                              + bottom_left
                                              + bottom_right
                                              + top_right,
                                              "8"),
                                             (top.to_owned()
                                              + middle
                                              + bottom
                                              + top_left
                                              + bottom_right
                                              + top_right,
                                              "9"),
                                             (top.to_owned()
                                              + bottom
                                              + top_left
                                              + bottom_left
                                              + bottom_right
                                              + top_right,
                                              "0")].iter()
                                                   .map(|(k, v)| (k.clone(), v.to_string()))
                                                   .collect();
  number_map
}

pub fn solve() {
  let lines = read_file();
  let res = find_encoding(&lines);
  println!("Part two --> {res}");
}
