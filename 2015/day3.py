# 2015 - DAY 3 - PERFECTLY SPHERICAL HOUSES IN A VACUUM
# https://adventofcode.com/2015/day/3

import os

with open(os.path.dirname(__file__)+'/inputs/day3.txt', 'r') as f:
    directions = f.read()
f.close()

# PART 1
history = [(0,0)]

for i in range(len(directions)):
    last = history[-1]
    if directions[i]=='v':
        history.append((last[0],last[1]-1))
    elif directions[i]=='^':
        history.append((last[0],last[1]+1))
    elif directions[i]=='>':
        history.append((last[0]+1,last[1]))
    elif directions[i]=='<':
        history.append((last[0]-1,last[1]))

print(len(set(history)))


# PART 2

history = [(0,0), (0,0)]

for i in range(len(directions)):
    last = history[-2]
    if directions[i]=='v':
        history.append((last[0],last[1]-1))
    elif directions[i]=='^':
        history.append((last[0],last[1]+1))
    elif directions[i]=='>':
        history.append((last[0]+1,last[1]))
    elif directions[i]=='<':
        history.append((last[0]-1,last[1]))

print(len(set(history)))