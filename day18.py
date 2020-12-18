# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/18

from AdventOfCode.common import load_input, timer


def evaluate_expr(expr, mode='standard'):
    levels = {l: [] for l in range(expr.count('(') + 1)}
    level = 0
    for char in expr:
        if char == '(':
            level += 1
        elif char == ')':
            parenthesis_val = str(evaluate_pars(' '.join(levels[level]), mode))
            levels[level - 1].append(parenthesis_val)
            levels[level] = []
            level -= 1
        else:
            levels[level].append(char)
    return int(evaluate_pars(' '.join(levels[0]), mode))


def evaluate_pars(expr, mode='standard'):
    to_eval = expr
    if mode == 'standard':
        while '+' in to_eval or '*' in to_eval:
            n1, op, n2 = to_eval.split(' ')[:3]
            to_eval = str(eval(n1+op+n2)) + to_eval[len(' '.join([n1, op, n2])):]
        return to_eval
    elif mode == 'add_first':
        # Resolve every +, then fallback to normal evaluation
        while '+' in to_eval:
            op = '+'
            n1, n2 = '', ''
            i = to_eval.find(op) - 1
            j = to_eval.find(op) + 1
            while i >= 0:
                if to_eval[i].strip() and not to_eval[i].isdigit():
                    break
                else:
                    if to_eval[i].isdigit():
                        n1 = to_eval[i] + n1
                    i -= 1
            while j <= len(to_eval) - 1:
                if to_eval[j].strip() and not to_eval[j].isdigit():
                    break
                else:
                    if to_eval[j].isdigit():
                        n2 += to_eval[j]
                    j += 1
            replace = ' '.join([n1, op, n2])
            k = to_eval.find(replace)
            new_eval = ''
            if k > 0:
                new_eval += to_eval[0:k].strip()
            new_eval += f' {eval(replace)} '
            if k + len(replace) < len(to_eval):
                new_eval += to_eval[k + len(replace) + 1: len(to_eval)].strip()
            to_eval = new_eval.strip()
        return evaluate_pars(to_eval, 'standard')
    raise ValueError(f"Unknown mode: '{mode}'")


@timer
def problem1_solution():
    expressions = [''.join(e.split()) for e in load_input(18, 1)]
    return sum([evaluate_expr(e) for e in expressions])


@timer
def problem2_solution():
    expressions = [''.join(e.split()) for e in load_input(18, 2)]
    return sum([evaluate_expr(e, 'add_first') for e in expressions])


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
