import deck

class Player(object):
    """docstring forPlayer."""
    def __init__(self):
        self.card1 = 0
        self.card2 = 0

    #setters
    def setCard1(self, card):
        self.card1 = card

    def setCard2(self, card):
        self.card2 = card

    def setBothCards(self, card1, card2):
        self.setCard1(card1)
        self.setCard2(card2)

    #getters
    def getCard1(self):
        return self.card1

    def getCard2(self):
        return self.card2

    def getBothCards(self):
        return (self.getCard1(), self.getCard2())

    def getBothCards_list(self):
        return [self.getCard1(), self.getCard2()]

    #other methods
    def showCards(self):
        for i in self.getBothCards():
            i.showCard()
