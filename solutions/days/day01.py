from collections import Counter

from ..utils.common import load_input, timer


LVALUES, RVALUES = [], []
for row in load_input(1):
    for lst, vl in zip((LVALUES, RVALUES), map(int, row.strip().split())):
        lst.append(vl)


@timer
def problem1_solution():
    return sum(abs(lv - rv) for lv, rv in zip(*map(sorted, (LVALUES, RVALUES))))


@timer
def problem2_solution():
    right_values_counter = Counter(RVALUES)
    return sum(lv * right_values_counter[lv] for lv in LVALUES)


def main():
    print(f"** Solution to problem 1: {problem1_solution()} **")
    print(f"** Solution to problem 2: {problem2_solution()} **")


if __name__ == "__main__":
    main()
