# part 1 is in O(n) (unlike naive O(n^2) approach)
# part 2 is in O(n) (unlike O(factorial) naive recursive approach)
# thanks to dynamic programming and fixed subsequence length.
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils import utils

INPUT = utils.read_input_lines('input.txt')
INPUT = [[int(i) for i in list(line)] for line in INPUT]
L = 12


def find_largest_subdigits(digits) -> int:
    best_l = digits[0]
    best_r = digits[1]

    for i in range(1, len(digits) - 1):
        l = digits[i]
        r = digits[i + 1]
        if l > best_l:
            best_l = l
            best_r = r
        elif r > best_r:
            best_r = r
    return best_l * 10 + best_r


def part1():
    print(sum([find_largest_subdigits(row) for row in INPUT]))


def get_max_subsequence(row) -> int:
    cache = {}
    for i in range(1, len(row) + 1):
        for j in range(1, min(L, i) + 1):
            v1 = cache.get((i - 1, j), 0)
            v2 = 10 * cache.get((i - 1, j - 1), 0) + row[i - 1]
            cache[(i, j)] = max(v1, v2)

    return cache[(len(row), L)]


def part2():
    print(sum([get_max_subsequence(row) for row in INPUT]))


part2()
