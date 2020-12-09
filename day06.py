# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/6

from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)


def answer_count(groups, mode):
    if mode == 'any':
        return sum(len(set(''.join(answers))) for answers in groups)
    elif mode == 'all':
        count = 0
        for answers in groups:
            if len(answers) == 1:
                count += len(answers[0])
                continue
            sorted_answers = sorted(answers, key=lambda a: len(a))
            for char in sorted_answers[0]:
                if all(char in a for a in sorted_answers[1:]):
                    count += 1
        return count
    raise ValueError(f"Invalid mode '{mode}'")


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day06_1.txt'), 'r') as input1:
        gs = tuple(map(lambda x: x.split('\n'), input1.read().split('\n\n')))
    return answer_count(gs, 'any')


def problem2_solution():
    with open(path.join(CURDIR, 'inputs', f'day06_2.txt'), 'r') as input2:
        gs = tuple(map(lambda x: x.split('\n'), input2.read().split('\n\n')))
    return answer_count(gs, 'all')


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
