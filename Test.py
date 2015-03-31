from MenuItemSubClass import *
from Order import *
item1 = FoodItem('Burrito',-.10,'Guac',True, True)
print item1.getName()
item2 = Appetizer('Sampler',5,'',True,True)
print item2.getPrice()

# Order tests
order1 = Order(0)
order2 = Order(1)
order1.addItem(item2)
order1.addItem(item1)
order1.addItem(item1)
order2.addItem(item2)
order1.printItems()
order1.removeItem(item1)
print order1.split(2)
print order2.calculateBill()

