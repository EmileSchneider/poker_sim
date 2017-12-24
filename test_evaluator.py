import deck
import gameEvaluator
import headsUpGame
import player

# test royal flush
player = player.Player()
player.setBothCards(deck.Card('A', 'H'), deck.Card('Q', 'H'))
table = [deck.Card('J','H'),deck.Card('10','H'),deck.Card('K','H'),deck.Card('7','C'),deck.Card('2','S')]

evalu = gameEvaluator.Evaluator(table, player)
evalu.sortCards()
evalu.checkRoyalFlush()

#test straigh flush

player.setBothCards(deck.Card('3', 'D'), deck.Card('6', 'D'))
table = [deck.Card('4', 'D'), deck.Card('5', 'D'), deck.Card('7', 'D'), deck.Card('7', 'C'), deck.Card('2', 'S')]
evalu = gameEvaluator.Evaluator(table, player)
evalu.checkStraightFlush()
