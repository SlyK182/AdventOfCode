# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/17

from itertools import product

from AdventOfCode.common import load_input, timer


def evolve(grid, dim):
    coords = range(len(dim))

    # Add new borders if any of the positions of the current borders has an
    # active state
    minmax = [(min(dim[i]), max(dim[i])) for i in coords]
    if any(
        a
        for pos, a in grid.items()
        if any(pos[i] in minmax[i] for i in coords)
    ):
        for pos in product(
            *[range(minmax[c][0] - 1, minmax[c][1] + 2) for c in coords]
        ):
            if pos not in grid:
                grid[tuple(pos)] = 0
            for c in coords:
                dim[c].add(pos[c])

    # Compute new values
    new_vals = {}
    deltas = sorted(product(*[(-1, 0, 1)] * len(dim)))
    for pos, active in sorted(grid.items()):
        active_nearby = 0
        for delta in deltas:
            if not any(delta):
                continue
            nearby = tuple([pos[c] + delta[c] for c in coords])
            active_nearby += grid.get(nearby, 0)
        if active and active_nearby not in (2, 3):
            new_vals[pos] = 0
        elif not active and active_nearby == 3:
            new_vals[pos] = 1

    grid.update(new_vals)


def make_grid(data, dim):
    grid = {}
    for y, row in enumerate(data, start=1):
        dim[1].add(y)
        for x, val in enumerate(row.strip(), start=1):
            dim[0].add(x)
            grid[tuple([x, y] + [0] * (len(dim) - 2))] = 1 if val == '#' else 0
    for d in dim[2:]:
        d.add(0)
    return grid


@timer
def problem1_solution():
    dim3 = [set(), set(), set()]
    grid = make_grid(load_input(17, 1), dim3)
    for _ in range(6):
        evolve(grid, dim3)
    return sum(grid.values())


@timer
def problem2_solution():
    dim4 = [set(), set(), set(), set()]
    grid = make_grid(load_input(17, 2), dim4)
    for _ in range(6):
        evolve(grid, dim4)
    return sum(grid.values())


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
