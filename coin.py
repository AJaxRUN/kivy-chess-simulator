from .constants import Color
from .types import Coord, CoinPath


class Coin:
	def __init__(self, initial_position: Coord, is_first_move: bool = True):
		self._current_pos = initial_position
		self.is_first_move = is_first_move
	
	def is_valid_move(self, to_pos: Coord) -> bool:
		assert len(to_pos) == 2, "to_pos can have only 2 coordinates"
		return False

	def get_all_valid_moves(self):
		pass

	def bound_and_equality_check(self, target_pos: Coord) -> bool:
		x_pos, y_pos = target_pos
		return (0 <= x_pos < 8) and (0 <= y_pos < 8) and self._current_pos != target_pos
		
	def find_diff(self, target_pos: Coord) -> Coord:
		x_from, y_from = self._current_pos
		x_to, y_to = target_pos
		return (abs(x_from - x_to), abs(y_from - y_to))

	def get_path(self, to_pos: Coord) -> CoinPath:
		return []

	def set_position(self, to_pos: Coord) -> None:
		self._current_pos = to_pos
		self.is_first_move = False


class Knight(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)

class Rook(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return x_diff == 0 or y_diff == 0

class Pawn(Coin):
	def __init__(self, initial_position: Coord, color: Color):
		super.__init__(initial_position)
		self.color = color
		
	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return (self.is_first_move and y_diff == 2 and x_diff == 0) or (y_diff == 1 and x_diff <= 1)

class Bishop(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return x_diff == y_diff


class King(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return x_diff <= 1 and y_diff <= 1
