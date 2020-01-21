# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2019/day/1

from math import floor

MODULE_MASSES = [
    129192.00, 58561.00, 57267.00, 95382.00, 84995.00, 127372.00,
    93598.00, 97264.00, 138550.00, 79327.00, 135661.00, 139468.00,
    108860.00, 149642.00, 72123.00, 128333.00, 69002.00, 98450.00,
    86267.00, 70171.00, 101333.00, 79822.00, 142539.00, 142743.00,
    51371.00, 111381.00, 62073.00, 72210.00, 125168.00, 135952.00,
    131060.00, 121842.00, 88234.00, 146774.00, 136571.00, 126719.00,
    50644.00, 75696.00, 51195.00, 77171.00, 118052.00, 83691.00,
    133779.00, 149814.00, 64847.00, 110697.00, 92695.00, 59453.00,
    139517.00, 129487.00, 79271.00, 97896.00, 146987.00, 149822.00,
    71866.00, 90797.00, 104732.00, 54997.00, 50139.00, 134115.00,
    133017.00, 144979.00, 89428.00, 124750.00, 91833.00, 57252.00,
    67195.00, 121624.00, 102706.00, 138245.00, 127700.00, 124098.00,
    110382.00, 121557.00, 103613.00, 133576.00, 122801.00, 112306.00,
    120203.00, 134696.00, 76129.00, 84576.00, 80854.00, 147237.00,
    71025.00, 127513.00, 143631.00, 125090.00, 115698.00, 57979.00,
    84880.00, 120177.00, 147389.00, 88380.00, 114688.00, 56355.00,
    126265.00, 58220.00, 63523.00, 130179.00,
]


def calculate_fuel(module_mass):
    """ Returns fuel for a single module mass """
    return max(floor(module_mass / 3) - 2, 0)


def calculate_fuel_split(masses):
    """ Returns list of fuel amounts, adding fuel mass itself """
    fuel_amounts = []

    for mass in masses:
        fuel = calculate_fuel(mass)
        fuel_amounts.append(fuel)
        while fuel > 0:
            # Fuel itself has a mass: compute additional fuel
            fuel = calculate_fuel(fuel)
            fuel_amounts.append(fuel)

    return fuel_amounts


def problem1_solution():
    return sum(calculate_fuel(m) for m in MODULE_MASSES)


def problem2_solution():
    return sum(calculate_fuel_split(MODULE_MASSES))


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
