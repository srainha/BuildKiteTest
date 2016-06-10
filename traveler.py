class Traveler(object):
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
	def moveHorz(self, distance):
		self.x += distance
	def moveVert(self, distance):
		self.y += distance
	def move(self, x=0, y=0):
		self.x += x
		self.y += y
	def location(self):
		return (self.x,self.y)
	def pname(self):
		return self.name
