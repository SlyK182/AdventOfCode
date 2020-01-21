# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2019/day/5

from .day02 import IntCode, Instruction


INPUT_CODE = [
    3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 86, 8, 225, 1101,
    82, 69, 225, 101, 36, 65, 224, 1001, 224, -106, 224, 4, 224, 1002, 223, 8,
    223, 1001, 224, 5, 224, 1, 223, 224, 223, 102, 52, 148, 224, 101, -1144,
    224, 224, 4, 224, 1002, 223, 8, 223, 101, 1, 224, 224, 1, 224, 223, 223,
    1102, 70, 45, 225, 1002, 143, 48, 224, 1001, 224, -1344, 224, 4, 224, 102,
    8, 223, 223, 101, 7, 224, 224, 1, 223, 224, 223, 1101, 69, 75, 225, 1001,
    18, 85, 224, 1001, 224, -154, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224,
    224, 1, 224, 223, 223, 1101, 15, 59, 225, 1102, 67, 42, 224, 101, -2814,
    224, 224, 4, 224, 1002, 223, 8, 223, 101, 3, 224, 224, 1, 223, 224, 223,
    1101, 28, 63, 225, 1101, 45, 22, 225, 1101, 90, 16, 225, 2, 152, 92, 224,
    1001, 224, -1200, 224, 4, 224, 102, 8, 223, 223, 101, 7, 224, 224, 1, 223,
    224, 223, 1101, 45, 28, 224, 1001, 224, -73, 224, 4, 224, 1002, 223, 8,
    223, 101, 7, 224, 224, 1, 224, 223, 223, 1, 14, 118, 224, 101, -67, 224,
    224, 4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 4,
    223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999,
    1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1,
    99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999,
    1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225,
    225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1,
    99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 7,
    677, 677, 224, 102, 2, 223, 223, 1005, 224, 329, 1001, 223, 1, 223, 1008,
    226, 226, 224, 1002, 223, 2, 223, 1005, 224, 344, 1001, 223, 1, 223, 1107,
    677, 226, 224, 1002, 223, 2, 223, 1006, 224, 359, 1001, 223, 1, 223, 107,
    677, 677, 224, 102, 2, 223, 223, 1005, 224, 374, 101, 1, 223, 223, 1108,
    677, 226, 224, 102, 2, 223, 223, 1005, 224, 389, 1001, 223, 1, 223, 1007,
    677, 677, 224, 1002, 223, 2, 223, 1005, 224, 404, 101, 1, 223, 223, 1008,
    677, 226, 224, 102, 2, 223, 223, 1005, 224, 419, 101, 1, 223, 223, 1108,
    226, 677, 224, 102, 2, 223, 223, 1006, 224, 434, 1001, 223, 1, 223, 8, 677,
    226, 224, 1002, 223, 2, 223, 1005, 224, 449, 101, 1, 223, 223, 1008, 677,
    677, 224, 1002, 223, 2, 223, 1006, 224, 464, 1001, 223, 1, 223, 1108, 226,
    226, 224, 1002, 223, 2, 223, 1005, 224, 479, 1001, 223, 1, 223, 1007, 226,
    677, 224, 102, 2, 223, 223, 1005, 224, 494, 1001, 223, 1, 223, 1007, 226,
    226, 224, 102, 2, 223, 223, 1005, 224, 509, 101, 1, 223, 223, 107, 677,
    226, 224, 1002, 223, 2, 223, 1006, 224, 524, 1001, 223, 1, 223, 108, 677,
    677, 224, 102, 2, 223, 223, 1006, 224, 539, 101, 1, 223, 223, 7, 677, 226,
    224, 102, 2, 223, 223, 1006, 224, 554, 1001, 223, 1, 223, 1107, 226, 677,
    224, 102, 2, 223, 223, 1005, 224, 569, 101, 1, 223, 223, 108, 677, 226,
    224, 1002, 223, 2, 223, 1006, 224, 584, 101, 1, 223, 223, 108, 226, 226,
    224, 102, 2, 223, 223, 1006, 224, 599, 1001, 223, 1, 223, 1107, 226, 226,
    224, 102, 2, 223, 223, 1006, 224, 614, 1001, 223, 1, 223, 8, 226, 677, 224,
    102, 2, 223, 223, 1006, 224, 629, 1001, 223, 1, 223, 107, 226, 226, 224,
    102, 2, 223, 223, 1005, 224, 644, 101, 1, 223, 223, 8, 226, 226, 224, 102,
    2, 223, 223, 1006, 224, 659, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2,
    223, 223, 1005, 224, 674, 101, 1, 223, 223, 4, 223, 99, 226
]
INPUT_INST = [1]
OUTPUT_CODE = []


class DiagnosticInstruction(Instruction):

    def __init__(self, intcode):
        super().__init__(intcode)
        opcode = str(self.opcode).zfill(5)
        self.opcode = int(opcode[-2:])
        self.params_modes = [int(c) for c in reversed(opcode[:3])]

    def compute_opcode_3(self):
        self.set_input_val()

    def compute_opcode_4(self):
        self.print_output_val()

    @classmethod
    def get_compute_opcode_methods(cls):
        methods = super().get_compute_opcode_methods()
        methods.update({
            3: cls.compute_opcode_3,
            4: cls.compute_opcode_4,
        })
        return methods

    def multiply(self):
        if len(self.params) != 3:
            self.intcode.error = "Invalid params: {}" \
                .format(', '.join([str(p) for p in self.params]))
            return
        code = self.start_code
        vals = {
            n + 1: code[p] if (m == 0 and n + 1 != 3) else p
            for n, (m, p) in enumerate(zip(self.params_modes, self.params))
        }
        code[vals[3]] = vals[1] * vals[2]
        self.update(code, 4)

    def print_output_val(self):
        if len(self.params) <= 1:
            self.intcode.error = "Invalid params: {}" \
                .format(', '.join([str(p) for p in self.params]))
            return
        code = self.start_code
        param, mode = self.params[0], self.params_modes[0]
        while OUTPUT_CODE:
            OUTPUT_CODE.pop()
        OUTPUT_CODE.append(code[param] if mode == 0 else param)
        print(OUTPUT_CODE[0])
        self.update(code, 2)

    def set_input_val(self):
        if len(self.params) <= 1:
            self.intcode.error = "Invalid params: {}" \
                .format(', '.join([str(p) for p in self.params]))
            return
        code = self.start_code
        param = self.params[0]
        code[param] = INPUT_INST[0]
        self.update(code, 2)

    def sum(self):
        if len(self.params) != 3:
            self.intcode.error = "Invalid params: {}" \
                .format(', '.join([str(p) for p in self.params]))
            return
        code = self.start_code
        vals = {
            n + 1: code[p] if (m == 0 and n + 1 != 3) else p
            for n, (m, p) in enumerate(zip(self.params_modes, self.params))
        }
        code[vals[3]] = vals[1] + vals[2]
        self.update(code, 4)


class DiagnosticCode(IntCode):
    _instruction_cls = DiagnosticInstruction


def problem1_solution():
    intcode_list = INPUT_CODE
    diagcode = DiagnosticCode(intcode_list)
    diagcode.compute_all()
    return OUTPUT_CODE[0]


def problem2_solution():
    return "No solution yet!"


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
