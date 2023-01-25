from player_file import *




class BlackJack_Deck(Base_Deck):
    def populate(self):
        for suit in BlackJack_Card.SUITS:
            for rank in BlackJack_Card.RANKS:
                card = BlackJack_Card(rank, suit)
                self.cards.append(card)

class BlackJack_Card(Base_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isFaceUp:
            val = BlackJack_Card.RANKS.index(self.rank)+1
            if val > 10:
                val = 10
        else:
            val = None

        return val

class BlackJack_Hand(Base_Hand):

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        #add up card values and treat each ace as a 1
        t = 0
        for card in self.cards:
            t += card.value

        have_ace = False
        for card in self.cards:
            if card.value == BlackJack_Card.ACE_VALUE:
                have_ace = True
            if have_ace and t<=11:
                t+= 10

    def __str__(self):
        ret = Base_Hand.__str__(self)+"\n"
        ret += self.name+"\n"
        ret += str(self.total)

        return ret

    def is_busted(self):
        return self.total>21

    def flipHand(self):
        for card in self.cards:
            card.isFaceUp = True


class BlackJack_Player(BlackJack_Hand):

    def is_hitting(self):
        response = ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def lose(self):
        print(self.name,"loses")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")
    def bust(self):
        print(self.name, "busts.")
        self.lose()


class BlackJack_Dealer(BlackJack_Hand):
    def is_hitting(self):
        pass


    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

