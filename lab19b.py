#! /usr/bin/env python

import os
import string
from collections import Counter

file_dir = "../class_data/"
alice_fn = "alice_in_wonderland.dat"
dictionary_fn = "words.txt"

alice_words = Counter()

with open(os.path.expanduser(file_dir + alice_fn), 'r') as f:
    alice = f.read().lower().translate(
        str.maketrans(
            string.punctuation,
            ' ' * len(string.punctuation),
            "'"
        )
    ).split()

with open(os.path.expanduser(file_dir + dictionary_fn), 'r') as f:
    words = f.read().lower().translate(
        str.maketrans(
            string.punctuation,
            ' ' * len(string.punctuation),
            "'"
        )
    ).split()

alice_words.update(alice)
alice_top_20 = alice_words.most_common(20)

total_alice_words = len(alice)
unique_alice_words = len(set(alice))
unknown_alice_words = len(set(alice) - set(words))

print(f'{"Total words in book:":<22s}{total_alice_words:>7,}')
print(f'{"Unique words in book:":<22s}{unique_alice_words:>7,}')
print(f'{"Unknown words in book:":<22s}{unknown_alice_words:>7,}')

for item in alice_top_20:
    print(f'{item[0]:.<10s}{item[1]:.>7,}')
print()
