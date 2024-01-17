import numpy as np
import math 

input = ["LLR","AAA = (BBB, BBB)","BBB = (AAA, ZZZ)","ZZZ = (ZZZ, ZZZ)"]

input = ['LR','11A = (11B, XXX)','11B = (XXX, 11Z)','11Z = (11B, XXX)','22A = (22B, XXX)','22B = (22C, 22C)','22C = (22Z, 22Z)','22Z = (22B, 22B)','XXX = (XXX, XXX)']
with open("Data/day8_input.txt") as f:
    input = f.read().splitlines()

directions = input[0]
nodelist = input[1::]

directions = [int(x) for x in directions.replace("L","0").replace("R","1")]
nodelist = [x.replace('(',"").replace(')',"").split(" = ") for x in nodelist if x != '']

nodes = dict()
for i in nodelist:
    nodes[i[0]] = i[1].split(", ")

i = 0 # direction iterator
j = 0 # total steps
node = 'AAA'
while node != 'ZZZ' and j < 1000000:
    node = nodes[node][directions[i]]
    j += 1    
    if i == len(directions)-1:
        i = 0
    else:
        i += 1

j

# Part 2
all_end_A = [x for x in nodes.keys() if x[2] == "A"]
all_end_Z = [x for x in nodes.keys() if x[2] == "Z"]


y = []

for a in all_end_A:
    i = 0
    j = 0
    steps = 0
    node = a
    while True:
        new_node = nodes[node][directions[i]]
        i = 0 if i >= len(directions) - 1 else i+1 
        j += 1
        node = new_node
        if node[2] == 'Z':
            y.append(j)
            break

y