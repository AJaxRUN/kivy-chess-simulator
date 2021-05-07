from .constants import Color
from .types import Coord, CoinPath


class Coin:
	def __init__(self, initial_position: Coord, color: Color, is_first_move: bool = True):
		self.current_pos = initial_position
		self.is_first_move = is_first_move
		self.color = color

	@staticmethod
	def is_valid_move(to_pos: Coord) -> None:
		assert len(to_pos) == 2, "to_pos can have only 2 coordinates"

	def get_all_valid_moves(self):
		pass

	def bound_and_equality_check(self, target_pos: Coord) -> bool:
		x_pos, y_pos = target_pos
		return (0 <= x_pos < 8) and (0 <= y_pos < 8) and self.current_pos != target_pos
		
	@staticmethod
	def static_find_diff(from_pos: Coord, target_pos: Coord, is_absolute_y: bool = True) -> Coord: # is_absolute_y is used to figure out the direction of coin movement (up / down)
		x_from, y_from = from_pos
		x_to, y_to = target_pos
		if is_absolute:
			return (abs(x_to - x_from), abs(y_to - y_from))
		return (abs(x_to - x_from), y_to - y_from)

	def find_diff(self, target_pos: Coord, is_absolute_y: bool = True) -> Coord:
		return Coin.static_find_diff(self.current_pos, target_pos, is_absolute_y)

	def get_path(self, to_pos: Coord) -> CoinPath:
		return []

	def set_position(self, to_pos: Coord) -> None:
		self.current_pos = to_pos
		self.is_first_move = False


class Knight(Coin):
	def __init__(self, initial_position: Coord, color: Color):
		super.__init__(initial_position, color)

	def is_valid_move(self, to_pos: Coord) -> bool:
		Coin.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)

class Rook(Coin):
	def __init__(self, initial_position: Coord, color: Color):
		super.__init__(initial_position, color)

	@staticmethod
	def static_is_valid_move(from_pos: Coord, to_pos: Coord) -> bool:
		Coin.is_valid_move(to_pos)
		x_diff, y_diff = Coin.find_diff(from_pos, to_pos)
		return x_diff == 0 or y_diff == 0
		
	def is_valid_move(self, to_pos: Coord):
		return Rook.check_is_valid(self.current_pos, to_pos)

class Pawn(Coin):
	def __init__(self, initial_position: Coord, color: Color):
		super.__init__(initial_position, color)
		
	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos, False)
		is_y_move_valid = (y_diff < 0 and self.color == Color.black) or (y_diff > 0 and self.color == Color.white)
		abs_y_diff = abs(y_diff)
		return is_y_move_valid and ((self.is_first_move and abs_y_diff == 2 and x_diff == 0) or (abs_y_diff == 1 and x_diff <= 1))

class Bishop(Coin):
	def __init__(self, initial_position: Coord, color: Color):
		super.__init__(initial_position)

	@staticmethod
	def static_is_valid_move(from_pos: Coord, to_pos: Coord) -> bool:
		Coin.is_valid_move(to_pos)
		x_diff, y_diff = Coin.find_diff(from_pos, to_pos)
		return x_diff == y_diff
		
	def is_valid_move(self, to_pos: Coord) -> bool:
		return Bishop.static_is_valid_move(self.current_pos, to_pos)

class King(Coin):
	def __init__(self, initial_position: Coord, color: Color):
		super.__init__(initial_position, color)

	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		return x_diff <= 1 and y_diff <= 1

class Queen(Coin):
	def __init__(self, initial_position: Coord):
		super.__init__(initial_position)

	def is_valid_move(self, to_pos: Coord) -> bool:
		super.is_valid_move(to_pos)
		x_diff, y_diff = self.find_diff(to_pos)
		if not (Rook.is_valid_move(self.current_pos, to_pos) and Bishop.is_valid_move(self.current_pos, to_pos)):
			return False
		pass