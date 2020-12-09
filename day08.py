# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/8

from os import path
from pathlib import Path

CURDIR = str(Path(path.abspath(__file__)).parent)


class Console:

    def __init__(self, instructions):
        self.instructions = instructions
        self.position = 1
        self.accumulator = 0
        self.executed = []

    @property
    def stop(self):
        pos = self.position
        first_instruction = min(self.instructions)
        last_instruction = max(self.instructions)

        # Program exited: if the last instruction has been executed, return
        # 100 (OK code) else 200
        if not first_instruction <= pos <= last_instruction:
            if self.executed[-1] == max(self.instructions):
                return 100
            return 200

        # Program is looping: return 300
        elif pos in self.executed:
            return 300

        # No stop condition found
        return 0

    def run(self):
        while not self.stop:
            op, val = self.instructions[self.position]
            getattr(self, f'run_{op}')(val)

    def run_acc(self, val):
        self.executed.append(self.position)
        self.accumulator += val
        self.position += 1

    def run_jmp(self, val):
        self.executed.append(self.position)
        self.position += val

    def run_nop(self, val):
        self.executed.append(self.position)
        self.position += 1


def parse_instruction(instr):
    o, v = instr.split(' ')
    o = o.lower().strip()
    return o, (1 if v[0] == '+' else -1) * int(v[1:])


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day08_1.txt'), 'r') as input1:
        instructions = {
            n: parse_instruction(i)
            for n, i in enumerate(input1.readlines(), 1)
        }
    console = Console(instructions)
    console.run()
    return console.accumulator if console.stop == 300 else "Solution not found"


def problem2_solution():
    with open(path.join(CURDIR, 'inputs', f'day08_2.txt'), 'r') as input2:
        instructions = {
            n: parse_instruction(i)
            for n, i in enumerate(input2.readlines(), 1)
        }
    for patch in [
        (n, 'jmp' if o == 'nop' else 'nop', v)
        for n, (o, v) in instructions.items()
        if o in ('jmp', 'nop')
    ]:
        n, o, v = patch
        patched_instructions = instructions.copy()
        patched_instructions[n] = (o, v)
        console = Console(patched_instructions)
        console.run()
        if console.stop == 100:
            return console.accumulator
    return "Solution not found"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
