# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/5

from AdventOfCode.input_loader import load_input


def binary_to_decimal(b):
    return sum(2 ** i * int(c) for i, c in enumerate(reversed(b)))


def compute_seat(ticket):
    row = binary_to_decimal(ticket[:7].replace('F', '0').replace('B', '1'))
    col = binary_to_decimal(ticket[7:].replace('L', '0').replace('R', '1'))
    return row, col


def compute_seat_id(ticket):
    row, column = compute_seat(ticket)
    return int(row * 8 + column)


def problem1_solution():
    return max([compute_seat_id(t.strip()) for t in load_input(5, 1)])


def problem2_solution():
    seat_ids = [compute_seat_id(t.strip()) for t in load_input(5, 2)]
    seat_ids.sort()
    for x in range(len(seat_ids) - 1):
        if seat_ids[x + 1] - seat_ids[x] == 2:
            return seat_ids[x] + 1
    return "No solution found"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
