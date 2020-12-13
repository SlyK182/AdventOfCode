# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/12

from AdventOfCode.input_loader import load_input


def run_ship(commands):
    x, y = 0, 0
    directions = [      # Ordered counterclockwise:
        ( 1,  0),       # East
        ( 0,  1),       # North
        (-1,  0),       # West
        ( 0, -1),       # South
    ]
    direction = directions[0]
    for command in commands:
        act = command[0]
        value = int(command[1:])
        if act == 'N':
            y += value
        elif act == 'S':
            y -= value
        elif act == 'E':
            x += value
        elif act == 'W':
            x -= value
        elif act in ('L', 'R'):
            angle = value if act == 'L' else - value
            new_dir_index = (directions.index(direction) + angle // 90) % 4
            direction = directions[new_dir_index]
        elif act == 'F':
            x += direction[0] * value
            y += direction[1] * value
    return x, y


def run_with_waypoint(commands):
    x, y = 0, 0
    wpx, wpy = 10, 1
    for command in commands:
        act = command[0]
        value = int(command[1:])
        if act == 'N':
            wpy += value
        elif act == 'S':
            wpy -= value
        elif act == 'E':
            wpx += value
        elif act == 'W':
            wpx -= value
        elif act in ('L', 'R'):
            angle = value if act == 'L' else - value
            # This code below should be rewritten by using appropriate
            # trigonometric functions; however, those would result in floating
            # point errors most of the time, and since every angle in the input
            # file is either ±90, ±180 or ±270, I'll simply switch manually the
            # coordinates according to the angle value
            if angle in (90, -270):
                wpx, wpy = -wpy, wpx
            elif angle in (180, -180):
                wpx, wpy = -wpx, -wpy
            elif angle in (270, -90):
                wpx, wpy = wpy, -wpx
        elif act == 'F':
            x += wpx * value
            y += wpy * value
    return x, y


def problem1_solution():
    x, y = run_ship(list(map(lambda x: x.strip(), load_input(12, 1))))
    return abs(x) + abs(y)


def problem2_solution():
    x, y = run_with_waypoint(list(map(lambda x: x.strip(), load_input(12, 2))))
    return abs(x) + abs(y)


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
