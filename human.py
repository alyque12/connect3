from game import Player

class HumanPlayer(Player):
	def __init__(self, char) -> None:
		super().__init__(char)
		
	def choose_action(self, game):
		count = 0
		for action in game.init_state.actions(self.char):
			print(f'{count}: {action}')
			count += 1
		print("Please choose an action: ", end="")
		userInput = input()
		userInput = int(userInput)
		return game.init_state.actions(self.char)[userInput]
