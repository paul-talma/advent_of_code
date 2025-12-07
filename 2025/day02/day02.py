# simple regex using groups
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils import utils

INPUT = utils.read_input_sequence('input.txt')

pattern = r'(\d+)\1+'


def match(id):
    str_id = str(id)
    return re.fullmatch(pattern, str_id)


def part1():
    total = 0
    for r in INPUT:
        lower, upper = r.split('-')
        for id in range(int(lower), int(upper) + 1):
            if match(id):
                total += id

    print(f'Total: {total}')


part1()
