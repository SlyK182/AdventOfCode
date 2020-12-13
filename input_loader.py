# Author: ComradeSlyK (gregorini.silvio@gmail.com)

import sys

from os import path
from pathlib import Path


def load_input(day, num):
    curdir = str(Path(path.abspath(__file__)).parent)
    day = str(day).zfill(2)
    filename = f'day{day}_{num}'
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'test':
        filename += '_test'
    filename += '.txt'
    with open(path.join(curdir, 'inputs', filename), 'r') as f:
        return f.readlines()
