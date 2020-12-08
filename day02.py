# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2019/day/1

from collections import Counter
from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)


def get_params(line):
    n, l, p = line.strip().split(' ')
    n0, n1 = tuple(map(int, n.split('-')))
    return n0, n1, l[0], p


def problem1_solution():
    count = 0
    with open(path.join(CURDIR, 'inputs', f'day02_1.txt'), 'r') as input1:
        for n1, n2, char, pword in tuple(map(get_params, input1.readlines())):
            if n1 <= Counter(pword).get(char, 0) <= n2:
                count += 1
    return count or "Solution not found."


def problem2_solution():
    count = 0
    with open(path.join(CURDIR, 'inputs', f'day02_2.txt'), 'r') as input2:
        for i1, i2, char, pword in tuple(map(get_params, input2.readlines())):
            char = char[0]
            if (char == pword[i1 - 1]) != (char == pword[i2 - 1]):
                count += 1
    return count or "Solution not found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
