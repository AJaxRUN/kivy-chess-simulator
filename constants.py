from enum import Enum

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
