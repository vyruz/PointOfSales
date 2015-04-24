from Order import *

class User:

	def __init__ (self):
		self.__orders = []

	def createOrder(self, ID):
		newOrder = Order(ID)
		self.__orders.append(newOrder)
		return newOrder
		
	def getOrder(self, ID):
		#search the list of orders for the order with the specified ID
		for order in self.__orders:
			if(order.getID() == ID):
				return order
		return None

	def removeOrder(self, ID):
		for order in self.__orders:
			if(order.getID() == ID):
				self.__orders.remove(order)
