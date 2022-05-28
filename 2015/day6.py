# 2015 - DAY 6 - PROBABLY A FIRE HAZARD
# https://adventofcode.com/2015/day/6

import os
import regex
import numpy as np

with open(os.path.dirname(__file__)+'/inputs/day6.txt', 'r') as f:
    instructions = f.read().split('\n')
f.close()

# PART 1

grid = np.full((1000,1000), False)

for i in instructions:
    coord = [int(a) for a in regex.findall(r'\d+', i)]
    if coord:
        x_i, y_i, x_f, y_f = coord
        if i.startswith('turn on'):
            grid[x_i:x_f+1, y_i:y_f+1] = True
        elif i.startswith('turn off'):
            grid[x_i:x_f+1, y_i:y_f+1] = False
        elif i.startswith('toggle'):
            grid[x_i:x_f+1, y_i:y_f+1] = ~grid[x_i:x_f+1, y_i:y_f+1]

print((grid==True).sum())

# Part 2

grid = np.zeros((1000,1000))

for i in instructions:
    coord = [int(a) for a in regex.findall(r'\d+', i)]
    if coord:
        x_i, y_i, x_f, y_f = coord
        if i.startswith('turn on'):
            grid[x_i:x_f+1, y_i:y_f+1] += 1
        elif i.startswith('turn off'):
            grid[x_i:x_f+1, y_i:y_f+1] -= 1
            grid = grid.clip(0)
        elif i.startswith('toggle'):
            grid[x_i:x_f+1, y_i:y_f+1] += 2

print(np.sum(grid))
