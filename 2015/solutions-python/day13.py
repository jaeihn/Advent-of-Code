# 2015 - DAY 13 - KNIGHTS OF THE DINNER TABLE
# https://adventofcode.com/2015/day/13

import os
import numpy as np
import pandas as pd
import pulp


with open(os.path.dirname(__file__)+'/inputs/day13.txt', 'r') as f:
    data = f.read().split('\n')
f.close()

data = [d.split() for d in data if d]


# PART 1
unique_members = list(set([d[0] for d in data]))
neighbors = []
happiness = pd.DataFrame(np.full((len(unique_members), len(unique_members)), -np.inf), columns=unique_members, index=unique_members)

for d in data:
    person1 = d[0]
    person2 = d[-1][:-1]
    varname = "_".join(sorted([person1, person2]))

    if varname not in neighbors:
        neighbors.append(varname)

    if happiness[person1][person2] == -np.inf:
        if 'gain' in d:
            happiness[person1][person2] = int(d[3])
            happiness[person2][person1] = int(d[3])
        elif 'lose' in d:
            happiness[person1][person2] = -int(d[3])
            happiness[person2][person1] = -int(d[3])
    else:
        if 'gain' in d:
            happiness[person1][person2] += int(d[3])
            happiness[person2][person1] += int(d[3])
        elif 'lose' in d:
            happiness[person1][person2] -= int(d[3])
            happiness[person2][person1] -= int(d[3])

neigh_var = []
happy_score = []

for n in neighbors:
    neigh_var.append(pulp.LpVariable(n, cat=pulp.LpBinary))
    happy_score.append(happiness[n.split('_')[0]][n.split('_')[-1]])

# set up linear optimization problem
problem = pulp.LpProblem("max_happy", pulp.LpMaximize)
problem += pulp.lpDot(neigh_var, happy_score), 'Objective Function'

# constraints 
problem += pulp.lpSum(neigh_var) == len(unique_members), 'all members are seated'

for m in unique_members:
    problem += pulp.lpSum([p for p in neigh_var if m in str(p)]) == 2, 'Appears exactly twice_'+m

problem.solve(pulp.PULP_CBC_CMD(msg=0))
print(problem.objective.value())



# PART 2

# Add myself to the table

for n in unique_members:
    neigh_var.append(pulp.LpVariable('Me_'+n, cat=pulp.LpBinary))
    happy_score.append(0)

unique_members.append('Me')

# set up linear optimization problem
problem = pulp.LpProblem("max_happy", pulp.LpMaximize)
problem += pulp.lpDot(neigh_var, happy_score), 'Objective Function'

# constraints 
problem += pulp.lpSum(neigh_var) == len(unique_members), 'all members are seated'

for m in unique_members:
    problem += pulp.lpSum([p for p in neigh_var if m in str(p)]) == 2, 'Appears exactly twice_'+m

problem.solve(pulp.PULP_CBC_CMD(msg=0))
print(problem.objective.value())
