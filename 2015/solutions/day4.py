# 2015 - DAY 4 - THE IDEAL STOCKING STUFFER
# https://adventofcode.com/2015/day/4

import hashlib

input = 'bgvyzdsv'

# PART 1
number = 0

while True:
    key = input + str(number)
    if hashlib.md5(key.encode()).hexdigest().startswith('00000'):
        print(number)
        break
    number += 1

# PART 2
number = 0

while True:
    key = input + str(number)
    if hashlib.md5(key.encode()).hexdigest().startswith('000000'):
        print(number)
        break
    number += 1
