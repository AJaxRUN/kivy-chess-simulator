from enum import Enum
from typing import Union

#type for tuple
Coord = tuple[int]
CoinPath = Union[list[Coord], None]

class Board_Status(Enum):
	active = 1
	check = 2
	stalemate = 3
	checkmate = 4

class Board_Response(Enum):
	invalid_move = 5
	valid_move = 6

class Color(Enum):
	white = 1
	black = 2
	
class Coin:
	def __init__(self, initial_position: Coord, color: Color):
		self._current_pos = initial_position
		self.color = color
	
	def is_valid_move(self, to_pos: Coord) -> bool:
		assert len(to_pos) == 2, "to_pos can have only 2 coordinates"
		return self._is_valid_bounds(to_pos) and self._current_pos != to_pos

	def get_all_valid_moves(self):
		pass

	def _is_valid_bounds(target_pos: Coord) -> bool:
		x_pos, y_pos = target_pos
		return (0 <= x_pos < 8) and (0 <= y_pos < 8)
		
	def find_diff(target_pos: Coord) -> Coord:
		x_from, y_from = self._current_pos
		x_to, y_to = target_pos
		return (abs(x_from - x_to), abs(y_from - y_to))

	def set_position(to_pos: Coord):
		self._current_pos = to_pos


class Knight(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> CoinPath:
		bound_check = super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return [] if bound_check and ((x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)) else None

class Rook(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> CoinPath:
		bound_check = super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		if not (bound_check and (x_diff == 0 or y_diff == 0)):
			return None
		if x_diff == 0:
			return []

class Pawn(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)
		self.is_first_move = False
		
	def is_valid_move(self, to_pos: Coord) -> bool:
		bound_check = super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		if ((self.color == Color.white and y_pos == 1) or (self.color == Color.black and y_pos == 6))
			return [] if bound_check and (y_diff <= 2) else None
		return [] if bound_check and (y_diff == 1) else None

class Bishop(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		bound_check = super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return bound_check and (x_diff == y_diff)


class King(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		bound_check = super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return [] if bound_check and (x_diff <= 1 and y_diff <= 1) else None


class Board:
	def __init__(self):
		self.reset_board()

	def initialiseBoard(self): #Initialize the board with coins
		pass

	def reset_board(self):
		self.board = [[''  for i in range(8)] for i in range(8)]
		self.turn = Player_Turn.white #player turn: w-white, b-black
		self.status = Board_Status.active #check, checkmate, stalemate, active

	def status_check(self) -> bool:
		return self.status == Board_Status.active
			
	def move_coin(self, coin: Coin, target_pos: Coord) -> :
		if self.status_check():
			return self.status.name
		path = coin.is_valid_move(target_pos):
		if path is None:
			return 'invalid_move'

		#coin.isvalidmove
		#pathcheck
		#destinationcheck
		pass
		