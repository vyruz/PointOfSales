from MenuItem import *
class FoodItem(MenuItem):
	def __init__ (self, name, price, comments, GF, Veg):
		self.name = name
		self.setPrice(price)
		self.avail = True
		self.comments = comments
		self.glutenfree = GF
		self.vegetarian = Veg

	def getGlutenFree(self):
		return self.glutenfree

	def getVegetarian(self):
		return self.vegetarian

class Entre(FoodItem):
	pass
class Appetizer(FoodItem):
	pass
# class Dessert(FoodItem):
# 	pass
class DrinkItem(MenuItem):
	def __init__ (self, name, cost, com):
		self.name = name
		self.price = cost
		self.avail = True
		self.comments = com


class SoftDrink(DrinkItem):
	#why do we need a separate class for this?
	def __init__ (self, name, cost, com):
		self.name = name
		self.price = cost
		self.avail = True
		self.comments = com

class HardDrink(DrinkItem):	
	def __init__ (self, name, cost, abv, com):
		self.name = name
		self.price = cost
		self.abv = abv
		self.avail = True
		self.comments = com
        
