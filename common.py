# Author: ComradeSlyK (gregorini.silvio@gmail.com)

import sys
import time

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


def timer(func):
    def wrapper(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        fname = f'{func.__name__}() in {func.__code__.co_filename}'
        ints, decs = str(round(te - ts, 5)).split('.')
        t = '.'.join([ints.zfill(5), decs + '0' * (5 - len(decs))])
        print(f'{fname}: {t} s')
        return result
    return wrapper
