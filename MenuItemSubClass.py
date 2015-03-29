from MenuItem import *
class FoodItem(MenuItem):
	def __init__ (self, name, price, comments, GF, Veg):
		self.name = name
		self.setPrice(price)
		self.avail = True
		self.comments = ""
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
class Dessert(FoodItem):
	pass
class DrinkItem(MenuItem):
	def __init__ (self, name, price, comments):
		pass
class SoftDrink(DrinkItem):
	pass
class HardDrink(DrinkItem):
	pass