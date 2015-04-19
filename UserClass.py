class User:

	def __init__ (self, orders):
		self.__orders = []

	def CreateOrder(self):
		newOrder = Order(1)
		self.__orders.append(newOrder)
		