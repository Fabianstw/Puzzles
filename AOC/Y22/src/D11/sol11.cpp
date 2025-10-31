//
// Copyright
//

#include "D11/sol11.h"

#include <algorithm>
#include <iostream>
#include <optional>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::optional;
using std::string;
using std::vector;

struct Rule {
  vector<int64_t> items;
  string operation;
  optional<int> operand;  // For operations like "*", "+", but not "^2"
  int test;
  int true_target;
  int false_target;
};

const vector<Rule> TEST_MONKEYS = {{{79, 98}, "*", 19, 23, 2, 3},
                                   {{54, 65, 75, 74}, "+", 6, 19, 2, 0},
                                   {{79, 60, 97}, "^2", std::nullopt, 13, 1, 3},
                                   {{74}, "+", 3, 17, 0, 1}};

const vector<Rule> REAL_MONKEYS = {
    {{50, 70, 54, 83, 52, 78}, "*", 3, 11, 2, 7},
    {{71, 52, 58, 60, 71}, "^2", std::nullopt, 7, 0, 2},
    {{66, 56, 56, 94, 60, 86, 73}, "+", 1, 3, 7, 5},
    {{83, 99}, "+", 8, 5, 6, 4},
    {{98, 98, 79}, "+", 3, 17, 1, 0},
    {{76}, "+", 4, 13, 6, 3},
    {{52, 51, 84, 54}, "*", 17, 19, 4, 1},
    {{82, 86, 91, 79, 94, 92, 59, 94}, "+", 7, 2, 5, 3}};

int frequentMonkeys(std::vector<Rule>& monkeys) {
  vector<int> monkeyItemCount(monkeys.size(), 0);
  for (int i = 0; i < 20; i++) {
    for (int j = 0; j < monkeys.size(); j++) {
      monkeyItemCount[j] += monkeys[j].items.size();
      auto& monkey = monkeys[j];
      for (const auto ITEM : monkey.items) {
        int item1 = ITEM;
        if (monkey.operation == "*") {
          item1 *= monkey.operand.value();
        } else if (monkey.operation == "+") {
          item1 += monkey.operand.value();
        } else if (monkey.operation == "^2") {
          item1 *= item1;
        }
        item1 /= 3;

        if (item1 % monkey.test == 0) {
          monkeys[monkey.true_target].items.push_back(item1);
        } else {
          monkeys[monkey.false_target].items.push_back(item1);
        }
      }
      monkeys[j].items.clear();
    }
  }
  const auto FIRST_MAX =
      *std::max_element(monkeyItemCount.begin(), monkeyItemCount.end());
  monkeyItemCount.erase(
      std::remove(monkeyItemCount.begin(), monkeyItemCount.end(), FIRST_MAX),
      monkeyItemCount.end());
  const auto SECOND_MAX =
      *std::max_element(monkeyItemCount.begin(), monkeyItemCount.end());
  return FIRST_MAX * SECOND_MAX;
}

int64_t frequentMonkeys2(vector<Rule>& monkeys) {
  constexpr int64_t MOD = 11 * 7 * 3 * 5 * 17 * 13 * 19 * 2;
  vector<int64_t> monkeyItemCount(monkeys.size(), 0);
  for (int i = 0; i < 10000; i++) {
    for (int j = 0; j < monkeys.size(); j++) {
      monkeyItemCount[j] += monkeys[j].items.size();
      auto& monkey = monkeys[j];
      for (const auto ITEM : monkey.items) {
        int64_t item1 = ITEM;
        if (monkey.operation == "*") {
          item1 *= monkey.operand.value();
        } else if (monkey.operation == "+") {
          item1 += monkey.operand.value();
        } else if (monkey.operation == "^2") {
          item1 *= item1;
        }
        item1 %= MOD;
        if (item1 % monkey.test == 0) {
          monkeys[monkey.true_target].items.push_back(item1);
        } else {
          monkeys[monkey.false_target].items.push_back(item1);
        }
      }
      monkeys[j].items.clear();
    }
  }
  const auto FIRST_MAX =
      *std::max_element(monkeyItemCount.begin(), monkeyItemCount.end());
  monkeyItemCount.erase(
      std::remove(monkeyItemCount.begin(), monkeyItemCount.end(), FIRST_MAX),
      monkeyItemCount.end());
  const auto SECOND_MAX =
      *std::max_element(monkeyItemCount.begin(), monkeyItemCount.end());
  return FIRST_MAX * SECOND_MAX;
}

void solve11() {
  cout << "Day 11 solutions" << endl;
  vector<Rule> monkeysCopy1 = REAL_MONKEYS;
  cout << "Part A: " << frequentMonkeys(monkeysCopy1) << endl;
  vector<Rule> monkeysCopy2 = REAL_MONKEYS;
  cout << "Part B: " << frequentMonkeys2(monkeysCopy2) << endl;
}
