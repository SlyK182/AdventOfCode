# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/13

from AdventOfCode.common import load_input, timer


@timer
def problem1_solution():
    data = load_input(13, 1)
    ts = int(data[0])
    bus_ids = [int(i) for i in data[1].strip().split(',') if i != 'x']
    earliest_bus_id = 0
    min_wait_time = min(bus_ids)
    for bus_id in bus_ids:
        wait_time = bus_id - divmod(ts, bus_id)[1]
        if wait_time <= min_wait_time:
            min_wait_time = wait_time
            earliest_bus_id = bus_id
    return earliest_bus_id * min_wait_time


@timer
def problem2_solution():
    data = load_input(13, 2)
    bus_ids = [int(i) if i != 'x' else i for i in data[1].strip().split(',')]
    bus_ids_delta = []  # List of tuples made as (Bus ID, offset)
    for n, bus_id in tuple(filter(lambda i: i[1] != 'x', enumerate(bus_ids))):
        if n == 0:
            bus_ids_delta.append((bus_id, 0))
        else:
            bus_ids_delta.append((bus_id, bus_id - (n % bus_id)))
    # Going to use the LCM: sort the deltas so that we start right away with
    # big numbers, instead of cycling through small ones
    bus_ids_delta.sort(key=lambda i: i[1], reverse=True)
    lcm = 1
    ts = bus_ids_delta[0][1]
    for n, delta in enumerate(bus_ids_delta[:-1]):
        lcm *= delta[0]
        while ts % bus_ids_delta[n+1][0] != bus_ids_delta[n+1][1]:
            ts += lcm
    return ts


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
