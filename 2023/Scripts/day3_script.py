import pandas as pd
import re

test = [
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

def adjacent(mat,i,j):
    mat.iloc[i-1:i+2,j-1:j+2] = True
    


engine = [x for x in range(len(test))]
numer = [x for x in range(len(test))]
adj = numer

for l in range(len(test)):
    line = [re.sub(string=x,repl='#',pattern='[\+]|[\^]|[\*]|[\$]|[\?]') for x in test[l]]
    engine[l] = line 
    numer[l] = [str(x).isnumeric() for x in line]
    adj[l] = [False for x in line]


for i in range(len(test)):
    for j in range(len(test[l])):
        if test[i][j] == "#":
            adj[i-1][j-1,j,j+2] = True
            adj[i][j-1:j+2] = True
            adj[i+1][j-1:j+2] = True
            
[j-1:j+2]






