from Order import *
class User:

	def __init__ (self):
		self.__orders = []

	def CreateOrder(self):
		newOrder = Order(1)
		self.__orders.append(newOrder)
		return newOrder


		