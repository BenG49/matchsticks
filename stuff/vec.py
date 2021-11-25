
class vec:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# str
	def __repr__(self) -> str: return self.__str__()
	def __str__(self) -> str:
		return f'({self.x}, {self.y})'

	# arr
	def __setitem__(self, i, n):
		if i < -2 or i > 1: raise IndexError
		
		if i == 0 or i == -2:
			self.x = n
		else:
			self.y = n

	def __getitem__(self, i) -> float:
		if i < -2 or i > 1: raise IndexError

		if i == 0 or i == -2:
			return self.x
		else:
			return self.y

	def __delitem__(self, i): pass

	def __len__(self) -> int: return 2

	# eq
	def __eq__(self, o):
		return isinstance(o, vec) and self.x == o.x and self.y == o.y

	def __hash__(self) -> int:
		return (self.x, self.y).__hash__()

	def __mul__(self, o):
		if isinstance(o, vec):
			pass
