# 2015 - DAY 7 - SOME ASSEMBLY REQUIRED
# https://adventofcode.com/2015/day/7

import os

with open(os.path.dirname(__file__)+ '/inputs/day7.txt', 'r') as f:
     instructions = f.read().split('\n')
f.close()

# Part 1 
def find(w, instructs):
    ins = []

    for i in range(len(instructs)):
        ins.append(instructs[i].split())

    ins = [x for x in ins if x!=[]]

    sorted_ins = []
    defined = set()

    while w not in defined:

        check = ins[0][-1]
        to = ins[0].index('->')

        if len(ins[0])==3 and ins[0][0].isdigit():
            sorted_ins.insert(0,ins[0])
            defined.add(check)
            ins.pop(0)
            continue
        
        inputs = [x for x in ins[0][:to] if x.islower()]

        if set(inputs).issubset(defined):
            sorted_ins.append(ins[0])
            ins.pop(0)
            defined.add(check)
        else:
            ins.append(ins[0])
            ins.pop(0)
    
    # following instructions to assign value
    wires = {}
    while w not in wires:

        b = sorted_ins.pop(0)
        sorted_ins.append(b)

        if 'AND' in b:
            if b[0].isdigit():
                wires[b[-1]] = int(b[0]) & wires[b[2]]
            elif b[2].isdigit():
                wires[b[-1]] = wires[b[0]] & int(b[2]) 
            else:
                wires[b[-1]] = wires[b[0]] & wires[b[2]]
        elif 'OR' in b:
            if b[0].isdigit():
                wires[b[-1]] = int(b[0]) | wires[b[2]]
            elif b[2].isdigit():
                wires[b[-1]] = wires[b[0]]| int(b[2])
            else:
                wires[b[-1]] = wires[b[0]] | wires[b[2]]
        elif 'RSHIFT' in b:
            wires[b[-1]] = wires[b[0]] >> int(b[2])
        elif 'LSHIFT' in b:
            wires[b[-1]] = wires[b[0]] << int(b[2])
        elif 'NOT' in b:
            wires[b[-1]] = ~wires[b[1]]   
        elif b[0] in wires:
            wires[b[-1]] = wires[b[0]]
        else:
            wires[b[-1]] = int(b[0])
    # return value 
    return wires[w]

print(find('a', instructions))


# Part 2

override_b = find('a', instructions)
override_ins = [x for x in instructions if not x.endswith(' b')]
override_ins.append(str(override_b)+' -> b')

print(find('a', override_ins))