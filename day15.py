# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/15

from AdventOfCode.input_loader import load_input


def memory(nums, end):
    n2p = {n: p for p, n in enumerate(nums, start=1)}
    turn = len(nums) + 1
    spkn = 0
    while turn < end:
        n2p[spkn], spkn = turn, 0 if spkn not in n2p else turn - n2p[spkn]
        turn += 1
    return spkn


def problem1_solution():
    return memory(list(map(int, load_input(15, 1)[0].split(','))), 2020)


def problem2_solution():
    return memory(list(map(int, load_input(15, 2)[0].split(','))), 30000000)


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
