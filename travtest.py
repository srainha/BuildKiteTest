import unittest
from traveler import *

#test instances of traveler
class MyTest(object):
	def __init__(self, traveler):
		self.myTraveler = traveler
	def testMove(self):
		self.myTraveler.move(4,5)
		assert (4,5) == self.myTraveler.location()
		self.myTraveler.move(1,5)
		assert (4,5) == self.myTraveler.location()