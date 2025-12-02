#include "aoc17-utils.h"
#include <iostream>
#include <ostream>
#include <string>

void printPart(std::string &output, int part) {
  std::cout << "Phase " << part << ": " << output << '\n';
}

int main() {
  Registers registers;
  Program program1;
  Output output;
  std::string path = "input.txt";
  parseInput(path, program1, registers);
  runProgram(program1, registers, output);
  std::cout << "Phase 1: " << formatOutput(output) << std::endl;

  Program program2;
  path = "input.txt";
  parseInput(path, program2, registers);
  int res = findQuine(program2, registers);
  std::cout << "Phase 2: " << res << std::endl;
  return 0;
}
