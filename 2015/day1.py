# 2015 - DAY 1 - NOT QUITE LISP
# https://adventofcode.com/2015/day/1

import os
with open(os.path.dirname(__file__)+'/inputs/day1.txt', 'r') as f:
    input = f.read()
f.close()

# PART 1
print(len(input) - 2*(input.count(')')))

# PART 2
floor = 0

for i in range(len(input)):
    if floor==-1:
        print(i)
        break
    elif input[i]=='(':
        floor+=1
    elif input[i]==')':
        floor-=1
