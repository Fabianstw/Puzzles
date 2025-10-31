//
// Copyright [2025]
//

#include "D8/sol8.h"

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;

int countVisibleTrees(const vector<string>& lines) {
  int visible = 0;

  for (int i = 0; i < lines.size(); i++) {
    for (int j = 0; j < lines[i].size(); j++) {
      if (i == 0 || j == 0 || i == lines.size() - 1 ||
          j == lines[i].size() - 1) {
        visible++;
        continue;
      }
      // check if all to the left are smaller
      bool left = true;
      for (int k = j - 1; k >= 0; k--) {
        if (lines[i][k] >= lines[i][j]) {
          left = false;
          break;
        }
      }
      // check if all to the right are smaller
      bool right = true;
      for (int k = j + 1; k < lines[i].size(); k++) {
        if (lines[i][k] >= lines[i][j]) {
          right = false;
          break;
        }
      }
      // check if all to the top are smaller
      bool top = true;
      for (int k = i - 1; k >= 0; k--) {
        if (lines[k][j] >= lines[i][j]) {
          top = false;
          break;
        }
      }
      // check if all to the bottom are smaller
      bool bottom = true;
      for (int k = i + 1; k < lines.size(); k++) {
        if (lines[k][j] >= lines[i][j]) {
          bottom = false;
          break;
        }
      }
      if (left || right || top || bottom) {
        visible++;
      }
    }
  }

  return visible;
}

int viewingDistance(const std::vector<std::string>& grid, int i, int j,
                    const int DI, const int DJ) {
  int distance = 0;
  const int ROWS = grid.size();
  const int COLS = grid[0].size();
  const char HEIGHT = grid[i][j];

  i += DI;
  j += DJ;

  while (i >= 0 && i < ROWS && j >= 0 && j < COLS) {
    distance++;
    if (grid[i][j] >= HEIGHT) break;
    i += DI;
    j += DJ;
  }

  return distance;
}

int bestSpot(const std::vector<std::string>& lines) {
  int bestScore = 0;
  for (int i = 0; i < lines.size(); i++) {
    for (int j = 0; j < lines[0].size(); j++) {
      int score = viewingDistance(lines, i, j, 0, -1) *
                  viewingDistance(lines, i, j, 0, 1) *
                  viewingDistance(lines, i, j, -1, 0) *
                  viewingDistance(lines, i, j, 1, 0);
      bestScore = std::max(bestScore, score);
    }
  }
  return bestScore;
}

void solve8() {
  cout << "Day 8 solutions: " << endl;
  std::vector<std::string> lines = readFile("D8/inp.txt");
  cout << "Part A: " << countVisibleTrees(lines) << endl;
  cout << "Part B: " << bestSpot(lines) << endl;
}
