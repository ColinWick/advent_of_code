import re
import pandas as pd

with open("Data/day2_input.txt") as f:
    input = f.read().splitlines()

#input = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#         'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#         'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#         'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#         'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

def extract_color(game_draws,color):
    color_count = 0
    colors = re.findall("[0-9]* "+color,game_draws)
    for c in colors:
        for num in re.findall('[0-9]*',c):
            if num != "":
                color_count += int(num)
    return color_count

bgr = pd.DataFrame(columns=['game','draw','blue','green','red'])

for i in range(len(input)):
    draws = input[i].split(";")
    for d in range(len(draws)):
        current_game = {'game':i,'draw':d,'blue':extract_color(draws[d],'blue'),'green':extract_color(draws[d],'green'),'red':extract_color(draws[d],'red')}
        current_game = pd.DataFrame(current_game,index=[0])
        bgr = pd.concat([bgr,current_game]).reset_index(drop=True)

# part 1
failed_games = (
    bgr
    .query("blue > 14 | green > 13 | red > 12")
    )['game']


successful_games = (
    bgr
    .query('game not in @failed_games')
    ['game']
    .unique()
)

sum(successful_games + 1)

# part 2
(
    bgr
    .groupby(['game'])['red','green','blue']
    .max()
    .assign(power = lambda x: x['red'] * x['green'] * x['blue'] )
    .agg({'power':'sum'})
)
bgr