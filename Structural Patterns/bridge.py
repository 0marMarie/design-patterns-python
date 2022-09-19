# Author     :  Omar Hamed Marie
# Description:  Bridge lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.
# Date       :  19 SEP 2022
# Version    :  V 1.0

class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""
    def draw_circle(self, x, y, radius):
        print(f"API 2 drawing a circle at ({x}, {y} with radius {radius}!)")
        

class Circle(object):
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		"""Implementation-independent"""
		self._radius *= percent


#Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Build the second Circle object using API Two
circle2 = Circle(2, 4, 6, DrawingAPITwo())
#Draw a circle
circle2.draw()
