from ..utils.common import load_input, timer


def _is_safe(levels, retry: bool = False):
    positive_sign, negative_sign, diffs = False, False, []
    for idx in range(len(levels) - 1):
        diff = levels[idx + 1] - levels[idx]
        if diff > 0:
            positive_sign = True
        elif diff < 0:
            negative_sign = True
        diffs.append(diff)
    if positive_sign != negative_sign and all(0 < abs(d) <= 3 for d in diffs):
        return True
    elif retry:
        return any(_is_safe(levels[:i] + levels[i + 1:], False) for i in range(len(levels)))
    return False


REPORTS = tuple(map(lambda r: tuple(map(int, r.split())), load_input(2)))
REPORTS_SAFETY = {r: (_is_safe(r), _is_safe(r, retry=True)) for r in REPORTS}


@timer
def problem1_solution():
    return sum(v[0] for v in REPORTS_SAFETY.values())


@timer
def problem2_solution():
    return sum(v[1] for v in REPORTS_SAFETY.values())


def main():
    print(f"** Solution to problem 1: {problem1_solution()} **")
    print(f"** Solution to problem 2: {problem2_solution()} **")


if __name__ == "__main__":
    main()
