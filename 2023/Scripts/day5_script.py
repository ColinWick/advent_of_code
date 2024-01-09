import numpy as np

with open("Data/day5_test.txt") as f:
    input = f.read().splitlines()
    input = [i for i in input if i != '']


seeds = input[0]
seeds = seeds.split(" ")[1::]
seeds = [int(x) for x in seeds]
input = input[1::]

# Part 1 code
# create data structure for the maps
maps = dict()
map_nums = list()
for i in input:
    if i.find("to") > 0:
        # if it's the name of an instruction store it as a key
        map_name = str(i).replace(" map:","").replace("-to-","-")
        maps[map_name] = []
        map_nums = list()
    else:
        # if it's an instruction, store it in the most recent key
        maps[map_name] = maps[map_name] + [[int(x) for x in i.split(" ")]]
    
seed_to_loc = dict()
for input_seed in seeds:
    print(seeds.index(input_seed))
    seed_to_loc[input_seed] = list()
    current_seed = int(input_seed)
    for current_map_set in maps.keys():
        print(current_map_set) 
        source = list()
        destination = list()
        keys = maps[current_map_set]
        for current_map in keys:            
            source = range(current_map[1],current_map[1]+current_map[2])
            destination = range(current_map[0],current_map[0]+current_map[2])

            if len(source) != len(destination):
                print('len issues')
        
            if current_seed in source:
                current_seed = destination[source.index(int(current_seed))]
                break


        seed_to_loc[input_seed] = seed_to_loc[input_seed]+[current_seed]


seed_to_loc
my_minimum = int()

for x in seed_to_loc.keys():
    this_number = seed_to_loc[x][6]
    if my_minimum == 0 or my_minimum > this_number:
        my_minimum = this_number

my_minimum

# Part 2 code

all_seeds = list()
for i in range(len(seeds)):
    if i % 2 == 0:
        start = seeds[i]
        end = seeds[i]+seeds[i+1]
        all_seeds = all_seeds + [[start,end]]
all_seeds

mapped_formulas = dict()
formulas = list()
for x in maps.keys():
    mapped_formulas[x] = list()
    for i in range(len(maps[x])):
        current_map = maps[x][i]
        formula = [current_map[0]-current_map[1], current_map[1],current_map[1]+current_map[2]]
        # delta (add to input), input range start, input range end
        mapped_formulas[x] = mapped_formulas[x] + [formula]
    
current_seeds = [x for x in all_seeds]
next_seeds = current_seeds
for map_set in mapped_formulas:
    current_seeds = [x for x in next_seeds]
    next_seeds = list()
    for seed_list in current_seeds:
        seed_list.sort()
        seed_list = [int(x) for x in seed_list]
        for form in mapped_formulas[map_set]:
            form = [int(x) for x in form]
            print(seed_list)
            print(form)
            if seed_list[0] >= form[1] and seed_list[1] <= form[2]:
                next_seeds = next_seeds + [[seed_list[0] + form[0], seed_list[1] + form[0]]]
            elif seed_list[0] < form[1] and seed_list[1] <= form[2]:
                next_seeds = next_seeds + [[seed_list[0],form[1]-1]]
                next_seeds = next_seeds + [[form[1]+form[0],seed_list[1]+form[0]]]
            elif seed_list[0] >= form[1] and seed_list[1] > form[2]:
                next_seeds = next_seeds + [[seed_list[0],form[1]-1]]
                next_seeds = next_seeds + [[form[1]+form[0],seed_list[1]+form[0]]]
    