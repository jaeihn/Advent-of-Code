# 2015 - DAY 25 - LET IT SNOW
# https://adventofcode.com/2015/day/25


# PART 1 

row = 2978
col = 3083

row_start = 1
increment = 0

for i in range(0,row+col-1):
    row_start += increment
    increment += 1

idx = row_start+col-1

val = 20151125
mul = 252533
div = 33554393

for i in range(1, idx):
    val = val*mul%div

print(val)


# PART 2
