# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/7

from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)
EMPTY = 'no other bags'
MY_COLOR = 'shiny gold'


def contains_color(cmap, container, color):
    # NB: if ``container`` is not in ``cmap``, the empty generator will be
    # evaluated as ``False``, which is what we want
    return cmap.get(container, {}).get(color) \
        or any(contains_color(cmap, k, color) for k in cmap.get(container, {}))


def count_inner_colors(cmap, color):
    return sum(
        v * (1 + count_inner_colors(cmap, c))
        for c, v in cmap.get(color, {}).items()
    )


def map_policies_to_colors(policies):
    color_map = {}
    for pol in policies:
        pol = pol.strip().replace('.', '')
        container, contained = pol.split('contain')
        color = normalize_color(container.replace('bags', ''))
        color_map[color] = {}
        if EMPTY in contained.strip():
            continue
        contained = contained.replace('bags', '').replace('bag', '')
        for qty_color in contained.split(','):
            qty, *contained_color = qty_color.strip().split(' ')
            contained_color = normalize_color(' '.join(contained_color))
            color_map[color][contained_color] = int(qty)
    return color_map


def normalize_color(color):
    return color.lower().strip()


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day07_1.txt'), 'r') as input1:
        policies = tuple(map(lambda x: x.strip(), input1.readlines()))
    cmap = map_policies_to_colors(policies)
    return len([c for c in cmap if contains_color(cmap, c, MY_COLOR)])


def problem2_solution():
    with open(path.join(CURDIR, 'inputs', f'day07_2.txt'), 'r') as input2:
        policies = tuple(map(lambda x: x.strip(), input2.readlines()))
    cmap = map_policies_to_colors(policies)
    return count_inner_colors(cmap, MY_COLOR)


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
