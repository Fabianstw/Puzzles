//
// Copyright Fabian Stiewe
//

#include "utils/utils.h"

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> splitString(const std::string& str,
                                     const std::string& delimiter) {
  std::vector<std::string> tokens;

  if (delimiter.empty()) {
    for (char ch : str) {
      tokens.emplace_back(1, ch);
    }
  } else {
    std::stringstream ss(str);
    std::string token;

    while (std::getline(ss, token, delimiter[0])) {
      tokens.push_back(token);
    }
  }

  return tokens;
}

std::vector<std::string> readFile(const std::string& filename) {
  std::vector<std::string> lines;

  if (std::ifstream file(filename); file.is_open()) {
    std::string line;
    while (std::getline(file, line)) {
      lines.push_back(line);
    }
    file.close();
  } else {
    std::cerr << "Unable to open file" << std::endl;
  }

  return lines;
}
