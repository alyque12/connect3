from util import *
from game import Game
from connect3 import State
from human import HumanPlayer
from agent import RandomPlayer, MinimaxPlayer

if __name__ == "__main__":
	p1 = get_arg(1)
	p2 = get_arg(2)
	if p1 == "human":
		p1 = HumanPlayer("X")
	elif p1 == "random":
		p1 = RandomPlayer("X")
	elif p1 == "minimax":
		p1 = MinimaxPlayer("X")
	if p2 == "human":
		p2 = HumanPlayer("O")
	elif p2 == "random":
		p2 = RandomPlayer("O")
	elif p2 == "minimax":
		p2 = MinimaxPlayer("O")
	game = Game(p1, p2, State())
	game.play()
	