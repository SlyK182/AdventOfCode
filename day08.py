# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/8

from AdventOfCode.common import load_input, timer

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


@timer
def problem1_solution():
    prog = {n: parse_instruction(i) for n, i in enumerate(load_input(8, 1), 1)}
    console = Console(prog)
    console.run()
    return console.accumulator if console.stop == 300 else "Solution not found"


@timer
def problem2_solution():
    prog = {n: parse_instruction(i) for n, i in enumerate(load_input(8, 2), 1)}
    for num, (op, val) in prog.items():
        op = {'nop': 'jmp', 'jmp': 'nop'}.get(op)
        if not op:
            continue
        patched_instructions = prog.copy()
        patched_instructions[num] = (op, val)
        console = Console(patched_instructions)
        console.run()
        if console.stop == 100:
            return console.accumulator
    return "Solution not found"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
