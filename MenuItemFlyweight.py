#not sure how to integrate a flyweight because each menu item can have a unique comment

from Order import *

class MenuItemFlyweight():

	def __init__(self):
		self.pool = []

	def getItem(item, type):
		#search the pool for the item. If it's not there,
		#create a new instance of it
		for poolItem in self.pool:
			if(poolItem.getName() = item):
				return poolItem.getName
			else:
				#create a new instance. Must be given the type to do so.
				#(entre, appetizer, dessert, hard drink, soft drink)
				if(type == "entre"):
					pool.append(Entre(item, ))
