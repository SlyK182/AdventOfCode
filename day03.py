# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2019/day/1

from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)
OPEN = '.'
TREE = '#'


def tree_counter(data, **deltas):
    count, x, y = 0, 0, 0
    while y in data:
        if x >= len(data[y]):
            x = x % len(data[y])
        if data[y][x] == TREE:
            count += 1
        x += deltas['x']
        y += deltas['y']
    return count


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day03_1.txt'), 'r') as input1:
        data = dict(enumerate(map(lambda l: l.strip(), input1.readlines())))
    return tree_counter(data, x=3, y=1) or "Solution not found."


def problem2_solution():
    res = 1
    with open(path.join(CURDIR, 'inputs', f'day03_2.txt'), 'r') as input2:
        data = dict(enumerate(map(lambda l: l.strip(), input2.readlines())))
        for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
            res *= tree_counter(data, x=x, y=y)
    return res or "Solution not found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
