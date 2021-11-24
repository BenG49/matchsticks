from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def set_color(r: float, g: float, b: float):
	glColor3f(r, g, b)

def rect(pos: tuple, size: tuple):
	glBegin(GL_QUADS)
	glVertex2f(*pos)
	glVertex2f(pos[0] + size[0], pos[1])
	glVertex2f(pos[0] + size[0], pos[1] + size[1])
	glVertex2f(pos[0], pos[1] + size[1])
	glEnd()

def line(a: tuple, b: tuple, width: float = None):
	if width:
		glLineWidth(width)

	glBegin(GL_LINES)
	glVertex2f(*a)
	glVertex2f(*b)
	glEnd()

def loop(function):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	glViewport(0, 0, 500, 500)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	function()

	glutSwapBuffers()

def wrapper(function, title: str, size: tuple = (500, 500), pos: tuple = (0, 0)):
	# init glut
	glutInit()
	# set display mode
	glutInitDisplayMode(GLUT_RGBA)
	# set display size
	glutInitWindowSize(*size)
	# set display position
	glutInitWindowPosition(*pos)
	# title
	win = glutCreateWindow(title)
	# call display funciton
	glutDisplayFunc(lambda: loop(function))
	# draw idle
	glutIdleFunc(lambda: loop(function))
	glutMainLoop()
