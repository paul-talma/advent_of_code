import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils import utils

INPUT = utils.read_input_lines('input.txt')
INPUT = [(line[0], int(line[1:])) for line in INPUT]


def part1():
    INITIAL = 50
    MAX = 100
    SIGN_DICT = {'R': 1, 'L': -1}
    val = INITIAL
    counter = 0
    for instruction in INPUT:
        dir = instruction[0]
        sign = SIGN_DICT[dir]
        val += sign * instruction[1]
        val = val % MAX
        if val == 0:
            counter += 1
    print(f'The code is: {counter}')


def part2():
    INITIAL = 50
    MAX = 100
    SIGN_DICT = {'R': 1, 'L': -1}
    val = INITIAL
    counter = 0
    # __import__('ipdb').set_trace()
    for instruction in INPUT:
        dir = instruction[0]
        sign = SIGN_DICT[dir]
        displacement = instruction[1]
        if dir == 'L':
            val = (MAX - val) % MAX
        val += displacement
        turns, val = divmod(val, MAX)
        turns = abs(turns)
        if turns == 0:
            counter += val == 0
        else:
            counter += turns
        if dir == 'L':
            val = (MAX - val) % MAX
    print(f'The code is: {counter}')


part2()
