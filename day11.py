# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/11

from itertools import product

from AdventOfCode.input_loader import load_input


def evolve_map(old, mode):
    new = {}
    for (row, col), seat in old.items():
        new_seat = seat.copy()
        occ = get_occupied_seats(old, row, col, mode)
        if seat['type'] == 'L' and not occ:
            new_seat['type'] = '#'
        elif seat['type'] == '#' and occ >= (4 if mode == 'adjacent' else 5):
            new_seat['type'] = 'L'
        new[(row, col)] = new_seat
    return new


def get_seat_map(seat_map_input):
    return {
        (r, c): {'type': seat_type, 'near': []}
        for r, seat_str in enumerate(seat_map_input, start=1)
        for c, seat_type in enumerate(seat_str.strip(), start=1)
    }


def get_occupied_seats(seat_map, row, col, mode):
    occupied = 0
    if mode == 'adjacent':
        occupied = len([
            (row + dr, col + dc)
            for dr, dc in product((-1, 0, 1), (-1, 0, 1))
            if not dr == dc == 0
            if (row + dr, col + dc) in seat_map
            if seat_map[(row + dr, col + dc)]['type'] == '#'
        ])
    elif mode == 'first_seen':
        for dr, dc in product((-1, 0, 1), (-1, 0, 1)):
            if dr == dc == 0:
                continue
            k = 1
            while True:
                drk, dck = k * dr + row, k * dc + col
                if (drk, dck) not in seat_map:
                    break
                elif seat_map[(drk, dck)]['type'] == 'L':
                    break
                elif seat_map[(drk, dck)]['type'] == '#':
                    occupied += 1
                    break
                k += 1
    return occupied


def problem1_solution():
    old_map = {}
    new_map = get_seat_map(load_input(11, 1))
    while old_map != new_map:
        old_map, new_map = new_map, evolve_map(new_map, 'adjacent')
    return len([s for s in new_map.values() if s['type'] == '#'])


def problem2_solution():
    old_map = {}
    new_map = get_seat_map(load_input(11, 2))
    while old_map != new_map:
        old_map, new_map = new_map, evolve_map(new_map, 'first_seen')
    return len([s for s in new_map.values() if s['type'] == '#'])


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
