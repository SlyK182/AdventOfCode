import re

from ..utils.common import load_input, timer

DATA = "".join(load_input(3))


@timer
def problem1_solution():
    return sum(
        eval(v, {}, {'mul': int.__mul__})
        for v in re.findall(r"mul\(\d{1,3},\d{1,3}\)", DATA)
    )


@timer
def problem2_solution():
    to_sum = ""
    to_check = str(DATA)
    while to_check:
        if to_check.startswith("don't()"):
            if (do_idx := to_check.find("do()")) != -1:
                to_check = to_check[do_idx:]
            else:
                to_check = ""
        else:
            if (dont_idx := to_check.find("don't()")) == -1:
                to_sum += to_check
                to_check = ""
            else:
                to_sum += to_check[:dont_idx]
                to_check = to_check[dont_idx:]
    return sum(
        eval(v, {}, {'mul': int.__mul__})
        for v in re.findall(r"mul\(\d{1,3},\d{1,3}\)", to_sum)
    )


def main():
    print(f"** Solution to problem 1: {problem1_solution()} **")
    print(f"** Solution to problem 2: {problem2_solution()} **")


if __name__ == "__main__":
    main()
