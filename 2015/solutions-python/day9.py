# 2015 - DAY 9 - ALL IN A SINGLE NIGHT
# https://adventofcode.com/2015/day/9

import os
import pulp 

with open(os.path.dirname(__file__)+ '/inputs/day9.txt', 'r') as f:
     map_data = f.read()
f.close()

locations = list(set([d for d in map_data.split() if d[0].isupper()]))
roads = map_data.split('\n')
roads = (d for d in roads if d)


road_variables = []
road_lengths = []

for road in roads:
    road_variables.append(pulp.LpVariable(road.split()[0]+'_'+road.split()[2], cat=pulp.LpBinary))
    road_lengths.append(int(road.split()[-1]))

# set up linear optimization problem
problem = pulp.LpProblem("shortest_path", pulp.LpMinimize)
problem += pulp.lpDot(road_variables, road_lengths), 'Objective Function'

# constraints 
problem += pulp.lpSum(road_variables) == 7, 'Maximum of seven paths'

for l in locations:
    problem += pulp.lpSum([r for r in road_variables if l in str(r)]) <= 2, 'Appears at most twice_'+l
    problem += pulp.lpSum([r for r in road_variables if l in str(r)]) >= 1, 'Appears at least once_'+l
problem.solve(pulp.PULP_CBC_CMD(msg=0))
print(problem.objective.value())


# Part 2

# redefine linear optimization problem
problem = pulp.LpProblem("longest_path", pulp.LpMaximize)

# objective function and constraints remain the same
problem += pulp.lpDot(road_variables, road_lengths), 'Objective Function'
problem += pulp.lpSum(road_variables) == 7, 'Maximum of seven paths'

for l in locations:
    problem += pulp.lpSum([r for r in road_variables if l in str(r)]) <= 2, 'Appears at most twice_'+l
    problem += pulp.lpSum([r for r in road_variables if l in str(r)]) >= 1, 'Appears at least once_'+l

problem.solve(pulp.PULP_CBC_CMD(msg=0))
print(problem.objective.value())

