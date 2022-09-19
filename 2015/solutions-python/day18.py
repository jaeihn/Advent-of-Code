

# 2015 - DAY 18 - LIKE A GIF FOR YOUR YARD 
# https://adventofcode.com/2015/day/18

import os
import numpy as np

with open(os.path.dirname(__file__)+'/inputs/day18.txt', 'r') as f:
    config = f.read().split('\n')
f.close()

# PART 1
config = "".join(config)
lights = np.full((100,100), False)

for i in range(len(config)):
    if config[i]=='#':
        lights[i//100][i%100] = True
    else:
        lights[i//100][i%100] = False


def update(grid):
    for i in range(len(config)):
        neighbors = []
        try: 
            neighbors.append(grid[i//100 -1][i%100])
        except:
            pass
        try:
            neighbors.append(grid[i//100 +1][i%100])
        except:
            pass
        try:
            neighbors.append(grid[i//100][i%100 -1])
        except:
            pass
        try:
            neighbors.append(grid[i//100][i%100 +1])
        except:
            pass
        try:
            neighbors.append(grid[i//100 -1][i%100 -1])
        except:
            pass
        try:
            neighbors.append(grid[i//100 +1][i%100 -1])
        except:
            pass
        try:
            neighbors.append(grid[i//100 -1][i%100 +1])
        except:
            pass
        try:
            neighbors.append(grid[i//100 +1][i%100 +1])
        except:
            pass
        
        nextgrid = np.full((100,100), False)

        if grid[i//100][i%100]:
            if sum(neighbors)==2 or sum(neighbors)==3:
                nextgrid[i//100][i%100] = True
            else:
                nextgrid[i//100][i%100] = False
        else:
            if sum(neighbors)==3:
                nextgrid[i//100][i%100] = True
            else:
                nextgrid[i//100][i%100] = False
    return nextgrid


for i in range(10):
    lights = update(lights)

print(sum(sum(lights)))