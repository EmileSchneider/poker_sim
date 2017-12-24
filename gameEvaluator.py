from random import randint

class Evaluator(object):
    """docstring for Evaluator."""
    def __init__(self, table, player):
        self.table = table
        self.player = player
        self.cards = []
        self.results = ''

    def sortCards(self):
        sorting = []
        for i in self.table:
            sorting.append(i)
        for i in self.player.getBothCards_list():
            sorting.append(i)

        while sorting.__len__() > 0:
            sort = sorting[0]
            for i in sorting:
                if i.pos > sort.pos:
                    sort = i
            self.cards.append(sort)
            sorting.remove(sort)

    def checkHighCard(sef):
        pass

    def checkRoyalFlush(self):
        self.sortCards()
        work_list = self.cards[0:5]
        colour_list = []
        for i in work_list:
            colour_list.append(i.colour)

        print(colour_list)
        print(colour_list[randint(0, colour_list.__len__() - 1)])
        print(type(colour_list[randint(0, colour_list.__len__() - 1)]))
        print('==')
        print(all(colour_list) == colour_list[randint(0, colour_list.__len__() - 1)])

        #why does this not equal to true WTF man WTF
        if not all(colour_list) == colour_list[randint(0, colour_list.__len__() - 1)]:
            pass
            #print("FALSE")

        value_list = []
        for i in work_list:
            value_list.append(i.value)

        if not value_list[0] == 'A':
            print("FALSE")
        else:
            print("is a royal flush")

    def checkStraightFlush(self):
        self.sortCards()
        colour_counter = 0
        cards = []
        for i in self.cards:
            for j in self.cards:
                if i.colour == j.colour and i.value != j.value:
                    colour_counter += 1
                    cards.append(i)
        if colour_counter < 5:
            print('not a straight flush')

        value_counter = 0
        for i in cards:
            if i.pos - cards[cards.index(i) + 1 == 1:
                value_counter = value_counter + 1
        if value_counter != 5:
            print('not a straight flush')

    def checkFourOfAKind(self):
        self.sortCards()
        counter = 0
        for i in self.cards:
            for j in self.cards:
                if i.value == j.value and i.colour != j.colour:
                    counter += 1
        if counter == 4:
            print("is a four of a kind")
        else:
            print('is not a four of a kind')

    def checkFullHouse(self):
        self.sortCards()
        if self.checkThreeOfAKind() and self.checkPair():
            print('is a full house')

    def checkFlush(self):
        counter = 0
        for i in self.cards:
            for j in self.cards:
                if i.colour == j.colour:
                    counter += 1
        if counter >= 5:
            print('is a flush')

    def checkStraight(self):
        self.sortCards()
        counter = 0
        for i in self.cards:
            if self.cards[self.cards.index(i) + 1].pos - i.pos == 1:
                counter += 1
        if counter >= 5:
            print('is a straight')

    def checkThreeOfAKind(self):
        self.sortCards
        counter = 0
        for i in self.cards:
            for j in self.cards:
                if i.value == j.value and i.colour != j.colour:
                    counter += 1
        if counter == 3:
            print("is a three of a kind")

    def checkTwoPair(self):
        pass

    def checkPair(self):
        self.sortCards()
        counter = 0
        for i in self.cards:
            for j in self.cards:
                if i.value == j.value and i.colour != j.colour:
                    counter += 1
        if counter == 2:
            print('it is a pair')
