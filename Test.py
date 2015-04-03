from MenuItemSubClass import *
from Order import *
item1 = FoodItem('Burrito',10,'Guac',True, True)
print item1.getName()
item2 = Appetizer('Sampler',5,'',True,True)
print item2.getPrice()
item3 = DrinkItem('Water', 0,'free')

# Order tests
order1 = Order(0)
order2 = Order(1)
order1.addItem(item1)
order1.addItem(item1)

print("|"*140)
order1.printItems()
order2.printItems()
print ("Order 1 Total $" +str(order1.calculateBill()))
print ("Order 2 Total $" +str(order2.calculateBill()))

