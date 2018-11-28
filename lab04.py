#! /usr/bin/env python

import os
import string
from operator import itemgetter

file_dir = "../class_data/"
alice_fn = "alice_in_wonderland.dat"
dictionary_fn = "words.txt"

# create word dictionary and initialize it with counts of zero
# words = dict()
dictlist = list()
with open(os.path.expanduser(file_dir + dictionary_fn), 'r') as dictfile, \
        open(os.path.expanduser(file_dir + alice_fn), 'r') as alicefile:
    for line in dictfile:
        dictlist.append(line.strip().lower())
    # words[line.strip().lower()] = 0
    words = dict.fromkeys(dictlist, 0)

    alice_words = []

    for raw_line in alicefile:
        line = raw_line.translate(
            str.maketrans(
                string.punctuation,             # characters to replace
                ' ' * len(string.punctuation),  # replacements
                "'"                             # characters to delete
            )
        ).lower().strip()
        alice_words.extend(line.split())

alice_words_set = set(alice_words)
dict_words_set = set(words.keys())

words_unk = alice_words_set - dict_words_set
for w in alice_words:
    if w not in words_unk:
        words[w] += 1

# ordered_words = sorted([(v, k) for k, v in words.items()])
ordered_words = sorted(words.items(), key=itemgetter(1))

print()
print(f'Total words in English dictionary we used: {len(words)}')
print(f'Total words in book: {len(alice_words):>7n}')
print(f'Total unique words in book: {len(alice_words_set)}')
print(f'Percentage of English words used in book: '
      f'{len(alice_words_set)/len(words):6.2%}')
print(f'The word "{ordered_words[-1][1]}" is the most frequently used with '
      f'{ordered_words[-1][0]} occurances.')
print(f'The {len(words_unk)} words not found in the dictionary are:')
print()
# n = 0
# for w in sorted(words_unk):
#     n += 1
#     print(f'{w:<20s}', end=' ')
#     if n >= 6:
#         print()
#         n = 0
for n in range(0,20):
    w = ordered_words.pop()
    print(f'{w[1]:.<7}{w[0]:.>7}')
print()
