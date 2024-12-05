import math
import time

from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
SOLUTIONS_DIR = ROOT_DIR / "solutions"
DAYS_DIR = SOLUTIONS_DIR / "days"
INPUTS_DIR = SOLUTIONS_DIR / "inputs"
UTILS_DIR = SOLUTIONS_DIR / "utils"


def load_input(day: int, num: int):
    with open(INPUTS_DIR.joinpath(f"day{str(day).zfill(2)}_{num}.txt"), "r") as f:
        yield from map(str.strip, f.readlines())


def timer(func):
    def wrapper(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        delta = te - ts
        hh, remainder = divmod(delta, 3600)
        mm, ss = divmod(remainder, 60)
        remainder, ss = math.modf(ss)
        remainder, milliss = math.modf(remainder * 1000)
        micross = math.modf(remainder * 1000)[1]
        hh, mm, ss, milliss, micross = tuple(map(int, (hh, mm, ss, milliss, micross)))
        print(f"{func.__module__}.{func.__name__}(): {hh}h {str(mm).zfill(2)}m {str(ss).zfill(2)}s {str(milliss).zfill(3)}ms {str(micross).zfill(3)}μs")
        return result
    return wrapper
