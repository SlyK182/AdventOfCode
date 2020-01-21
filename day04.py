# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2019/day/4

import operator

from collections import Counter


MIN = 372037
MAX = 905157


def check_non_decreasing(coeffs):
    min_c = 0
    for c in coeffs:
        if c >= min_c:
            min_c = c
        else:
            raise ValueError


def check_count(coeffs, operator, benchmark):
    counter = dict(Counter(coeffs))
    if not any(operator(v, benchmark) for v in counter.values()):
        raise ValueError


def get_valid_passwords(constrains):
    valid_pws = []
    for x in range(MIN, MAX + 1):
        coeffs = to_coeffs(x)
        try:
            for const in constrains:
                const(coeffs)
            valid_pws.append(coeffs)
        except ValueError:
            pass
    return valid_pws


def to_coeffs(value):
    if value <= 0:
        raise ValueError
    coeffs = []
    for x in list(reversed(range(6))):
        c, value = divmod(value, 10 ** x)
        coeffs.append(c)
    return coeffs


def problem1_solution():
    return len(
        get_valid_passwords(
            [lambda c: check_non_decreasing(c),
             lambda c: check_count(c, operator.gt, 1)]
        )
    )


def problem2_solution():
    return len(
        get_valid_passwords(
            [lambda c: check_non_decreasing(c),
             lambda c: check_count(c, operator.eq, 2)]
        )
    )


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))

