# 2015 - DAY 10 - ELVES LOOK, ELVES SAY
# https://adventofcode.com/2015/day/10


input = "1321131112"


######## VERSION 1 ########

def group(input):

    separated = [i for i in input]
    grouped = [input[0]]

    for i in range(1,len(separated)):
        if separated[i]==separated[i-1]:
            grouped[-1] = grouped[-1]+separated[i]
        else:
            grouped.append(separated[i])

    return grouped


def look(groups):

    say = ""
    for g in groups:
        say += str(len(g))+g[0]
    return say


import time
start = time.time()

# PART 1

for i in range(40):    
    input = look(group(input))

print(len(input))


# PART 2

for i in range(10):    
    input = look(group(input))

print(len(input))


end = time.time()
print(end - start)


######### VERSION 2 (Faster) ##########

input = "1321131112"

def look(input):

    input = [i for i in input]

    say = ['1', input.pop(0)]

    for i in input:
        if i==say[-1]:
            say[-2]= str(int(say[-2])+1)
        else:
            say += ['1', i]

    return say


start = time.time()

# PART 1 
for i in range(40):    
    input = look(input)

print(len(input))

# PART 2

for i in range(10):    
    input = look(input)

print(len(input))

end = time.time()
print(end - start)