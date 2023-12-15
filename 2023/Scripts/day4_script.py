import re

input =[
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]


with open("Data/day4_input.txt") as f:
    input = f.read().splitlines()

data = dict()

for x in enumerate(input):
    sides = re.split(":",x[1])[1].split("|")
    winner = [x for x in sides[0].split(" ") if x != ""]
    myside = [x for x in sides[1].split(" ") if x != ""]
    overlap = [m for m in myside if m in winner]
    
    if overlap == []:
        score = 0
    else:
        score = 2 ** (len(overlap)-1)
    
    data[x[0]] = [winner,myside,overlap,score]

sum = 0
for a in data.keys():
    sum += data[a][3]

sum

# Part 2 
counts = dict()
for x in data.keys():
    counts[x] = 1
card_defs = data

for x in counts.keys():
    overlap = card_defs[x][2]
    overlap
    if card_defs[x] != '':
        for y in range(1,len(overlap)+1):
            counts[x+y] += 1 * counts[x]
            y

mysum = 0
for x in counts.items():
    mysum += x[1]

mysum
