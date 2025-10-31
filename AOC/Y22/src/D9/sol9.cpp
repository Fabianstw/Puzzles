//
// Copyright 2025
//

#include "D9/sol9.h"

#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;

int uniquePositions(const vector<string>& lines) {
  std::tuple<int, int> positionHead = {0, 0};
  std::tuple<int, int> positionTail = {0, 0};
  std::set<std::tuple<int, int>> positions;
  positions.insert(positionHead);

  for (const auto& line : lines) {
    vector<string> tokens = splitString(line, " ");
    string dir = tokens[0];
    int steps = std::stoi(tokens[1]);
    for (int i = 0; i < steps; i++) {
      if (dir == "U") {
        std::get<1>(positionHead)++;
      } else if (dir == "D") {
        std::get<1>(positionHead)--;
      } else if (dir == "L") {
        std::get<0>(positionHead)--;
      } else if (dir == "R") {
        std::get<0>(positionHead)++;
      }
      // Check if the tail needs to move
      if (std::abs(std::get<0>(positionHead) - std::get<0>(positionTail)) > 1 ||
          std::abs(std::get<1>(positionHead) - std::get<1>(positionTail)) > 1) {
        // Move the tail left, right, up or down to the head
        if (std::get<0>(positionHead) > std::get<0>(positionTail)) {
          std::get<0>(positionTail)++;
        } else if (std::get<0>(positionHead) < std::get<0>(positionTail)) {
          std::get<0>(positionTail)--;
        }
        if (std::get<1>(positionHead) > std::get<1>(positionTail)) {
          std::get<1>(positionTail)++;
        } else if (std::get<1>(positionHead) < std::get<1>(positionTail)) {
          std::get<1>(positionTail)--;
        }
      }
      // Add the tail position to the set
      positions.insert(positionTail);
    }
  }

  return positions.size();
}

int longRopeUniquePositions(const vector<string>& lines) {
  vector<std::tuple<int, int>> positions(10, {0, 0});
  std::set<std::tuple<int, int>> tailPositions;
  tailPositions.insert(positions[0]);

  for (const auto& line : lines) {
    vector<string> tokens = splitString(line, " ");
    string dir = tokens[0];
    int steps = std::stoi(tokens[1]);
    for (int i = 0; i < steps; i++) {
      if (dir == "U") {
        std::get<1>(positions[0])++;
      } else if (dir == "D") {
        std::get<1>(positions[0])--;
      } else if (dir == "L") {
        std::get<0>(positions[0])--;
      } else if (dir == "R") {
        std::get<0>(positions[0])++;
      }
      // Move the tail
      for (int j = 1; j < positions.size(); j++) {
        if (std::abs(std::get<0>(positions[j - 1]) -
                     std::get<0>(positions[j])) > 1 ||
            std::abs(std::get<1>(positions[j - 1]) -
                     std::get<1>(positions[j])) > 1) {
          // Move the tail left, right, up or down to the head
          if (std::get<0>(positions[j - 1]) > std::get<0>(positions[j])) {
            std::get<0>(positions[j])++;
          } else if (std::get<0>(positions[j - 1]) <
                     std::get<0>(positions[j])) {
            std::get<0>(positions[j])--;
          }
          if (std::get<1>(positions[j - 1]) > std::get<1>(positions[j])) {
            std::get<1>(positions[j])++;
          } else if (std::get<1>(positions[j - 1]) <
                     std::get<1>(positions[j])) {
            std::get<1>(positions[j])--;
          }
        }
      }
      // Add the tail position to the set
      tailPositions.insert(positions.back());
    }
  }

  return tailPositions.size();
}

void solve9() {
  cout << "Day 9 solutions:" << endl;
  const std::vector<std::string> LINES = readFile("D9/inp.txt");
  cout << "Part A: " << uniquePositions(LINES) << endl;
  cout << "Part B: " << longRopeUniquePositions(LINES) << endl;
}
