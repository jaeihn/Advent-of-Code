# 2015 - DAY 7 - SOME ASSEMBLY REQUIRED
# https://adventofcode.com/2015/day/7

import os

with open(os.path.dirname(__file__)+ '/inputs/day7.txt', 'r') as f:
     instructions = f.read().split('\n')
f.close()

# Part 1 
def find(w, instructs):

    # split instructions
    ins = []

    for i in range(len(instructs)):
        ins.append(instructs[i].split())

    ins = [x for x in ins if x!=[]]

    # sort instructions
    sorted_ins = []
    defined = set()

    while w not in defined:

        check = ins[0][-1]

        if len(ins[0])==3 and ins[0][0].isdigit():
            sorted_ins.insert(0,ins[0])
            defined.add(check)
            ins.pop(0)
            continue
        
        inputs = [x for x in ins[0][:-2] if x.islower()]

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

        inst = sorted_ins.pop(0)

        if 'AND' in inst:
            if inst[0].isdigit():
                wires[inst[-1]] = int(inst[0]) & wires[inst[2]]
            elif inst[2].isdigit():
                wires[inst[-1]] = wires[inst[0]] & int(inst[2]) 
            else:
                wires[inst[-1]] = wires[inst[0]] & wires[inst[2]]
        elif 'OR' in inst:
            if inst[0].isdigit():
                wires[inst[-1]] = int(inst[0]) | wires[inst[2]]
            elif inst[2].isdigit():
                wires[inst[-1]] = wires[inst[0]]| int(inst[2])
            else:
                wires[inst[-1]] = wires[inst[0]] | wires[inst[2]]
        elif 'RSHIFT' in inst:
            wires[inst[-1]] = wires[inst[0]] >> int(inst[2])
        elif 'LSHIFT' in inst:
            wires[inst[-1]] = wires[inst[0]] << int(inst[2])
        elif 'NOT' in inst:
            wires[inst[-1]] = ~wires[inst[1]]   
        elif inst[0] in wires:
            wires[inst[-1]] = wires[inst[0]]
        else:
            wires[inst[-1]] = int(inst[0])
    # return value 
    return wires[w]

print(find('a', instructions))


# Part 2

override_b = find('a', instructions)
override_ins = [x for x in instructions if not x.endswith(' b')]
override_ins.append(str(override_b)+' -> b')

print(find('a', override_ins))