from random import randint

values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
colours = ['H','C','S','D']

class Card:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour
        self.pos = values.index(value)

    def showCard(self):
        print(self.value, self.colour)

class Deck:
    def __init__(self):
        self.values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.colour = ['H','C','S','D']
        self.deck = []
        for i in values:
            for j in colours:
                self.deck.append(Card(i,j))

    def getCard(self, col, val):
        for i in self.deck:
            if i.val == val and i.col == col:
                return i
        print('col or val where of wrong format')

    def showDeck(self):
        for i in self.deck:
            print(i.showCard)
