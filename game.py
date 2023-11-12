from abc import ABC, abstractmethod
import util

class Player(ABC):
	def __init__(self, char) -> None:
		self.char = char
		
	@abstractmethod
	def choose_action(self, game):
		pass
	
class Game:
	def __init__(self, p1, p2, init_state) -> None:
		self.p1 = p1
		self.p2 = p2
		self.init_state = init_state
		self.active_player = self.p1
		
	def play(self):
		while not self.init_state.game_over():
			p1_choice = self.p1.choose_action(self)
			self.init_state = self.init_state.execute(p1_choice)
			util.pprint(self.init_state)
			if self.init_state.game_over():
				break
			self.active_player = self.p2
			p2_choice = self.p2.choose_action(self)
			self.init_state = self.init_state.execute(p2_choice)
			util.pprint(self.init_state)
		print(f"{self.init_state.winner()} wins")
		
	def opponent(self, player):
		if self.p1 == player:
			opponent = self.p2.char
		else:
			opponent = self.p1.char
		return opponent
		