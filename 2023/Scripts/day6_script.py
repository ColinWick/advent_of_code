import pandas as pd 
import numpy as np

with open('2023/Data/day6_input.txt') as d:
    data = d.readlines()
    time = data[0]
    dist = data[1]

#time = "Time:      7  15   30"
#time = [int(x) for x in time.split(" ")[1::] if x != '']
time = int(time.replace(" ","").split(":")[1])
60808676 
#dist = "Distance:  9  40  200"
#dist = [int(x) for x in dist.split(" ")[1::] if x != '']
dist = int(dist.replace(" ","").split(":")[1])
601116315591300

def distance_travelled(hold_val,total_time_val):
    x = hold_val * (total_time_val - hold_val)
    return x

def races(total_time,record):
    counter = 0
    hold = 0
    while hold < total_time:
        hold += 1
        travel = distance_travelled(hold_val = hold, total_time_val = total_time)
        if travel > record:
            counter += 1
        
    return counter

# Part 1
prod = 1
for i in range(len(time)):
    prod *= races(time[i],dist[i])
prod

# Part 2
# This will break your computer - 
    # races(total_time=time,record=dist)

# Analytic solution?
a = 1
b =  -time
c = dist

hi = (-b + (b**2 - 4 * a * c) ** 0.5) / 2
lo = (-b - (b**2 - 4 * a * c) ** 0.5) / 2

np.round(hi - lo)
