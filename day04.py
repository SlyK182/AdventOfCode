# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/4

from os import path
from pathlib import Path
from string import digits, hexdigits

CURDIR = str(Path(path.abspath(__file__)).parent)


def validate_byr(byr):
    return 1920 <= int(byr) <= 2002


def validate_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth']


def validate_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def validate_hcl(hcl):
    return len(hcl) == 7 \
        and hcl.startswith('#') \
        and all(c in hexdigits for c in hcl[1:])


def validate_hgt(hgt):
    if hgt.endswith('cm'):
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith('in'):
        return 59 <= int(hgt[:-2]) <= 76
    return False


def validate_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def validate_pid(pid):
    return len(pid) == 9 and all(c in digits for c in pid)


FIELDS = {
    # Birth Year
    'byr': {
        'mandatory': True,
        'validate': validate_byr,
    },
    # Country ID
    'cid': {
        'mandatory': False,
        'validate': None,
    },
    # Eye Color
    'ecl': {
        'mandatory': True,
        'validate': validate_ecl,
    },
    # Expiration Year
    'eyr': {
        'mandatory': True,
        'validate': validate_eyr,
    },
    # Hair Color
    'hcl': {
        'mandatory': True,
        'validate': validate_hcl,
    },
    # Height
    'hgt': {
        'mandatory': True,
        'validate': validate_hgt,
    },
    # Issue Year
    'iyr': {
        'mandatory': True,
        'validate': validate_iyr,
    },
    # Passport ID
    'pid': {
        'mandatory': True,
        'validate': validate_pid,
    },
}


def has_all_mandatory_fields(pdict):
    return all(f in pdict for f in FIELDS if FIELDS[f]['mandatory'])


def has_all_valid_fields(pdict):
    return has_all_mandatory_fields(pdict) \
        and all(
        FIELDS[f]['validate'](pdict.get(f))
        for f in FIELDS
        if FIELDS[f]['validate']
    )


def passport_dict(passport_as_string):
    return dict(
        d.split(':')
        for d in passport_as_string.replace('\n', ' ').split(' ')
    )


def problem1_solution():
    with open(path.join(CURDIR, 'inputs', f'day04_1.txt'), 'r') as input1:
        plist = tuple(map(passport_dict, input1.read().split('\n\n')))
    return len(tuple(filter(has_all_mandatory_fields, plist)))


def problem2_solution():
    with open(path.join(CURDIR, 'inputs', f'day04_2.txt'), 'r') as input2:
        plist = tuple(map(passport_dict, input2.read().split('\n\n')))
    return len(tuple(filter(has_all_valid_fields, plist)))


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
