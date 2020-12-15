# Author: Silvio Gregorini (silviogregorini@openforce.it)

from AdventOfCode.common import timer


@timer
def main():
    from os import path
    from pathlib import Path
    from subprocess import call

    curdir = str(Path(path.abspath(__file__)).parent)
    pybin = Path(path.join(curdir, 'venv-AOC2020/bin/python3'))
    for x in range(1, 26):
        day = str(x).zfill(2)
        pyfile = Path(path.join(curdir, f'day{day}.py'))
        if pyfile.exists():
            print(f"Day {day}")
            call([pybin, str(pyfile)])
        else:
            return


if __name__ == '__main__':
    main()
