input = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

with open("Data/day1_input.txt") as f:
    input = f.read().splitlines()

def grab_number(item,which_side):
    list = [x for x in item if str(x).isnumeric()]
    if which_side == 'front':
        out = str(list[0])
    else:
        out = str(list[-1])
    return out

def replace_digits(item):
    numdict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

    mylen = len(item)+1
    
    for l in range(0,mylen):
        test = item[0:l] 
        for d in numdict.keys():
            test = test.replace(d,numdict[d])
        a = [x for x in test if str(x).isnumeric()]
        if a:
            a[0]
            break        
        
    for l in range(0,mylen):
        test = item[mylen-l-1:mylen] 
        for d in numdict.keys():
            test = test.replace(d,numdict[d])
        b = [x for x in test if str(x).isnumeric()]
        if b:
            b[-1]
            break       

    return str(a[0]) + str(b[-1])

mysum = 0 
for i in range(len(input)):
    print(input[i])
    item = replace_digits(input[i])

    print(item)
    mysum += int(item)

mysum