# Author: ComradeSlyK (gregorini.silvio@gmail.com)


def main():
    from os import path
    from pathlib import Path
    from subprocess import call

    curdir = Path(path.abspath(__file__)).parent
    pybin = Path(path.join(str(curdir), 'venv-AOC2019/bin/python3'))
    for x in range(1, 26):
        day = str(x).zfill(2)
        pyfile = Path(path.join(str(curdir), f'day{day}.py'))
        if pyfile.exists():
            print(f"Day {day}")
            call([pybin, str(pyfile)])
        else:
            return


if __name__ == '__main__':
    main()
