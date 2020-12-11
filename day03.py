# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/3

from AdventOfCode.input_loader import load_input

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
    data = dict(enumerate(map(lambda l: l.strip(), load_input(3, 1))))
    return tree_counter(data, x=3, y=1) or "Solution not found."


def problem2_solution():
    data = dict(enumerate(map(lambda l: l.strip(), load_input(3, 2))))
    res = 1
    for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res *= tree_counter(data, x=x, y=y)
    return res or "Solution not found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
