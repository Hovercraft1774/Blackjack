import random
from cards_file import *
class Base_Hand():



    def __init__(self,name):
        self.cards = []
        self.name = name

    def add_card(self, card):
        self.cards.append(card)

    def give_card(self,card, other_hand):
        self.cards.remove(card)
        other_hand.add_card(card)

    def flip_all(self):
        for card in self.cards:
            card.flip()

    def clear_hand(self):
        self.cards = []

    def __str__(self):
        ret = ""
        if self.cards:
            for card in self.cards:
                ret += str(card)

        else:
            ret = "<EMPTY>"

        return ret

class Base_Deck(Base_Hand):

    def populate(self):
        for suit in Base_Card.SUITS:
            for rank in Base_Card.RANKS:
                card = Base_Card(rank, suit)
                self.cards.append(card)


    def shuffle(self):
        import random
        random.shuffle(self.cards)


    def deal(self,hands_list,per_hand = 1):
        cards_needed = len(hands_list)*per_hand
        if(self.amount >= cards_needed):
            for rounds in range(per_hand):
                for hand in hands_list:
                    top_card = self.cards[0]
                    self.give_card(top_card,hand)
        else:
            for hand in hands_list:
                hand.clear_hand()
            self.clear_hand()
            self.populate()
            self.shuffle()
            self.deal(hands_list,per_hand)


    @property
    def amount(self):
        return len(self.cards)



if __name__ == "__main__":
    print("This is not a program, Try importing and using the classes")
    input("\n\n Press Enter to Exit")

