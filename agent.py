from game import Player
from random import randint
from connect3 import State
from game import Game
import util

class RandomPlayer(Player):
	def __init__(self, char) -> None:
		super().__init__(char)
		
	def choose_action(self, game):
		choice = randint(0, len(game.init_state.actions(self.char))-1)
		return game.init_state.actions(self.char)[choice]
	
class MinimaxPlayer(Player):
	def __init__(self, char) -> None:
		super().__init__(char)
		self.choice = None
		
	def _eval_function(self, state, treeDepth):
		if state.winner() == self.char:
			return 10 - treeDepth
		elif state.winner() != self.char and state.winner() != None:
			return treeDepth - 10
		else:
			return 0

	def minimax(self, game, treeDepth, isMax):
		if (game.init_state.game_over()):
			return self._eval_function(game.init_state, treeDepth)
			
		if isMax:
			value = -1000000
			for action in game.init_state.actions(game.p1.char):
				new_game = Game(game.p1, game.p2, game.init_state.clone().execute(action))
				value = max(value, self.minimax(new_game, treeDepth+1, not isMax))
			return value
		else:
			value = 1000000
			for action in game.init_state.actions(game.p2.char):
				new_game = Game(game.p1, game.p2, game.init_state.clone().execute(action))
				value = min(value, self.minimax(new_game, treeDepth+1, not isMax))
			return value

	def choose_action(self, game):
		bestValue = -1000000
		choice = None
		
		for action in game.init_state.actions(self.char):
			new_game = Game(game.p1, game.p2, game.init_state.clone().execute(action))
			value = self.minimax(new_game, 0, False)
			
			if value > bestValue:
				bestValue = value
				choice = action
			print(f'vale: {value}, best value: {bestValue}')
			print(f'action: {action}')

		return choice
