# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/10

from collections import Counter

from AdventOfCode.input_loader import load_input


def get_arrangements(jolts):
    jolts.extend([0, max(jolts) + 3])
    jolts.sort(reverse=True)
    counter = {max(jolts): 1}
    for j in jolts[1:]:
        counter[j] = 0
        for k in (1, 2, 3):
            counter[j] += counter.get(j + k, 0)
    return counter[0]


def get_jumps(jolts):
    jolts.extend([0, max(jolts) + 3])
    jolts.sort()
    return Counter([jolts[x+1] - jolts[x] for x in range(len(jolts) - 1)])


def problem1_solution():
    jumps = get_jumps(list(map(int, load_input(10, 1))))
    return jumps[1] * jumps[3] or "Solution not found"


def problem2_solution():
    return get_arrangements(list(map(int, load_input(10, 2)))) \
        or "Solution not found"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
