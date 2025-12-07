import itertools
import math

path = './2025/day06/input.txt'


def read_input_part_1(path):
    with open(path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        ops = lines[-1].split()
        nums = [[int(s) for s in l.split()] for l in lines[:-1]]
        nums = list(zip(*nums))
        return nums, ops


def part1():
    total = 0
    nums, ops = read_input_part_1(path)
    for n, o in zip(nums, ops):
        if o == '+':
            total += sum(n)
        else:
            total += math.prod(n)

    print(total)


def read_input_part_2(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        nums = list(itertools.zip_longest(*lines[:-1], fillvalue=' '))[:-1]
        nums.append((' ',))
        ops = lines[-1].strip().split()

    return nums, ops


def part2():
    nums, ops = read_input_part_2(path)
    total = 0
    op_id = 0
    accumulated = []
    for line in nums:
        joined = ''.join(line)
        if joined.strip():
            accumulated.append(int(joined))
        else:
            op = ops[op_id]
            if op == '+':
                total += sum(accumulated)
            else:
                total += math.prod(accumulated)
            op_id += 1
            accumulated = []

    print(total)


part2()
