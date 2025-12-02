#include "aoc17-utils.h"
#include <cmath>
#include <iostream>
#include <regex>
#include <string>

void parseInput(const std::string &path, Program &program,
                Registers &registers) {
  std::ifstream file(path);
  if (!file.is_open()) {
    throw std::runtime_error("Error: file not found " + path);
  }
  std::string line;
  while (std::getline(file, line)) {
    if (line[0] == 'R') {
      int reg = getNum(line);
      registers.push_back(reg);
    } else if (line[0] == 'P') {
      getProgram(line, program);
    }
  }
}

int getNum(std::string &line) {
  std::regex pattern(R"(\d+)");
  std::smatch match;
  std::regex_search(line, match, pattern);
  return std::stoi(match[0]);
}

void getProgram(std::string &line, Program &program) {
  std::regex pattern(R"((\d+),(\d+))");
  std::smatch match;
  std::sregex_iterator iter(line.begin(), line.end(), pattern);
  std::sregex_iterator end;
  std::string::const_iterator searchStart(line.cbegin());

  while (iter != end) {
    for (unsigned i = 1; i < iter->size(); i += 2) {
      Name name = static_cast<Name>(std::stoi((*iter)[i]));
      int operand = std::stoi((*iter)[i + 1]);
      Instruction inst = Instruction(name, operand);
      program.push_back(inst);
    }
    ++iter;
  }
}

int matchToInt(std::smatch &match, int index) {
  return std::stoi(match[index].str());
}

int combo(int val, Registers &registers) {
  switch (val) {
  case 4:
    return registers[a];
  case 5:
    return registers[b];
  case 6:
    return registers[c];
  default:
    return val;
  }
}

void write(int res, Registers &registers, Register reg) {
  registers[reg] = res;
}

void jump(int val, InstructionPointer &IP) { IP = val; }

void execute(const Instruction &inst, Registers &registers,
             InstructionPointer &IP, Output &output) {
  Name name = inst.name;
  int operand;
  int res;
  switch (name) {
  case adv: {
    operand = combo(inst.operand, registers);
    int num = registers[a];
    int div = pow(2, operand);
    res = num / div;
    write(res, registers, a);
    IP++;
    break;
  }

  case bxl: {
    operand = inst.operand;
    int reg = registers[b];
    res = operand ^ reg;
    write(res, registers, b);
    IP++;
    break;
  }

  case bst: {
    operand = combo(inst.operand, registers);
    operand %= 8;
    write(operand, registers, b);
    IP++;
    break;
  }

  case jnz: {
    if (registers[a] == 0) {
      IP++;
      break;
    }
    jump(inst.operand, IP);
    break;
  }

  case bxc: {
    res = registers[b] ^ registers[c];
    write(res, registers, b);
    IP++;
    break;
  }

  case out: {
    operand = combo(inst.operand, registers);
    operand %= 8;
    output.push_back(operand);
    IP++;
    break;
  }

  case bdv: {
    operand = combo(inst.operand, registers);
    int num = registers[a];
    int div = pow(2, operand);
    res = num / div;
    write(res, registers, b);
    IP++;
    break;
  }

  case cdv: {
    operand = combo(inst.operand, registers);
    int num = registers[a];
    int div = pow(2, operand);
    res = num / div;
    write(res, registers, c);
    IP++;
    break;
  }
  }
}

void runProgram(const Program &prog, Registers &registers, Output &output) {
  InstructionPointer IP = 0;
  int programLength = prog.size();
  while (IP < programLength) {
    Instruction inst = prog[IP];
    execute(inst, registers, IP, output);
  }
}

std::string formatOutput(Output &output) {
  std::string out;
  for (int x : output) {
    out += std::to_string(x);
    out.push_back(',');
  }
  out.pop_back();
  return out;
}

std::string progToString(const Program &prog) {
  std::string res;
  for (Instruction inst : prog) {
    res += std::to_string(inst.name) + std::to_string(inst.operand);
  }
  return res;
}

std::string outputToString(const Output &out) {
  std::string res;
  for (int i : out) {
    res += std::to_string(i);
  }
  return res;
}

int findQuine(const Program &program, Registers &registers) {
  std::string programString = progToString(program);
  int regA = 0;
  while (true) {
    if (regA % 1000000 == 0) {
      std::cout << regA << '\n';
    }
    registers[a] = regA;
    Output out;
    runProgram(program, registers, out);
    std::string outputString = outputToString(out);
    if (outputString == programString) {
      return regA;
    }
    regA++;
  }
}
