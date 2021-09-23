# 2015 - DAY 1 - NOT QUITE LISP
# https://adventofcode.com/2015/day/1

with open('inputs/day1.txt', 'r') as f:
    input = f.read()

# PART 1
print(len(input) - 2*(list(input).count(')')))

# PART 2
floor = 0

for i in range(len(input)):
    if floor==-1:
        print(i)
        break
    elif input[i]=='(':
        floor+=1
    elif input[i]==')':
        floor-=1
