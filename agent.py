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
		
	def _eval_function(self, state, treeDepth):
		if state.winner() == self.char:
			return 10 - treeDepth
		elif state.winner() != self.char and state.winner() != None:
			return treeDepth - 10
		else:
			return 0

	def minimax(self, game:Game, depth:int, isMax:bool):
		if depth == 5 or game.init_state.game_over():
			return self._eval_function(game.init_state, depth)
		
		if isMax:
			value = -100000
			for action in game.init_state.actions(self.char):
				new_game = Game(game.p1, game.p2, game.init_state.clone().execute(action))
				value = max(value, self.minimax(new_game, depth+1, False))
			return value
		else:
			value = 100000
			for action in game.init_state.actions(game.opponent(self)):
				new_game = Game(game.p1, game.p2, game.init_state.clone().execute(action))
				value = min(value, self.minimax(new_game, depth+1, True))
			return value

	def choose_action(self, game):
		bestValue = -100000
		choice = None
		
		for action in game.init_state.actions(self.char):
			new_game = Game(game.p1, game.p2, game.init_state.clone().execute(action))
			value = self.minimax(new_game, 0, False)

			if value > bestValue:
				bestValue = value
				choice = action
		return choice
