# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/19

from itertools import product

from AdventOfCode.common import load_input, timer


def dictify_rules(rules):
    rules_dict = {}
    for rule in rules:
        num, vals = rule.split(': ')
        num = int(num)
        if "\"" not in vals:
            rules_dict[num] = [
                tuple(map(int, val.split(' ')))
                for val in vals.split(' | ')
            ]
        else:
            rules_dict[num] = eval(vals.strip())
    return rules_dict


def get_valid_msgs(rules, done=None, num=0):
    done = dict(done or [])
    if num in done:
        return done[num]
    vals = rules[num]
    if isinstance(vals, str):
        done[num] = vals
        return vals
    valid_msgs = []
    for v in vals:
        valid_msgs += [
            ''.join(c) for c in product(
                *[get_valid_msgs(rules, done, i) for i in v]
            )
        ]
    done[num] = valid_msgs
    return valid_msgs


@timer
def problem1_solution():
    data = load_input(19, 1)
    rules = dictify_rules(data[:data.index('\n')])
    valid_msgs = set(get_valid_msgs(rules))
    msgs = [m.strip() for m in data[data.index('\n') + 1:]]
    return len(valid_msgs.intersection(msgs))


@timer
def problem2_solution():
    return "No solution found"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
