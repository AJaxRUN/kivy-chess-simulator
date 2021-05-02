from .constants import Board_Status, Color
from .types import Coord
from .coin import Coin


class Board:
	def __init__(self):
		self.reset_board()

	def initialiseBoard(self): #Initialize the board with coins
		pass

	def reset_board(self):
		self.board = [[''  for i in range(8)] for i in range(8)]
		self.turn = Color.white # player turn
		self.status = Board_Status.active # check, checkmate, stalemate, active

	def status_check(self) -> bool:
		return self.status == Board_Status.active
			
	def move_coin(self, coin: Coin, target_pos: Coord):
		if self.status_check():
			return self.status.name
		path = coin.is_valid_move(target_pos):
		if path is None:
			return 'invalid_move'

		#coin.isvalidmove
		#pathcheck
		#destinationcheck
		pass
