import deck
import gameEvaluator
import headsUpGame
import player

deck = deck.Deck()
p1 = player.Player()
p2 = player.Player()
game = headsUpGame.HeadsUpGame(p1, p2, deck)

game.dealCards()
game.dealFlop()
game.dealTurn()
game.dealRiver()

evaluator = gameEvaluator.Evaluator(game.getTable(), game.getPlayer1())
evaluator.checkHighCard()

game.showTable()
print('=')
game.showHandCards()
