# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2019/day/2

INPUT_CODE = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 5, 19, 23,
    1, 23, 5, 27, 2, 27, 10, 31, 1, 5, 31, 35, 2, 35, 6, 39, 1, 6, 39, 43, 2,
    13, 43, 47, 2, 9, 47, 51, 1, 6, 51, 55, 1, 55, 9, 59, 2, 6, 59, 63, 1, 5,
    63, 67, 2, 67, 13, 71, 1, 9, 71, 75, 1, 75, 9, 79, 2, 79, 10, 83, 1, 6, 83,
    87, 1, 5, 87, 91, 1, 6, 91, 95, 1, 95, 13, 99, 1, 10, 99, 103, 2, 6, 103,
    107, 1, 107, 5, 111, 1, 111, 13, 115, 1, 115, 13, 119, 1, 13, 119, 123, 2,
    123, 13, 127, 1, 127, 6, 131, 1, 131, 9, 135, 1, 5, 135, 139, 2, 139, 6,
    143, 2, 6, 143, 147, 1, 5, 147, 151, 1, 151, 2, 155, 1, 9, 155, 0, 99, 2,
    14, 0, 0
]


def setup_code(input_code, to_update):
    new_code = [i for i in input_code]
    for x, y in to_update.items():
        if x < len(new_code):
            new_code[x] = y
    return new_code


class Instruction:
    """
    `intcode` stores the IntCode to which the Instruction is related

    `start_code` stores the code before computing the instruction

    `end_code` stores the code after computing the instruction

    `opcode` defines the operation that should be done by current instruction

    `params` defines which params should be used (at most 3 elements)

    `prev`, `next` store previous/following instruction for given IntCode
    """

    def __init__(self, intcode):
        self.intcode = intcode
        self.start_code = intcode.code
        self.end_code = None
        self.opcode = intcode.code[intcode.address]
        self.params = [
            intcode.code[intcode.address + x]
            for x in (1, 2, 3)
            if intcode.address + x < len(intcode.code)
        ]
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '[{}]'.format(
            ', '.join(str(c) for c in [self.opcode] + self.params)
        )

    def compute(self):
        method = self.get_compute_opcode_methods().get(self.opcode)
        if method:
            method(self)
        else:
            self.intcode.error = "Invalid opcode '{}' at position '{}'" \
                .format(self.opcode, self.intcode.address)
        self.intcode.update_instructions(self)

    def compute_opcode_1(self):
        self.sum()

    def compute_opcode_2(self):
        self.multiply()

    def compute_opcode_99(self):
        self.halt()

    @classmethod
    def get_compute_opcode_methods(cls):
        return {
            1: cls.compute_opcode_1,
            2: cls.compute_opcode_2,
            99: cls.compute_opcode_99,
        }

    def halt(self):
        self.end_code = self.start_code
        self.intcode.code = self.end_code
        self.intcode.stop = True

    def multiply(self):
        if len(self.params) != 3:
            self.intcode.error = "Invalid params: {}" \
                .format(', '.join([str(p) for p in self.params]))
            return
        pos1, pos2, pos3 = self.params
        code = self.start_code
        code[pos3] = code[pos1] * code[pos2]
        self.update(code, 4)

    def sum(self):
        if len(self.params) != 3:
            self.intcode.error = "Invalid params: {}" \
                .format(', '.join([str(p) for p in self.params]))
            return
        pos1, pos2, pos3 = self.params
        code = self.start_code
        code[pos3] = code[pos1] + code[pos2]
        self.update(code, 4)

    def update(self, code, steps):
        self.end_code = code
        self.intcode.code = code
        self.intcode.address += steps


class IntCode:
    """
    `code` stores the current code (list of integers)

    `start_code` stores the starting code (list of integers)

    `address` stores the position of the memory address while reading and
    updating the IntCode itself (integer)

    `stop` is False until an halt code (99) is met (boolean)

    `error` is valued when an error occurs (string)
    """
    _instruction_cls = Instruction

    def __init__(self, code_list):
        self.start_code = code_list
        self.code = code_list
        self.address = 0
        self.stop = False
        self.error = ""
        self.instructions = []

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code

    def compute_all(self):
        """
        Computes every iteration until halt code is met or an error is raised
        """
        self.reset()
        while self.address < len(self.code) and not (self.stop or self.error):
            self.compute_next()

    def compute_next(self):
        instruction = self._instruction_cls(self)
        instruction.compute()

    def reset(self):
        self.__init__(self.start_code)

    def update_instructions(self, instr):
        if self.instructions:
            instr.prev = self.instructions[-1]
            instr.prev.next = instr
        self.instructions.append(instr)


def problem1_solution():
    intcode_list = setup_code(INPUT_CODE, {1: 12, 2: 2})
    intcode = IntCode(intcode_list)
    intcode.compute_all()
    return intcode.code[0] if not intcode.error else intcode.error


def problem2_solution():
    for noun in range(100):
        for verb in range(100):
            intcode_list = setup_code(INPUT_CODE, {1: noun, 2: verb})
            intcode = IntCode(intcode_list)
            intcode.compute_all()
            if intcode.code[0] == 19690720:
                return 100 * noun + verb
    return "No couple found."


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
