# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/1

from itertools import combinations

from AdventOfCode.input_loader import load_input


def problem1_solution():
    data = tuple(map(int, load_input(1, 1)))
    for num1 in data:
        num2 = 2020 - num1
        if num2 in data:
            return num1 * num2
    return "Solution not found."


def problem2_solution():
    data = tuple(map(int, load_input(1, 2)))
    for num1, num2 in combinations(data, 2):
        num3 = 2020 - num1 - num2
        if num3 in data:
            return num1 * num2 * num3
    return "Solution not found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
