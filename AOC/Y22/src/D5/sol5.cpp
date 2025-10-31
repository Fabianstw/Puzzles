//
// Copyright 2025
//

#include "D5/sol5.h"

#include <iostream>
#include <string>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;

string rearrange(const vector<string>& input) {
  /*
    [V]     [B]                     [F]
    [N] [Q] [W]                 [R] [B]
    [F] [D] [S]     [B]         [L] [P]
    [S] [J] [C]     [F] [C]     [D] [G]
    [M] [M] [H] [L] [P] [N]     [P] [V]
    [P] [L] [D] [C] [T] [Q] [R] [S] [J]
    [H] [R] [Q] [S] [V] [R] [V] [Z] [S]
    [J] [S] [N] [R] [M] [T] [G] [C] [D]
     1   2   3   4   5   6   7   8   9

   Brute-Force stacks, too lazy to parse them ...
   */

  vector<vector<string>> stacks = {{"J", "H", "P", "M", "S", "F", "N", "V"},
                                   {"S", "R", "L", "M", "J", "D", "Q"},
                                   {"N", "Q", "D", "H", "C", "S", "W", "B"},
                                   {"R", "S", "C", "L"},
                                   {"M", "V", "T", "P", "F", "B"},
                                   {"T", "R", "Q", "N", "C"},
                                   {"G", "V", "R"},
                                   {"C", "Z", "S", "P", "D", "L", "R"},
                                   {"D", "S", "J", "V", "G", "P", "B", "F"}};

  for (const auto& line : input) {
    if (line.empty() || line[0] == ' ' || line[0] == '[') {
      continue;
    }
    vector<string> tokens = splitString(line, " ");
    for (int i = 0; i < std::stoi(tokens[1]); i++) {
      string ele = stacks[std::stoi(tokens[3]) - 1].back();
      stacks[std::stoi(tokens[3]) - 1].pop_back();
      stacks[std::stoi(tokens[5]) - 1].push_back(ele);
    }
  }

  string result;
  for (const auto& stack : stacks) {
    if (!stack.empty()) {
      result += stack.back();
    }
  }
  return result;
}

string rearrange2(const vector<string>& input) {
  vector<vector<string>> stacks = {{"J", "H", "P", "M", "S", "F", "N", "V"},
                                   {"S", "R", "L", "M", "J", "D", "Q"},
                                   {"N", "Q", "D", "H", "C", "S", "W", "B"},
                                   {"R", "S", "C", "L"},
                                   {"M", "V", "T", "P", "F", "B"},
                                   {"T", "R", "Q", "N", "C"},
                                   {"G", "V", "R"},
                                   {"C", "Z", "S", "P", "D", "L", "R"},
                                   {"D", "S", "J", "V", "G", "P", "B", "F"}};

  for (const auto& line : input) {
    if (line.empty() || line[0] == ' ' || line[0] == '[') {
      continue;
    }
    vector<string> tokens = splitString(line, " ");
    vector<string> tmp = {};
    for (int i = 0; i < std::stoi(tokens[1]); i++) {
      string ele = stacks[std::stoi(tokens[3]) - 1].back();
      stacks[std::stoi(tokens[3]) - 1].pop_back();
      tmp.push_back(ele);
    }
    for (int i = static_cast<int>(tmp.size()) - 1; i >= 0; i--) {
      stacks[std::stoi(tokens[5]) - 1].push_back(tmp[i]);
    }
  }

  string result;
  for (const auto& stack : stacks) {
    if (!stack.empty()) {
      result += stack.back();
    }
  }
  return result;
}

void solve5() {
  cout << "Day 5 solutions:" << endl;
  const vector<string> LINES = readFile("D5/inp.txt");
  cout << "Part A: " << rearrange(LINES) << endl;
  cout << "Part B: " << rearrange2(LINES) << endl;
}
