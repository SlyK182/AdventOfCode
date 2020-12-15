# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/2

from collections import Counter

from AdventOfCode.common import load_input, timer


def get_params(line):
    n, l, p = line.strip().split(' ')
    n0, n1 = tuple(map(int, n.split('-')))
    return n0, n1, l[0], p


@timer
def problem1_solution():
    count = 0
    for n1, n2, char, pword in tuple(map(get_params, load_input(2, 1))):
        if n1 <= Counter(pword).get(char, 0) <= n2:
            count += 1
    return count or "Solution not found."


@timer
def problem2_solution():
    count = 0
    for i1, i2, char, pword in tuple(map(get_params, load_input(2, 2))):
        char = char[0]
        if (char == pword[i1 - 1]) != (char == pword[i2 - 1]):
            count += 1
    return count or "Solution not found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
