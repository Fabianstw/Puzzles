//
// Copyright 2025 Fabian Stiewe
//

#include "D1/sol1.h"

#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

using std::cerr;
using std::cout;
using std::endl;
using std::greater;
using std::ifstream;
using std::sort;
using std::stoi;
using std::string;
using std::vector;

vector<string> readFileLines() {
  vector<string> lines;

  if (ifstream file("D1/inp.txt"); file.is_open()) {
    string line;
    while (std::getline(file, line)) {
      lines.push_back(line);
    }
    file.close();
  } else {
    std::cerr << "Unable to open file" << std::endl;
  }

  return lines;
}

int getMostCalories(const vector<string>& elves) {
  int currentCalories = 0;
  int currentMax = 0;
  for (const auto& elve : elves) {
    if (!elve.empty()) {
      currentCalories += stoi(elve);
    } else {
      if (currentCalories > currentMax) {
        currentMax = currentCalories;
      }
      currentCalories = 0;
    }
  }
  return currentMax;
}

int topThreeCalories(const vector<string>& elves) {
  int currentCalories = 0;
  vector<int> calories;
  for (const auto& elve : elves) {
    if (!elve.empty()) {
      currentCalories += stoi(elve);
    } else {
      calories.push_back(currentCalories);
      currentCalories = 0;
    }
  }
  // sort in decreasing order
  sort(calories.begin(), calories.end(), greater<>());

  return calories[0] + calories[1] + calories[2];
}

void solve() {
  const vector<string> LINES = readFileLines();
  cout << "Day 1 solutions:" << endl;
  cout << getMostCalories(LINES) << endl;
  cout << topThreeCalories(LINES) << endl;
}
