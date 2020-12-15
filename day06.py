# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/6

from AdventOfCode.common import load_input, timer


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


@timer
def problem1_solution():
    gs = tuple(g.split('\n') for g in ''.join(load_input(6, 1)).split('\n\n'))
    return answer_count(gs, 'any')


@timer
def problem2_solution():
    gs = tuple(g.split('\n') for g in ''.join(load_input(6, 2)).split('\n\n'))
    return answer_count(gs, 'all')


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
