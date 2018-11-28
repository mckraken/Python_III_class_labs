#! /usr/bin/env python

from pprint import pprint

c = lambda x: round(5 / 9 * (x - 32), 2)

clist = [(f, c(f)) for f in range(-40, 120, 10) if f not in [0, 50]]
cset = {(f, c(f)) for f in range(-40, 120, 10) if f not in [0, 50]}
cdict = {f: c(f) for f in range(-40, 120, 10) if f not in [0, 50]}

pprint(clist)
pprint(cset)
pprint(cdict)
