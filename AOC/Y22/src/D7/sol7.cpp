//
// Copyright
//

#include "D7/sol7.h"

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;

string joinPath(const vector<string>& pathVec) {
  if (pathVec.empty()) return "/";
  string path;
  for (const string& part : pathVec) {
    path += "/" + part;
  }
  return path;
}

std::unordered_map<string, int> getFolderSizes(const vector<string>& lines) {
  std::unordered_map<string, int> folderSizes;
  vector<string> currentPath;

  for (size_t i = 1; i < lines.size(); ++i) {
    if (const string& line = lines[i]; line[0] == '$') {
      if (line[2] == 'c') {
        if (line[5] == '.') {
          if (!currentPath.empty()) currentPath.pop_back();  // cd ..
        } else {
          string folder = line.substr(5);
          currentPath.push_back(folder);  // cd xyz
        }
      }
    } else {
      if (line[0] != 'd') {
        // file with size
        size_t spacePos = line.find(' ');
        int size = stoi(line.substr(0, spacePos));
        // Update size of all parent directories
        for (size_t depth = 0; depth <= currentPath.size(); ++depth) {
          string subPath =
              joinPath({currentPath.begin(), currentPath.begin() + depth});
          folderSizes[subPath] += size;
        }
      }
    }
  }
  return folderSizes;
}

int dirSizes(const vector<string>& lines, const int THRESHOLD) {
  std::unordered_map<string, int> folderSizes = getFolderSizes(lines);
  int result = 0;
  for (const auto& [folder, size] : folderSizes) {
    if (size <= THRESHOLD) {
      result += size;
    }
  }
  return result;
}

int deleteFolder(const vector<string>& lines, int threshold) {
  std::unordered_map<string, int> folderSizes = getFolderSizes(lines);
  const int TOTAL_SIZE = folderSizes["/"];
  int currentBest = TOTAL_SIZE;
  for (const auto& [folder, size] : folderSizes) {
    if (folder == "/") continue;  // Skip the root folder
    if (TOTAL_SIZE - size > threshold) continue;
    if (size < currentBest) {
      currentBest = size;
    }
  }
  return currentBest;
}

void solve7() {
  cout << "Day 7 solutions: " << endl;
  const vector<string> LINES = readFile("D7/inp.txt");
  cout << "Part A: " << dirSizes(LINES, 100000) << endl;
  cout << "Part B: " << deleteFolder(LINES, 40000000) << endl;
}
