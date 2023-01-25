# Tyler Johnson
# 1/19/2023
# Black Jack
import random
from cards_file import *
from player_file import *

def main():
    deck = Base_Deck("Steve")
    deck.populate()
    deck.shuffle()
    tim = Base_Hand("tim")
    joe = Base_Hand("joe")
    players = [tim,joe]
    deck.deal(players,len(deck.cards)//len(players))

    print(tim.name)
    print(len(tim.cards))
    tim.cards[0].flip()
    print(tim.cards[0])

    print(joe.name)
    print(len(joe.cards))
    joe.cards[0].flip()
    print(joe.cards[0])



main()


