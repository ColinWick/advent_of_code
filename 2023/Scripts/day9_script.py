hist = ["0 3 6 9 12 15",
"1 3 6 10 15 21",
"10 13 16 21 30 45"]
hist = [[int(x) for x in h.split(" ")] for h in hist]

with open("Data/day9_input.txt") as f:
    data = f.read().splitlines()
    hist = [[int(x) for x in h.split(" ")] for h in data]


i = 1
mylist = hist[0]
def take_diff(mylist):
    while True:
        all_diffs = list()
        diffs = list()
        for i in range(1,mylist.__len__()):
            num = mylist[i] - mylist[i-1]
            diffs = diffs + [num]

        return diffs


extrap = list()
extrap_back = list()
for l in hist:
    l = [l]
    r = 0
    while True:
        
        if r == 0:
            diff = take_diff(l[0])
        else: 
            diff = take_diff(diff)

        l = l + [diff]

        if all([x == 0 for x in diff]):
            break
        else:
            r += 1
    extrap = extrap + [sum([x[-1] for x in l])]

    # Part 2
    left_end = [x[0] for x in l][::]
    quiet = left_end.pop()
    new_val = [0]

    while left_end:
        new_val = new_val + [left_end.pop() - new_val[-1]]
    extrap_back = extrap_back + [new_val[-1]]

sum(extrap)
sum(extrap_back)


