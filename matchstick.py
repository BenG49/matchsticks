from copy import deepcopy
from math import floor, ceil
from typing import Optional

from gl import *

class State:
	def __init__(self, start: set = None, iter_start: int = 0):
		self.s = {(0, -1), (-1, 0)} if start is None else start
		self.i = iter_start

		self.edges = {(0, -1), (-1, 0)} if start is None else {
			s for s in start if self.single_box(s[0], s[1])
		}

	def __str__(self) -> str:
		bounds = (
			min(x for x, y in self.s),
			min(y for x, y in self.s),
			max(x for x, y in self.s),
			max(y for x, y in self.s),
		)

		out = ''
		for y in range(bounds[1], bounds[3] + 1):
			for x in range(bounds[0], bounds[2] + 1):
				out += 'O' if (x, y) in self.s else ' '

			if y != bounds[3]:
				out += '\n'
		return out

	def box_coord(self, n, i = None) -> int:
		if not i: i = self.i

		if i % 2 == 1:
			return ceil(n / 2)
		else:
			return floor(n / 2)

	def box_coords(self, x, y, i = None) -> tuple:
		if not i: i = self.i

		return (self.box_coord(x, i),
		        self.box_coord(y, i))

	# box coords
	def single_box(self, x, y) -> Optional[tuple]:
		f_pos = None
		pos = (x * 2 - self.i % 2, y * 2 - self.i % 2)

		for j in range(2):
			for i in range(2):
				if (i + pos[0], j + pos[1]) in self.s:
					if f_pos: return None
					else: f_pos = (((i + 1) % 2 + pos[0], j + pos[1]),
					               (i + pos[0], (j + 1) % 2 + pos[1]))

		return f_pos
	
	def iter(self):
		out = deepcopy(self.s)
		new_edges = set([])

		# loop through boxes in bounds
		for x, y in self.edges:
			b = self.single_box(x, y)

			# add neighbors of single
			if b:
				out.add(b[0])
				out.add(b[1])

				e1 = self.box_coords(*b[0], self.i + 1)
				e2 = self.box_coords(*b[1], self.i + 1)

				if e1 in new_edges: new_edges.remove(e1)
				else: new_edges.add(e1)
				
				if e2 in new_edges: new_edges.remove(e2)
				else: new_edges.add(e2)

		self.i += 1
		self.s = out
		self.edges = new_edges

def main():
	set_color(1.0, 0.0, 0.0)
	line((0, 0), (100, 100), 2)

	# s = State()
	# print(s)
	# s.iter()
	# print('-')
	# print(s)
	# s.iter()
	# print('-')
	# print(s)

if __name__ == '__main__':
	# main()
	wrapper(main, 'a')
