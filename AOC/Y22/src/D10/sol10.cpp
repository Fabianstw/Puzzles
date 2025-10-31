//
// Copyright
//

#include "D10/sol10.h"

#include <iostream>
#include <string>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;

int registerValue(const std::vector<std::string>& lines) {
  int sum = 0;
  int cycle = 0;
  int registerVal = 1;

  auto maybeUpdateSum = [&](int currentCycle) {
    if ((currentCycle - 20) % 40 == 0 && currentCycle <= 220) {
      sum += currentCycle * registerVal;
    }
  };

  for (const auto& line : lines) {
    if (line == "noop") {
      cycle++;
      maybeUpdateSum(cycle);
    } else {
      const int VAL = std::stoi(splitString(line, " ")[1]);
      cycle++;
      maybeUpdateSum(cycle);
      cycle++;
      maybeUpdateSum(cycle);
      registerVal += VAL;
    }
  }

  return sum;
}

void drawImage(const vector<string>& lines) {
  int cycle = 0;
  int registerVal = 1;
  vector drawLines(6, string(40, '.'));
  int index = 0;

  auto drawPixel = [&](const int CURRENT_CYCLE) {
    int pos = CURRENT_CYCLE % 40;
    if (pos >= registerVal - 1 && pos <= registerVal + 1) {
      drawLines[index][pos] = '#';
    } else {
      drawLines[index][pos] = '.';
    }
    if (++cycle % 40 == 0) {
      index++;
    }
  };

  for (const auto& line : lines) {
    if (line == "noop") {
      drawPixel(cycle);
    } else {
      drawPixel(cycle);
      drawPixel(cycle);
      registerVal += std::stoi(splitString(line, " ")[1]);
    }
  }

  for (const auto& drawLine : drawLines) {
    cout << drawLine << '\n';
  }
}

void solve10() {
  cout << "Day 10 solutions:" << endl;
  const vector<string> LINES = readFile("D10/inp.txt");
  cout << "Part A: " << registerValue(LINES) << endl;
  cout << "Part B:" << endl;
  drawImage(LINES);

  /*
    ####.#..#.###..#..#.####.###..#..#.####.
    #....#.#..#..#.#..#.#....#..#.#..#....#.
    ###..##...#..#.####.###..#..#.#..#...#..
    #....#.#..###..#..#.#....###..#..#..#...
    #....#.#..#.#..#..#.#....#....#..#.#....
    ####.#..#.#..#.#..#.####.#.....##..####.
  */
}
