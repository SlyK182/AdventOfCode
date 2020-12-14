# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/14

from itertools import product

from AdventOfCode.input_loader import load_input


def binarystr_to_decimalstr(b):
    return str(sum(2 ** i * int(c) for i, c in enumerate(reversed(b))))


def decimalstr_to_binarystr(d):
    n = []
    intd = int(d)
    while intd > 1:
        intd, r = divmod(intd, 2)
        n.insert(0, str(r))
    n.insert(0, str(intd))
    return ''.join(n)


def problem1_solution():
    mask = ''
    mem = {}
    for line in map(lambda x: x.strip(), load_input(14, 1)):
        if line.startswith('mask'):
            mask = line.replace('mask = ', '')
            continue
        # Retrieve address and value in base 10
        addr, decval = line.replace('mem[', '').replace(']', '').split(' = ')
        # Convert value to base 2, fill chars to make its length reach 36
        binval = decimalstr_to_binarystr(decval).zfill(36)
        # Apply mask rules
        newbinval = ''.join(b if m == 'X' else m for b, m in zip(binval, mask))
        # Convert back to base 10, set in memory to its address
        mem[addr] = binarystr_to_decimalstr(newbinval)
    return sum([int(v) for v in mem.values()])


def problem2_solution():
    mask = ''
    mem = {}
    for line in map(lambda x: x.strip(), load_input(14, 2)):
        if line.startswith('mask'):
            mask = line.replace('mask = ', '')
            continue
        # Retrieve address and value in base 10
        addr, decval = line.replace('mem[', '').replace(']', '').split(' = ')
        # Convert address to base 2, fill chars to make its length reach 36
        binaddr = decimalstr_to_binarystr(addr).zfill(36)
        # Apply mask rules
        maskedaddr = ''.join(
            b if m == '0' else m if m == '1' else 'X'
            for b, m in zip(binaddr, mask)
        )
        # For each X in the masked address, apply once 0 and once 1 (so, for 2
        # Xs, we'll have 4 possible substitutions: (0, 0), (0, 1), (1, 0),
        # (1, 1), giving 4 different addresses)
        for bits in product(*[(0, 1) for _ in range(maskedaddr.count('X'))]):
            newaddr = maskedaddr.replace('X', '{}').format(*bits)
            # Convert back to base 10, set its value in memory
            mem[binarystr_to_decimalstr(newaddr)] = decval
    return sum([int(v) for v in mem.values()])


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
