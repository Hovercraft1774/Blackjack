


import tkinter



class Base_Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♠","♣","❤","♦"]



    def __init__(self, rank, suit): #below is a doc string, similar to comment, but can be called and shown to explain help.
        """Constructor this is called to Build an object from this class"""
        self.isFaceUp = False
        self.rank = rank
        self.suit = suit



    def __str__(self):
        """returns a string rep of the object"""
        ret = ""
        if self.isFaceUp:
            ret = str.format("""
                     ----------
                    |{0:2}{1}      |
                    |          |
                    |          |
                    |          |
                    |     {1} {0:2}|
                     ----------
                    """, self.rank,self.suit)
        else:
            ret = """
                     ----------
                    | ~~~~~~~~ |
                    | ^  /\\    |
                    | v  <>  ^ |
                    |    \\/  v |
                    | ~~~~~~~~ |
                     ----------
                    """

        return ret

    def flip(self):
        """Toggle the isFaceUp bool value"""
        self.isFaceUp = not self.isFaceUp


    @property
    def value(self):
        if self.isFaceUp:
            return Base_Card.RANKS.index(self.rank)+1
        else:
            return 0











if __name__ == "__main__":
    print("This is not a program, Try importing and using the classes")
    input("\n\n Press Enter to Exit")

