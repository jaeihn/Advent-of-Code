

# 2015 - DAY 17 - NO SUCH THING AS TOO MUCH 
# https://adventofcode.com/2015/day/17

import os
import itertools

with open(os.path.dirname(__file__)+'/inputs/day17.txt', 'r') as f:
    containers = [int(l) for l in f.read().split('\n') if l]
    f.close()


comb = list(itertools.product([0, 1], repeat=len(containers)))

def dot(v1, v2):
    return(sum([i*j for (i,j) in zip(v1, v2)]))

count = []

for c in comb:
    if dot(containers, list(c))==150:
        count.append(sum(list(c)))

print(len(count))


# PART 2
minimum = [c for c in count if c==min(count)]

print(len(minimum))


