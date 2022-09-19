# 2015 - DAY 12 - JSAbacusFramework.io
# https://adventofcode.com/2015/day/12

import os
import regex
import json
with open(os.path.dirname(__file__)+'/inputs/day12.txt', 'r') as f:
    data = f.read()
f.close()


# PART 1

def docsum(input):
    sum = 0
    for num in regex.findall(r'-?\d+', input):
        sum += int(num)
    return sum

print(docsum(data))


# PART 2

json_data = json.loads(data)

def nored_sum(jlist):
    sum = 0

    for x in jlist:
        if type(x)==dict:
            if 'red' in x.values():
                sum += 0
            else:
                sum += nored_sum(list(x.values()))
        if type(x) is list:
            sum += nored_sum(x)
        if type(x)==int:
            sum += x
    
    return sum 


print(nored_sum(json_data))