//
// Copyright 2025 Fabian Stiewe
//

#include "D3/sol3.h"

#include <algorithm>
#include <cctype>
#include <iostream>
#include <set>
#include <string>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;

int getPriority(const char ITEM) {
  if (std::islower(ITEM)) {
    return ITEM - 'a' + 1;
  }
  if (std::isupper(ITEM)) {
    return ITEM - 'A' + 27;
  }
  return -1;
}

int countFalseOrder(const vector<string>& lines) {
  int totalScore = 0;

  for (const auto& line : lines) {
    vector<string> parts = splitString(line, "");
    int mid = static_cast<int>(parts.size()) / 2;
    std::set<std::string> seenObjects;
    for (int i = 0; i < mid; i++) {
      seenObjects.insert(parts[i]);
    }
    for (int i = mid; i < parts.size(); i++) {
      if (seenObjects.find(parts[i]) != seenObjects.end()) {
        totalScore += getPriority(parts[i][0]);
        break;
      }
    }
  }

  return totalScore;
}

int countBadgeNumbers(const vector<string>& lines) {
  int totalScore = 0;

  for (int i = 0; i < lines.size(); i += 3) {
    std::set<std::string> part1;
    std::set<std::string> part2;
    std::set<std::string> part3;

    vector<string> parts1 = splitString(lines[i], "");
    part1.insert(parts1.begin(), parts1.end());

    vector<string> parts2 = splitString(lines[i + 1], "");
    part2.insert(parts2.begin(), parts2.end());

    vector<string> parts3 = splitString(lines[i + 2], "");
    part3.insert(parts3.begin(), parts3.end());

    std::set<std::string> intersection12;
    std::set<std::string> intersection123;
    // Compute intersection of part_1 and part_2
    std::set_intersection(
        part1.begin(), part1.end(), part2.begin(), part2.end(),
        std::inserter(intersection12, intersection12.begin()));

    // Compute intersection of the result with part_3
    std::set_intersection(
        intersection12.begin(), intersection12.end(), part3.begin(),
        part3.end(), std::inserter(intersection123, intersection123.begin()));

    totalScore += getPriority((*intersection123.begin())[0]);
  }

  return totalScore;
}

void solve3() {
  cout << "Day 3 solutions: " << endl;
  std::string filename = "D3/inp.txt";
  const vector<string> LINES = readFile(filename);
  cout << "Part A: " << countFalseOrder(LINES) << endl;
  cout << "Part B: " << countBadgeNumbers(LINES) << endl;
}
