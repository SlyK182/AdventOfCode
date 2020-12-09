# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/9

from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)
P1_SOL = 0


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day09_1.txt'), 'r') as input1:
        data = tuple(map(int, input1.readlines()))
    for x in range(25, len(data) + 1):
        curr_num = data[x]
        previous_nums = data[x - 25:x]
        if not any(abs(curr_num - p) in previous_nums for p in previous_nums):
            # Problem 2 requires to find a series of consecutive numbers that
            # add up to Problem 1 solution, so we'll put the solution here
            # without having to compute it again later
            global P1_SOL
            P1_SOL = curr_num
            return curr_num
    return "Solution not found"


def problem2_solution():
    with open(path.join(CURDIR, 'inputs', f'day09_2.txt'), 'r') as input2:
        data = tuple(map(int, input2.readlines()))
    for y in range(2, len(data) + 1):
        for x in range(y, len(data) + 1):
            if sum(data[x - y:x]) == P1_SOL:
                return min(data[x - y:x]) + max(data[x - y:x])
    return "Solution not found"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
