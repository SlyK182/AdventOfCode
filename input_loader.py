# Author: ComradeSlyK (gregorini.silvio@gmail.com)

from os import path
from pathlib import Path


def load_input(day, num):
    curdir = str(Path(path.abspath(__file__)).parent)
    day = str(day).zfill(2)
    with open(path.join(curdir, 'inputs', f'day{day}_{num}.txt'), 'r') as f:
        return f.readlines()
