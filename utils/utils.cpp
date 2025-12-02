#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>

typedef std::vector<std::vector<char>> Grid;
Grid gridInput(std::string &path) {
  std::ifstream input(path);
  Grid grid;

  if (!input.is_open()) {
    throw std::runtime_error("Error: could not open file " + path);
  }
  std::string line;
  while (std::getline(input, line)) {
    std::vector<char> currLine;
    for (char ch : line) {
      currLine.push_back(ch);
    }
    grid.push_back(currLine);
  }

  return grid;
}
