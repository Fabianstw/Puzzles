//
// Copyright 2025 Fabian Stiewe
//

#include "D2/sol2.h"

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::ifstream;
using std::string;
using std::vector;

vector<string> readFileLines2() {
  vector<string> lines;

  if (ifstream file("D2/inp.txt"); file.is_open()) {
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

std::vector<std::string> split(const std::string& str, char delimiter) {
  std::vector<std::string> tokens;
  std::stringstream ss(str);
  std::string token;

  while (std::getline(ss, token, delimiter)) {
    tokens.push_back(token);
  }

  return tokens;
}

std::map<std::string, std::string> mapping = {
    {"A", "X"}, {"B", "Y"}, {"C", "Z"}};
std::map<std::string, int> scores = {{"X", 1}, {"Y", 2}, {"Z", 3}};
std::map<std::string, int> gameScores = {
    {"AX", 3}, {"AY", 6}, {"AZ", 0}, {"BX", 0}, {"BY", 3},
    {"BZ", 6}, {"CX", 6}, {"CY", 0}, {"CZ", 3},
};

int totalScore(const vector<string>& lines) {
  int totalScore = 0;

  for (const auto& line : lines) {
    vector<string> lineParts = split(line, *" ");
    totalScore += scores[lineParts[1]];
    totalScore += gameScores[lineParts[0] + lineParts[1]];
  }

  return totalScore;
}

int totalScoreChangedRules(const vector<string>& lines) {
  int totalScore = 0;

  std::map<std::string, std::string> winMap = {
      {"A", "Y"}, {"B", "Z"}, {"C", "X"}};
  std::map<std::string, std::string> looseMap = {
      {"A", "Z"}, {"B", "X"}, {"C", "Y"}};

  for (const auto& line : lines) {
    vector<string> lineParts = split(line, *" ");
    if (lineParts[1] == "X") {
      totalScore += scores[looseMap[lineParts[0]]];
    } else if (lineParts[1] == "Y") {
      totalScore += scores[mapping[lineParts[0]]] + 3;
    } else if (lineParts[1] == "Z") {
      totalScore += scores[winMap[lineParts[0]]] + 6;
    }
  }

  return totalScore;
}

void solve2() {
  cout << "Day 2 solutions:" << endl;
  const vector<string> LINES = readFileLines2();
  cout << "Part A: " << totalScore(LINES) << endl;
  cout << "Part B: " << totalScoreChangedRules(LINES) << endl;
}
