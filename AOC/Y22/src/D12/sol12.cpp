//
// Copyright
//

#include "D12/sol12.h"

#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include "utils/utils.h"

using std::cout;
using std::endl;
using std::map;
using std::pair;
using std::queue;
using std::string;
using std::tuple;
using std::vector;

struct GraphData {
  map<tuple<int, int>, vector<tuple<int, int>>> adj;
  tuple<int, int> start;
  tuple<int, int> end;
};

GraphData createAdjList(vector<string>& lines, bool version1 = false) {
  map<tuple<int, int>, vector<tuple<int, int>>> adj;
  tuple<int, int> start;
  tuple<int, int> end;

  const int N = lines.size();
  const int M = lines[0].size();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (lines[i][j] == 'S') {
        start = {i, j};
        lines[i][j] = 'a';
      } else if (lines[i][j] == 'E') {
        end = {i, j};
        lines[i][j] = 'z';
      }
    }
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      const char CURRENT = lines[i][j];
      vector<pair<int, int>> directions = {
          {-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down, left, right
      for (auto [di, dj] : directions) {
        int ni = i + di;

        if (int nj = j + dj; ni >= 0 && ni < N && nj >= 0 && nj < M) {
          // If letters are same, one less, or one more
          if (version1) {
            if (const char NEIGHBOR = lines[ni][nj]; NEIGHBOR <= CURRENT + 1) {
              adj[{i, j}].push_back({ni, nj});
            }
          } else {
            if (const char NEIGHBOR = lines[ni][nj]; NEIGHBOR >= CURRENT - 1) {
              adj[{i, j}].push_back({ni, nj});
            }
          }
        }
      }
    }
  }

  return {adj, start, end};
}

int shortestPath(vector<string>& lines) {
  GraphData g = createAdjList(lines, true);

  map<tuple<int, int>, bool> visited;
  queue<pair<tuple<int, int>, int>> q;  // (position, distance)

  q.push({g.start, 0});
  visited[g.start] = true;

  while (!q.empty()) {
    auto [current, dist] = q.front();
    q.pop();

    auto [ci, cj] = current;
    auto [ei, ej] = g.end;
    if (ci == ei && cj == ej) {
      return dist;
    }

    for (auto& neighbor : g.adj[current]) {
      if (!visited[neighbor]) {
        visited[neighbor] = true;
        q.push({neighbor, dist + 1});
      }
    }
  }

  return -1;  // no path found
}

int bestStarting(vector<string> lines) {
  GraphData g = createAdjList(lines);

  map<tuple<int, int>, bool> visited;
  queue<pair<tuple<int, int>, int>> q;  // (position, distance)

  q.push({g.end, 0});
  visited[g.end] = true;

  while (!q.empty()) {
    auto [current, dist] = q.front();
    q.pop();

    auto [ci, cj] = current;
    if (lines[ci][cj] == 'a') {
      return dist;
    }

    for (auto& neighbor : g.adj[current]) {
      if (!visited[neighbor]) {
        visited[neighbor] = true;
        q.push({neighbor, dist + 1});
      }
    }
  }

  return -1;  // no path found
}

void solve12() {
  cout << "Day 12 solutions:" << endl;
  vector<string> lines = readFile("D12/inp.txt");
  cout << "Part A: " << shortestPath(lines) << endl;
  vector<string> lines2 = readFile("D12/inp.txt");
  cout << "Part B: " << bestStarting(lines2) << endl;
}
