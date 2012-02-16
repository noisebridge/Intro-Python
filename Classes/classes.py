#!/usr/bin/env python

class Products(object):

	'''def setProduct(self, name, price, toys):
		self.price = price
		self.name = name '''


	def getProduct(self):
		print "%s: $%s" % (self.name, self.price)

	def __init__(self, name, price):
		self.price = price
		self.name = name

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name
	
	



class Cereal(Products):

	def __init__(self, name, price, toy):
		self.Toy = toy
		#super(Cereal,self).__init__(name,price)

	'''def addToy(self, Toy):
		self.toy = Toy'''


c1 = Cereal("capt crunch", "4.95", "Whistle")
