from .constants import Board_Status, Color, Board_Response, Keywords_For_Text_Splitting
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
			
	def move_coin(self, coin: Coin, target_pos: Coord) -> str:
		if self.status_check():
			return self.status.name
		is_valid_move = coin.is_valid_move(target_pos)
		if not is_valid_move:
			return Board_Response.invalid_move.name
		#coin.isvalidmove
		#pathcheck
		#destinationcheck
		pass

	def split_input_str(self, input_coord: str) -> list[str]:
		
	
	def main(self, input_coord: str) -> str:
		if input_coord.strip() == '':
			return Board_Response.invalid_move.name
		
		
