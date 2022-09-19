# 2015 - DAY 5 - DOESN'T HE HAVE INTERN-ELVES FOR THIS?
# https://adventofcode.com/2015/day/5

import regex
import os

with open(os.path.dirname(__file__)+'/inputs/day5.txt', 'r') as f:
    strings = f.read().split()
f.close()

# PART 1
vowels = ['a', 'e', 'i', 'o', 'u']

naughty = 0 

for s in strings:
    if regex.match(r"\w*(ab|cd|pq|xy)\w*", s):
        naughty += 1
    elif regex.match(r"\w*(\w)\1{1,}\w*", s) is None:
        naughty += 1
    elif len([c for c in s if c in vowels])<3:
        naughty += 1

print(len(strings)-naughty)


# PART 2

naughty = 0

for s in strings:
    if regex.match(r"\w*(\w\w)\w*\1\w*", s) is None:
        naughty += 1
    elif regex.match(r"\w*(\w)[^\1]\1\w*", s) is None:
        naughty +=1

print(len(strings)-naughty)

