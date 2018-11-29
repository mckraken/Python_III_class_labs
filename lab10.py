#! /usr/bin/env python

from sys import argv, stderr, exit


def factorial_func(x):
    try:
        x = int(x)
    except ValueError:
        print(f'{x} ({type(x)}) is not valid for conversion',
              file=stderr)
        exit(1)
        # continue

    if x == 1:
        return 1
    elif not x > 1:
        return "we need a positive integer"
    return x * factorial_func(x - 1)

print(factorial_func(argv[1]))
