from MenuItemSubClass import *
from Order import *
item1 = FoodItem('Burrito',-.10,'Guac',True, True)
print item1.getName()
item2 = Appetizer('Sampler',5,'',True,True)
print item2.getPrice()
order1 = Order(0)
order1.addItem(item2)
print order1.calculateBill()
