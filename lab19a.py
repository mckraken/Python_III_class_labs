#! /usr/bin/env python

import os
import string
from collections import Counter

file_dir = "../class_data/"
alice_fn = "alice_in_wonderland.dat"

with open(os.path.expanduser(file_dir + alice_fn), 'r') as f:
    alice = f.read().lower().translate(
        str.maketrans(
            "",
            "",
            string.whitespace
        )
    )

alice_characters = Counter(alice)
alice_top_20 = alice_characters.most_common(20)

for item in alice_top_20:
    print(f'{item[0]:.<3s}{item[1]:.>8,}')
print()
