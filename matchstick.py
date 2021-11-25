from copy import deepcopy
from math import floor, ceil
from typing import Optional

from stuff import *

class State:
	def __init__(self, init: set = None):
		self.squares = {(0, -1), (-1, 0)} if init is None else init
		self.lines = []
		self.i = 0

		self.update_lines()
		self.iter()

	def box_coord(self, n, i = None) -> int:
		if not i: i = self.i

		return ceil(n / 2) if i % 2 == 1 else floor(n / 2)

	# translate from pos to 2x2 box based on i
	def box_coords(self, x, y, i = None) -> tuple:
		return (self.box_coord(x, i),
		        self.box_coord(y, i))

	'''
	# much less lines, but worse performance
	def update_lines(self):
		def add_line(a: tuple, b: tuple):
			d = dst(a, b)

			def vert_replace(x: tuple, y: tuple, _d: float, i: int) -> bool:
				if d + _d == dst(x, y):
					self.lines[i] = (x, y)
					return True
				return False

			for i, p in enumerate(self.lines):
				_a, _b = p
				_d = dst(_a, _b)

				if a == _a and b != _b and vert_replace(b, _b, _d, i):
					return
				elif a == _b and b != _a and vert_replace(b, _a, _d, i):
					return
				elif b == _a and a != _b and vert_replace(a, _b, _d, i):
					return
				elif b == _b and a != _a and vert_replace(a, _a, _d, i):
					return

			self.lines.append((a, b))

		for x, y in self.s:
			if self.i % 2 == 0:
				add_line((x + 1, y), (x, y + 1))
			else:
				add_line((x, y), (x + 1, y + 1))
	'''

	# convert all current squares to lines
	def update_lines(self):
		for x, y in self.squares:
			if self.i % 2 == 0:
				self.lines.append(((x + 1, y), (x, y + 1)))
			else:
				self.lines.append(((x, y), (x + 1, y + 1)))

	# box coords
	def single_box(self, x, y) -> Optional[tuple]:
		f_pos = None
		pos = (x * 2 - self.i % 2, y * 2 - self.i % 2)

		for j in range(2):
			for i in range(2):
				if (i + pos[0], j + pos[1]) in self.squares:
					if f_pos: return None
					else: f_pos = (((i + 1) % 2 + pos[0], j + pos[1]),
					               (i + pos[0], (j + 1) % 2 + pos[1]))

		return f_pos
	
	def iter(self):
		out = set([])

		# loop through boxes in bounds
		for x, y in self.squares:
			b = self.single_box(*self.box_coords(x, y))

			# add neighbors of single
			if b:
				out.add(b[0])
				out.add(b[1])

		self.update_lines()

		self.i += 1
		self.squares = out

	def draw(self, center: tuple, size: int = 10, width: int = 1):
		for a, b, in self.lines:
			line(t_add(rot(t_mul(a, size), 135), center),
			     t_add(rot(t_mul(b, size), 135), center),
			     width)

state = State()
size = (500, 500)
center = [size[0] / 2, size[1] / 2]
sz = 4

# handle keys
def keys(key: str, mousex: int, mousey: int):
	global sz

	if key == b'-':
		sz /= 2
	elif key == b'+' or key == b'=':
		sz *= 2
	elif key == b'w': center[1] -= 10
	elif key == b'a': center[0] += 10
	elif key == b's': center[1] += 10
	elif key == b'd': center[0] -= 10
	else:
		state.iter()

def draw():
	state.draw(center, sz, 2)

if __name__ == '__main__':
	wrapper(draw, keys, 'matchsticks', size)
