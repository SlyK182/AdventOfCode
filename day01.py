# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/1

from itertools import combinations
from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day01_1.txt'), 'r') as input1:
        data = tuple(map(lambda x: int(x.strip()), input1.readlines()))
        for num1 in data:
            num2 = 2020 - num1
            if num2 in data:
                return num1 * num2
    return "Solution not found."


def problem2_solution():
    with open(path.join(CURDIR, 'inputs', f'day01_2.txt'), 'r') as input2:
        data = tuple(map(lambda x: int(x.strip()), input2.readlines()))
        for num1, num2 in combinations(data, 2):
            num3 = 2020 - num1 - num2
            if num3 in data:
                return num1 * num2 * num3
    return "Solution not found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
