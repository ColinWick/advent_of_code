import pandas as pd 
import numpy as np

dealt = ["32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"]

with open("Data/day7_input.txt") as d:
    data = d.readlines()

dealt = [[x.split(" ")[0],int(x.split(" ")[1])] for x in dealt]
dealt = [[x.split(" ")[0],int(x.split(" ")[1])] for x in data]

def convert(x):
    if x.isdigit():
        return int(x)
    elif x == "T":
        return 10
    elif x == "J":
        return 11
    elif x == "Q":
        return 12
    elif x == "K":
        return 13
    elif x == "A":
        return 14

def define_cards(hand_string):    
        myhand = [convert(x) for x in hand_string]
        return myhand

def power_level(cards):
#    cards = define_cards('KK677')
    hand_size = len(cards)
    counts = [cards.count(x) for x in cards]
    unique_cards = [x for x in set(cards)]
    unique_cards.sort()

    if 5 in counts: # 5 set
        ranking = 7
    elif 4 in counts: # 4 set
        ranking = 6
    elif 3 in counts and 2 in counts: # 3 of a kind
        ranking = 5
    elif 3 in counts: # 2 pair
        ranking = 4
    elif len([x for x in counts if x == 2]) == 4: # BUG HERE
        ranking = 3
    elif len([x for x in counts if x == 2]) == 2: # BUG HERE
        ranking = 2
    else:
        ranking = 1

    return ranking


    
class hand():
    def __init__(self, hand_string, bid) -> None:
        self.hand_string = hand_string
        self.cards = define_cards(self.hand_string)
        self.power_ranking = power_level(self.cards)
        self.bid = int(bid)

card_cols = ['cards','bid','power_ranking','c1','c2','c3','c4','c5']
hand_df = pd.DataFrame()
for deal in dealt:
    current_hand = hand(deal[0],deal[1])
    current_hand_data = [current_hand.hand_string] + [current_hand.bid, current_hand.power_ranking] + current_hand.cards
    hand_df = pd.concat([hand_df,pd.DataFrame(current_hand_data).T])

hand_df.columns = card_cols

# Rank hands
hand_df = hand_df.sort_values(by=['power_ranking','c1','c2','c3','c4','c5'],ascending=True)
#hand_df = hand_df.sort_values(by=[],ascending=True)
ranks = [x + 1 for x in range(0,len(dealt))]
hand_df = hand_df.assign(ranking=ranks)
hand_df['score'] = hand_df.bid * hand_df.ranking

hand_df['score'].agg(sum)