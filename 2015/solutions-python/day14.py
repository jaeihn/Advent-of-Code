# 2015 - DAY 14 - REINDEER OLYMPICS
# https://adventofcode.com/2015/day/14

import os
import regex
import json
with open(os.path.dirname(__file__)+'/inputs/day14.txt', 'r') as f:
    data = f.read().split('\n')
f.close()


# PART 1

def distance(speed, sprint, rest, time):
    cycle = speed*sprint 
    remainder = time%(sprint+rest)

    dist = int(time/(sprint+rest))*cycle

    if remainder <= sprint:
        dist += remainder*speed
    else:
        dist += cycle
    
    return dist 


def race(rdata, time):
    records = []
    reindeers = [d.split() for d in rdata if d]

    for r in reindeers:
        speed, sprint, rest = [int(i) for i in r if i.isdigit()]
        records.append(distance(speed,sprint,rest,time))

    return max(records)


print(race(data,2503))



# PART 2



def pointrace(rdata, time):

    reindeers = [d.split() for d in rdata if d]
    points = [0]*len(reindeers)

    for t in range(1,time+1):
        records = []

        for r in reindeers:
            speed, sprint, rest = [int(i) for i in r if i.isdigit()]
            records.append(distance(speed,sprint,rest,t))

        for i in range(len(records)): 
            if records[i]==max(records):
                points[i]+=1
    return max(points)


print(pointrace(data,2503))