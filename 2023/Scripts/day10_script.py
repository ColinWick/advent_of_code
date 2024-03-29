import pandas as pd

loop = ["FF7FSF7F7F7F7F7F---7",
"L|LJ||||||||||||F--J",
"FL-7LJLJ||||||LJL-77",
"F--JF--7||LJLJIF7FJ-",
"L---JF-JLJIIIIFJLJJ7",
"|F|F-JF---7IIIL7L|7|",
"|FFJF7L7F-JF7IIL---7",
"7-L-JL7||F7|L7F-7F7|",
"L.L7LFJ|||||FJL7||LJ",
"L7JLJL-JLJLJL--JLJ.L"]
#with open('Data/day10_input.txt') as f:
#    loop = f.read().splitlines()

loop = [[x for x in j] for j in loop]

for i in range(len(loop)):
    for j in range(len(loop[i])):
        if loop[i][j] == "S":
            start = [i,j]


def bound(ind,dir,*max):
    m = int(max[0]) if max else 0
    if dir in ['up','left']:
        x = 0 if ind-1 < 0 else ind-1
    if dir in ['down','right']:
        x = m if ind+1 >= m else ind+1
    return x

def possible_moves(loop,i,j):
    moves = list()
    if loop[i][j] in ['|','L','J','S'] and loop[bound(i,'up',0)][j] in ['|','7','F']:
        moves = moves + [[-1,0]]
    if loop[i][j] in ['|','7','F','S'] and loop[bound(i,'down',len(loop))][j] in ['|','L','J']:
        moves = moves + [[1,0]]
    if loop[i][j] in ['-','L','F','S'] and loop[i][bound(j,'right',len(loop[i]))] in ['-','J','7']:
        moves = moves + [[0,1]]
    if loop[i][j] in ['-','7','J','S'] and loop[i][bound(j,'left',0)] in ['-','L','F']:
        moves = moves + [[0,-1]]
    
    return moves

def manhattan_distance(start_i = 0, start_j = 0, i = 0, j = 0):
    x = (i - start_i)
    y = (j - start_j)
    d = x + y
    return d

steps = 0
passed = [['.' for j in x] for x in loop]
md = [['.' for j in x] for x in loop]
i1 = start[0]
i2 = start[0]
j1 = start[1]
j2 = start[1]

# track moves in part 2
moves = []
pd.DataFrame(passed)
while True:
    passed[i1][j1] = steps
    passed[i2][j2] = steps

    md[i1][j1] = manhattan_distance(start[0],start[1],i1,j1)
    #md[i2][j2] = manhattan_distance(start[0],start[1],i2,j2)

    m1 = possible_moves(loop,i1,j1)
    #m2 = possible_moves(loop,i2,j2)
    
    if passed[i1 + m1[0][0]][j1 + m1[0][1]] == '.':
        i1 += m1[0][0]
        j1 += m1[0][1]
    else:
        i1 += m1[1][0]
        j1 += m1[1][1]
    
    #if passed[i2 + m2[0][0]][j2 + m2[0][1]] == '.':
    #    i2 += m2[0][0]
    #    j2 += m2[0][1]
    #else:
    #    i2 += m2[1][0]
    #    j2 += m2[1][1]
    
    

    if passed[i1][j1] != ".":
        break


    steps += 1
    
# Part 1    
(steps + 1) / 2

# Part 2 is a dykstrjas
# Update: PART 2 is NOT a dykstras. Original code below
passed




















if False:
    passed
    i = 0 
    j = 0

    # At first thought a simple walk would do it, but the algo fails if the network touches a boundary point. instead, plugging the entire boundary in
    #points = [[i,j]]
    width = len(passed[0])-1
    height = len(passed)-1
    points = [[i,0] for i in range(height)] + [[i,width] for i in range(height)] + [[0,j] for j in range(width)] + [[height,j] for j in range(width)] 

    while points:
        # Current point we are checking
        i = points[0][0]
        j = points[0][1]
        
        # Create 4 coordinates for points around our current position using bound helper
        i1 = bound(i,'up',0)
        i2 = bound(i,'down',len(passed)-1)
        j1 = bound(j,'left',0)
        j2 = bound(j,'right',len(passed[0])-1)

        # Check state of each adjacent point and update data holding
        if passed[i1][j] == '.':
            points = points + [[i1,j]]
            passed[i1][j] = 'X'
        
        if passed[i2][j] == '.':
            points = points + [[i2,j]]
            passed[i2][j] = 'X'
        
        if passed[i][j1] == '.':
            points = points + [[i,j1]]
            passed[i][j1] = 'X'

        if passed[i][j2] == '.':
            points = points + [[i,j2]]
            passed[i][j2] = 'X'

        # Bump top point from the list. We only add a point to the list if it isn't an "X"  so this list will always be finite
        points = points[1::]

        # break if i or j get too large for some crazy reason. 
        # REAL break condition comes when there are no points in list 
        if i > len(passed) or j > len(passed[0]):
            break

    counter = 0
    for i in passed:
        for j in i:
            if j == '.':
                counter += 1

    pd.DataFrame(passed).iloc[50:100,110::]


    import pandas as pd

loop = ["FF7FSF7F7F7F7F7F---7",
"L|LJ||||||||||||F--J",
"FL-7LJLJ||||||LJL-77",
"F--JF--7||LJLJIF7FJ-",
"L---JF-JLJIIIIFJLJJ7",
"|F|F-JF---7IIIL7L|7|",
"|FFJF7L7F-JF7IIL---7",
"7-L-JL7||F7|L7F-7F7|",
"L.L7LFJ|||||FJL7||LJ",
"L7JLJL-JLJLJL--JLJ.L"]
#with open('Data/day10_input.txt') as f:
#    loop = f.read().splitlines()

loop = [[x for x in j] for j in loop]

for i in range(len(loop)):
    for j in range(len(loop[i])):
        if loop[i][j] == "S":
            start = [i,j]

def bound(index,direction,m):
    if direction == 'L':
        index = max(index-1,0)
    elif direction == 'U':
        index = max(index-1,0)
    if direction == 'R':
        index = min(index+1,m)
    elif direction == 'D':
        index = min(index+1,m)
    
    return index

def move_logic(loop,i,j):
    moves = list()
    if loop[i][j] in ['|','L','J','S'] and loop[bound(i,'up',0)][j] in ['|','7','F']:
        moves = moves + [[-1,0]]
    if loop[i][j] in ['|','7','F','S'] and loop[bound(i,'down',len(loop))][j] in ['|','L','J']:
        moves = moves + [[1,0]]
    if loop[i][j] in ['-','L','F','S'] and loop[i][bound(j,'right',len(loop[i]))] in ['-','J','7']:
        moves = moves + [[0,1]]
    if loop[i][j] in ['-','7','J','S'] and loop[i][bound(j,'left',0)] in ['-','L','F']:
        moves = moves + [[0,-1]]
    
    return moves

def manh_dist(i0 = 0, j0 = 0, i1 = 0, j1 = 0):
    x = (i1 - i0)
    y = (j1 - j0)
    d = abs(x + y)
    return d

steps = 0
step_log = [['.' for j in x] for x in loop]