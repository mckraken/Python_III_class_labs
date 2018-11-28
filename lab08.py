#! /usr/bin/env python

import random


def ran_gen_test():
    start = int(random.random() * 100)
    end = random.randrange(start, 101)
    print(start, end)

    i = start
    while i <= end:
        if i % 2 == 0:
            yield i
        else:
            yield "odd"
        i += 1


for z in ran_gen_test():  # As an iterator
    print(z, end=' ')
print('\nNo more numbers... finished')

nxt_gen = ran_gen_test()
while True:   # By directly accessing each item in order
    try:
        print(next(nxt_gen), end=' ')
    except StopIteration:
        print('\nNo more numbers... finished')
        break

nxt_gen = ran_gen_test()
while True:   # By directly accessing each item in order
    try:
        print(nxt_gen.__next__(), end=' ')
    except StopIteration:
        print('\nNo more numbers... finished')
        break

