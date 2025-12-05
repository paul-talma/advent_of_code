import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils import utils

INPUT = utils.read_input_lines_as_lists('input.txt')
X, Y = len(INPUT), len(INPUT[0])


def inbounds(x, y):
    return 0 <= x < X and 0 <= y < Y


def check(i, j):
    adjacent = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if inbounds(i + x, j + y) and INPUT[i + x][j + y] == '@':
                adjacent += 1

    return adjacent < 5


def part1():
    count = 0
    for i in range(X):
        for j in range(Y):
            if INPUT[i][j] == '@':
                count += check(i, j)
    print(count)


def sweep():
    count = 0
    for i in range(X):
        for j in range(Y):
            if INPUT[i][j] == '@':
                if check(i, j):
                    count += 1
                    INPUT[i][j] = '.'
    return count


def part2():
    removed = 0
    while True:
        count = sweep()
        removed += count
        if count == 0:
            print(removed)
            return


part2()
