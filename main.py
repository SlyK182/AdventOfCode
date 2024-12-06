#!/usr/bin/env python
from argparse import ArgumentParser
from solutions.days import main


def _get_args():
    parser = ArgumentParser()
    parser.add_argument("-d", "--days", type=lambda a: list(map(int, a.split(','))))
    return parser.parse_args()


if __name__ == '__main__':
    args = _get_args()
    main(args.days or None)
