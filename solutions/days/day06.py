from ..utils.common import load_input, timer
from collections import OrderedDict

MAP = list(list(x) for x in load_input(6))
POS = [(row, col) for row in range(len(MAP)) for col in range(len(MAP[row])) if MAP[row][col] == "^"][0]
DIRECTION = (-1, 0)


def _traverse(pos: tuple[int, int], direction: tuple[int, int], map_: list[list[str]]):
    route = OrderedDict()
    while True:
        if (pos, direction) in route:
            return route, True  # Loop found
        route[(pos, direction)] = None
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        try:
            if map_[new_pos[0]][new_pos[1]] == "#":
                direction = (direction[1], - direction[0])
            else:
                pos = new_pos
        except IndexError:
            return route, False  # Exit found


@timer
def problem1_solution():
    return len(set(x[0] for x in _traverse(tuple(POS), tuple(DIRECTION), list(MAP))[0]))


@timer
def problem2_solution():
    loops = 0
    map_ = [list(x) for x in MAP]
    for r, c in [(row, col) for row in range(len(MAP)) for col in range(len(MAP[row]))]:
        if map_[r][c] == ".":
            map_[r][c] = "#"
            if _traverse(tuple(POS), tuple(DIRECTION), map_)[1]:
                loops += 1
            map_[r][c] = "."
    return loops


def main():
    print(f"** Solution to problem 1: {problem1_solution()} **")
    print(f"** Solution to problem 2: {problem2_solution()} **")


if __name__ == "__main__":
    main()
