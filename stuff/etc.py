from math import sin, cos, pi, sqrt

TO_RAD = pi / 180

def t_mul(t: tuple, n: int) -> tuple:
	return tuple([i * n for i in t])

def t_div(t: tuple, n: int) -> tuple:
	return tuple([i / n for i in t])

def t_add(a: tuple, b: tuple) -> tuple:
	return tuple([a[i] + b[i] for i in range(len(a))])

def dst(a: tuple, b: tuple) -> float:
	return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def rot(t: tuple, angle: int) -> tuple:
	s = sin(angle * TO_RAD)
	c = cos(angle * TO_RAD)

	return (t[0] * c - t[1] * s,
	        t[0] * s + t[1] * c)
