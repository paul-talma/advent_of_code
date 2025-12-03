import inspect
from pathlib import Path


def read_input_lines(path='input.txt'):
    caller_path = Path(inspect.stack()[1].filename).parent
    filepath = caller_path / path
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def read_input_sequence(path='input.txt'):
    caller_path = Path(inspect.stack()[1].filename).parent
    filepath = caller_path / path
    with open(filepath, 'r') as f:
        lines = f.read().split(',')
    return lines


def vec_add(v1, v2):
    return (v1[0] + v2[0]), (v1[1] + v2[1])
