# 2015 - DAY 2 - I WAS TOLD THERE WOULD BE NO MATH
# https://adventofcode.com/2015/day/2

with open('inputs/day2.txt', 'r') as f:
    gifts = f.read().split()

# PART 1
def wrapper(gift):
    dimensions = [int(x) for x in gift.split('x')]
    l, w, h = dimensions

    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = l*w*h / max(dimensions)
    
    return int(surface_area+slack)

print(sum([wrapper(gift) for gift in gifts]))


# PART 2

def ribbon(gift):
    dimensions = [int(x) for x in gift.split('x')]
    l, w, h = dimensions 

    perimeter = 2*(l+w+h - max(dimensions))
    bow = l*w*h

    return int(perimeter+bow)

print(sum([ribbon(gift) for gift in gifts]))