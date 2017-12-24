import player
import deck
from random import randint

class HeadsUpGame(object):
    """docstring for HeadsUpGame."""
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.table = []

    def getRandomCard(self):
        card = self.deck.deck[randint(0, self.deck.deck.__len__() - 1)]
        self.deck.deck.remove(card)
        return card

    def getTable(self):
        return self.table

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

    def dealCards(self):
        self.player1.setBothCards(self.getRandomCard(), self.getRandomCard())
        self.player2.setBothCards(self.getRandomCard(), self.getRandomCard())

    def dealFlop(self):
        for i in range(0,3):
            self.table.append(self.getRandomCard())

    def dealRiver(self):
        self.table.append(self.getRandomCard())

    def dealTurn(self):
        self.table.append(self.getRandomCard())

    def showTable(self):
        for i in self.table:
            i.showCard()

    def showHandCards(self):
        self.player1.showCards()
        print('==')
        self.player2.showCards()
