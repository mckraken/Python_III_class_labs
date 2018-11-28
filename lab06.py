#! /usr/bin/env python

from pprint import pprint


clist = [(f, 5 / 9 * (f - 32)) for f in range(-40, 120, 10) if f not in [0, 50]]
cset = {(f, 5 / 9 * (f - 32)) for f in range(-40, 120, 10) if f not in [0, 50]}
cdict = {f: 5 / 9 * (f - 32) for f in range(-40, 120, 10) if f not in [0, 50]}

pprint(clist)
pprint(cset)
pprint(cdict)
