import pandas as pd
import re

input = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."
]

with open("Data/day3_input.txt") as f:
    input = f.read().splitlines()

sym = []
for x in input:
    for i in x:
        if i == ".":
            i = 0
        if str(i).isnumeric():
            pass
        else:
            sym = sym +[i]
sym = list(set(sym))

engine = [x for x in range(len(input))]

for l in range(len(input)):
    line = [re.sub(string=x,repl='#',pattern='[\@,\$,\-,\&,\=,\/,\%,\+,\*,\#]') for x in input[l]]
    engine[l] = line 

#loop through each element
# if an element is a number, add it to the current number.
# if the element is adjacent to a # then set the adj state to True
# if past element was numeric but current element is not numeric  
nums = list()
current_element = str()
past_element = str()
for i in range(len(engine)):
    adj_state = False
    current_number = ""
    upper = max(0,i-1)
    lower = min(len(engine)-1,i+1)
    
    for j in range(len(engine[i])):
        left = max(0,j-1)
        right = min(len(engine[i])-1,j+1)

        current_element = str(engine[i][j])
        past_element = str(engine[i][left])
                
        current_pos_adjacent = any(["#" in engine[upper][left:right+1], 
                    "#" in engine[i][left:right+1],
                    "#" in engine[lower][left:right+1]])
        
        if current_pos_adjacent and current_element.isnumeric():
            adj_state = True

        if current_element.isnumeric():
            current_number = str(current_number) + str(current_element)

        if not current_element.isnumeric() and adj_state == True and past_element.isnumeric():
            nums = nums + [current_number]
            print(current_number)
            adj_state = False
            current_number = ""
        
        elif not current_element.isnumeric() and adj_state == False and past_element.isnumeric():
            adj_state = False
            current_number = ""
sum([int(x) for x in nums])        

nums2 = [x for x in nums]
nums = list()
current_element = str()
past_element = str()

for i in range(len(engine)):
    adjacent_state = False
    current_number = ""
    upper = max(0,i-1)
    lower = min(len(engine)-1,i+1)

    for j in range(len(engine[i])):
        left = max(0,j-1)
        right = min(len(engine[i])-1,j+1)
        
        current_element = str(engine[i][j])
        
        past_element = str(engine[i][left])

        current_position_adjacent = any(['#' in engine[upper][left:right+1] + engine[i][left:right+1] + engine[lower][left:right+1]])
        # Turn on adjacency
        if adjacent_state == False and current_position_adjacent == True:
            adjacent_state = True

        if current_element.isnumeric():
            current_number = str(current_number) + str(current_element)
        elif not current_element.isnumeric() and past_element.isnumeric() and adjacent_state == True:
            nums = nums + [current_number]
            adjacent_state = False
            current_number = ""
        else:
            adjacent_state = False
            current_number = ""

i

pd.DataFrame(engine)
nums
nums2

sum([int(x) for x in nums])
nums
540324
543867 # works? why
545066

# so deep in the sauce that I was going to have to restart completely and hadn't touched for a week so figured cut my losses and keep moving. Might come back and re-try.
# Went down a deeply wrong path since I was able to replicate using the sample input, but it didnt' scale to the full one.

# I GAVE UP. BELOW is from a guy from reddit
# https://www.reddit.com/r/adventofcode/comments/189m3qw/comment/kbw3j89/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import re
from collections import defaultdict
from math import prod

data = input

with open("Data/day3_input.txt") as f:
    lines = f.read().split("\n")

# building symbols grid as {xy_position: symbol}
symbols = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            symbols[(x, y)] = c
symbols
# checking if a number has a rectangular neighborhood containing a symbol and
# building a gear grid as {gear_position: [part numbers list]}
gears = defaultdict(list)

part_numbers_sum = 0
for y, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        for (s_x, s_y), c in symbols.items():
            if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                num = int(match.group())
                part_numbers_sum += num
                if c == "*":
                    gears[(s_x, s_y)].append(num)
                break

# ========= PART 1 =========
print(part_numbers_sum)

# ========= PART 2 =========
print(sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2))