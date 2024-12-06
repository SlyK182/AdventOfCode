from collections import defaultdict

from ..utils.common import load_input, timer

RULES = []
UPDATES = []
curr = RULES
for row in load_input(5):
    if not row:
        curr = UPDATES
    else:
        curr.append(row)

UPDATES = list(map(lambda u: list(map(int, u.split(","))), UPDATES))

RULES_MAP = defaultdict(set)
for rule in RULES:
    pre, post = map(int, rule.split("|"))
    RULES_MAP[pre].add(post)


def _is_page_valid(idx, page, update):
    return idx == 0 or not RULES_MAP[page].intersection(update[:idx])


def _is_update_valid(update):
    return all(_is_page_valid(idx, page, update) for idx, page in enumerate(update))


def _fix_update(update):
    fixed_update = []
    for idx, page in enumerate(update):
        if _is_page_valid(idx, page, fixed_update):
            fixed_update.append(page)
        else:
            intersection = RULES_MAP[page].intersection(fixed_update[:idx])
            if new_index := min(fixed_update.index(i) for i in intersection):
                fixed_update.insert(new_index, page)
            else:
                fixed_update = [page] + fixed_update
    return fixed_update if _is_update_valid(fixed_update) else _fix_update(fixed_update)


@timer
def problem1_solution():
    valid_updates = []
    for update in UPDATES:
        if _is_update_valid(update):
            valid_updates.append(update)
    return sum(u[int(len(u) / 2)] for u in valid_updates)


@timer
def problem2_solution():
    fixed_updates = []
    for update in sorted(UPDATES, key=lambda u: len(u)):
        if not _is_update_valid(update):
            fixed_updates.append(_fix_update(update))
    return sum(u[int(len(u) / 2)] for u in fixed_updates)


def main():
    print(f"** Solution to problem 1: {problem1_solution()} **")
    print(f"** Solution to problem 2: {problem2_solution()} **")


if __name__ == "__main__":
    main()
