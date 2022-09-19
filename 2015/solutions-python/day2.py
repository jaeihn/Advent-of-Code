# 2015 - DAY 2 - I WAS TOLD THERE WOULD BE NO MATH
# https://adventofcode.com/2015/day/2

import os

with open(os.path.dirname(__file__)+'/inputs/day2.txt', 'r') as f:
    gifts = f.read().split()
f.close()


# PART 1
def wrapper(gift):
    l, w, h = [int(x) for x in gift.split('x')]

    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = l*w*h / max(l,w,h)

    return int(surface_area+slack)

print(sum([wrapper(gift) for gift in gifts]))



# PART 2

def ribbon(gift):
    l, w, h = [int(x) for x in gift.split('x')]

    perimeter = 2*(l+w+h - max(l,w,h))
    bow = l*w*h

    return int(perimeter+bow)

print(sum([ribbon(gift) for gift in gifts]))