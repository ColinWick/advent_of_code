import pandas as pd 
import numpy as np

hand_string = "32T3K"

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
        myhand.sort()
        return myhand



    

def compare_hands(h1,h2):
    
    return win_state

class hand():
    def __init__(self, hand_string, bid) -> None:
        self.hand_string = hand_string
        self.cards = define_cards(self.hand_string)
        self.power_level(self.cards)
        self.bid = int(bid)

    def __str__(self) -> str:
        self.hand_string

first_hand = hand(hand_string,100)


def power_level_5_card(cards):
    first_hand.cards,[first_hand.cards.count(x) for x in first_hand.cards]

    if len(np.unique(first_hand.cards)) == 1: # 5 set
        return 7
    elif len(np.unique(first_hand.cards)) == 1: # 4 set
        return 6
    elif len(np.unique(first_hand.cards)) == 1: # 4 set
        return 6


    5 # boat
    4 # threekind
    3 # two pair
    2 # pair
    1 # high_card
