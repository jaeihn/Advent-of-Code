# 2015 - DAY 8 - MATCHSTICKS
# https://adventofcode.com/2015/day/8

import os
import regex

with open(os.path.dirname(__file__)+ '/inputs/day8.txt', 'r') as f:
     lines = f.read().split()
f.close()

# Part 1
code = sum([len(x) for x in lines])
memory = sum([len(x.encode("utf-8").decode('unicode-escape'))-2 for x in lines])

print(code-memory)

# Part 2
extended = sum([len(regex.sub('"', '"\"', repr(x))) for x in lines])

print(extended - code)