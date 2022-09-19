# 2015 - DAY 16 - AUNT SUE
# https://adventofcode.com/2015/day/16

import os
import regex

with open(os.path.dirname(__file__)+'/inputs/day16.txt', 'r') as f:
    memory = f.read().split('\n')
f.close()

for i in range(len(memory)):
    memory[i] = regex.sub(r"[,:]","",memory[i])

the_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

sues = [True]*500

for i in range(500):
    details = memory[i].split()
    for k in the_sue.keys():
        if k in details:
            test = int(details[details.index(k)+1])
            if the_sue[k]!=test:
                sues[i] = False

for i in range(500):
    if sues[i]==True:
        print(memory[i])


# PART 2

sues = [True]*500

for i in range(500):
    details = memory[i].split()
    for k in the_sue.keys():
        if k in details:
            test_value = int(details[details.index(k)+1])
            if k=='cats' or k=='trees':
                if the_sue[k] >= test_value:
                    sues[i] = False
            elif k=='pomeranians'or k=='goldfish':
                if the_sue[k] <= test_value:
                    sues[i] = False
            else:
                if the_sue[k] != test_value:
                    sues[i] = False

print()
for i in range(500):
    if sues[i]==True:
        print(memory[i])